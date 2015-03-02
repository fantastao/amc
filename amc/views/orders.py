# -*- coding: utf-8 -*-

import json

from flask import (Blueprint, views, render_template,
                   redirect, url_for)

from flask.ext.login import current_user, login_required

from amc.models import (OrderModel, OrderProductModel,
                        OrderHistoryModel, PayModel)
from amc.utils import now

bp = Blueprint('order', __name__)


class TrolleyView(views.MethodView):

    template = 'front/shopping_trolley.html'

    @login_required
    def get(self):
        '''
        # 从购物车表中获取产品信息
        trolley = current_user.trolley
        if not trolley:
            # 没有购物车的错误界面，不可能发生
            return
        # forms add here
        else:
            products = trolley.products
        return render_template(self.template, products=products)
        '''
        return render_template(self.template)


class TrolleyCommitView(views.MethodView):
    """点击提交，生成订单后清空购物车
       本来可以和TrolleyView放一起使用post方法来提交，
       考虑到没有表单提交，所以分开用get请求提交订单"""

    @login_required
    def get(self):
        items = current_user.trolley.products
        if not items:
            return

        # 创建订单，载入历史
        order = OrderModel.create(user_id=current_user.id)
        OrderHistoryModel.create(
            order_id=order.id,
            status=order.status,
            operator_id=current_user.id)

        # 填充订单信息，将购物车结账清算
        for item in items:
            if not item.is_supplied:
                # 某件产品库存不足
                return

            product = item.product
            OrderProductModel.create(
                order_id=order.id,
                product_id=item.product_id,
                product_quantity=item.product_quantity,
                product_price=product.price)

            # 修改库存
            product.quantity -= item.product_quantity
            product.date_updated = now()
            product.save()

            # 清空购物车
            item.delete()

        return redirect(url_for('user.order'))


class TrolleyItemsView(views.MethodView):

    @login_required
    def get(self):
        trolley = current_user.trolley
        products_list = []
        if trolley:
            products = trolley.products
            for item in products:
                product = {}
                product["product_id"] = item.product_id
                product["quantity"] = item.product_quantity
                product["price"] = item.product_price
                product["name"] = item.product.name
                products_list.append(product)
        return json.dumps(products_list)


class OrderCancelView(views.MethodView):
    """用户取消订单"""

    STATUS_ALLOW = [OrderModel.STATUS_LAUNCH, OrderModel.STATUS_CONFIRM]

    @login_required
    def get(self, id):
        order = OrderModel.query.get(id)
        if not order:
            return
        if order.user_id != current_user.id:
            # 非当前用户的订单
            return
        if order.status not in self.STATUS_ALLOW:
            # 订单处于不被允许取消的状态
            return

        # 修改库存
        for item in order.products:
            product = item.product
            product.quantity += item.product_quantity
            product.date_updated = now()
            product.save()
            # 这里不能delete，否则取消掉的订单为空订单
            # item.delete()

        # 更新状态，载入历史
        order.update(
            status=OrderModel.STATUS_CANCEL,
            date_updated=now())
        OrderHistoryModel.create(
            order_id=id,
            status=order.status,
            operator_id=current_user.id)

        return redirect(url_for('user.order'))


class OrderSuccessView(views.MethodView):
    """用户确认收获，生成收款单"""

    @login_required
    def get(self, id):
        order = OrderModel.query.get(id)
        if not order:
            return
        if order.user_id != current_user.id:
            # 非当前用户的订单
            return
        if order.status != OrderModel.STATUS_DISPATCH:
            # 订单处不处于货物发出状态
            return

        # 更新状态，载入历史
        order.update(
            status=OrderModel.STATUS_SUCCESS,
            date_updated=now())
        OrderHistoryModel.create(
            order_id=id,
            status=order.status,
            operator_id=current_user.id)

        # 生成收款单
        PayModel.create(
            order_id=id,
            amount=order.order_price)

        return redirect(url_for('user.order'))


class OrderReturnView(views.MethodView):
    """申请退货，暂时不处理"""

    @login_required
    def get(self, id):
        pass


bp.add_url_rule(
    '/trolley/',
    view_func=TrolleyView.as_view('trolley'))
bp.add_url_rule(
    '/trolley/commit/',
    view_func=TrolleyCommitView.as_view('trolley_commit'))
bp.add_url_rule(
    '/trolley/items/',
    view_func=TrolleyItemsView.as_view('items_trolley'))
bp.add_url_rule(
    '/order/cancel/<int:id>/',
    view_func=OrderCancelView.as_view('order_cancel'))
bp.add_url_rule(
    '/order/success/<int:id>/',
    view_func=OrderSuccessView.as_view('order_success'))
bp.add_url_rule(
    '/order/return/<int:id>/',
    view_func=OrderReturnView.as_view('order_return'))
