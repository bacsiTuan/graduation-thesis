# coding: utf8
from flask_restful import Resource
from app.decorators import parse_params, check_token
from flask_restful.reqparse import Argument
from app.api.position import PositionService
from app.constants import Role


# ns = Namespace(name="position", description="position")


# @ns.route("")
class APIPosition(Resource):
    @parse_params(
        Argument("name", location=['values', 'json'], required=True, help="name", type=str, default=None),
    )
    @check_token(role=[Role.HR.value])
    def post(self, **kwargs):
        resource = PositionService.create(**kwargs)
        return resource

    @parse_params(
        Argument("name", location=['values', 'json'], required=True, help="name", type=str, default=None),
        Argument("id", location=['values', 'json'], required=True, help="id", type=str, default=None),
    )
    @check_token(role=[Role.HR.value])
    def put(self, **kwargs):
        resource = PositionService.update(**kwargs)
        return resource


# @ns.route("/<string:position_id>")
class APIPositionById(Resource):
    def get(self, position_id):
        resource = PositionService.get_by_id(position_id)
        return resource


# @ns.route("/filter-table")
class APIPositionFilterTable(Resource):
    @parse_params(
        Argument("created_by", location=['values', 'json'], required=False, help="created by", type=str, default=None),
        Argument("updated_by", location=['values', 'json'], required=False, help="updated by", type=str,
                 default=None),
        Argument("pageNumber", location=["args"], required=False, help="pageNumber", type=int, default=0),
        Argument("pageSize", location=["args"], required=False, help="pageSize", type=int, default=20),
        Argument("sortType", location=["args"], required=False, help="sortType", type=str, default="ASC"),
        Argument("sortBy", location=["args"], required=False, help="sortBy", type=str, default="code"),
    )
    @check_token(role=[Role.HR.value])
    def post(self, **kwargs):
        resource = PositionService.filter_table(**kwargs)
        return resource
