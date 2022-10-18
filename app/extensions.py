# coding: utf8
import os
import urllib.parse
from dotenv import load_dotenv

load_dotenv(override=False)
import mongoengine
from flask_redis import FlaskRedis
from tuan_lib.database import ActiveAlchemy  # noqa
from tuan_lib.http import FlaskRequestId  # noqa

# redis = FlaskRedis()
#
# MONGODB_HOST = os.environ.get("DB_MONGO_HOST") or "<your mongodb host>"
# MONGODB_PORT = int(os.environ.get("DB_MONGO_PORT") or "27017")
# MONGODB_DB = os.environ.get("DB_MONGO_DATABASE") or "<your mongodb database>"
# MONGODB_USERNAME = os.environ.get('DB_MONGO_USERNAME') or None
# MONGODB_PASSWORD = os.environ.get('DB_MONGO_PASSWORD') or None
# MONGODB_REPLICASET = os.environ.get('DB_MONGODB_REPLICASET') or None  # 'rs0'
# MONGODB_READ_PREFERENCE = os.environ.get('MONGODB_READ_PREFERENCE') or 'secondaryPreferred'
# MONGODB_RETRY_WRITES = 'false'
#
# MONGODB_URL = f'mongodb://'
# if MONGODB_USERNAME is not None and MONGODB_PASSWORD is not None:
#     MONGODB_URL = f'{MONGODB_URL}{urllib.parse.quote(MONGODB_USERNAME)}:{urllib.parse.quote(MONGODB_PASSWORD)}@{MONGODB_HOST}:{MONGODB_PORT}/'
# else:
#     MONGODB_URL = f'{MONGODB_URL}{MONGODB_HOST}:{MONGODB_PORT}/'
#
# if MONGODB_DB is not None:
#     MONGODB_URL = f'{MONGODB_URL}{MONGODB_DB}'
# MONGODB_URL = f'{MONGODB_URL}?retryWrites={MONGODB_RETRY_WRITES}'
# if MONGODB_READ_PREFERENCE is not None:
#     MONGODB_URL = f'{MONGODB_URL}&readPreference={MONGODB_READ_PREFERENCE}'
# if MONGODB_REPLICASET is not None:
#     MONGODB_URL = f'{MONGODB_URL}&replicaSet={MONGODB_REPLICASET}'
#
# db_mongo = mongoengine.connect(host=MONGODB_URL)
DB_TYPE = os.environ['DB_MYSQL_TYPE'] or 'mysql'
DB_CONNECTOR = os.environ['DB_MYSQL_CONNECTOR'] or 'pymysql'
DB_USERNAME = os.environ['DB_MYSQL_USER']
DB_PASSWORD = os.environ['DB_MYSQL_PASS']
DB_HOST = os.environ['DB_MYSQL_HOST']
DB_PORT = os.environ['DB_MYSQL_PORT']
DB_NAME = os.environ['DB_MYSQL_DBNAME']
DATABASE_URL = f'{DB_TYPE}+{DB_CONNECTOR}://{urllib.parse.quote(DB_USERNAME)}:{urllib.parse.quote(DB_PASSWORD)}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

db = ActiveAlchemy(DATABASE_URL)
flask_request_id = FlaskRequestId()
