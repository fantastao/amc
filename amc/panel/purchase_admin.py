# -*- coding: utf-8 -*-

from flask import (Blueprint, render_template,
                   views, url_for, redirect)

from amc.models import PurchaseModel, ProductModel
from amc.utils import now

from .forms import PurchaseInfoForm

bp = Blueprint('purchase_admin', __name__)


class PurchaseListAdmin(views.MethodView):
    """`get`: 查询采购列表"""

    template = 'panel/purchase_list.html'

    def get(self):
        purchases = (PurchaseModel.query
                     .order_by(PurchaseModel.date_created.desc())
                     .all())
        return render_template(self.template, purchases=purchases)


class PurchaseCreateAdmin(views.MethodView):
    """`get`: 获取创建表单
       `post`: 创建采购事项"""

    template = 'panel/purchase_detail.html'

    def get(self):
        form = PurchaseInfoForm()
        return render_template(self.template, form=form)

    def post(self):
        form = PurchaseInfoForm()
        if not form.validate_on_submit():
            return render_template(self.template, form=form)
        purchase = PurchaseModel(
            product_id=form.product_id.data,
            product_quantity=form.product_quantity.data)
        purchase.save()
        return redirect(url_for('.list'))


class PurchaseConfirmAdmin(views.MethodView):
    """`get`: 采购入库确认，修改库存"""

    def get(self, id):
        purchase = PurchaseModel.query.get(id)
        if not purchase or purchase.status == PurchaseModel.STATUS_OVER:
            # 采购不存在或者已经结束
            return
        product = ProductModel.query.get(purchase.product_id)
        if not product:
            return
        purchase.status = PurchaseModel.STATUS_OVER
        purchase.save()
        product.quantity += purchase.product_quantity
        product.date_updated = now()
        product.save()
        return redirect(url_for('.list'))


class PurchaseDetailAdmin(views.MethodView):
    """`get`: 查询采购详情
       `post`: 更新采购信息,一旦下单，不允许更新"""

    template = 'panel/purchase_detail.html'

    def get(self, id):
        purchase = PurchaseModel.query.get(id)
        if not purchase:
            return
        form = PurchaseInfoForm(
            product_id=purchase.product_id,
            product_quantity=purchase.product_quantity)
        return render_template(self.template, form=form)

    def post(self, id):
        purchase = PurchaseModel.query.get(id)
        if not purchase:
            return
        form = PurchaseInfoForm()
        if not form.validate_on_submit():
            return render_template(self.template, form=form)
        purchase.product_id = form.product_id.data
        purchase.product_quantity = form.product_quantity.data
        purchase.save()
        return redirect(url_for('.detail', id=purchase.id))


class PurchaseDeleteAdmin(views.MethodView):
    """`get`: 删除采购清单"""

    def get(self, id):
        purchase = PurchaseModel.query.get(id)
        if not purchase:
            return
        purchase.delete()
        return redirect(url_for('.list'))


bp.add_url_rule(
    '/admin/purchases/',
    view_func=PurchaseListAdmin.as_view('list'))
bp.add_url_rule(
    '/admin/purchases/create/',
    view_func=PurchaseCreateAdmin.as_view('create'))
bp.add_url_rule(
    '/admin/purchases/confirm/<int:id>/',
    view_func=PurchaseConfirmAdmin.as_view('confirm'))
bp.add_url_rule(
    '/admin/purchases/delete/<int:id>/',
    view_func=PurchaseDeleteAdmin.as_view('delete'))
"""
bp.add_url_rule(
    '/admin/purchases/<int:id>/',
    view_func=PurchaseDetailAdmin.as_view('detail'))
"""
