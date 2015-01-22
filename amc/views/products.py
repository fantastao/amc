# -*- coding: utf-8 -*-

from flask import Blueprint, views, render_template

from amc.models import ProductModel


bp = Blueprint('product', __name__)


class ProductListView(views.MethodView):

    template = 'front/products.html'

    def get(self):
        # products = ProductModel.query.all()
        products = [{'id':1,'name':'book','price':50,'quantity':50,'made_in':'china'},{'id':2,'name':'food','price':100,'quantity':'100','made_in':'japan'}]
        return render_template(self.template, products=products)


class ProductDetailView(views.MethodView):

    template = 'front/product_detail.html'

    def get(self, id):
        # product = ProductModel.query.get(id)
        product = {'id':1,'name':'book','price':50,'quantity':50,'made_in':'china'}
        if not product:
            # 没有这个产品的错误界面
            pass
        return render_template(self.template, product=product)


bp.add_url_rule(
    '/products',
    view_func=ProductListView.as_view('list'))
bp.add_url_rule(
    '/product/<int:id>',
    view_func=ProductDetailView.as_view('detail'))
