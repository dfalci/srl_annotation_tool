# -*- coding: utf-8; -*-
# Copyright (c) 2018, Visual Sistemas Eletrônicos - danielfalci@visual.com.br
#
# All rights reserved.


from singleton import Singleton
import ConfigParser
from dotmap import DotMap

@Singleton
class SystemConfig(object):

    def __init__(self):
        self.config = None
        self.db = DotMap()
        self.files = DotMap()

    def map(self):
        self.config = ConfigParser.ConfigParser()
        self.config.read('/Users/danielfalci/development/pycharm/teste/database.properties')
        self.db.usuario = self.config.get('database', 'usuario')
        self.db.senha = self.config.get('database', 'senha')
        self.db.porta = int(self.config.get('database', 'porta'))
        self.db.host = self.config.get('database', 'host')
        self.db.type = self.config.get('database', 'type')
        self.db.database = self.config.get('database', 'database')
        self.files.resource_dir = self.config.get('files', 'resource')


if __name__ == '__main__':
    SystemConfig.Instance().map()
    print SystemConfig.Instance().db.usuario
    print SystemConfig.Instance().files.resourceDir


