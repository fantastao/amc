# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, views

from flask.ext.login import login_required

from amc.permissions import panel_permission

bp = Blueprint('admin_index', __name__)


class AdminIndex(views.MethodView):
    """后台管理首页"""

    template = 'panel/admin_index.html'

    @login_required
    @panel_permission.require(401)
    def get(self):
        return render_template(self.template)


bp.add_url_rule(
    '/admin/',
    view_func=AdminIndex.as_view('index'))
