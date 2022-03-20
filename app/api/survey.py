#!/usr/bin/env python
# -*- coding: utf-8 -*-
from loguru import logger
import requests
import json
from app.constants.globals import *

URL = f"{BACKEND_HOST}/survey"


class SurveyService(object):
    @classmethod
    def get_by_id(cls, survey_id):
        url = f"{URL}/{survey_id}"
        response = requests.get(url)
        return response.json()

    @classmethod
    def filter_table(cls, **kwargs):
        url = f"{URL}/filter-table"
        data = kwargs
        response = requests.post(url, json=data, params=data)
        return response.json()

    @classmethod
    def get_data_select(cls, code_or_name):
        pass

    @classmethod
    def delete_by_id(cls, survey_id):
        url = f"{URL}/{survey_id}"
        response = requests.delete(url)
        return response.json()

    @classmethod
    def create(cls, **kwargs):
        response = requests.post(URL, json=kwargs)
        return response.json()

    @classmethod
    def update(cls, **kwargs):
        response = requests.put(URL, json=kwargs)
        return response.json()
