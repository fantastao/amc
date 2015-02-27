# -*- coding: utf-8 -*-

import re

from flask.ext.wtf import Form
from wtforms.validators import DataRequired, Optional, Length
from wtforms import PasswordField, StringField, BooleanField, FieldList
from wtforms import ValidationError
from flask.ext.login import login_user

from amc.utils import check_password
from amc.models import AuthModel


class LoginForm(Form):

    account = StringField('account', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

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
            return False
        # login user here
        login_user(auth.user)
        return True


class UserProfileForm(Form):

    name = StringField(
        u'用户名',
        validators=[DataRequired(), Length(min=2, max=20)])
    phone = StringField(u'电话', validators=[Optional()])
    address = StringField(u'地址',
                          validators=[Optional(), Length(min=2, max=256)])

    def validate_phone(form, field):
        re_mobile = re.compile(r'^((\+86)|(86))?(1)[3|4|5|7|8|]\d{9}$')
        if not re.match(re_mobile, field.data):
            raise ValidationError('Not a phone number')
