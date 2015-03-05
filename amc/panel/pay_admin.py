# -*- coding: utf-8 -*-

from flask import (Blueprint, render_template,
                   views, url_for, redirect)

from amc.models import PayModel, DueModel

from .forms import PayInfoForm

bp = Blueprint('pay_admin', __name__)


class PayListAdmin(views.MethodView):
    """`get`: 查询账款列表"""

    template = 'panel/pay_list.html'

    def get(self):
        pays = (PayModel.query
                .order_by(PayModel.date_created.desc())
                .all())
        return render_template(self.template, pays=pays)


class DueListAdmin(views.MethodView):
    """`get`: 查询应付款列表"""

    template = 'panel/due_list.html'

    def get(self):
        dues = (DueModel.query
                .order_by(DueModel.date_created.desc())
                .all())
        return render_template(self.template, dues=dues)


class PayCreateAdmin(views.MethodView):
    """大多数情况: 订单完成后自动创建
       `get`: 获取创建表单
       `post`: 创建账款事项"""

    template = 'panel/pay_detail.html'

    def get(self):
        form = PayInfoForm()
        return render_template(self.template, form=form)

    def post(self):
        form = PayInfoForm()
        if not form.validate_on_submit():
            return render_template(self.template, form=form)
        pay = PayModel()
        pay.order_id = form.order_id.data
        pay.status = form.status.data
        # 在表单对数据进行校验不能完全保证数据库commit操作正常
        # 所以要加上异常处理
        pay.save()
        return redirect(url_for('.detail', id=pay.id))


class PayDetailAdmin(views.MethodView):
    """`get`: 查询账款详情
       `post`: 更新账款信息"""

    template = 'panel/pay_detail.html'

    def get(self, id):
        pay = PayModel.query.get(id)
        if not pay:
            return
        form = PayInfoForm(
            order_id=pay.order_id,
            status=pay.status)
        return render_template(self.template, form=form)

    def post(self, id):
        pay = PayModel.query.get(id)
        if not pay:
            return
        form = PayInfoForm()
        if not form.validate_on_submit():
            return render_template(self.template, form=form)
        pay.order_id = form.order_id.data
        pay.status = form.status.data
        pay.save()
        return redirect(url_for('.detail', id=pay.id))


class PayDeleteAdmin(views.MethodView):
    """`get`: 删除账单清单"""

    def get(self, id):
        pay = PayModel.query.get(id)
        if not pay:
            return
        pay.delete()
        return redirect(url_for('.list'))


bp.add_url_rule(
    '/admin/pays/',
    view_func=PayListAdmin.as_view('pay_list'))
bp.add_url_rule(
    '/admin/dues/',
    view_func=DueListAdmin.as_view('due_list'))
"""
bp.add_url_rule(
    '/admin/pays/create/',
    view_func=PayCreateAdmin.as_view('create'))
bp.add_url_rule(
    '/admin/pays/<int:id>/',
    view_func=PayDetailAdmin.as_view('detail'))
bp.add_url_rule(
    '/admin/pays/delete/<int:id>/',
    view_func=PayDeleteAdmin.as_view('delete'))
"""
