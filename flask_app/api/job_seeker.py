# coding: utf8
from flask_restplus import Namespace
import flask_restplus as frp
from loguru import logger
from app.decorators import parse_params, check_token, check_token_admin
from flask_restful.reqparse import Argument
from app.api.job_seekers import JobSeekersService

ns = Namespace(name="job-seeker", description="job seeker")


@ns.route("")
class APIJobSeekers(frp.Resource):
    @parse_params(
        Argument("name", location=['values', 'json'], required=False, help="name", type=str, default=None),
        Argument("address", location=['values', 'json'], required=False, help="address", type=str, default=None),
        Argument("email", location=['values', 'json'], required=False, help="email", type=str, default=None),
        Argument("dob", location=['values', 'json'], required=False, help="dob", type=str, default=None),
        Argument("phone_number", location=['values', 'json'], required=False, help="phone_number", type=str,
                 default=None),
        Argument("gender", location=['values', 'json'], required=False, help="gender", type=str, default=None),
        Argument("cccd", location=['values', 'json'], required=False, help="cccd", type=str, default=None),
        Argument("position", location=['values', 'json'], required=False, help="position", type=str, default=None),
        Argument("skills", location=['values', 'json'], required=False, help="skills", type=str, default=None),
        Argument("status", location=['values', 'json'], required=False, help="status", type=str, default=None),
    )
    def post(self, **kwargs):
        try:
            logger.info(kwargs)
            resource = JobSeekersService.add_job_seekers(**kwargs)
            return {
                       "success": True
                   }, 200
        except Exception as e:
            logger.error(e)

    @parse_params(
        Argument("id", location=['values', 'json'], required=False, help="id", type=str, default=None),
        Argument("code", location=['values', 'json'], required=False, help="code", type=str, default=None),
        Argument("name", location=['values', 'json'], required=False, help="name", type=str, default=None),
        Argument("address", location=['values', 'json'], required=False, help="address", type=str, default=None),
        Argument("email", location=['values', 'json'], required=False, help="email", type=str, default=None),
        Argument("dob", location=['values', 'json'], required=False, help="dob", type=str, default=None),
        Argument("phone_number", location=['values', 'json'], required=False, help="phone_number", type=str,
                 default=None),
        Argument("gender", location=['values', 'json'], required=False, help="gender", type=str, default=None),
        Argument("cccd", location=['values', 'json'], required=False, help="cccd", type=str, default=None),
        Argument("position", location=['values', 'json'], required=False, help="position", type=str, default=None),
        Argument("skills", location=['values', 'json'], required=False, help="skills", type=str, default=None),
        Argument("status", location=['values', 'json'], required=False, help="status", type=str, default=None),
    )
    def put(self, **kwargs):
        logger.info(kwargs)
        resource = JobSeekersService.update_job_seekers(**kwargs)
        return {
                   "success": True
               }, 200


@ns.route("/filter-table")
class APIJobSeekersFilter(frp.Resource):
    @parse_params(
        Argument("code", location=['values', 'json'], required=False, help="code", type=str, default=None),
        Argument("name", location=['values', 'json'], required=False, help="name", type=str, default=None),
        Argument("email", location=['values', 'json'], required=False, help="email", type=str, default=None),
        Argument("cccd", location=['values', 'json'], required=False, help="cccd", type=str, default=None),
        Argument("position", location=['values', 'json'], required=False, help="position", type=str, default=None),
        Argument("skills", location=['values', 'json'], required=False, help="skills", type=str, default=None),
        Argument("pageNumber", location=["args"], required=False, help="pageNumber", type=int, default=0),
        Argument("pageSize", location=["args"], required=False, help="pageSize", type=int, default=20),
        Argument("sortType", location=["args"], required=False, help="sortType", type=str, default="ASC"),
        Argument("sortBy", location=["args"], required=False, help="sortBy", type=str, default="code"),
    )
    def post(self, **kwargs):
        try:
            logger.info(kwargs)
            resource = JobSeekersService.filter_table(**kwargs)
            return {
                       "success": True
                   }, 200
        except Exception as e:
            logger.error(e)

# @ns.route("/<int:job_seeker_id>")
# class APIJobSeekersByID(frp.Resource):
