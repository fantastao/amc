# -*- coding: utf-8 -*-

from .base import ModelBase, SurrogatePK, db


# product divide into different categories with attributions
PRODUCT_CATEGORIES = []

class ProductModel(SurrogatePK, ModelBase):

    __tablename__ = 'product'

    name = db.Column(db.String(64), nullable=False)
    category = db.Column(db.String(64), nullable=False)
    description = db.Column(db.UnicodeText(), nullable=True)
    price = db.Column(db.Float(), nullable=False)
    quantity = db.Column(db.Integer(), nullable=False, default=0)
    date_created = db.Column(db.DateTime(timezone=True), nullable=False,
                             server_default=db.func.current_timestamp())
    date_updated = db.Column(db.DateTime(timezone=True), nullable=False,
                             server_default=db.func.current_timestamp())

    # 产品的订单
    product_orders = db.relationship(
        'OrderProductModel',
        backref='product',
        primaryjoin='ProductModel.id==OrderProductModel.product_id',
        foreign_keys='OrderProductModel.product_id',
        uselist=True)


class LackedProductHistoryModel(SurrogatePK, ModelBase):
    
    __tablename__ = 'lacked_product_history'

    product_id = db.Column(db.Integer(), nullable=False, index=True)
    order_id = db.Column(db.Integer(), nullable=False, index=True)
    quantity = db.Column(db.Integer(), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), nullable=False,
                             server_default=db.func.current_timestamp())
