# -*- coding: utf-8 -*-

from sqlalchemy import sql
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from .base import ModelBase, SurrogatePK, db


class AuthModel(SurrogatePK, ModelBase):

    __tablename__ = 'auth'

    user_id = db.Column(db.Integer(), nullable=False)
    account = db.Column(db.String(64), nullable=False, unique=True)
    pw_hash = db.Column(db.String(256), nullable=False)
    is_verified = db.Column(db.Boolean(), nullable=False,
                            server_default=sql.false())
    date_created = db.Column(db.DateTime(timezone=True), nullable=False,
                             server_default=db.func.current_timestamp())

    user = db.relationship(
        'UserModel',
        primaryjoin='UserModel.id==AuthModel.user_id',
        foreign_keys='AuthModel.user_id')

    @classmethod
    def get_by_account(cls, account):
        return cls.query.filter_by(account=account).first()

    @classmethod
    def account_exists_verified(cls, account):
        try:
            auth = cls.query.filter_by(account=account).one()
        except MultipleResultsFound as e:
            raise e  # should never happen
        except NoResultFound as e:
            return False
        if auth and auth.is_verified:
            return True
        return False
