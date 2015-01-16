# -*- coding: utf-8 -*-

from flask import (request, views, Blueprint,
                   url_for, render_template)

bp = Blueprint('home', __name__)


class HomeView(views.MethodView):

    def get(self):
        return render_template('home.html')

bp.add_url_rule('/', view_func=HomeView.as_view('index'))
