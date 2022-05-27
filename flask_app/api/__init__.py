# coding: utf8
from flask import Blueprint
from flask_restful import Api

from flask_app.api.ping import APIPing
from flask_app.api.tasks import APITasks
from flask_app.api.users import (
    APIUser,
    APILogin,
    APIFilterTable,
    APIUserById
)
from flask_app.api.job_seeker import (
    APIJobSeekers,
    APIJobSeekersFilter,
    APIJobSeekersByID,
    APIJobSeekersExperience,
    APIJobSeekersAwards,
    APIJobSeekersFilterTableLess,
    APIJobSeekersReferrerSettings,
    APIJobSeekersEvaluate,
    APIActivateJobSeeker,
    APIExportExcel
)

from flask_app.api.referrer import (
    APIReferrer,
    APIReferrerById,
    APIReferrerFilterTable,
    APIReferrerFilterTableLess,
    APIReferrerActivateReferrer,
    APIReferrerExportExcel,
)
from flask_app.api.request import (
    APIRequest,
    APIRequestById,
    APIRequestUnassigned,
    APIRequestByJobSeeker,
    APIRequestFindByReferrerId,
    APIRequestDraft,
    APIRequestAssignReferrer,
    APIRequestAssignJobSeeker,
    APIRequestDataSelect,
    APIRequestFilterTable,
    APIRequestFilterDetails,
    APIRequestComplete,
    APIRequestExportExcel
)
from flask_app.api.response import (
    APIResponse,
    APIResponseById
)
from flask_app.api.survey import (
    APISurvey,
    APISurveyById,
    APISurveyFilterTable,
    APISurveyOptions
)
from flask_app.api.position import (
    APIPosition,
    APIPositionById,
    APIPositionFilterTable,
)

from flask_app.api.skill import (
    APISkill,
    APISkillById,
    APISkillFilterTable
)

bp = Blueprint("api", __name__, url_prefix="/references/api/1.0")

api = Api(bp)

api.add_resource(APIPing, "/ping")

api.add_resource(APITasks, "/tasks")

# API user
api.add_resource(APIUser, "/users")
api.add_resource(APILogin, "/users/login")
api.add_resource(APIFilterTable, "/users/filter-table")
api.add_resource(APIUserById, "/users/<string:user_id>")

# API job seekers
api.add_resource(APIJobSeekers, "/job-seeker")
api.add_resource(APIJobSeekersFilter, "/job-seeker/filter-table")
api.add_resource(APIJobSeekersByID, "/job-seeker/<string:job_seeker_id>")
api.add_resource(APIJobSeekersExperience, "/job-seeker/experiences")
api.add_resource(APIJobSeekersAwards, "/job-seeker/awards")
api.add_resource(APIJobSeekersFilterTableLess, "/job-seeker/filter-table-less")
api.add_resource(APIJobSeekersEvaluate, "/job-seeker/evaluate")
api.add_resource(APIActivateJobSeeker, "/job-seeker/<string:job_seeker_code>/activate-job-seeker/<int:confirm_number>")
api.add_resource(APIExportExcel, "/job-seeker/export-excel")

# API referrer
api.add_resource(APIReferrer, "/referrer")
api.add_resource(APIReferrerById, "/referrer/<string:referrer_id>")
api.add_resource(APIReferrerFilterTable, "/referrer/filter-table")
api.add_resource(APIReferrerFilterTableLess, "/referrer/filter-table-less")
api.add_resource(APIReferrerActivateReferrer,
                 "/referrer/<string:referrer_code>/active-referrer/<string:confirm_number>")
api.add_resource(APIReferrerExportExcel, "/referrer/export-excel")

# API request
api.add_resource(APIRequest, "/request")
api.add_resource(APIRequestById, "/request/<string:request_id>")
api.add_resource(APIRequestUnassigned, "/request/<string:request_id>/unassign")
api.add_resource(APIRequestByJobSeeker, "/request/job-seeker/<string:job_seeker_id>")
api.add_resource(APIRequestFindByReferrerId, "/request/referrer/<string:referrer_id>")
api.add_resource(APIRequestDraft, "/request/draft")
api.add_resource(APIRequestAssignReferrer, "/request/assign-referrer")
api.add_resource(APIRequestAssignJobSeeker, "/request/assign-job-seeker")
api.add_resource(APIRequestDataSelect, "/request/data-select")
api.add_resource(APIRequestFilterTable, "/request/filter-table")
api.add_resource(APIRequestFilterDetails, "/request/filter-details")
api.add_resource(APIRequestComplete, "/request/<string:request_id>/complete")
api.add_resource(APIRequestExportExcel, "/request/export-excel")

# API response
api.add_resource(APIResponse, "/response/request/<string:request_id>")
api.add_resource(APIResponseById, "/response/<string:response_id>")

# API survey
api.add_resource(APISurvey, "/survey")
api.add_resource(APISurveyById, "/survey/<string:survey_id>")
api.add_resource(APISurveyFilterTable, "/survey/filter-table")
api.add_resource(APISurveyOptions, "/survey/options")

# API position
api.add_resource(APIPosition, "/position")
api.add_resource(APIPositionById, "/position/<string:position_id>")
api.add_resource(APIPositionFilterTable, "/position/filter-table")

# API skill
api.add_resource(APISkill, "/skill")
api.add_resource(APISkillById, "/skill/<string:skill_id>")
api.add_resource(APISkillFilterTable, "/skill/filter-table")
