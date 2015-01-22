# -*- coding: utf-8 -*-

from flask import (request, Blueprint, render_template,
                   redirect, url_for)
# from flask.ext.login import login_required, logout_user

# from amc.models import ProductModel


bp = Blueprint('management', __name__, url_prefix='/management')

@bp.route('/', methods=['GET', 'POST'])
def management_index():
    if request.method == 'GET':
        # products = ProductModel.get_all_products()
        products = [{'id':1,'name':'product','category':'G', 'price':50, 'quantity':1000, 'made_in':'china'}, {'id':2,'name':'product','category':'M', 'price':30, 'quantity':2000, 'made_in':'japan'}]
        return render_template('management/management.html')
    '''
    elif request.method == 'POST':
        form = LoginForm(request.form)
        if not form.validate():
            # return form.errors rendered in templates
            return render_template('login.html', form=form)
        # after form validate finish,login_user directly
        # login_user(auth.user)
        return redirect(request.args.get('next') or url_for('home.index'))
    '''

@bp.route('/orders', methods=['GET', 'POST'])
def management_orders():
    if request.method == 'GET':
        # products = ProductModel.get_all_products()
        products = [{'id':1,'name':'product','category':'G', 'price':50, 'quantity':1000, 'made_in':'china'}, {'id':2,'name':'product','category':'M', 'price':30, 'quantity':2000, 'made_in':'japan'}]
        # return render_template('management/management.html')
        return "here"



