# coding: utf8
from flask import Blueprint
from flask_restplus import Api

from flask_app.api.ping import ns as ping_ns
from flask_app.api.tasks import ns as task_ns
from flask_app.api.users import ns as user_ns
from flask_app.api.job_seeker import ns as job_seeker_ns
from flask_app.api.referrer import ns as referrer_ns
from flask_app.api.request import ns as request_ns
from flask_app.api.response import ns as response_ns
from flask_app.api.survey import ns as survey_ns
from flask_app.api.position import ns as position_ns
from flask_app.api.skill import ns as skill_ns

bp = Blueprint("api", __name__, url_prefix="/v1")

api = Api()
api.init_app(bp, version="1.0", title="Flask API", description="Flask API", ui=False, doc=False, add_specs=False)

api.add_namespace(ns=ping_ns)
api.add_namespace(ns=task_ns)
api.add_namespace(ns=user_ns)
api.add_namespace(ns=job_seeker_ns)
api.add_namespace(ns=referrer_ns)
api.add_namespace(ns=request_ns)
api.add_namespace(ns=response_ns)
api.add_namespace(ns=survey_ns)
api.add_namespace(ns=position_ns)
api.add_namespace(ns=skill_ns)
