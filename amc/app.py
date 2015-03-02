# -*- coding: utf-8 -*-

from flask import Flask
from werkzeug.utils import import_string

from amc.extensions import db, migrate, login_manager
from amc._settings import DevConfig

bps = [
    # 'amc.apis.open:bp',
    # 'amc.apis.panel:bp',
    'amc.views.home:bp',
    'amc.views.auth:bp',
    'amc.views.products:bp',
    'amc.views.orders:bp',
    'amc.views.users:bp',
    'amc.panel.index:bp',
    'amc.panel.user_admin:bp',
    'amc.panel.order_admin:bp',
    'amc.panel.product_admin:bp',
    'amc.panel.purchase_admin:bp',
    'amc.panel.pay_admin:bp',
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
