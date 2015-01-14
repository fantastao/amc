# -*- coding: utf-8 -*-

class DevConfig:

    DEBUG = True
    STATIC_FOLDER = 'static'
    SQLALCHEMY_DATABASE_URI = 'postgresql://amc:aaaa@localhost/amc'
    SQLALCHEMY_ECHO = True


class ProdConfig(DevConfig):

    DEBUG = False
    SQLALCHEMY_ECHO = False
