# coding: utf8
from flask_restplus import Namespace
import flask_restplus as frp
from loguru import logger
from app.decorators import parse_params, check_token
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
    )
    def post(self, **kwargs):
        resource = RequestService.create(**kwargs)
        # return {
        #            "success": True
        #        }, 200
        return resource

    @parse_params(
        Argument("title", location=['values', 'json'], required=False, help="title", type=str, default=None),
        Argument("type", location=['values', 'json'], required=False, help="type", type=str, default=None),
        Argument("id", location=['values', 'json'], required=False, help="id", type=str, default=None),
        Argument("due_date", location=['values', 'json'], required=False, help="due_date", type=str, default=None),
        Argument("title", location=['values', 'json'], required=False, help="title", type=str, default=None),
    )
    def put(self, **kwargs):
        resource = RequestService.update(**kwargs)
        # return {
        #            "success": True
        #        }, 200
        return resource


@ns.route("/<string:request_id>")
class APIRequestById(frp.Resource):
    def get(self, request_id):
        resource = RequestService.get_by_id(request_id)
        # return {
        #            "success": True
        #        }, 200
        return resource

    def delete(self, request_id):
        resource = RequestService.delete_by_id(request_id)
        # return {
        #            "success": True
        #        }, 200
        return resource


@ns.route("/<string:request_id>/unassign")
class APIRequestUnassigned(frp.Resource):
    @parse_params(
        Argument("type", location=["args"], required=False, help="type", type=str, default=None),
    )
    def put(self, request_id, **kwargs):
        kwargs['request_id'] = request_id
        resource = RequestService.remove_job_seeker(**kwargs)
        # return {
        #            "success": True
        #        }, 200
        return resource


@ns.route("/job-seeker/<string:job_seeker_id>")
class APIRequestByJobSeeker(frp.Resource):
    @parse_params(
        Argument("type", location=["args"], required=False, help="type", type=str, default=None),
    )
    def get(self, job_seeker_id, **kwargs):
        kwargs['job_seeker_id'] = job_seeker_id
        resource = RequestService.get_simple_request_response_by_job_seeker_id(**kwargs)
        # return {
        #            "success": True
        #        }, 200
        return resource


@ns.route("/referrer/<string:referrer_id>")
class APIRequestFindByReferrerId(frp.Resource):
    # findByReferrerId
    def get(self, referrer_id):
        resource = RequestService.find_by_referrer_id(referrer_id)
        # return {
        #            "success": True
        #        }, 200
        return resource


@ns.route("/draft")
class APIRequestDraft(frp.Resource):
    @parse_params(
        Argument("type", location=["args"], required=False, help="type", type=str, default=None),
        Argument("pageNumber", location=["args"], required=False, help="pageNumber", type=int, default=0),
        Argument("pageSize", location=["args"], required=False, help="pageSize", type=int, default=20),
        Argument("sortType", location=["args"], required=False, help="sortType", type=str, default="ASC"),
        Argument("sortBy", location=["args"], required=False, help="sortBy", type=str, default="code"),
    )
    def get(self, **kwargs):
        resource = RequestService.find_by_type_and_job_seeker_is_null(**kwargs)
        # return {
        #            "success": True
        #        }, 200
        return resource


@ns.route("/assign-referrer")
class APIRequestAssignReferrer(frp.Resource):
    # AssignReferrerDTO
    @parse_params(
        Argument("request_id", location=['values', 'json'], required=False, help="request_id", type=str, default=None),
        Argument("referrer_id", location=['values', 'json'], required=False, help="referrer_id", type=str,
                 default=None),
        Argument("relationship_type", location=['values', 'json'], required=False, help="relationship_type", type=str,
                 default=None),
        Argument("relationship_desc", location=['values', 'json'], required=False, help="relationship_desc", type=str,
                 default=None),
    )
    def put(self, **kwargs):
        resource = RequestService.assign_referrer(**kwargs)
        # return {
        #            "success": True
        #        }, 200
        return resource


@ns.route("/assign-job-seeker")
class APIRequestAssignJobSeeker(frp.Resource):
    # AssignJobSeekerDTO
    @parse_params(
        Argument("request_id", location=['values', 'json'], required=False, help="request_id", type=str, default=None),
        Argument("job_seeker_id", location=['values', 'json'], required=False, help="job_seeker_id", type=str,
                 default=None),
    )
    def put(self, **kwargs):
        resource = RequestService.assign_job_seeker(**kwargs)
        # return {
        #            "success": True
        #        }, 200
        return resource


@ns.route("/data-select")
class APIRequestDataSelect(frp.Resource):
    @parse_params(
        Argument("codeOrName", location=["args"], required=False, help="codeOrName", type=str, default="code"),
    )
    def get(self, **kwargs):
        resource = RequestService.get_data_select(**kwargs)
        # return {
        #            "success": True
        #        }, 200
        return resource


@ns.route("/filter-table")
class APIRequestFilterTable(frp.Resource):
    @parse_params(
        Argument("title", location=['values', 'json'], required=False, help="title", type=str, default=None),
        Argument("to_due_date", location=['values', 'json'], required=False, help="to_due_date", type=str,
                 default=None),
        Argument("from_due_date", location=['values', 'json'], required=False, help="from_due_date", type=str,
                 default=None),
        Argument("job_seeker", location=['values', 'json'], required=False, help="job_seeker", type=str, default=None),
        Argument("referrer", location=['values', 'json'], required=False, help="referrer", type=str, default=None),
        Argument("pageNumber", location=["args"], required=False, help="pageNumber", type=int, default=0),
        Argument("pageSize", location=["args"], required=False, help="pageSize", type=int, default=20),
        Argument("sortType", location=["args"], required=False, help="sortType", type=str, default="ASC"),
        Argument("sortBy", location=["args"], required=False, help="sortBy", type=str, default="code"),
    )
    def post(self, **kwargs):
        resource = RequestService.filter_table(**kwargs)
        # return {
        #            "success": True
        #        }, 200
        return resource


@ns.route("/filter-details")
class APIRequestFilterDetails(frp.Resource):
    @parse_params(
        Argument("title", location=['values', 'json'], required=False, help="title", type=str, default=None),
        Argument("to_due_date", location=['values', 'json'], required=False, help="to_due_date", type=str,
                 default=None),
        Argument("from_due_date", location=['values', 'json'], required=False, help="from_due_date", type=str,
                 default=None),
        Argument("to_created_at", location=['values', 'json'], required=False, help="to_created_at", type=str,
                 default=None),
        Argument("from_created_at", location=['values', 'json'], required=False, help="from_created_at", type=str,
                 default=None),
        Argument("job_seeker", location=['values', 'json'], required=False, help="job_seeker", type=str, default=None),
        Argument("type", location=['values', 'json'], required=False, help="type", type=str, default=None),
        Argument("referrer", location=['values', 'json'], required=False, help="referrer", type=str, default=None),
        Argument("pageNumber", location=["args"], required=False, help="pageNumber", type=int, default=0),
        Argument("pageSize", location=["args"], required=False, help="pageSize", type=int, default=20),
        Argument("sortType", location=["args"], required=False, help="sortType", type=str, default="ASC"),
        Argument("sortBy", location=["args"], required=False, help="sortBy", type=str, default="code"),
    )
    def post(self, **kwargs):
        resource = RequestService.filter_details(**kwargs)
        # return {
        #            "success": True
        #        }, 200
        return resource


@ns.route("/<string:request_id>/complete")
class APIRequestComplete(frp.Resource):
    def put(self, request_id):
        resource = RequestService.complete(request_id)
        # return {
        #            "success": True
        #        }, 200
        return resource


@ns.route("/export-excel")
class APIRequestExportExcel(frp.Resource):
    @parse_params(
        Argument("title", location=['values', 'json'], required=False, help="title", type=str, default=None),
        Argument("to_due_date", location=['values', 'json'], required=False, help="to_due_date", type=str,
                 default=None),
        Argument("from_due_date", location=['values', 'json'], required=False, help="from_due_date", type=str,
                 default=None),
        Argument("job_seeker", location=['values', 'json'], required=False, help="job_seeker", type=str, default=None),
        Argument("referrer", location=['values', 'json'], required=False, help="referrer", type=str, default=None),
        Argument("sortBy", location=["args"], required=False, help="sortBy", type=str, default="code"),
    )
    def post(self, **kwargs):
        resource = RequestService.export_excel(**kwargs)
        # return {
        #            "success": True
        #        }, 200
        return resource
