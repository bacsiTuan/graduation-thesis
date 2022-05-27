#!/usr/bin/env python
# -*- coding: utf-8 -*-
from loguru import logger
import requests
import json
from app.constants.globals import *

URL = f"{BACKEND_HOST}/position"


class PositionService(object):
    @classmethod
    def create(cls, **kwargs):
        response = requests.post(URL, json=kwargs)
        return response.json()

    @classmethod
    def update(cls, **kwargs):
        response = requests.put(URL, json=kwargs)
        return response.json()

    @classmethod
    def get_by_id(cls, position_id):
        url = f"{URL}/{position_id}"
        response = requests.get(url)
        return response.json()

    @classmethod
    def filter_table(cls, **kwargs):
        url = f"{URL}/filter-table"
        response = requests.post(url, json=kwargs, params=kwargs)
        return response.json()

