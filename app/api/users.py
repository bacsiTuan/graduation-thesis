#!/usr/bin/env python
# -*- coding: utf-8 -*-
from loguru import logger

from app.decorators import sqlalchemy_session
from app import models as m
from app.repositories.users import user_repo
from app.helper import LoginHelper


class UsersService(object):
    @classmethod
    @sqlalchemy_session()
    def create_user(cls, **kwargs):
        user = user_repo.create(**kwargs)
        return user.json

    @classmethod
    def login(cls, **kwargs):
        login = LoginHelper.check_password(
            name=kwargs.get('user_name'),
            pwd=kwargs.get('password')
        )
        return login
