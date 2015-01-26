# -*- coding: utf-8 -*-

from .base import ModelBase, SurrogatePK, db


# product divide into different categories with attributions
PRODUCT_CATEGORIES = ['G', 'M', 'S']


class ProductModel(SurrogatePK, ModelBase):

    __tablename__ = 'product'

    name = db.Column(db.String(64), nullable=False, index=True)
    category = db.Column(db.String(64), nullable=False, default='M')
    description = db.Column(db.UnicodeText(), nullable=True)
    price = db.Column(db.Float(), nullable=False, index=True)
    quantity = db.Column(db.Integer(), nullable=False, default=0)
    made_in = db.Column(db.String(64), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True),
                             nullable=False, index=True,
                             server_default=db.func.current_timestamp())
    date_updated = db.Column(db.DateTime(timezone=True),
                             nullable=False, index=True,
                             server_default=db.func.current_timestamp())


class LackedProductHistoryModel(SurrogatePK, ModelBase):

    __tablename__ = 'lacked_product_history'

    product_id = db.Column(db.Integer(), nullable=False, index=True)
    order_id = db.Column(db.Integer(), nullable=False, index=True)
    quantity = db.Column(db.Integer(), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), nullable=False,
                             server_default=db.func.current_timestamp())
