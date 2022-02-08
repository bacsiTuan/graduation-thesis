# coding: utf8
from flask_restplus import Namespace
import flask_restplus as frp
from loguru import logger

ns = Namespace(name="ping", description="Ping pong")


@ns.route("")
class APIPing(frp.Resource):
    # @parse_params(
    #     Argument("transaction_id", location=["args"], required=True, help="transaction id", type=str, default=None),
    # )
    def get(self, **kwargs):
        logger.warning(kwargs)
        logger.warning(1)
        return {"ping": "pong"}, 200
