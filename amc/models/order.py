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

    user_id = db.Column(db.Integer(), nullable=False, index=True)
    status = db.Column(db.String(64), nullable=False,
                       index=True, default=STATUS_LAUNCH)
    date_created = db.Column(db.DateTime(timezone=True),
                             nullable=False, index=True,
                             server_default=db.func.current_timestamp())
    date_updated = db.Column(db.DateTime(timezone=True),
                             nullable=False, index=True,
                             server_default=db.func.current_timestamp())

    products = db.relationship(
        'OrderProductModel',
        backref='order',
        primaryjoin='OrderModel.id==OrderProductModel.order_id',
        foreign_keys='OrderProductModel.order_id',
        uselist=True)

    pay = db.relationship(
        'PayModel', backref='order',
        primaryjoin='PayModel.order_id==OrderModel.id',
        foreign_keys='PayModel.order_id',
        uselist=False)

    @hybrid_property
    def order_price(self):
        order_fee = 0
        for product in self.products:
            order_fee += product.total_price
        return order_fee

    @hybrid_property
    def is_supplied(self):
        for product in self.products:
            if not product.is_supplied:
                return False
        return True


class OrderProductModel(ModelBase):

    __tablename__ = 'order_product'

    order_id = db.Column(db.Integer(), primary_key=True)
    product_id = db.Column(db.Integer(), primary_key=True, index=True)
    product_quantity = db.Column(db.Integer(), nullable=False)
    # in case that price altered
    product_price = db.Column(db.Float(), nullable=False)

    product = db.relationship(
        'ProductModel',
        primaryjoin='ProductModel.id==OrderProductModel.product_id',
        foreign_keys='OrderProductModel.product_id',
        uselist=False)

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
    operator_id = db.Column(db.Integer(), nullable=True, index=True)
    date_created = db.Column(db.DateTime(timezone=True),
                             nullable=False, index=True,
                             server_default=db.func.current_timestamp())


class ShoppingTrolleyModel(SurrogatePK, ModelBase):

    __tablename__ = 'shopping_trolley'

    user_id = db.Column(db.Integer(), nullable=False, index=True)
    date_created = db.Column(db.DateTime(timezone=True),
                             nullable=False, index=True,
                             server_default=db.func.current_timestamp())
    date_updated = db.Column(db.DateTime(timezone=True),
                             nullable=False, index=True,
                             server_default=db.func.current_timestamp())

    products = db.relationship(
        'TrolleyProductModel',
        primaryjoin='ShoppingTrolleyModel.id==TrolleyProductModel.trolley_id',
        foreign_keys='TrolleyProductModel.trolley_id',
        uselist=True)


class TrolleyProductModel(ModelBase):

    __tablename__ = 'trolley_product'

    trolley_id = db.Column(db.Integer(), primary_key=True)
    product_id = db.Column(db.Integer(), primary_key=True, index=True)
    product_quantity = db.Column(db.Integer(), nullable=False)

    product = db.relationship(
        'ProductModel',
        primaryjoin='ProductModel.id==TrolleyProductModel.product_id',
        foreign_keys='TrolleyProductModel.product_id',
        uselist=False)
