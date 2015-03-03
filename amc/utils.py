# -*- coding: utf-8 -*-

from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash


def now():
    import pytz
    now = datetime.utcnow()
    now = pytz.utc.localize(now)
    return now


def localtime(dt):
    """convert pql datetime to local datetime"""
    from dateutil import tz
    local_tz = tz.gettz('Asia/Shanghai')
    dt = dt.astimezone(local_tz)
    return dt 


def fmt_time(dt):
    """精确到分"""
    dt = localtime(dt)
    fmt = "%Y-%m-%d %H:%M"
    dt = dt.strftime(fmt)
    return dt


def set_password(pw):
    return generate_password_hash(pw)


def check_password(pw_hash, pw):
    return check_password_hash(pw_hash, pw)


# 由于不开放注册，所以由管理员给用户登陆账号
origin_pw_hash = set_password('123456')
