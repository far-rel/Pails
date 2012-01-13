# -*- coding: UTF8 -*-

from ModelGenerator import ModelGenerator
from EmptyGenerator import EmptyGenerator
from LayoutGenerator import LayoutGenerator
from ManageGenerator import ManageGenerator
from RoutingGenerator import RoutingGenerator
from ConfigGenerator import ConfigGenerator

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
Generator.register('default', 'empty', EmptyGenerator)
Generator.register('default', 'layout', LayoutGenerator)
Generator.register('default', 'config', ConfigGenerator)
Generator.register('default', 'manage', ManageGenerator)
Generator.register('default', 'routing', RoutingGenerator)