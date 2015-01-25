# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, views

from flask.ext.login import login_required, current_user


bp = Blueprint('user', __name__, url_prefix='/user')


class UserProfileView(views.MethodView):

    template = 'front/profile.html'

    @login_required
    def get(self):
        return render_template(self.template, user=current_user)


class UserOrdersView(views.MethodView):

    template = 'front/orders.html'

    @login_required
    def get(self):
        orders = current_user.orders
        return render_template(self.template, orders=orders)


bp.add_url_rule(
    '/profile/',
    view_func=ProfileView.as_view('profile'))
