# -*- coding: utf-8 -*-
# 这个后台管理先不要动

from flask import (Blueprint, render_template,
                   views, url_for, redirect)

from amc.utils import origin_pw_hash
from amc.models import OrderModel, UserModel, AuthModel

from .forms import UserInfoForm

bp = Blueprint('admin', __name__, url_prefix='/admin')


class AdminIndex(views.MethodView):
    """后台管理首页"""

    template = 'panel/index.html'

    def get(self):
        return render_template(self.template)


bp.add_url_rule(
    '/',
    view_func=AdminIndex.as_view('index'))


class OrdersAdmin(views.MethodView):
    """订单管理,按照订单状态分几个表格展示"""

    template = 'panel/order_admin.html'

    def get(self):
        orders = OrderModel.query.all()
        return render_template(self.template, orders=orders)


class ProductsAdmin(views.MethodView):
    """库存管理"""

    template = 'panel/product_admin.html'

    def get(self):
        return render_template(self.template)


class PurchaseAdmin(views.MethodView):
    """采购管理"""

    template = 'panel/purchase_admin.html'

    def get(self):
        return render_template(self.template)


class UserAdmin(views.MethodView):
    """用户管理，暂时不允许删除用户"""

    template_list = 'panel/user_list.html'
    template_detail = 'panel/user_detail.html'

    def get(self, id=None):
        if id is not None:
            user = UserModel.query.get(id)
            form = UserInfoForm(
                name=user.name,
                phone=user.phone,
                address=user.address,
                account=user.auth.account)
            return render_template(self.template_detail, form=form)
        form = UserInfoForm()
        return render_template(self.template_detail, form=form)

    def post(self, id=None):
        if id is not None:
            # 修改用户信息
            pass

        form = UserInfoForm()
        if not form.validate_on_submit():
            return render_template(self.template_detail, form=form)
        user = UserModel()
        user.name = form.name.data
        user.phone = form.phone.data
        user.address = form.address.data
        # 在表单对数据进行校验不能完全保证数据库commit操作正常
        # 所以要加上异常处理
        user.save()
        auth = AuthModel()
        auth.user_id = user.id
        auth.account = form.account.data
        auth.pw_hash = origin_pw_hash
        auth.is_verified = True
        auth.save()
        return redirect(url_for('.userlist'))


bp.add_url_rule(
    '/users/',
    view_func=UserAdmin.as_view('userlist'),
    methods=['GET', 'POST'])
bp.add_url_rule(
    '/users/<int:id>/',
    view_func=UserAdmin.as_view('userdetail'),
    methods=['GET', 'POST'])
