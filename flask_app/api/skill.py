# coding: utf8
from flask_restful import Resource
from loguru import logger
from app.decorators import parse_params, check_token
from flask_restful.reqparse import Argument
from app.api.skill import SkillService
from app.constants import Role


# ns = Namespace(name="skill", description="skill")


# @ns.route("")
class APISkill(Resource):
    @parse_params(
        Argument("name", location=['values', 'json'], required=True, help="name", type=str, default=None),
    )
    @check_token(role=[Role.HR.value])
    def post(self, **kwargs):
        resource = SkillService.create(**kwargs)
        return resource

    @parse_params(
        Argument("name", location=['values', 'json'], required=True, help="name", type=str, default=None),
        Argument("id", location=['values', 'json'], required=True, help="id", type=str, default=None),
    )
    @check_token(role=[Role.HR.value])
    def put(self, **kwargs):
        resource = SkillService.update(**kwargs)
        return resource


# @ns.route("/<string:skill_id>")
class APISkillById(Resource):
    def get(self, skill_id):
        resource = SkillService.get_by_id(skill_id)
        return resource


# @ns.route("/filter-table")
class APISkillFilterTable(Resource):
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
        resource = SkillService.filter_table(**kwargs)
        return resource
