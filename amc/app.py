# -*- coding: utf-8 -*-

from flask import Flask
from amc.extensions import db, migrate

def create_app():
    app = Flask(__name__)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
