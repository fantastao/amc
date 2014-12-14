# -*- coding: utf-8 -*-

from sqlalchemy.ext.hybrid import hybrid_property

from .base import ModelBase, SurrogatePK, db


class OrderModel(SurrogatePK, ModelBase):

    __tablename__ = 'order'

    custom_id = db.Column(db.Integer(), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), nullable=False,
                             server_default=db.func.current_timestamp())

    products = db.relationship(
        'OrderProductModel',
        primaryjoin='OrderModel.id==OrderProductModel.order_id',
        foregin_keys='OrderProductModel.order_id',
        uselist=True)


class OrderProductModel(ModelBase):

    __tablename__ = 'order_product'

    order_id = db.Column(db.Integer(), primary_key=True)
    product_id = db.Column(db.Integer(), primary_key=True)
    product_quantity = db.Column(db.Integer(), nullable=False)
    product_price = db.Column(db.Float(), nullable=False)

    @hybrid_property
    def total_price(self):
        return self.product_quantity * self.product_price
