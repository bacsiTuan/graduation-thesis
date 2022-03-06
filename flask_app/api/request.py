# coding: utf8
from flask_restplus import Namespace
import flask_restplus as frp
from loguru import logger
from app.decorators import parse_params, check_token, check_token_admin
from flask_restful.reqparse import Argument
from app.api.request import RequestService

ns = Namespace(name="request", description="request")


@ns.route("")
class APIRequest(frp.Resource):
    @parse_params(
        Argument("title", location=['values', 'json'], required=False, help="title", type=str, default=None),
        Argument("type", location=['values', 'json'], required=False, help="type", type=str, default=None),
        Argument("status", location=['values', 'json'], required=False, help="status", type=int, default=None),
        Argument("due_date", location=['values', 'json'], required=False, help="due_date", type=str, default=None),
        Argument("title", location=['values', 'json'], required=False, help="title", type=str, default=None),
    )
    def post(self, **kwargs):
        resource = RequestService.create(**kwargs)
        return {
                   "success": True
               }, 200

    @parse_params(
        Argument("title", location=['values', 'json'], required=False, help="title", type=str, default=None),
        Argument("type", location=['values', 'json'], required=False, help="type", type=str, default=None),
        Argument("id", location=['values', 'json'], required=False, help="id", type=int, default=None),
        Argument("due_date", location=['values', 'json'], required=False, help="due_date", type=str, default=None),
        Argument("title", location=['values', 'json'], required=False, help="title", type=str, default=None),
    )
    def put(self, **kwargs):
        resource = RequestService.update(**kwargs)
        return {
                   "success": True
               }, 200


@ns.route("/<int:request_id>")
class APIRequestById(frp.Resource):
    def get(self, request_id):
        resource = RequestService.get_by_id(request_id)
        return {
                   "success": True
               }, 200

    def delete(self, request_id):
        resource = RequestService.delete_by_id(request_id)
        return {
                   "success": True
               }, 200


@ns.route("/<int:request_id>/unassign")
class APIRequestUnassigned(frp.Resource):
    @parse_params(
        Argument("type", location=["args"], required=False, help="type", type=str, default=None),
    )
    def get(self, request_id):
        resource = RequestService.remove_job_seeker(request_id)
        return {
                   "success": True
               }, 200


@ns.route("job-seeker/<string:job_seeker_id>")
class APIRequestByJobSeeker(frp.Resource):
    @parse_params(
        Argument("type", location=["args"], required=False, help="type", type=str, default=None),
    )
    def get(self, job_seeker_id):
        resource = RequestService.get_simple_request_response_by_job_seeker_id(job_seeker_id)
        return {
                   "success": True
               }, 200