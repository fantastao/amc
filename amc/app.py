# -*- coding: utf-8 -*-

from flask import Flask
from werkzeug.utils import import_string

from amc.extensions import db, migrate
from amc._settings import DevConfig

bps = [
    'amc.views.home:bp',
]


def create_app(config=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    for bp in bps:
        app.register_blueprint(import_string(bp))
