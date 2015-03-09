# -*- coding: utf-8 -*-

from sqlalchemy.ext.hybrid import hybrid_property

from .base import ModelBase, SurrogatePK, db


# product divide into different categories with attributions
PRODUCT_CATEGORIES = ['G', 'M', 'S']


class ProductModel(SurrogatePK, ModelBase):

    __tablename__ = 'product'

    name = db.Column(db.String(64), nullable=False, index=True)
    img = db.Column(db.String(256), nullable=False, default='/static/img/common.png')
    category = db.Column(db.String(64), nullable=False, default='M')
    description = db.Column(db.UnicodeText(), nullable=True)
    price = db.Column(db.Float(), nullable=False, index=True)
    quantity = db.Column(db.Integer(), nullable=False, default=0)
    safe_quantity = db.Column(db.Integer(), nullable=False, default=50)
    made_in = db.Column(db.String(64), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True),
                             nullable=False, index=True,
                             server_default=db.func.current_timestamp())
    date_updated = db.Column(db.DateTime(timezone=True),
                             nullable=False, index=True,
                             server_default=db.func.current_timestamp())

    @hybrid_property
    def is_safe(self):
        return self.quantity >= self.safe_quantity


class LackedProductHistoryModel(SurrogatePK, ModelBase):

    __tablename__ = 'lacked_product_history'

    product_id = db.Column(db.Integer(), nullable=False, index=True)
    user_id = db.Column(db.Integer(), nullable=False, index=True)
    quantity = db.Column(db.Integer(), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), nullable=False,
                             server_default=db.func.current_timestamp())
