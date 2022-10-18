#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from sqlalchemy import create_engine, Table, Column, Integer, String
from dotenv import load_dotenv
from app.extensions import db


# sẽ có sẵn 1 vài trường trong mixin
class MyModel(db.Model):
    __tablename__ = "contract"
    name = db.Column(db.String(25))
    is_live = db.Column(db.Boolean, default=False)


# Put at the end of the model module to auto create all models
db.create_all()
