#!/usr/bin/env python
# -*- coding: utf-8 -*-
from loguru import logger

from app.decorators import sqlalchemy_session
from app import models as m
from app.repositories.users import user_repo
from app.helper import LoginHelper, JWTHelper
from app.errors.exceptions import BadRequest


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
        if login:
            token = JWTHelper.gen_auth_token(
                identity=login.id,
                email=login.email,
                role_id=login.role_id,
            )
            logger.info(token)
            return token

    @classmethod
    def get_by_username(cls, username):
        user = user_repo.find_by_user_name(username)
        if user is None:
            raise BadRequest(message="User not found")
        return user.json

    @classmethod
    @sqlalchemy_session()
    def update(cls, **kwargs):
        params_request = {
            'id': kwargs.get('id'),
            'role_id': kwargs.get('roles'),
            'email': kwargs.get('email'),
            'status': kwargs.get('status'),
            'username': kwargs.get('username'),
        }
        user = user_repo.find_by_user_name(params_request.get('username'))
        if user is None:
            raise BadRequest(message="Không tìm thấy người dùng")

        for key in params_request:
            if key != 'id' and key != 'username' and params_request.get(key) is not None:
                setattr(user, key, params_request.get(key))
        user.save()
        return True
