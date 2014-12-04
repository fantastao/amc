# -*- coding: utf-8 -*-

class DevConfig:

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://amc:aaaa@localhost/amc'


class ProdConfig(DevConfig):

    DEBUG = False
