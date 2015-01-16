# -*- coding: utf-8 -*-

from werkzeug.security import generate_password_hash, check_password_hash


def set_password(pw):
    return generate_password_hash(pw)


def check_password(pw_hash, pw):
    return check_password_hash(pw_hash, pw)
