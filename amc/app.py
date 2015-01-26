# -*- coding: utf-8 -*-

from flask import Flask
from werkzeug.utils import import_string

from amc.extensions import db, migrate, login_manager
from amc._settings import DevConfig

bps = [
    'amc.views.home:bp',
    'amc.views.auth:bp',
    'amc.views.products:bp',
    'amc.views.orders:bp',
    'amc.panel.management:bp',
]


def create_app(config=DevConfig):
    app = Flask(__name__, static_folder=config.STATIC_FOLDER)
    app.config.from_object(config)
    register_blueprints(app)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'


def register_blueprints(app):
    for bp in bps:
        app.register_blueprint(import_string(bp))
