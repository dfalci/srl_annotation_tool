# -*- coding: utf-8; -*-
# Copyright (c) 2018, Visual Sistemas Eletrônicos - danielfalci@visual.com.br
#
# All rights reserved.

class Singleton:

    def __init__(self, itemDecorated):
        self.__itemDecorated = itemDecorated

    def Instance(self):
        try:
            return self.__instance
        except AttributeError:
            self.__instance = self.__itemDecorated()
            return self.__instance

    def __call__(self):
        raise TypeError('singleton access violated')

    def __instancecheck__(self, instance):
        return isinstance(instance, self.__itemDecorated)