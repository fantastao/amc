# -*- coding: utf-8 -*-

import pickle
import json

from flask import (Blueprint, views, render_template, request,
                   redirect, url_for)

from flask.ext.login import current_user, login_required

from amc.models import ProductModel, OrderModel, OrderProductModel, ShoppingTrolleyModel, TrolleyProductModel


bp = Blueprint('order', __name__)


class OrderDetailView(views.MethodView):

    template = 'front/order_detail.html'

    @login_required
    def get(self, id):
        order = OrderModel.query.get(id)
        if current_user is not order.user:
            # 订单不是当前用户的禁止访问
            return
        return render_template(self.template, order=order)


class TrolleyView(views.MethodView):
    """修改购物车信息如添加产品购买数量，
    删除已经添加的产品等用api完成
    """

    template = 'front/shopping_trolley.html'

    @login_required
    def get(self):
        '''
        # 从购物车表中获取产品信息
        trolley = current_user.trolley
        if not trolley:
            # 没有购物车的错误界面，不可能发生
            products = {}
        # forms add here
        else:
            products = trolley.products
        return render_template(self.template, products=products)
        '''
        return render_template(self.template)


    @login_required
    def post(self):
        # 点击提交，生成订单后清空购物车
        trolley = current_user.trolley
        if not trolley:
            return
        # 创建订单
        order = OrderModel.create(user_id=current_user.id)
        # 填充订单信息
        product_info = pickle.dumps(trolley.product_info)
        if product_info and isinstance(product_info, dict):
            for product_id, product_quantity in product_info.items():
                product = ProductModel.query.get(product_id)
                if not product:
                    # 没有该产品的错误
                    return
                product_price = product.price
                OrderProductModel.create(
                    order_id=order.id,
                    product_id=product_id,
                    product_quantity=product_quantity,
                    product_price=product_price)
        trolley.update(product_info=None)
        return redirect(url_for('order.detail', id=order.id))

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
                product["price"] = item.product.price
                product["name"] = item.product.name
                products_list.append(product)
        return json.dumps(products_list)

class TrolleyAddView(views.MethodView):

    @login_required
    def get(self):
        product_id = int(request.args.get('product_id'))
        product_quantity = int(request.args.get('product_quantity'))
        trolley = current_user.trolley
        if not trolley:
            trolley = ShoppingTrolleyModel(
                user_id=current_user.id)
            trolley.save()

        for item in trolley.products:
            if (product_id == item.product_id):
                if (product_quantity == item.product_quantity):
                    return json.dumps({"status":"exists"})
                else:
                    item.update(product_quantity=product_quantity)
                    return json.dumps({"status":"updated"})
        # 不存在该产品
        trolley_product =TrolleyProductModel(
            trolley_id=trolley.id,
            product_id=product_id,
            product_quantity=product_quantity)
        trolley_product.save()
        return json.dumps({"status":"created"})

class TrolleyUpdateView(views.MethodView):

    @login_required
    def get(self):
        product_id = int(request.args.get('product_id'))
        product_quantity = int(request.args.get('product_quantity'))
        trolley = current_user.trolley
        if not trolley:
            trolley = ShoppingTrolleyModel(
                user_id=current_user.id)
            trolley.save()

        for item in trolley.products:
            if (product_id == item.product_id):
                item.update(product_quantity=product_quantity)
        
        products_list = []
        products = trolley.products
        for item in products:
            product = {}
            product["product_id"] = item.product_id
            product["quantity"] = item.product_quantity
            product["price"] = item.product.price
            product["name"] = item.product.name
            products_list.append(product)
        return json.dumps(products_list)

class TrolleyDeleteView(views.MethodView):

    @login_required
    def get(self):
        product_id = int(request.args.get('product_id'))
        trolley = current_user.trolley

        for item in trolley.products:
            if (product_id == item.product_id):
                item.delete()
        
        products_list = []
        products = trolley.products
        for item in products:
            product = {}
            product["product_id"] = item.product_id
            product["quantity"] = item.product_quantity
            product["price"] = item.product.price
            product["name"] = item.product.name
            products_list.append(product)
        return json.dumps(products_list)

bp.add_url_rule(
    '/order/<int:id>/',
    view_func=OrderDetailView.as_view('detail'))
bp.add_url_rule(
    '/trolley/',
    view_func=TrolleyView.as_view('trolley'))
bp.add_url_rule(
    '/trolley/items/',
    view_func=TrolleyItemsView.as_view('items_trolley'))
bp.add_url_rule(
    '/trolley/add/',
    view_func=TrolleyAddView.as_view('add_trolley'))
bp.add_url_rule(
    '/trolley/update/',
    view_func=TrolleyUpdateView.as_view('update_trolley'))
bp.add_url_rule(
    '/trolley/delete/',
    view_func=TrolleyDeleteView.as_view('delete_trolley'))
