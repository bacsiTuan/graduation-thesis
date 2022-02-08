# coding: utf8
from flask import current_app, jsonify
from loguru import logger
from werkzeug.exceptions import HTTPException

from .exceptions import ApiException


def api_error_handler(error):
    if isinstance(error, ApiException):
        logger.warning(
            f'HTTP_STATUS_CODE: {error.status_code} - {error.to_dict}')
        return jsonify(error.to_dict), error.status_code
    if isinstance(error, HTTPException):
        return jsonify({'error': {'code': error.code, 'message': error.description}}), error.code
    return jsonify({'error': {'code': 500, 'message': 'Internal Server Error'}}), 500
