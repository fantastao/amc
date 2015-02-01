# -*- coding: utf-8 -*-

import re

from flask.ext.wtf import Form
from wtforms.validators import DataRequired, Optional, Length, Email
from wtforms import StringField
from wtforms.fields.html5 import EmailField
from wtforms import ValidationError

# from amc.models import AuthModel


class UserInfoForm(Form):
    """后台创建用户，修改用户信息"""

    name = StringField(
        u'用户名',
        validators=[DataRequired(), Length(min=2, max=20)])
    phone = StringField(u'电话', validators=[Optional()])
    address = StringField(u'地址',
                          validators=[Optional(), Length(min=2, max=256)])
    account = EmailField(u'邮箱（即登录名）', validators=[DataRequired(), Email()])

    """
    def validate_account(form, field):
        auth = AuthModel.get_by_account(field.data)
        if auth:
            raise ValidationError('Account exists')
    """

    def validate_phone(form, field):
        re_mobile = re.compile(r'^((\+86)|(86))?(1)[3|4|5|7|8|]\d{9}$')
        if not re.match(re_mobile, field.data):
            raise ValidationError('Not a phone number')
