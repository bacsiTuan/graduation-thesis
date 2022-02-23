# coding: utf8
from app import models as m
from app import helper
from loguru import logger
from app.constants import Status


class UserRepository(object):
    def create(self, **kwargs):
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

    def find_active_user(self, user_id):
        user = m.Users.query().filter(
            m.Users.id == user_id,
            m.Users.status == Status.ON.value
        ).first()
        return user


user_repo = UserRepository()
