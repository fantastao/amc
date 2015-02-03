# -*- coding: utf-8 -*-

from flask import views, Blueprint, request, jsonify, abort

from amc.models import OrderModel

from .rest import AmcValidator

bp = Blueprint('panel', __name__)


schema_dict = {
    'status': {'type': 'string'},
}


class OrderPanelAPI(views.MethodView):

    def put(self, id):
        schema = {
            'status': schema_dict['status'],
        }
        order_info = request.get_json()
        v = AmcValidator(schema)
        if not v(order_info):
            abort(422)
        order = OrderModel.update(**order_info)
        return jsonify(order.as_dict()), 200
