# coding: utf8
from flask import Blueprint


bp = Blueprint("errors", __name__)


from app.errors import handler  # noqa
