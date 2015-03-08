# -*- coding: utf-8 -*-

from flask import (request, Blueprint, render_template,
                   redirect, url_for)
from flask.ext.login import login_required, logout_user

from .forms import LoginForm


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        form = LoginForm()
        return render_template('login.html', form=form)
    elif request.method == 'POST':
        form = LoginForm()
        if not form.validate_on_submit():
            # return form.errors rendered in templates
            return render_template('login.html', form=form)
        # after form validate finish,login_user directly
        # login_user(auth.user)
        return redirect(request.args.get('next') or url_for('home.index'))


@bp.route('/logout/', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.index'))
