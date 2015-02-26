# -*- coding: utf-8 -*-

from flask import views, Blueprint, render_template

from amc.models import ProductModel

bp = Blueprint('home', __name__)


class HomeView(views.MethodView):

    template = 'front/home.html'

    def get(self):
        products = ProductModel.query.limit(4).all()
        return render_template(self.template, products=products)

bp.add_url_rule('/', view_func=HomeView.as_view('index'))
