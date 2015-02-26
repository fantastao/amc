# -*- coding: utf-8 -*-

from flask import (Blueprint, render_template,
                   views, url_for, redirect, flash)

from amc.models import ProductModel

from .forms import ProductInfoForm

bp = Blueprint('product_admin', __name__)


class ProductListAdmin(views.MethodView):
    """`get`: 查询产品列表"""

    template = 'panel/product_list.html'

    def get(self):
        products = ProductModel.query.all()
        return render_template(self.template, products=products)


class ProductCreateAdmin(views.MethodView):
    """`get`: 获取创建表单
       `post`: 创建产品"""

    template = 'panel/product_detail.html'

    def get(self):
        form = ProductInfoForm()
        return render_template(self.template, form=form)

    def post(self):
        form = ProductInfoForm()
        if not form.validate_on_submit():
            return render_template(self.template, form=form)
        product = ProductModel(
            name=form.name.data,
            category=form.category.data,
            description=form.description.data,
            price=form.price.data,
            quantity=form.quantity.data,
            safe_quantity=form.safe_quantity.data,
            made_in=form.made_in.data)
        # 在表单对数据进行校验不能完全保证数据库commit操作正常
        # 所以要加上异常处理
        product.save()
        flash(u'产品创建成功')
        return redirect(url_for('.detail', id=product.id))


class ProductDetailAdmin(views.MethodView):
    """`get`: 查询单个产品详情
       `post`: 更新单个产品信息"""

    template = 'panel/product_detail.html'

    def get(self, id):
        product = ProductModel.query.get(id)
        if not product:
            return
        form = ProductInfoForm(
            name=product.name,
            category=product.category,
            description=product.description,
            price=product.price,
            quantity=product.quantity,
            safe_quantity=product.safe_quantity,
            made_in=product.made_in)
        return render_template(self.template, form=form)

    def post(self, id):
        product = ProductModel.query.get(id)
        if not product:
            return
        form = ProductInfoForm()
        if not form.validate_on_submit():
            return render_template(self.template, form=form)
        product.name = form.name.data
        product.category = form.category.data
        product.description = form.description.data
        product.price = form.price.data
        product.quantity = form.quantity.data
        product.safe_quantity = form.safe_quantity.data
        product.made_in = form.made_in.data
        product.save()
        flash(u'产品更新成功')
        return redirect(url_for('.detail', id=product.id))


class ProductDeleteAdmin(views.MethodView):
    """`get`: 删除单个产品"""

    def get(self, id):
        product = ProductModel.query.get(id)
        if not product:
            return
        product.delete()
        flash(u'产品删除成功')
        return redirect(url_for('.list'))


bp.add_url_rule(
    '/admin/products/',
    view_func=ProductListAdmin.as_view('list'))
bp.add_url_rule(
    '/admin/products/create/',
    view_func=ProductCreateAdmin.as_view('create'))
bp.add_url_rule(
    '/admin/products/<int:id>/',
    view_func=ProductDetailAdmin.as_view('detail'))
bp.add_url_rule(
    '/admin/products/delete/<int:id>/',
    view_func=ProductDeleteAdmin.as_view('delete'))
