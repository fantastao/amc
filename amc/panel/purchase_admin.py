# -*- coding: utf-8 -*-

from flask import (Blueprint, render_template,
                   views, url_for, redirect, flash)

from amc.models import PurchaseModel

from .forms import PurchaseInfoForm

bp = Blueprint('purchase_admin', __name__)


class PurchaseListAdmin(views.MethodView):
    """`get`: 查询采购列表"""

    template = 'panel/purchase_list.html'

    def get(self):
        purchases = PurchaseModel.query.all()
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
        purchase = PurchaseModel()
        purchase.product_id = form.product_id.data
        purchase.product_quantity = form.product_quantity.data
        purchase.status = form.status.data
        # 在表单对数据进行校验不能完全保证数据库commit操作正常
        # 所以要加上异常处理
        purchase.save()
        flash(u'采购创建成功')
        return redirect(url_for('.detail', id=purchase.id))

class PurchaseDetailAdmin(views.MethodView):
    """`get`: 查询采购详情
       `post`: 更新采购信息"""

    template = 'panel/purchase_detail.html'

    def get(self, id):
        purchase = PurchaseModel.query.get(id)
        if not purchase:
            return
        form = PurchaseInfoForm(
            product_id=purchase.product_id,
            product_quantity=purchase.product_quantity,
            status=purchase.status)
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
        purchase.status = form.status.data
        purchase.save()
        flash(u'采购更新成功')
        return redirect(url_for('.detail', id=purchase.id))

class PurchaseDeleteAdmin(views.MethodView):
    """`get`: 删除采购清单"""

    def get(self, id):
        purchase = PurchaseModel.query.get(id)
        if not purchase:
            return
        purchase.delete()
        flash(u'采购事项删除成功')
        return redirect(url_for('.list'))


bp.add_url_rule(
    '/admin/purchases/',
    view_func=PurchaseListAdmin.as_view('list'))
bp.add_url_rule(
    '/admin/purchases/create/',
    view_func=PurchaseCreateAdmin.as_view('create'))
bp.add_url_rule(
    '/admin/purchases/<int:id>/',
    view_func=PurchaseDetailAdmin.as_view('detail'))
bp.add_url_rule(
    '/admin/purchases/delete/<int:id>/',
    view_func=PurchaseDeleteAdmin.as_view('delete'))
