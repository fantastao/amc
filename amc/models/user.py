# -*- coding: utf-8 -*-

from sqlalchemy.ext.hybrid import hybrid_property
from flask.ext.login import UserMixin

from amc.extensions import login_manager
from amc._settings import ProdConfig

from .base import ModelBase, SurrogatePK, db


@login_manager.user_loader
def load_user(user_id):
    return UserModel.query.get(user_id)


class UserModel(SurrogatePK, ModelBase, UserMixin):

    credit_dict = {
        'high': u'信用情况较好',
        'common': u'信用情况一般',
        'low': u'信用情况较差',
    }

    __tablename__ = 'user'

    name = db.Column(db.String(64), nullable=False, index=True)
    avatar = db.Column(db.String(512), nullable=False,
                       default=ProdConfig.AVATAR_DEFAULT)
    phone = db.Column(db.String(), nullable=True)
    address = db.Column(db.String(), nullable=True)
    credit = db.Column(db.String(), nullable=False, index=True,
                       default=credit_dict.get('common'))
    date_created = db.Column(db.DateTime(timezone=True), nullable=False,
                             server_default=db.func.current_timestamp())

    auth = db.relationship(
        'AuthModel',
        backref='user',
        primaryjoin='UserModel.id==AuthModel.user_id',
        foreign_keys='AuthModel.user_id',
        uselist=False)

    trolley = db.relationship(
        'ShoppingTrolleyModel',
        backref='user',
        primaryjoin='UserModel.id==ShoppingTrolleyModel.user_id',
        foreign_keys='ShoppingTrolleyModel.user_id',
        uselist=False)

    orders = db.relationship(
        'OrderModel',
        backref='user',
        primaryjoin='UserModel.id==OrderModel.user_id',
        foreign_keys='OrderModel.user_id',
        uselist=True)

    @hybrid_property
    def is_admin(self):
        admin = AdminModel.query.get(self.id)
        return True if admin else False


class AdminModel(ModelBase):

    __tablename__ = 'admin'

    user_id = db.Column(db.Integer(), primary_key=True)
    department = db.Column(db.String(16), nullable=False)

    user = db.relationship(
        'UserModel', backref='admin',
        primaryjoin='UserModel.id==AdminModel.user_id',
        foreign_keys='AdminModel.user_id',
        uselist=False)
