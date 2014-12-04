# -*- coding: utf-8 -*-

from flask.ext.script import Manager, Server
from flask.ext.migrate import MigrateCommand

from amc.app import create_app

app = create_app()
manager = Manager(app)

manager.add_command('db', MigrateCommand)
manager.add_command('server', Server(host='0.0.0.0'))

if __name__ == '__main__':
    manager.run()
