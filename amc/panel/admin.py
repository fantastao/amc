# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, views

from amc.models import OrderModel

bp = Blueprint('admin_index', __name__)


class AdminIndex(views.MethodView):
    """后台管理首页"""

    template = 'panel/index.html'

    def get(self):
        return render_template(self.template)


bp.add_url_rule(
    '/admin/',
    view_func=AdminIndex.as_view('index'))


class OrdersAdmin(views.MethodView):
    """订单管理,按照订单状态分几个表格展示"""

    template = 'panel/order_admin.html'

    def get(self):
        orders = OrderModel.query.all()
        return render_template(self.template, orders=orders)


class ProductsAdmin(views.MethodView):
    """库存管理"""

    template = 'panel/product_admin.html'

    def get(self):
        return render_template(self.template)


class PurchaseAdmin(views.MethodView):
    """采购管理"""

    template = 'panel/purchase_admin.html'

    def get(self):
        return render_template(self.template)
