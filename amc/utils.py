# -*- coding: utf-8 -*-

from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash


def now():
    import pytz
    now = datetime.utcnow()
    now = pytz.utc.localize(now)
    return now


def set_password(pw):
    return generate_password_hash(pw)


def check_password(pw_hash, pw):
    return check_password_hash(pw_hash, pw)


# 由于不开放注册，所以由管理员给用户登陆账号
origin_pw_hash = set_password('123456')
