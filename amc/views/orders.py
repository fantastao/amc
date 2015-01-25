# -*- coding: utf-8 -*-

import pickle

from flask import (Blueprint, views, render_template,
                   redirect, url_for)

from flask.ext.login import current_user, login_required

from amc.models import ProductModel, OrderModel, OrderProductModel


bp = Blueprint('order', __name__)


class OrderDetailView(views.MethodView):

    template = 'front/order_detail.html'

    def get(self, id):
        pass


class TrolleyView(views.MethodView):

    template = 'front/shopping_trolley.html'

    @login_required
    def get(self):
        # 从购物车表中获取产品信息
        user = current_user
        if not user.is_custom:
            # 当前用户不是客户的错误界面
            return
        trolley = user.custom.trolley
        if not trolley:
            # 没有购物车的错误界面，不可能发生
            return
        product_info = pickle.dumps(trolley.product_info)
        if product_info and isinstance(product_info, dict):
            products = (ProductModel.query
                        .filter(ProductModel.id.in_(product_info.keys()))
                        .all())
            product_info = [(p, product_info.get(p.id)) for p in products]
        return render_template(self.template, product_info=product_info)

    @login_required
    def post(self):
        # 点击提交，生成订单后清空购物车
        user = current_user
        if not user.is_custom:
            return
        trolley = user.custom.trolley
        if not trolley:
            return
        # 创建订单
        order = OrderModel.create(custom_id=current_user.id)
        product_info = pickle.dumps(trolley.product_info)
        if product_info and isinstance(product_info, dict):
            for product_id, product_quantity in product_info:
                product = ProductModel.query.get(product_id)
                if not product:
                    # 没有该产品的错误
                    return
                product_price = product.price
                OrderProductModel.create(
                    order_id=order.id,
                    product_id=product_id,
                    product_quantity=product_price)
        trolley.update(product_info=None)
        return redirect(url_for('order.detail', id=order.id))


bp.add_url_rule(
    '/order/<int:id>',
    view_func=OrderDetailView.as_view('detail'))
bp.add_url_rule(
    '/trolley/<int:id>',
    view_func=TrolleyView.as_view('trolley'))
