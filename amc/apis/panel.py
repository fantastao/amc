# -*- coding: utf-8 -*-

from datetime import timedelta

from flask import views, Blueprint, request, jsonify, abort

from flask.ext.login import current_user, login_required

from amc.models import OrderModel, OrderHistoryModel, PayModel
from amc.utils import now
from amc.permissions import panel_permission

from .rest import AmcValidator

bp = Blueprint('panel', __name__, url_prefix='/apis/panel')


STATUS_ALLOW = [OrderModel.STATUS_CONFIRM, OrderModel.STATUS_DISPATCH,
                OrderModel.STATUS_CANCEL]

schema_dict = {
    'status': {'type': 'string', 'allowed': STATUS_ALLOW, 'required': True},
}


class OrderPanelAPI(views.MethodView):

    @login_required
    @panel_permission.require(401)
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

        # 若管理员取消订单，则修改库存
        if (status == OrderModel.STATUS_CANCEL):
            for item in order.products:
                product = item.product
                product.quantity += item.product_quantity
                product.date_updated = now()
                product.save()

        # 添加到订单修改历史 
        OrderHistoryModel.create(
            order_id=order.id,
            status=order.status,
            operator_id=current_user.id)

        return jsonify(order.as_dict()), 200

class IndexBarChartAPI(views.MethodView):

    @login_required
    @panel_permission.require(401)

    def get(self):
        results = dict()
        timeline = now() - timedelta(days=30)
        orders = (OrderModel.query
                        .filter(OrderModel.date_created > timeline)
                        .order_by(OrderModel.date_created.asc())
                        .all())
        for order in orders:
            timestamp = order.date_created.strftime('%Y-%m-%d')
            try:
                results[timestamp][0] += 1
                results[timestamp][1] += order.order_price
            except KeyError:
                results[timestamp] = [0,0]

        return jsonify(results)

class IndexPieChartAPI(views.MethodView):

    @login_required
    @panel_permission.require(401)

    def get(self):
        product_info = dict()
        timeline = now() - timedelta(days=7)
        orders = (OrderModel.query
                        .filter(OrderModel.date_created > timeline)
                        .all())
        for order in orders:
            products = order.products
            for product in products:
                product_id = product.product_id
                product_name = product.product.name
                product_quantity = product.product_quantity
                total_price = product.total_price
                try:
                    product_info[product_id][1] += product_quantity
                    product_info[product_id][2] += total_price
                except KeyError:
                    product_info[product_id] = [product_name, product_quantity, total_price]

        return jsonify(product_info)

bp.add_url_rule(
    '/order/<int:id>/',
    view_func=OrderPanelAPI.as_view('order'))
bp.add_url_rule(
    '/index_bar_chart/',
    view_func=IndexBarChartAPI.as_view('index_bar_chart'))
bp.add_url_rule(
    '/index_pie_chart/',
    view_func=IndexPieChartAPI.as_view('index_pie_chart'))
