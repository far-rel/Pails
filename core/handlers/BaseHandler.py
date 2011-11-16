# -*- conding: UTF8 -*-

from tornado.web import RequestHandler

class BaseHandler(RequestHandler):

    def __init__(self, controller, methods, param_names):
        self.__conroller = controller
        self.__methods = methods
        self.__param_names = param_names
    
    def get(self, *args):
        params = dict(zip(param_names, args))
        self.__controller().__dict__[self.__methods['GET']]()

    def post(self, *args):
        params = dict(zip(param_names, args))
        self.__controller().__dict__[self.__methods['PUT']]()

    def put(self, *args):
        params = dict(zip(param_names, args))
        self.__controller().__dict__[self.__methods['PUT']]()

    def delete(self, *args):
        params = dict(zip(param_names, args))
        self.__controller().__dict__[self.__methods['DELETE']]()