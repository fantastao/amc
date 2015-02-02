# -*- coding: utf-8 -*-

from flask import Blueprint, views, render_template

from amc.models import OrderModel

bp = Blueprint('order_admin', __name__)


class OrderAdmin(views.MethodView):
    """`get`: 查询订单列表,获取单个订单详情"""

    template_list = 'panel/order_list.html'
    template_detail = 'panel/order_detail.html'

    def get(self, id=None):
        if id is not None:
            order = OrderModel.query.get(id)
            if not order:
                return
            return render_template(self.template_detail, order=order)
        orders = OrderModel.query.all()
        return render_template(self.template_list, orders=orders)


bp.add_url_rule(
    '/admin/orders/',
    view_func=OrderAdmin.as_view('list'))
bp.add_url_rule(
    '/admin/order/<int:id>',
    view_func=OrderAdmin.as_view('detail'))
