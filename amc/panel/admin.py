# -*- coding: utf-8 -*-
# 这个后台管理先不要动

from flask import Blueprint, render_template, views

from amc.models import OrderModel

bp = Blueprint('admin', __name__)


class OrdersAdmin(views.MethodView):
    """订单管理"""

    template = 'panel/order_admin.html'

    def get(self):
        orders = OrderModel.query.all()
        return render_template(self.template, orders=orders)


class ProductsAdmin(views.MethodView):
    """产品管理"""

    template = 'panel/product_admin.html'    

    def get(self):
        return render_template(self.template)


class PurchaseAdmin(views.MethodView):
    """采购管理"""

    template = 'panel/purchase_admin.html'    

    def get(self):
        return render_template(self.template)


class UserAdmin(views.MethodView):
    """用户管理"""

    template = 'panel/user_admin.html'    

    def get(self):
        return render_template(self.template)


bp.add_url_rule(
    '/admin/orders/',
    view_func=OrdersAdmin.as_view('orders'))
bp.add_url_rule(
    '/admin/products/',
    view_func=ProductsAdmin.as_view('products'))
bp.add_url_rule(
    '/admin/purchases/',
    view_func=PurchaseAdmin.as_view('purchase'))
bp.add_url_rule(
    '/admin/users/',
    view_func=UserAdmin.as_view('users'))
