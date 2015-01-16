# -*- coding: utf-8 -*-

class DevConfig:

    DEBUG = True
    SECRET_KEY = '2a3m6c8'
    AVATAR_DEFAULT = 'http://chuantu.biz/t/62/1421399635x1822611447.png'
    STATIC_FOLDER = 'static'
    SQLALCHEMY_DATABASE_URI = 'postgresql://amc:aaaa@localhost/amc'
    SQLALCHEMY_ECHO = True


class ProdConfig(DevConfig):

    DEBUG = False
    SQLALCHEMY_ECHO = False
