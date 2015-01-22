# -*- coding: utf-8 -*-

from flask import request, Blueprint, render_template, redirect, views



bp = Blueprint('management', __name__)

class ManageIndexView(views.MethodView):
    
    template = 'management/order_manage.html'    
    
    def get(self):
        return render_template(self.template)

class ManageOrderView(views.MethodView):

    template = 'management/order_manage.html'    

    def get(self):
        return render_template(self.template)

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

