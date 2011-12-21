# -*- coding: UTF8 -*-
from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader

from tornado.web import RequestHandler

class BaseHandler(RequestHandler):

    def initialize(self, controller, methods, param_names, name, project_path):
        self.__controller = controller
        self.__methods = methods
        self.__param_names = param_names
        self.__name = name
        self.__env = Environment(loader = FileSystemLoader(project_path + '/app/views'))
    
    def get(self, *args):
        params = dict(zip(self.__param_names, args))
        self.__controller().__getattribute__(self.__methods['GET'])()
        temp = self.__env.get_template(self.__name + '/' + self.__methods['GET'] + '.html')
        self.write(temp.render())

    def post(self, *args):
        params = dict(zip(self.__param_names, args))
        self.__controller().__getattribute__(self.__methods['PUT'])()

    def put(self, *args):
        params = dict(zip(self.__param_names, args))
        self.__controller().__getattribute__(self.__methods['PUT'])()

    def delete(self, *args):
        params = dict(zip(self.__param_names, args))
        self.__controller().__getattribute__(self.__methods['DELETE'])()