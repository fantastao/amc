# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, views

from amc.models import ProductModel


bp = Blueprint('product', __name__)


class ProductListView(views.MethodView):

    template = 'front/products.html'

    def get(self):
        products = ProductModel.query.all()
        return render_template(self.template, products=products)


class ProductDetailView(views.MethodView):

    template = 'front/product_detail.html'

    def get(self, id):
        product = ProductModel.query.get(id)
        if not product:
            # 没有这个产品的错误界面
            return
        return render_template(self.template, product=product)


bp.add_url_rule(
    '/products',
    view_func=ProductListView.as_view('list'))
bp.add_url_rule(
    '/product/<int:id>',
    view_func=ProductDetailView.as_view('detail'))
