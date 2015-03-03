# -*- coding: utf-8 -*-

from flask import views, Blueprint, request, jsonify, abort

from flask.ext.login import login_required, current_user

from amc.models import TrolleyProductModel

from .rest import AmcValidator

bp = Blueprint('open', __name__, url_prefix='/apis/open')


schema_dict = {
    'id': {'type': 'integer', 'required': True},
    'quantity': {'type': 'integer', 'required': True},
}


class TrolleyOpenAPI(views.MethodView):

    @login_required
    def post(self):
        schema = {
            'product_id': schema_dict['id'],
            'product_quantity': schema_dict['quantity'],
        }
        trolley_info = request.get_json()
        v = AmcValidator(schema)
        if not v(trolley_info):
            abort(422)

        # 购物车在创建用户时已经创建
        if not current_user.trolley:
            abort(404)

        # 有一种情况，之前添加过又来添加一遍，会报错
        trolley_id = current_user.trolley.id
        product_id = trolley_info.get('product_id')
        if TrolleyProductModel.query.get((trolley_id, product_id)):
            # conflict
            abort(409)

        trolley_info['trolley_id'] = trolley_id
        item = TrolleyProductModel.create(**trolley_info)
        return jsonify(item.as_dict()), 201

    @login_required
    def put(self, id):
        schema = {
            'product_quantity': schema_dict['quantity'],
        }
        trolley_info = request.get_json()
        v = AmcValidator(schema)
        if not v(trolley_info):
            abort(422)
        trolley_id = current_user.trolley.id
        item = TrolleyProductModel.query.get((trolley_id, id))
        if not item:
            abort(404)
        item.update(**trolley_info)
        return jsonify(item.as_dict()), 200

    @login_required
    def delete(self, id):
        trolley_id = current_user.trolley.id
        item = TrolleyProductModel.query.get((trolley_id, id))
        if not item:
            abort(404)
        item.delete()
        return jsonify({}), 204


view_func = TrolleyOpenAPI.as_view('trolley')
bp.add_url_rule('/trolley/', view_func=view_func)
bp.add_url_rule('/trolley/<int:id>/', view_func=view_func)
