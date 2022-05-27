#!/usr/bin/env python
# -*- coding: utf-8 -*-
from loguru import logger
import requests
import json
from app.constants.globals import *

URL = f"{BACKEND_HOST}/request"


class RequestService(object):
    @classmethod
    def create(cls, **kwargs):
        url = f"{URL}"
        response = requests.post(url, json=kwargs)
        return response.json()

    @classmethod
    def update(cls, **kwargs):
        url = f"{URL}"
        response = requests.put(url, json=kwargs)
        return response.json()

    @classmethod
    def get_by_id(cls, request_id):
        url = f"{URL}/{request_id}"
        response = requests.get(url)
        return response.json()

    @classmethod
    def delete_by_id(cls, request_id):
        url = f"{URL}/{request_id}"
        response = requests.delete(url)
        return response.json()

    @classmethod
    def remove_job_seeker(cls, **kwargs):
        request_id = kwargs.get("request_id")
        url = f"{URL}/{request_id}/unassign"
        response = requests.put(url, params=kwargs)
        return response.json()

    @classmethod
    def get_simple_request_response_by_job_seeker_id(cls, **kwargs):
        job_seeker_id = kwargs.get("job_seeker_id")
        url = f"{URL}/job-seeker/{job_seeker_id}"
        response = requests.get(url, params=kwargs)
        return response.json()

    @classmethod
    def find_by_referrer_id(cls, referrer_id):
        url = f"{URL}/referrer/{referrer_id}"
        response = requests.get(url)
        return response.json()

    @classmethod
    def find_by_type_and_job_seeker_is_null(cls, **kwargs):
        url = f"{URL}/draft"
        response = requests.get(url, params=kwargs)
        return response.json()

    @classmethod
    def assign_referrer(cls, **kwargs):
        url = f"{URL}/assign-referrer"
        response = requests.put(url, json=kwargs)
        return response.json()

    @classmethod
    def assign_job_seeker(cls, **kwargs):
        url = f"{URL}/assign-job-seeker"
        response = requests.put(url, json=kwargs)
        return response.json()

    @classmethod
    def get_data_select(cls, **kwargs):
        url = f"{URL}/data-select"
        response = requests.get(url, params=kwargs)
        return response.json()

    @classmethod
    def filter_table(cls, **kwargs):
        url = f"{URL}/filter-table"
        data = kwargs
        response = requests.post(url, json=data, params=data)
        return response.json()

    @classmethod
    def filter_details(cls, **kwargs):
        url = f"{URL}/filter-details"
        data = kwargs
        response = requests.post(url, json=data, params=data)
        return response.json()

    @classmethod
    def complete(cls, request_id):
        url = f"{URL}/{request_id}/complete"
        response = requests.put(url)
        return response.json()

    @classmethod
    def export_excel(cls, **kwargs):
        pass
