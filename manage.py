#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from dotenv import load_dotenv
load_dotenv(override=False)

from flask_app import create_app  # noqa
from app.config import configs as config  # noqa

config_name = os.environ.get('FLASK_CONFIG') or 'develop'
config_app = config[config_name]
application = app = create_app(config_app)
