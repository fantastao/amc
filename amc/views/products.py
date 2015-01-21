# -*- coding: utf-8 -*-

from flask import (request, Blueprint, render_template,
                   redirect, url_for)
# from flask.ext.login import login_required, logout_user

from amc.models import ProductModel


bp = Blueprint('products', __name__, url_prefix='/products')

@bp.route('/', methods=['GET', 'POST'])
def products_index():
    if request.method == 'GET':
        # products = ProductModel.get_all_products()
        products = [{'id':1,'name':'product','category':'G', 'price':50, 'quantity':1000, 'made_in':'china'}, {'id':2,'name':'product','category':'M', 'price':30, 'quantity':2000, 'made_in':'japan'}]
        return render_template('products.html', products=products)
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


@bp.route('/details/<product_id>', methods=['GET', 'POST'])
def product_details(product_id):
    if request.method == 'GET':
        # product = ProductModel.get_by_id(product_id)
        products = [{'id':1,'name':'product','category':'G', 'price':50, 'quantity':1000, 'made_in':'china'}, {'id':2,'name':'product','category':'M', 'price':30, 'quantity':2000, 'made_in':'japan'}]
        product = {}
        for product in products:
            if product['id'] == product_id:
                break 
        return render_template('product_details.html', product=product)


@bp.route('/trolley', methods=['GET', 'POST'])
def shopping_trolley():
    if request.method == 'GET':
        return render_template('shopping_trolley.html')


