# coding: utf8
from flask_restplus import Namespace
import flask_restplus as frp
from loguru import logger
from app.decorators import parse_params
from flask_restful.reqparse import Argument
from app.api.tasks import TasksService
ns = Namespace(name="tasks", description="tasks ")


@ns.route("")
class APITasks(frp.Resource):
    @parse_params(
        Argument("task", location=['values', 'json'], required=True, help="task name", type=str, default=None),
    )
    def post(self, **kwargs):
        try:
            logger.warning(kwargs)
            tasks = TasksService.create_task(**kwargs)
            logger.warning(1)
            return {
                "success": True,
                "data": tasks
            }, 200
        except Exception as e:
            logger.error(e)
