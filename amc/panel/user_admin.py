# -*- coding: utf-8 -*-

from flask import (Blueprint, render_template,
                   views, url_for, redirect, abort)

from flask.ext.login import login_required

from amc.utils import origin_pw_hash
from amc.models import UserModel, AuthModel, ShoppingTrolleyModel
from amc.permissions import panel_permission

from .forms import UserInfoForm

bp = Blueprint('user_admin', __name__)


class UserListAdmin(views.MethodView):
    """`get`: 查询用户列表"""

    template = 'panel/user_list.html'

    @login_required
    @panel_permission.require(401)
    def get(self):
        users = UserModel.query.order_by(UserModel.id).all()
        return render_template(self.template, users=users)


class UserDetailAdmin(views.MethodView):
    """`get`: 查询单个用户详情
       `post`: 更新单个用户信息"""

    template = 'panel/user_detail.html'

    @login_required
    @panel_permission.require(401)
    def get(self, id):
        user = UserModel.query.get(id)
        if not user:
            abort(404, u'用户未找到')
        form = UserInfoForm(
            name=user.name,
            phone=user.phone,
            address=user.address,
            account=user.auth.account)
        return render_template(self.template, form=form)

    @login_required
    @panel_permission.require(401)
    def post(self, id):
        user = UserModel.query.get(id)
        if not user:
            abort(404, u'用户未找到')
        form = UserInfoForm()
        if not form.validate_on_submit():
            return render_template(self.template, form=form)
        user.name = form.name.data
        user.phone = form.phone.data
        user.address = form.address.data
        # 暂时不允许更新登录名
        # user.auth.account = form.account.data
        user.save()
        return redirect(url_for('.detail', id=user.id))


class UserCreateAdmin(views.MethodView):
    """`get`: 获取创建表单
       `post`: 创建用户"""

    template = 'panel/user_detail.html'

    @login_required
    @panel_permission.require(401)
    def get(self):
        form = UserInfoForm()
        return render_template(self.template, form=form)

    @login_required
    @panel_permission.require(401)
    def post(self):
        form = UserInfoForm()
        if not form.validate_on_submit():
            return render_template(self.template, form=form)
        user = UserModel(
            name=form.name.data,
            phone=form.phone.data,
            address=form.address.data)
        # 在表单对数据进行校验不能完全保证数据库commit操作正常
        # 所以要加上异常处理
        user.save()
        auth = AuthModel(
            user_id=user.id,
            account=form.account.data,
            pw_hash=origin_pw_hash,
            is_verified=True)
        auth.save()

        # 顺便创建购物车
        trolley = ShoppingTrolleyModel(user_id=user.id)
        trolley.save()

        return redirect(url_for('.list'))


class UserDeleteAdmin(views.MethodView):
    """`get`: 删除单个用户"""

    @login_required
    @panel_permission.require(401)
    def get(self, id):
        user = UserModel.query.get(id)
        if not user:
            abort(404, u'用户未找到')
        user.auth.delete()
        user.trolley.delete()
        user.delete()
        return redirect(url_for('.list'))


bp.add_url_rule(
    '/admin/users/',
    view_func=UserListAdmin.as_view('list'))
bp.add_url_rule(
    '/admin/users/<int:id>/',
    view_func=UserDetailAdmin.as_view('detail'))
bp.add_url_rule(
    '/admin/users/create/',
    view_func=UserCreateAdmin.as_view('create'))
bp.add_url_rule(
    '/admin/users/delete/<int:id>',
    view_func=UserDeleteAdmin.as_view('delete'))
