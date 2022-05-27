# coding: utf8
from flask_restful import Resource
from loguru import logger
from app.decorators import parse_params, check_token
from flask_restful.reqparse import Argument
from app.api.survey import SurveyService
from app.constants import Role

# ns = Namespace(name="survey", description="survey")


# @ns.route("")
class APISurvey(Resource):
    @parse_params(
        Argument("name", location=['values', 'json'], required=False, help="name", type=str,
                 default=None),
        Argument("questions", location=['values', 'json'], required=False, help="questions", type=dict, default=None,
                 action="append"),
    )
    @check_token(role=[Role.HR.value])
    def post(self, **kwargs):
        resource = SurveyService.create(**kwargs)
        return resource

    @parse_params(
        Argument("id", location=['values', 'json'], required=False, help="id", type=str,
                 default=None),
        Argument("code", location=['values', 'json'], required=False, help="code", type=str,
                 default=None),
        Argument("name", location=['values', 'json'], required=False, help="name", type=str,
                 default=None),
        Argument("questions", location=['values', 'json'], required=False, help="name", type=dict, default=None,
                 action="append"),
    )
    @check_token(role=[Role.HR.value])
    def put(self, **kwargs):
        resource = SurveyService.update(**kwargs)
        return resource


# @ns.route("/<string:survey_id>")
class APISurveyById(Resource):
    @check_token(role=[Role.HR.value])
    def get(self, survey_id):
        resource = SurveyService.get_by_id(survey_id)
        return resource

    @check_token(role=[Role.HR.value])
    def delete(self, survey_id):
        resource = SurveyService.delete_by_id(survey_id)
        return resource


# @ns.route("/filter-table")
class APISurveyFilterTable(Resource):
    @parse_params(
        Argument("code", location=['values', 'json'], required=False, help="code", type=str,
                 default=None),
        Argument("name", location=['values', 'json'], required=False, help="name", type=str, default=None),
        Argument("created_by", location=['values', 'json'], required=False, help="created_by", type=str, default=None),
        Argument("pageNumber", location=["args"], required=False, help="pageNumber", type=int, default=0),
        Argument("pageSize", location=["args"], required=False, help="pageSize", type=int, default=20),
        Argument("sortType", location=["args"], required=False, help="sortType", type=str, default="ASC"),
        Argument("sortBy", location=["args"], required=False, help="sortBy", type=str, default="code"),
    )
    @check_token(role=[Role.HR.value])
    def post(self, **kwargs):
        resource = SurveyService.filter_table(**kwargs)
        return resource


# @ns.route("/options")
class APISurveyOptions(Resource):
    @parse_params(
        Argument("codeOrName", location=["args"], required=False, help="sortBy", type=str, default="code"),
    )
    @check_token(role=[Role.HR.value])
    def get(self, **kwargs):
        resource = SurveyService.get_data_select(kwargs.get("codeOrName"))
        return resource
