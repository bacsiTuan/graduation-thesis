# coding: utf8
from flask_restplus import Namespace
import flask_restplus as frp
from loguru import logger
from app.decorators import parse_params, check_token
from flask_restful.reqparse import Argument
from app.api.users import UsersService

ns = Namespace(name="users", description="users")


@ns.route("")
class APITasks(frp.Resource):
    @parse_params(
        Argument("id", location=['values', 'json'], required=True, help="id", type=str, default=None),
        Argument("email", location=['values', 'json'], required=True, help="email", type=str, default=None),
        Argument("password", location=['values', 'json'], required=True, help="password", type=str, default=None),
        Argument("username", location=['values', 'json'], required=True, help="username", type=str, default=None),
    )
    def post(self, **kwargs):
        try:
            logger.warning(kwargs)
            user = UsersService.create_user(**kwargs)
            return {
                       "success": True,
                       "data": user
                   }, 200
        except Exception as e:
            logger.error(e)

    @parse_params(
        Argument("user_name", location=['values', 'json'], required=True, help="user name", type=str, default=None),
        Argument("password", location=['values', 'json'], required=True, help="password", type=str, default=None),
    )
    def put(self, **kwargs):
        logger.warning(kwargs)
        login = UsersService.login(**kwargs)
        if login:
            return {
                       "success": True,
                       "data": {
                           "login": True,
                           "token": login
                       }
                   }, 200
        else:
            return {
                       "success": True,
                       "data": {
                           "login": False,
                       }
                   }, 200

    @parse_params(
        Argument("user_name", location=['values', 'json'], required=True, help="user name", type=str, default=None),
    )
    @check_token()
    def get(self, **kwargs):
        user = UsersService.get_by_username(kwargs.get('user_name'))
        return {
                   "success": True,
                   "data": user
               }, 200
