# -*- coding: utf-8 -*-

from .base import ModelBase, SurrogatePK, db


class ProductModel(SurrogatePK, ModelBase):

    __tablename__ = 'product'

    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.UnicodeText(), nullable=True)
    price = db.Column(db.Float(), nullable=False)
    quantity = db.Column(db.Integer(), nullable=False, default=0)
