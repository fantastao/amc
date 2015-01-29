# -*- coding: utf-8 -*-

from flask import (Blueprint, render_template,
                   views, url_for, redirect, flash)

from flask.ext.login import login_required, current_user

from .forms import UserProfileForm

bp = Blueprint('user', __name__, url_prefix='/user')


class UserProfileView(views.MethodView):

    template = 'front/profile.html'

    @login_required
    def get(self):
        user = current_user
        form = UserProfileForm(
            name=user.name,
            phone=user.phone,
            address=user.address)
        return render_template(self.template, form=form)

    @login_required
    def post(self):
        form = UserProfileForm()
        if not form.validate_on_submit():
            return render_template(self.template, form=form)
        user = current_user
        form.populate_obj(user)
        user.save()
        flash(u'用户信息修改成功')
        return redirect(url_for('.profile'))


class UserOrdersView(views.MethodView):

    template = 'front/orders.html'

    @login_required
    def get(self):
        orders = current_user.orders
        return render_template(self.template, orders=orders)


bp.add_url_rule(
    '/profile/',
    view_func=UserProfileView.as_view('profile'))
