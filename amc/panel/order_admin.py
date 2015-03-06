# -*- coding: utf-8 -*-

from flask import Blueprint, views, render_template

from amc.models import OrderModel, OrderHistoryModel

bp = Blueprint('order_admin', __name__)


class OrderListAdmin(views.MethodView):
    """`get`: 查询订单列表"""

    template = 'panel/order_list.html'

    def get(self):
        orders = (OrderModel.query
                  .order_by(OrderModel.date_updated.desc())
                  .all())
        return render_template(self.template, orders=orders)


class OrderDetailAdmin(views.MethodView):
    """`get`: 获取单个订单详情,订单历史"""

    template = 'panel/order_detail.html'

    def get(self, id):
        order = OrderModel.query.get(id)
        if not order:
            return
        products = order.products
        history = OrderHistoryModel.query.filter_by(order_id=id).all()
        history.sort(key=lambda k:k.date_created, reverse=False)
        return render_template(self.template,
                               order=order, products=products, history=history)


bp.add_url_rule(
    '/admin/orders/',
    view_func=OrderListAdmin.as_view('list'))
bp.add_url_rule(
    '/admin/order/<int:id>/',
    view_func=OrderDetailAdmin.as_view('detail'))
