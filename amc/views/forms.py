# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms import validators
from wtforms import PasswordField, StringField
from flask.ext.login import login_user

from amc.utils import check_password
from amc.models import AuthModel


class LoginForm(Form):
    account = StringField('account',
                          validators=[validators.Required()])
    password = PasswordField('password', validators=[validators.Required()])

    def validate(self):
        base_validate = super(LoginForm, self).validate()
        if not base_validate:
            return False
        # extra validate
        if not AuthModel.account_exists_verified(self.account.data):
            self.account.errors.append('Account not exists or verified')
            return False
        auth = AuthModel.get_by_account(self.account.data)
        if not check_password(auth.pw_hash, self.password.data):
            self.password.errors.append('Password error')
        # login user here
        login_user(auth.user)
        return True
