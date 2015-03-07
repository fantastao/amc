# -*- coding: utf-8 -*-

from flask import session

from flask.ext.principal import Principal
from flask.ext.principal import Permission, RoleNeed, Identity

from amc.models import UserModel

# 这里设成False让默认的session格式来获取当前identity信息功能disable
# 然后利用identity_loader从flask-login的session获取自定义的identity
principal = Principal(use_sessions=False)
panel_permission = Permission(RoleNeed('panel'))


@principal.identity_loader
def current_user_identity():
    if not session.get('user_id'):
        return None
    user_id = session['user_id']
    identity = Identity(user_id)
    user = UserModel.query.get(user_id)
    if user and user.is_admin:
        identity.provides.add(RoleNeed('panel'))
    return identity
