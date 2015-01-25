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

    __tablename__ = 'user'

    name = db.Column(db.String(64), nullable=False, index=True)
    avatar = db.Column(db.String(512), nullable=False,
                       default=ProdConfig.AVATAR_DEFAULT)
    phone = db.Column(db.String(), nullable=True)
    address = db.Column(db.String(), nullable=True)
    date_created = db.Column(db.DateTime(timezone=True), nullable=False,
                             server_default=db.func.current_timestamp())

    @hybrid_property
    def is_custom(self):
        custom = CustomModel.query.get(self.id)
        return True if custom else False

    @hybrid_property
    def is_employee(self):
        employee = EmployeeModel.query.get(self.id)
        return True if employee else False


class CustomModel(ModelBase):

    credit_dict = {
        'high': u'信用情况较好',
        'common': u'信用情况一般',
        'low': u'信用情况较差',
    }

    __tablename__ = 'custom'

    user_id = db.Column(db.Integer(), primary_key=True)
    credit = db.Column(db.String(), nullable=False, index=True,
                       default=credit_dict.get('common'))

    user = db.relationship(
        'UserModel', backref='custom',
        primaryjoin='UserModel.id==CustomModel.user_id',
        foreign_keys='UserModel.id',
        uselist=False)

    trolley = db.relationship(
        'ShoppingTrolleyModel',
        backref='custom',
        primaryjoin='CustomModel.user_id==ShoppingTrolleyModel.custom_id',
        foreign_keys='ShoppingTrolleyModel.custom_id',
        uselist=True)


class EmployeeModel(ModelBase):

    __tablename__ = 'employee'

    user_id = db.Column(db.Integer(), primary_key=True)
    department = db.Column(db.String(16), nullable=False)

    user = db.relationship(
        'UserModel', backref='employee',
        primaryjoin='UserModel.id==EmployeeModel.user_id',
        foreign_keys='UserModel.id',
        uselist=False)
