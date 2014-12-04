# -*- coding: utf-8 -*-

from flask import Flask

from amc.extensions import db, migrate
from amc._settings import DevConfig


def create_app(config=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
