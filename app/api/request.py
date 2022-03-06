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
