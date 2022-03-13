#!/usr/bin/env python
# -*- coding: utf-8 -*-
from loguru import logger
import requests
import json
from app.constants.globals import *

URL = f"{BACKEND_HOST}/response"


class ResponseService(object):
    @classmethod
    def get_response_by_request(cls, request_id):
        url = f"{URL}/request/{request_id}"
        response = requests.get(url)
        return response

    @classmethod
    def delete(cls, response_id):
        url = f"{URL}/{response_id}"
        response = requests.delete(url)
        return response

    @classmethod
    def add_response(cls, **kwargs):
        url = f"{URL}"
        response = requests.put(url, json=json.dumps(kwargs))
        return response
