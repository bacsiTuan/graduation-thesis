# coding: utf8
from flask_restful import Resource
from loguru import logger
from app.decorators import parse_params, check_token
from flask_restful.reqparse import Argument
from app.api.referrer import ReferrerService
from app.constants import Role

# ns = Namespace(name="referrer", description="referrer")


# @ns.route("")
class APIReferrer(Resource):
    # CreateReferrerDTO
    @parse_params(
        Argument("name", location=['values', 'json'], required=False, help="name", type=str, default=None),
        Argument("email", location=['values', 'json'], required=False, help="email", type=str, default=None),
        Argument("phone_number", location=['values', 'json'], required=False, help="phone_number", type=str,
                 default=None),
    )
    @check_token(role=[Role.HR.value])
    def post(self, **kwargs):
        resource = ReferrerService.create(**kwargs)
        return resource

    # UpdateReferrerDTO
    @parse_params(
        Argument("id", location=['values', 'json'], required=False, help="id", type=str, default=None),
        Argument("code", location=['values', 'json'], required=False, help="code", type=str, default=None),
        Argument("name", location=['values', 'json'], required=False, help="name", type=str, default=None),
        Argument("email", location=['values', 'json'], required=False, help="email", type=str, default=None),
        Argument("phone_number", location=['values', 'json'], required=False, help="phone_number", type=str,
                 default=None),
    )
    @check_token(role=[Role.HR.value])
    def put(self, **kwargs):
        resource = ReferrerService.update(**kwargs)
        return resource


# @ns.route("/<string:referrer_id>")
class APIReferrerById(Resource):
    @check_token(role=[Role.HR.value, Role.ADMIN.value])
    def get(self, referrer_id):
        resource = ReferrerService.get_by_id(referrer_id)
        return resource

    @check_token(role=[Role.HR.value])
    def delete(self, referrer_id):
        resource = ReferrerService.delete_by_id(referrer_id)
        # return {
        #            "success": True
        #        }, 200
        return resource


# @ns.route("/filter-table")
class APIReferrerFilterTable(Resource):
    @parse_params(
        Argument("to_created_at", location=['values', 'json'], required=False, help="to created at", type=str,
                 default=None),
        Argument("from_created_at", location=['values', 'json'], required=False, help="from created at", type=str,
                 default=None),
        Argument("code", location=['values', 'json'], required=False, help="code", type=str, default=None),
        Argument("name", location=['values', 'json'], required=False, help="name", type=str, default=None),
        Argument("email", location=['values', 'json'], required=False, help="email", type=str, default=None),
        Argument("phone_number", location=['values', 'json'], required=False, help="phone_number", type=str,
                 default=None),
        Argument("pageNumber", location=["args"], required=False, help="pageNumber", type=int, default=0),
        Argument("pageSize", location=["args"], required=False, help="pageSize", type=int, default=20),
        Argument("sortType", location=["args"], required=False, help="sortType", type=str, default="ASC"),
        Argument("sortBy", location=["args"], required=False, help="sortBy", type=str, default="code"),
    )
    @check_token(role=[Role.HR.value, Role.ADMIN.value])
    def post(self, **kwargs):
        try:
            resource = ReferrerService.filter_table(**kwargs)
            return resource
        except Exception as e:
            logger.info(e)


# @ns.route("/filter-table-less")
class APIReferrerFilterTableLess(Resource):
    # FilterReferrerLessDTO
    @parse_params(
        Argument("created_by", location=['values', 'json'], required=False, help="created by", type=str,
                 default=None),
        Argument("code", location=['values', 'json'], required=False, help="code", type=str, default=None),
        Argument("name", location=['values', 'json'], required=False, help="name", type=str, default=None),
        Argument("email", location=['values', 'json'], required=False, help="email", type=str, default=None),
        Argument("phone_number", location=['values', 'json'], required=False, help="phone_number", type=str,
                 default=None),
        Argument("pageNumber", location=["args"], required=False, help="pageNumber", type=int, default=0),
        Argument("pageSize", location=["args"], required=False, help="pageSize", type=int, default=20),
        Argument("sortType", location=["args"], required=False, help="sortType", type=str, default="ASC"),
        Argument("sortBy", location=["args"], required=False, help="sortBy", type=str, default="code"),
    )
    @check_token(role=[Role.HR.value])
    def post(self, **kwargs):
        logger.info(kwargs)
        resource = ReferrerService.filter_table_less(**kwargs)
        return resource


# @ns.route("/<string:referrer_code>/active-referrer/<string:confirm_number>")
class APIReferrerActivateReferrer(Resource):
    def get(self, referrer_code, confirm_number):
        resource = ReferrerService.activate_referrer(referrer_code, confirm_number)
        # return {
        #            "success": True
        #        }, 200
        return resource


# @ns.route("/export-excel")
class APIReferrerExportExcel(Resource):
    @parse_params(
        Argument("to_created_at", location=['values', 'json'], required=False, help="to created at", type=str,
                 default=None),
        Argument("from_created_at", location=['values', 'json'], required=False, help="from created at", type=str,
                 default=None),
        Argument("code", location=['values', 'json'], required=False, help="code", type=str, default=None),
        Argument("name", location=['values', 'json'], required=False, help="name", type=str, default=None),
        Argument("email", location=['values', 'json'], required=False, help="email", type=str, default=None),
        Argument("phone_number", location=['values', 'json'], required=False, help="phone_number", type=str,
                 default=None),
        Argument("sortBy", location=["args"], required=False, help="sortBy", type=str, default="code"),
    )
    @check_token(role=[Role.HR.value, Role.ADMIN.value])
    def post(self, **kwargs):
        resource = ReferrerService.export_excel(**kwargs)
        return resource
