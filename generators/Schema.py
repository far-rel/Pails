# -*- coding: UTF8 -*-
import os

class Schema(object):

    __schemas = {}

    @staticmethod
    def register(template, name, cls):
        Schema.__schemas["{0:>s}.{1:>s}".format(template, name)] = cls

    def __init__(self, template, name):
        self.__instance = Schema.__schemas["{0:>s}.{1:>s}".format(template, name)]()

    def generate(self, dir, name, *args):
        pass

    def destroy(self):
        pass
    