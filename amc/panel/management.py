# -*- coding: utf-8 -*-

from flask import request, Blueprint, render_template, redirect, views

from amc.models import OrderModel

bp = Blueprint('management', __name__)

class ManageIndexView(views.MethodView):
    
    template = 'management/order_manage.html'    
    
    def get(self):
        # order = OrderModel.query.all()
        orders = [{'id':1,'customer_id':111, 'status':'launch'}, {'id':'2','customer_id':222,'status':'launch'}]
        return render_template(self.template, orders = orders)

class ManageOrderView(views.MethodView):

    template = 'management/order_manage.html'    

    def get(self):
        # order = OrderModel.query.all()
        orders = [{'id':1,'customer_id':111, 'status':'launch'}, {'id':'2','customer_id':222,'status':'launch'}]
        return render_template(self.template, orders = orders)

class ManageProductView(views.MethodView):

    template = 'management/product_manage.html'    

    def get(self):
        return render_template(self.template)

class ManagePurchaseView(views.MethodView):

    template = 'management/purchase_manage.html'    

    def get(self):
        return render_template(self.template)

class ManageAccountView(views.MethodView):

    template = 'management/account_manage.html'    

    def get(self):
        return render_template(self.template)

class ManageCustomerView(views.MethodView):

    template = 'management/customer_manage.html'    

    def get(self):
        return render_template(self.template)

class OrderDeleteView(views.MethodView):

    def get(self):
        id = request.args.get('id','1')
        '''
        item = OrderModel.query.get(id)
        status = OrderModel.delete(item)
        if item and status:
            return 'success'
        '''
        return 'success'

bp.add_url_rule(
    '/management/',
    view_func=ManageIndexView.as_view('index'))
bp.add_url_rule(
    '/management/orders/',
    view_func=ManageOrderView.as_view('order'))
bp.add_url_rule(
    '/management/products/',
    view_func=ManageProductView.as_view('product'))
bp.add_url_rule(
    '/management/purchases/',
    view_func=ManagePurchaseView.as_view('purchase'))
bp.add_url_rule(
    '/management/accounts/',
    view_func=ManageAccountView.as_view('account'))
bp.add_url_rule(
    '/management/customers/',
    view_func=ManageCustomerView.as_view('customer'))
bp.add_url_rule(
    '/order/delete/',
    view_func=OrderDeleteView.as_view('order_delete'))

