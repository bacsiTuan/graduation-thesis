# coding: utf8
from app import models as m
from app import helper
from loguru import logger


class UserRepository(object):
    def create(self, **kwargs):
        logger.info(1)
        user = m.Users(
            id=kwargs.get('id'),
            email=kwargs.get('email'),
            password=helper.LoginHelper.hash_password(kwargs.get('password')),
            username=kwargs.get('username'),
        )
        user.save()
        return user

    def find_by_user_name(self, user_name):
        user = m.Users.query().filter(
            m.Users.username == user_name,
        ).first()
        return user


user_repo = UserRepository()
