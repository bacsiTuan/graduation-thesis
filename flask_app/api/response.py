# coding: utf8
from flask_restplus import Namespace
import flask_restplus as frp
from loguru import logger
from app.decorators import parse_params, check_token
from flask_restful.reqparse import Argument
from app.api.response import ResponseService
from app.constants import Role

ns = Namespace(name="response", description="response")


@ns.route("/request/<string:request_id>")
class APIResponse(frp.Resource):
    @check_token(role=[Role.HR.value, Role.ADMIN.value])
    def get(self, request_id):
        resource = ResponseService.get_response_by_request(request_id)
        return resource


@ns.route("/<string:response_id>")
class APIResponseById(frp.Resource):
    @check_token(role=[Role.HR.value])
    def delete(self, response_id):
        resource = ResponseService.delete(response_id)
        return resource

    @parse_params(
        Argument("request_id", location=['values', 'json'], required=False, help="request_id", type=str, default=None),
        Argument("survey_id", location=['values', 'json'], required=False, help="survey_id", type=str, default=None),
    )
    @check_token(role=[Role.HR.value])
    def put(self, **kwargs):
        resource = ResponseService.add_response(**kwargs)
        return resource
