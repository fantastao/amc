# -*- coding: utf-8 -*-

from flask import (Blueprint, render_template,
                   views, url_for, redirect, abort)

from flask.ext.login import login_required

from amc.models import AdminModel
from amc.permissions import panel_permission

from .forms import RoleInfoForm

bp = Blueprint('extra_admin', __name__)


class RoleListAdmin(views.MethodView):

    template = 'panel/role_list.html'

    @login_required
    @panel_permission.require(401)
    def get(self):
        users = AdminModel.query.order_by(AdminModel.user_id).all()
        return render_template(self.template, users=users)


class RoleCreateAdmin(views.MethodView):

    template = 'panel/role_detail.html'

    @login_required
    @panel_permission.require(401)
    def get(self):
        form = RoleInfoForm()
        return render_template(self.template, form=form)

    @login_required
    @panel_permission.require(401)
    def post(self):
        form = RoleInfoForm()
        if not form.validate_on_submit():
            return render_template(self.template, form=form)
        role = AdminModel(
            user_id=form.user_id.data,
            department=form.department.data)
        role.save()
        return redirect(url_for('.list'))


class RoleDeleteAdmin(views.MethodView):

    @login_required
    @panel_permission.require(401)
    def get(self, id):
        role = AdminModel.query.get(id)
        if not role:
            abort(404, u'用户未找到')
        role.delete()
        return redirect(url_for('.list'))


bp.add_url_rule(
    '/admin/extras/',
    view_func=RoleListAdmin.as_view('list'))
bp.add_url_rule(
    '/admin/extras/create/',
    view_func=RoleCreateAdmin.as_view('create'))
bp.add_url_rule(
    '/admin/extras/delete/<int:id>/',
    view_func=RoleDeleteAdmin.as_view('delete'))
