# -*- coding: utf-8 -*-

from flask import Blueprint, views


bp = Blueprint('order', __name__)


class OrderDetailView(views.MethodView):

    template = 'front/shopping_trolley.html'

    def get(self, id):
        pass


class TrolleyView(views.MethodView):

    template = 'front/shopping_trolley.html'

    def get(self, id):
        # 从购物车表中获取信息
        pass

    def post(self):
        # 点击提交，购物车信息生成订单
        pass


bp.add_url_rule(
    '/order/<int:id>',
    view_func=OrderDetailView.as_view('detail'))
bp.add_url_rule(
    '/trolley/<int:id>',
    view_func=TrolleyView.as_view('trolley'))
