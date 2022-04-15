# coding: utf8
from flask_restplus import Namespace
import flask_restplus as frp
from loguru import logger
from app.decorators import parse_params, check_token
from flask_restful.reqparse import Argument
from app.api.users import UsersService
from flask import request
from app.constants import Role

ns = Namespace(name="users", description="users")


@ns.route("")
class APIUser(frp.Resource):
    @parse_params(
        Argument("roles", location=['values', 'json'], required=True, help="roles", type=str, default=None),
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
            return {
                       "success": False,
                       "data": e
                   }, 200

    @parse_params(
        Argument("user_name", location=['values', 'json'], required=True, help="user name", type=str, default=None),
    )
    @check_token(role=[Role.ADMIN.value, Role.HR.value])
    def get(self, **kwargs):
        # logger.info(request.headers.get("Authorization"))
        user = UsersService.get_by_username(kwargs.get('user_name'))
        return {
                   "success": True,
                   "data": user
               }, 200

    @parse_params(
        Argument("id", location=['values', 'json'], required=True, help="id", type=str, default=None),
        Argument("roles", location=['values', 'json'], required=False, help="roles", type=str, default=None),
        Argument("email", location=['values', 'json'], required=True, help="email", type=str, default=None),
        Argument("status", location=['values', 'json'], required=True, help="status", type=int, default=None),
        Argument("username", location=['values', 'json'], required=True, help="username", type=str, default=None),
    )
    def put(self, **kwargs):
        try:
            user = UsersService.update(**kwargs)
            return {
                       "success": user
                   }, 200
        except Exception as e:
            logger.error(e)


@ns.route("/login")
class APILogin(frp.Resource):
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


@ns.route("/filter-table")
class APIFilterTable(frp.Resource):
    @parse_params(
        Argument("username", location=['values', 'json'], required=False, help="user name", type=str,
                 default=None),
        Argument("email", location=['values', 'json'], required=False, help="email", type=str, default=None),
        Argument("pageNumber", location=["args"], required=False, help="pageNumber", type=int, default=0),
        Argument("pageSize", location=["args"], required=False, help="pageSize", type=int, default=20),
        Argument("sortType", location=["args"], required=False, help="sortType", type=str, default="ASC"),
        Argument("sortBy", location=["args"], required=False, help="sortBy", type=str, default="code"),
    )
    # @check_token(role=[Role.HR.value, Role.ADMIN.value])
    def post(self, **kwargs):
        resource = UsersService.filter_table(**kwargs)
        return resource


@ns.route("/<string:user_id>")
class APIUserById(frp.Resource):
    @check_token(role=[Role.HR.value, Role.ADMIN.value])
    def get(self, user_id):
        resource = UsersService.get_by_id(user_id)
        return resource

    @check_token(role=[Role.HR.value, Role.ADMIN.value])
    def delete(self, user_id):
        resource = UsersService.delete_by_id(user_id)
        return resource
