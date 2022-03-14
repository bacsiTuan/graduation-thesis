#!/usr/bin/env python
# -*- coding: utf-8 -*-
from loguru import logger
import requests
import json
from app.constants.globals import *

URL = f"{BACKEND_HOST}/referrer"


class ReferrerService(object):
    @classmethod
    def create(cls, **kwargs):
        url = f"{URL}"
        response = requests.post(url, json=json.dumps(kwargs))
        return response.json()

    @classmethod
    def update(cls, **kwargs):
        url = f"{URL}"
        response = requests.put(url, json=json.dumps(kwargs))
        return response.json()

    @classmethod
    def get_by_id(cls, referrer_id):
        url = f"{URL}/{referrer_id}"
        response = requests.get(url)
        return response.json()

    @classmethod
    def delete_by_id(cls, referrer_id):
        url = f"{URL}/{referrer_id}"
        response = requests.delete(url)
        return response.json()

    @classmethod
    def filter_table(cls, **kwargs):
        url = f"{URL}/filter-table"
        data = json.dumps(kwargs)
        response = requests.post(url, json=data, params=data)
        return response.json()

    @classmethod
    def filter_table_less(cls, **kwargs):
        url = f"{URL}/filter-table-less"
        data = json.dumps(kwargs)
        response = requests.post(url, json=data, params=data)
        return response.json()

    @classmethod
    def activate_referrer(cls, referrer_code, confirm_number):
        url = f"{URL}/{referrer_code}/active-referrer/{confirm_number}"
        response = requests.get(url)
        return response.json()

    @classmethod
    def export_excel(cls, **kwargs):
        pass
