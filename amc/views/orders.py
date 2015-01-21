# -*- coding: utf-8 -*-

from flask import (request, Blueprint, render_template,
                   redirect, url_for)

from amc.models import OrderModel, OrderProductModel, OrderHistoryModel, PayModel


bp = Blueprint('orders', __name__, url_prefix='/orders')

@bp.route('/new_order', methods=['GET', 'POST'])
def new_order():
    if request.method == 'GET':
        # order = request.args.get('order', None)
        order = {'custom_id':'123456', 'order_products':[{'product_id':1, 'quantity':10,'price':50},{'product_id':2, 'quantity':10, 'price': 30}]}
        create_new_order(order)
        return render_template('home.html')

def create_new_order(order):
    #  create new records in OrderModel,OrderProductModel, OrderHistoryModel, PayModel
    return
