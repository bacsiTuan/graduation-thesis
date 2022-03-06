#!/usr/bin/env python
# -*- coding: utf-8 -*-
from loguru import logger


class ReferrerService(object):
    @classmethod
    def create(cls, **kwargs):
        pass

    @classmethod
    def update(cls, **kwargs):
        pass

    @classmethod
    def get_by_id(cls, referrer_id):
        pass

    @classmethod
    def delete_by_id(cls, referrer_id):
        pass

    @classmethod
    def filter_table(cls, **kwargs):
        pass

    @classmethod
    def filter_table_less(cls, **kwargs):
        pass

    @classmethod
    def activate_referrer(cls, referrer_code, confirm_number):
        pass

    @classmethod
    def export_excel(cls, **kwargs):
        pass
