# -*- coding: utf-8 -*-

from flask import (Blueprint, render_template,
                   views, url_for, redirect)

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
        return render_template(self.template, form=form, user=user)

    @login_required
    def post(self):
        user = current_user
        form = UserProfileForm()
        if not form.validate_on_submit():
            return render_template(self.template, form=form, user=user)
        user = current_user
        form.populate_obj(user)
        user.save()
        return redirect(url_for('.profile'))


class UserOrdersView(views.MethodView):

    template = 'front/order_detail.html'

    @login_required
    def get(self):
        orders = current_user.orders
        orders.sort(key=lambda k:k.date_updated, reverse=True)
        return render_template(self.template, orders=orders)


bp.add_url_rule(
    '/profile/',
    view_func=UserProfileView.as_view('profile'))
bp.add_url_rule(
    '/orders/',
    view_func=UserOrdersView.as_view('order'))
