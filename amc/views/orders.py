# -*- coding: utf-8 -*-

from flask import (Blueprint, views, render_template,
                   redirect, url_for)

from flask.ext.login import current_user, login_required

from amc.models import OrderModel, OrderProductModel

bp = Blueprint('order', __name__)


class TrolleyView(views.MethodView):
    """修改购物车信息如添加产品购买数量，
    删除已经添加的产品等用api完成
    """

    template = 'front/shopping_trolley.html'

    @login_required
    def get(self):
        # 从购物车表中获取产品信息
        trolley = current_user.trolley
        if not trolley:
            # 没有购物车的错误界面，不可能发生
            return
        products = trolley.products
        return render_template(self.template, products=products)

    @login_required
    def post(self):
        # 点击提交，生成订单后清空购物车
        items = current_user.trolley.products
        if not items:
            # 购物车为空，不允许下单
            return

        # 创建订单，初始状态launch
        order = OrderModel.create(user_id=current_user.id)
        # 填充订单信息，将购物车结账清算
        for item in items:
            OrderProductModel.create(
                order_id=order.id,
                product_id=item.product_id,
                product_quantity=item.product_quantity,
                product_price=item.product.price)
            item.delete()
        
        return redirect(url_for('user.order', id=order.id))


bp.add_url_rule(
    '/trolley/',
    view_func=TrolleyView.as_view('trolley'))
