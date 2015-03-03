# -*- coding: utf-8 -*-

from flask import views, Blueprint, request, jsonify, abort

# from flask.ext.login import current_user, login_required

from amc.models import OrderModel, OrderHistoryModel
from amc.utils import now

from .rest import AmcValidator

bp = Blueprint('panel', __name__, url_prefix='/apis/panel')


STATUS_ALLOW = [OrderModel.STATUS_CONFIRM, OrderModel.STATUS_DISPATCH,
                OrderModel.STATUS_CANCEL]

schema_dict = {
    'status': {'type': 'string', 'allowed': STATUS_ALLOW, 'required': True},
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

        order = OrderModel.query.get(id)
        if not order:
            abort(404)

        # 不被允许的情况,403
        status = order_info.get('status')
        if (status == OrderModel.STATUS_CONFIRM and
                order.status != OrderModel.STATUS_LAUNCH):
            abort(403)
        if (status == OrderModel.STATUS_DISPATCH and
                order.status != OrderModel.STATUS_CONFIRM):
            abort(403)
        if (status == OrderModel.STATUS_CANCEL and
                order.status in [OrderModel.STATUS_DISPATCH,
                                 OrderModel.STATUS_SUCCESS,
                                 OrderModel.STATUS_CANCEL]):
            abort(403)

        order_info['date_updated'] = now()
        order.update(**order_info)

        # 没有权限管理时用2
        current_user_id = 2 
        OrderHistoryModel.create(
            order_id=order.id,
            status=order.status,
            operator_id=current_user_id)

        return jsonify(order.as_dict()), 200


bp.add_url_rule(
    '/order/<int:id>/',
    view_func=OrderPanelAPI.as_view('order'))
