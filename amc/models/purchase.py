# -*- coding: utf-8 -*-

from sqlalchemy.ext.hybrid import hybrid_property

from .base import ModelBase, SurrogatePK, db


class PurchaseModel(SurrogatePK, ModelBase):

    STATUS_BEGIN = 'begin'
    STATUS_OVER = 'over'

    __tablename__ = 'purchase'

    product_id = db.Column(db.Integer(), nullable=False, index=True)
    product_quantity = db.Column(db.Integer(), nullable=False)
    cost = db.Column(db.Float(), nullable=False)
    status = db.Column(db.String(64), nullable=False,
                       index=True, default=STATUS_BEGIN)
    date_created = db.Column(db.DateTime(timezone=True),
                             nullable=False, index=True,
                             server_default=db.func.current_timestamp())
    date_updated = db.Column(db.DateTime(timezone=True),
                             nullable=False, index=True,
                             server_default=db.func.current_timestamp())

    product = db.relationship(
            'ProductModel',
            foreign_keys='PurchaseModel.product_id',
            primaryjoin='ProductModel.id==PurchaseModel.product_id',
            uselist=False)

    due = db.relationship(
            'DueModel', backref='purchase',
            foreign_keys='DueModel.purchase_id',
            primaryjoin='DueModel.purchase_id==PurchaseModel.id',
            uselist=False)

    @hybrid_property
    def total_cost(self):
        return self.cost * self.product_quantity
