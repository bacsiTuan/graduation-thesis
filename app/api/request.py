#!/usr/bin/env python
# -*- coding: utf-8 -*-
from loguru import logger


class RequestService(object):
    @classmethod
    def create(cls, **kwargs):
        pass

    @classmethod
    def update(cls, **kwargs):
        pass

    @classmethod
    def get_by_id(cls, request_id):
        pass

    @classmethod
    def delete_by_id(cls, request_id):
        pass

    @classmethod
    def remove_job_seeker(cls, request_id):
        pass

    @classmethod
    def get_simple_request_response_by_job_seeker_id(cls, job_seeker_id):
        pass

    @classmethod
    def find_by_referrer_id(cls, referrer_id):
        pass

    @classmethod
    def find_by_type_and_job_seeker_is_null(cls, **kwargs):
        pass

    @classmethod
    def assign_referrer(cls, **kwargs):
        pass

    @classmethod
    def assign_job_seeker(cls, **kwargs):
        pass

    @classmethod
    def get_data_select(cls, **kwargs):
        pass

    @classmethod
    def filter_table(cls, **kwargs):
        pass

    @classmethod
    def filter_details(cls, **kwargs):
        pass

    @classmethod
    def complete(cls, request_id):
        pass

    @classmethod
    def export_excel(cls, **kwargs):
        pass
