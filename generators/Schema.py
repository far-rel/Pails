# -*- coding: UTF8 -*-
import os
from Generator import Generator
from ProjectSchema import ProjectSchema
from ModelSchema import ModelSchema
from Pails.utils.NameUtils import *

class Schema(object):

    __schemas = {}

    @staticmethod
    def register(template, name, cls):
        Schema.__schemas["{0:>s}.{1:>s}".format(template, name)] = cls

    def __init__(self, template, name):
        self.template = template
        self.__instance = Schema.__schemas["{0:>s}.{1:>s}".format(template, name)]()

    def generate(self, dir, name, *args):
        self.gen(self.__instance.file_schema, dir, name, *args)

    def gen(self, file_schema, dir, name, *args):
        for key in file_schema:
            plural = pluralize(name)
            if isinstance(file_schema[key], dict):
                new_dir = os.path.join(dir, key.format(name, plural))
                try:
                    os.mkdir(new_dir)
                except OSError:
                    pass
                self.gen(file_schema[key], new_dir, name, *args)
            else:
                new_file = os.path.join(dir, key.format(name, plural))
                if not os.path.exists(new_file):
                    f = open(new_file, 'w')
                    f.write(Generator(self.template, file_schema[key]).generate(name, *args))
                    f.close()
                

    def destroy(self, dir, name):
        self.__instance.des(dir, name)

    def des(self, dir, name):
        pass

Schema.register('default', 'project', ProjectSchema)
Schema.register('default', 'model', ModelSchema)