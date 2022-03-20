# coding: utf8
from flask_restplus import Namespace
import flask_restplus as frp
from loguru import logger
from app.decorators import parse_params, check_token
from flask_restful.reqparse import Argument
from app.api.survey import SurveyService

ns = Namespace(name="survey", description="survey")


@ns.route("/<string:survey_id>")
class APISurveyById(frp.Resource):
    def get(self, survey_id):
        resource = SurveyService.get_by_id(survey_id)
        # return {
        #            "success": True
        #        }, 200
        return resource


@ns.route("/filter-table")
class APISurveyFilterTable(frp.Resource):
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
    def post(self, **kwargs):
        resource = SurveyService.filter_table(**kwargs)
        # return {
        #            "success": True
        #        }, 200
        return resource


@ns.route("/options")
class APISurveyOptions(frp.Resource):
    @parse_params(
        Argument("codeOrName", location=["args"], required=False, help="sortBy", type=str, default="code"),
    )
    def get(self, **kwargs):
        resource = SurveyService.get_data_select(kwargs.get("codeOrName"))
        # return {
        #            "success": True
        #        }, 200
        return resource

