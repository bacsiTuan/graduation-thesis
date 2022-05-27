# coding: utf8
from loguru import logger
from flask_restful import Resource
# ns = Namespace(name="ping", description="Ping pong")


class APIPing(Resource):
    # @parse_params(
    #     Argument("transaction_id", location=["args"], required=True, help="transaction id", type=str, default=None),
    # )
    @staticmethod
    def get():
        # logger.warning(kwargs)
        logger.warning(1)
        return {"ping": "pong"}, 200
