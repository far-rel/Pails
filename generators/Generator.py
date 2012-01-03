# -*- coding: UTF8 -*-

from ModelGenerator import ModelGenerator

class Generator(object):

    __generators = {}

    @staticmethod
    def register(template, name, cls):
        Generator.__generators["{0:>s}.{1:>s}".format(template, name)] = cls

    def __init__(self, template, name):
        self.__instance = Generator.__generators["{0:>s}.{1:>s}".format(template, name)]()

    def generate(self, name, *args):
        return self.__instance.generate(name, args)

Generator.register('default', 'model', ModelGenerator)