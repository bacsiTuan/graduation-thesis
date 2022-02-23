# coding: utf8
import json
import time
import datetime
import jwt
import os
from base64 import b64encode, b64decode

from sqlalchemy.orm import DeclarativeMeta

from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

from time import sleep

from OpenSSL import crypto
from OpenSSL.crypto import X509, dump_publickey, dump_privatekey, load_privatekey, load_publickey
from loguru import logger
import bcrypt
from app.errors.exceptions import Unauthorized, BadRequest

from app.repositories.users import user_repo


class Helper(object):
    @classmethod
    def get_now_unixtimestamp(cls):
        return int(time.time())

    @classmethod
    def get_now_datetime(cls, format_date='%Y-%m-%d %H:%M:%S'):
        now = datetime.datetime.now()
        return now.strftime(format_date)

    @classmethod
    def timestamp_to_time(cls, timestamp: int) -> str:
        if len(str(timestamp)) > 5:
            return datetime.datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
        return ""


class AlchemyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)  # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)


class JWTHelper:
    @staticmethod
    def gen_auth_token(identity, email, role_id) -> str:
        return JWTHelper.encode_auth_token({
            "id": identity,
            "email": email,
            "expired": Helper.get_now_unixtimestamp() + 60 * 60,  # expire in 1h,
            "role": role_id
        })

    @staticmethod
    def encode_auth_token(payload) -> str:
        secret_key = os.environ.get("JWT_SECRET")
        logger.info(secret_key)
        """
        Generates the Auth Token
        :return String
        """
        try:
            return jwt.encode(
                payload,
                secret_key,
                algorithm='HS256'
            ).decode('utf-8')
        except Exception as e:
            logger.exception(e)

    @staticmethod
    def decode_auth_token(token):
        secret_key = os.environ.get("JWT_SECRET")
        """
        Decode the auth token
        """
        try:
            payload = jwt.decode(token, secret_key, algorithms='HS256')
            return payload
        except Exception as e:
            logger.exception(e)
            raise Unauthorized(message="Please log in again.")

            # return None

    @staticmethod
    def validate_token(token):
        data = JWTHelper.decode_auth_token(token)
        if data is None:
            pass
            # raise Unauthorized()

        expired = data.get("expired") or None
        user_id = data.get("id") or None

        if expired is None or user_id is None:
            raise Unauthorized()
        if expired < Helper.get_now_unixtimestamp():
            raise Unauthorized()
        if user_repo.find_active_user(user_id) is None:
            raise Unauthorized()


class LoginHelper(object):
    @staticmethod
    def hash_password(password: str):
        logger.info(1)
        # Encode password into a readable utf-8 byte code:
        password = password.encode('utf-8')
        # Hash the ecoded password and generate a salt:
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
        logger.info(hashed_password.decode('utf-8'))
        return hashed_password.decode('utf-8')

    @staticmethod
    def check_password(name: str, pwd: str):
        user = user_repo.find_by_user_name(name)
        if user is None:
            raise BadRequest(message="Sai tên đăng nhập")
        passwd = pwd.encode('utf-8')
        hashed = user.password.encode('utf-8')
        if bcrypt.checkpw(passwd, hashed):
            return user
        else:
            raise BadRequest(message="Sai mật khẩu")
