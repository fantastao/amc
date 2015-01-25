# -*- coding: utf-8 -*-

from flask import Blueprint, views


bp = Blueprint('apis', __name__, url_prefix='/apis')


class TrolleyAPI(views.MethodView):

    # 只要是custom用户，创建时购物车自动创建
    def put(self):
        pass
