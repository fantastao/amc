# -*- coding: utf-8 -*-

from sqlalchemy import sql

from .base import ModelBase, SurrogatePK, db


class UserModel(SurrogatePK, ModelBase):

    __tablename__ = 'user'

    name = db.Column(db.String(64), nullable=False, unique=True)
    password_hash = db.Column(db.String(64), nullable=False)
    is_custom = db.Column(db.Boolean(), nullable=False,
                          server_default=sql.true())
    is_admin = db.Column(db.Boolean(), nullable=False,
                         server_default=sql.false())
    is_root = db.Column(db.Boolean(), nullable=False,
                        server_default=sql.false())
    date_created = db.Column(db.DateTime(timezone=True),nullable=False,
                             server_default=db.func.current_timestamp())


class CustomModel(ModelBase):

    credit_dict = {
        'high': u'高',
        'common': u'中',
        'low': u'差',
        }

    __tablename__ = 'custom'

    user_id = db.Column(db.Integer(), primary_key=True)
    phone = db.Column(db.String(), nullable=False)
    address = db.Column(db.String(), nullable=False)
    credit = db.Column(db.String(), nullable=False,
                       server_default=credit_dict.get('common'))
