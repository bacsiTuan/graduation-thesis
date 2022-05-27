# coding: utf8
"""
Define the Users Model
"""
from app import helper
from app.extensions import db
from app.models.abc import BaseModel, MetaBaseModel
import datetime
from sqlalchemy import Column, DateTime
from app.constants import Status


class Users(db.BaseModel, BaseModel, metaclass=MetaBaseModel):
    """users Model"""

    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.String, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    created_by = db.Column(db.String, index=False, unique=False, nullable=True)
    email = db.Column(db.String, index=False, unique=False, nullable=True)
    password = db.Column(db.String, index=False, unique=False, nullable=True)
    role_id = db.Column(db.Integer, index=False, unique=False, nullable=False)
    status = db.Column(db.Integer, index=False, unique=False, nullable=False)
    updated_at = db.Column(db.String, index=False, unique=False, nullable=True)
    updated_by = db.Column(db.String, index=False, unique=False, nullable=True)
    username = db.Column(db.String, index=False, unique=False, nullable=True)
    job_seeker_id = db.Column(db.String, index=False, unique=False, nullable=True)

    def __init__(self, **kwargs):
        """ Create a new user """
        self.id = kwargs.get("id") or helper.Helper.create_uuid()
        self.created_at = kwargs.get("created_at") or helper.Helper.get_now_datetime()
        self.created_by = kwargs.get("created_by") or None
        self.email = kwargs.get("email") or None
        self.password = kwargs.get("password") or None
        self.role_id = kwargs.get("role_id") or 0
        self.status = kwargs.get("status") or Status.ON.value
        self.updated_at = kwargs.get("updated_at") or helper.Helper.get_now_datetime()
        self.updated_by = kwargs.get("updated_by") or None
        self.username = kwargs.get("username") or None
        self.job_seeker_id = kwargs.get("job_seeker_id") or None
