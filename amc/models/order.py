# -*- coding: utf-8 -*-

from sqlalchemy.ext.hybrid import hybrid_property

from .base import ModelBase, SurrogatePK, db


class OrderModel(SurrogatePK, ModelBase):

    STATUS_LAUNCH = 'launch'
    STATUS_CONFIRM = 'confirm'
    STATUS_DISPATCH = 'dispatch'
    STATUS_SUCCESS = 'success'
    STATUS_RETURN = 'return'
    STATUS_CANCEL = 'cancel'

    __tablename__ = 'order'

    custom_id = db.Column(db.Integer(), nullable=False)
    status = db.Column(db.String(64), nullable=False,
                       index=True, default=STATUS_LAUNCH)
    date_created = db.Column(db.DateTime(timezone=True),
                             nullable=False, index=True,
                             server_default=db.func.current_timestamp())
    date_updated = db.Column(db.DateTime(timezone=True),
                             nullable=False, index=True,
                             server_default=db.func.current_timestamp())

    # 订单的产品
    order_products = db.relationship(
        'OrderProductModel',
        backref='order',
        primaryjoin='OrderModel.id==OrderProductModel.order_id',
        foreign_keys='OrderProductModel.order_id',
        uselist=True)

    pay = db.relationship(
        'Pay',backref='order',
        primaryjoin='PayModel.order_id==Order.id',
        foreign_keys='PayModel.order_id',
        uselist=False)

    @hybrid_property
    def order_price(self):
        order_fee = 0
        for product in self.order_products:
            order_fee += product.total_price
        return order_fee

    @hybrid_property
    def is_supplied(self):
        for order_product in self.order_products:
            if not order_product.is_supplied:
                return False
        return True


class OrderProductModel(ModelBase):

    __tablename__ = 'order_product'

    order_id = db.Column(db.Integer(), primary_key=True)
    product_id = db.Column(db.Integer(), primary_key=True)
    product_quantity = db.Column(db.Integer(), nullable=False)
    product_price = db.Column(db.Float(), nullable=False)

    @hybrid_property
    def total_price(self):
        return self.product_quantity * self.product_price

    @hybrid_property
    def is_supplied(self):
        if self.product_quantity > self.product.quantity:
            return False
        return True


class OrderHistoryModel(SurrogatePK, ModelBase):

    __tablename__ = 'order_history'

    order_id = db.Column(db.Integer(), nullable=False, index=True)
    status = db.Column(db.String(64), nullable=False, index=True)
    date_created = db.Column(db.DateTime(timezone=True),
                             nullable=False, index=True,
                             server_default=db.func.current_timestamp())
