# -*- coding: utf-8 -*-

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate
from flask.ext.login import LoginManager


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
