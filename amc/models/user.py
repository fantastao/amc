# -*- coding: utf-8 -*-

from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug.security import generate_password_hash, check_password_hash

from .base import ModelBase, SurrogatePK, db


class UserModel(SurrogatePK, ModelBase):

    __tablename__ = 'user'

    name = db.Column(db.String(64), nullable=False, unique=True)
    pw_hash = db.Column(db.String(64), nullable=False)
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

    def set_password(self, pw):
        self.password_hash = generate_password_hash(pw)

    def check_password(self, pw):
        return check_password_hash(self.pw_hash, pw)


class CustomModel(ModelBase):

    credit_dict = {
        'high': u'信用情况较好',
        'common': u'信用情况一般',
        'low': u'信用情况较差',
    }

    __tablename__ = 'custom'

    user_id = db.Column(db.Integer(), primary_key=True)
    phone = db.Column(db.String(), nullable=False)
    address = db.Column(db.String(), nullable=False)
    credit = db.Column(db.String(), nullable=False,
                       server_default=credit_dict.get('common'))
    
    user = db.relationship(
        'UserModel',
        primaryjoin='UserModel.id==CustomModel.user_id',
        foreign_keys='UserModel.id',
        uselist=False)


class EmployeeModel(ModelBase):

    __tablename__ = 'employee'

    user_id = db.Column(db.Integer(), primary_key=True)
    department = db.Column(db.String(16), nullable=False)
    
    user = db.relationship(
        'UserModel',
        primaryjoin='UserModel.id==EmployeeModel.user_id',
        foreign_keys='UserModel.id',
        uselist=False)
