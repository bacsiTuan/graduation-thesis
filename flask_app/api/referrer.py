# coding: utf8
from flask_restplus import Namespace
import flask_restplus as frp
from loguru import logger
from app.decorators import parse_params, check_token, check_token_admin
from flask_restful.reqparse import Argument
from app.api.referrer import ReferrerService

ns = Namespace(name="referrer", description="referrer")


@ns.route("")
class APIReferrer(frp.Resource):
    # CreateReferrerDTO
    @parse_params(
        Argument("name", location=['values', 'json'], required=False, help="name", type=str, default=None),
        Argument("email", location=['values', 'json'], required=False, help="email", type=str, default=None),
        Argument("phone_number", location=['values', 'json'], required=False, help="phone_number", type=str,
                 default=None),
    )
    def post(self, **kwargs):
        resource = ReferrerService.create(**kwargs)
        return {
                   "success": True
               }, 200

    # UpdateReferrerDTO
    @parse_params(
        Argument("id", location=['values', 'json'], required=False, help="id", type=str, default=None),
        Argument("code", location=['values', 'json'], required=False, help="code", type=str, default=None),
        Argument("name", location=['values', 'json'], required=False, help="name", type=str, default=None),
        Argument("email", location=['values', 'json'], required=False, help="email", type=str, default=None),
        Argument("phone_number", location=['values', 'json'], required=False, help="phone_number", type=str,
                 default=None),
    )
    def put(self, **kwargs):
        resource = ReferrerService.update(**kwargs)
        return {
                   "success": True
               }, 200


@ns.route("/<int:referrer_id>")
class APIReferrerById(frp.Resource):
    def get(self, referrer_id):
        resource = ReferrerService.get_by_id(referrer_id)
        return {
                   "success": True
               }, 200

    def delete(self, referrer_id):
        resource = ReferrerService.delete_by_id(referrer_id)
        return {
                   "success": True
               }, 200


@ns.route("/filter-table")
class APIReferrerFilterTable(frp.Resource):
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
    def post(self, **kwargs):
        resource = ReferrerService.filter_table(**kwargs)
        return {
                   "success": True
               }, 200


@ns.route("/filter-table-less")
class APIReferrerFilterTableLess(frp.Resource):
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
    def post(self, **kwargs):
        logger.info(kwargs)
        resource = ReferrerService.filter_table_less(**kwargs)
        return {
                   "success": True
               }, 200


@ns.route("/<string:referrer_code/active-referrer/<string:confirm_number>")
class APIReferrerActivateReferrer(frp.Resource):
    def get(self, referrer_code, confirm_number):
        resource = ReferrerService.activate_referrer(referrer_code, confirm_number)
        return {
                   "success": True
               }, 200


@ns.route("/export-excel")
class APIReferrerExportExcel(frp.Resource):
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
    def post(self, **kwargs):
        resource = ReferrerService.export_excel(**kwargs)
        return {
                   "success": True
               }, 200
