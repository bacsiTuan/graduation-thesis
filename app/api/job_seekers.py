#!/usr/bin/env python
# -*- coding: utf-8 -*-
from loguru import logger


class JobSeekersService(object):
    @classmethod
    def add_job_seekers(cls, **kwargs):
        pass

    @classmethod
    def update_job_seekers(cls, **kwargs):
        pass

    @classmethod
    def filter_table(cls, **kwargs):
        pass

    @classmethod
    def delete(cls, job_seeker_id):
        pass

    @classmethod
    def get_by_id(cls, job_seeker_id):
        pass

    @classmethod
    def update_experiences(cls, **kwargs):
        pass

    @classmethod
    def update_awards(cls, **kwargs):
        pass

    @classmethod
    def filter_table_less(cls, **kwargs):
        pass

    @classmethod
    def evaluate_job_seeker(cls, **kwargs):
        pass

    @classmethod
    def activate_job_seeker(cls, job_seeker_code, confirm_number):
        pass

    @classmethod
    def export_excel(cls, **kwargs):
        pass
