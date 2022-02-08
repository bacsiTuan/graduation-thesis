# coding: utf8
import os
import urllib
from loguru import logger


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "<your secret key>"
    API_URL = os.environ.get("API_URL") or "<your api url>"
    MAXIMUM_USER_API = 3

    # MONGODB_HOST = os.environ.get("DB_MONGO_HOST") or "<your mongodb host>"
    # MONGODB_PORT = int(os.environ.get("DB_MONGO_PORT") or "27017")
    # MONGODB_DB = os.environ.get("DB_MONGO_DATABASE") or "<your mongodb database>"
    # MONGODB_USERNAME = os.environ.get('DB_MONGO_USERNAME') or ""
    # MONGODB_PASSWORD = os.environ.get('DB_MONGO_PASSWORD') or ""
    # MONGODB_REPLICASET = 'rs0'
    # MONGODB_READ_PREFERENCE = 'secondaryPreferred'
    # MONGODB_RETRY_WRITES = 'false'
    # MONGODB_SETTINGS = {
    #     'DB': MONGODB_DB,
    #     'USERNAME': MONGODB_USERNAME,
    #     'PASSWORD': MONGODB_PASSWORD,
    #     'HOST': MONGODB_HOST,
    #     'PORT': MONGODB_PORT,
    #     # 'REPLICASET': MONGODB_REPLICASET,
    #     # 'readPreference': MONGODB_READ_PREFERENCE,
    #     # 'retryWrites': MONGODB_RETRY_WRITES
    # }

    # REDIS_URL = os.environ.get('REDIS_URL') or '<your redis url>'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = "{engine}://{user}:{password}@{host}:{port}/{db}".format(
    #                             engine=os.environ.get("SQLALCHEMY_DATABASE_URI") or "mysql+pymysql",
    #                             user=os.environ.get("SQLALCHEMY_USER") or "<your sql username>",
    #                             password=os.environ.get("SQLALCHEMY_PASSWORD") or "<your sql password>",
    #                             host=os.environ.get("SQLALCHEMY_HOST") or "<your sql host>",
    #                             port=os.environ.get("SQLALCHEMY_PORT") or "<your sql port>",
    #                             db=os.environ.get("SQLALCHEMY_DATABASE") or "<your sql database>"
    #                         )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DB_TYPE = os.environ.get('DB_MYSQL_TYPE')
    DB_CONNECTOR = os.environ.get('DB_MYSQL_CONNECTOR')
    DB_USERNAME = os.environ.get('DB_MYSQL_USER')
    DB_PASSWORD = os.environ.get('DB_MYSQL_PASS')
    DB_HOST = os.environ.get('DB_MYSQL_HOST')
    DB_PORT = os.environ.get('DB_MYSQL_PORT')
    DB_NAME = os.environ.get('DB_MYSQL_DBNAME')
    SQLALCHEMY_DATABASE_URI = f'{DB_TYPE}+{DB_CONNECTOR}://{urllib.parse.quote(DB_USERNAME)}:{urllib.parse.quote(DB_PASSWORD)}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


class TestingConfig(Config):
    TESTING = True


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


configs = {
    "develop": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}
