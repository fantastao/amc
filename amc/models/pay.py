# -*- coding: utf-8 -*-

from .base import ModelBase, SurrogatePK, db


class PayModel(SurrogatePK, ModelBase):

    # two status cauz pay created after order success
    STATUS_PENDING = 'pending'
    STATUS_RECEIVED = 'received'

    __tablename__ = 'pay'

    order_id = db.Column(db.Integer(), nullable=False, index=True)
    status = db.Column(db.String(64), nullable=False,
                       index=True, default=STATUS_PENDING)
    amount = db.Column(db.Float(), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True),
                             nullable=False, index=True,
                             server_default=db.func.current_timestamp())
    date_updated = db.Column(db.DateTime(timezone=True),
                             nullable=False, index=True,
                             server_default=db.func.current_timestamp())
    def as_dict(self):
        result = {
            'id': self.id,
            'order_id': self.order_id,
            'status': self.status,
            'amount': self.amount,
            'date_created': self.date_created,
            'date_updated': self.date_updated,
        }
        return result

class DueModel(SurrogatePK, ModelBase):

    STATUS_PENDING = 'pending'
    STATUS_PAID = 'paid'

    __tablename__ = 'due'

    purchase_id = db.Column(db.Integer(), nullable=False, index=True)
    status = db.Column(db.String(64), nullable=False,
                       index=True, default=STATUS_PENDING)
    amount = db.Column(db.Float(), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True),
                             nullable=False, index=True,
                             server_default=db.func.current_timestamp())
    date_updated = db.Column(db.DateTime(timezone=True),
                             nullable=False, index=True,
                             server_default=db.func.current_timestamp())
