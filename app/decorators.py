# coding: utf8
from functools import wraps

from flask import request
from flask_restful import reqparse
from jsonschema import FormatChecker, validate
from jsonschema.exceptions import ValidationError
from app.extensions import db
from app.errors.exceptions import BadRequest
# from app.helper import JWTHelper
from loguru import logger


def use_args(**schema):
    def decorated(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            req_args = request.args.to_dict()
            if request.method in ('POST', 'PUT', 'PATCH', 'DELETE') \
                    and request.mimetype == 'application/json':
                req_args.update(request.get_json())
            req_args = {k: v for k, v in req_args.items(
            ) if k in schema['properties'].keys()}
            if 'required' in schema:
                for field in schema['required']:
                    if field not in req_args or not req_args[field]:
                        field_name = field
                        if field in schema['properties']:
                            if 'name' in schema['properties'][field]:
                                field_name = schema['properties'][field]['name']
                        raise BadRequest(message='{} is required'.format(field_name))
            try:
                validate(instance=req_args, schema=schema,
                         format_checker=FormatChecker())
            except ValidationError as exp:
                exp_info = list(exp.schema_path)
                error_type = ('type', 'format', 'pattern',
                              'maxLength', 'minLength')
                if set(exp_info).intersection(set(error_type)):
                    field = exp_info[1]
                    field_name = field
                    if field_name in schema['properties']:
                        if 'name' in schema['properties'][field]:
                            field_name = schema['properties'][field]['name']
                    message = '{} is not valid'.format(field_name)
                else:
                    message = exp.message  # pragma: no cover
                raise BadRequest(message=message)
            new_args = args + (req_args,)
            return func(*new_args, **kwargs)

        return wrapper

    return decorated


def parse_params(*arguments):
    """
    Parse the parameters
    Forward them to the wrapped function as named parameters
    """

    def parse(func):
        """ Wrapper """

        @wraps(func)
        def resource_verb(*args, **kwargs):
            """ Decorated function """
            parser = reqparse.RequestParser()

            for argument in arguments:
                parser.add_argument(argument)
            kwargs.update(parser.parse_args())

            return func(*args, **kwargs)

        return resource_verb

    return parse


def sqlalchemy_session(**schema):
    def decorated(func):

        @wraps(func)
        def resource_verb(*args, **kwargs):
            # MANUAL PRE PING
            try:
                db.session.execute("SELECT 1;")
                db.session.commit()
            except:
                db.session.rollback()
            finally:
                db.session.close()
                db.session.remove()

            result = None
            exception = None
            try:
                result = func(*args, **kwargs)
                db.session.commit()
            except Exception as exp:
                exception = exp
                if db.session.is_active:
                    db.session.rollback()
            finally:
                db.session.close()
                db.session.remove()

            if exception:
                raise exception
            return result

        return resource_verb

    return decorated


def check_token():
    def wrapper(func):
        @wraps(func)
        def decorator(*args, **kwargs):
            if request.headers.get("Authorization"):
                jwt_token = request.headers.get("Authorization")
                logger.info(jwt_token)
                # if jwt_token is None:
                #     pass
                auth_token = jwt_token.replace("Bearer ", "")
                JWTHelper.validate_token(auth_token)
            result = func(*args, **kwargs)

            return result

        return decorator

    return wrapper
