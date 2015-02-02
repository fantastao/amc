# -*- coding: utf-8 -*-

from flask import views, Blueprint, request

from amc.models import OrderModel

bp = Blueprint('panel', __name__)


class OrderPanelAPI(views.MethodView):

    def put(self, id):
        order_info = request.get_json()
        order = OrderModel.update(**order_info)
        return order.as_dict(), 201
