#!/usr/bin/env python
# coding: utf8
from werkzeug.exceptions import default_exceptions
from loguru import logger

from app.errors.handler import api_error_handler
from app.extensions import flask_request_id

from flask import Flask
from flask_cors import CORS


def create_app(config_app):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config_app)
    __init_app(app)
    __config_logging(app)
    __register_blueprint(app)
    __config_error_handlers(app)

    return app


def __config_logging(app):
    logger.info('Start flask...')


def __register_blueprint(app):
    from flask_app.api import bp as api_bp
    app.register_blueprint(api_bp)


def __init_app(app):
    try:
        #     # db_mongo.init_app(app)
        #     redis.init_app(app)
        flask_request_id.init_app(app)
    except Exception as e:
        logger.error(e)


def __config_error_handlers(app):
    for exp in default_exceptions:
        app.register_error_handler(exp, api_error_handler)
    app.register_error_handler(Exception, api_error_handler)
