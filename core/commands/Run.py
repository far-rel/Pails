# -*- coding:utf-8 -*-
import sys
from Command import Command
from tornado.ioloop import IOLoop
from tornado.web import Application
from Pails.core.handlers import BaseHandler

class Run(Command):

    def __init__(self, config, **params):
        Command.__init__(self, config, **params)

    def __call__(self):
        sys.path.append(self._config.project_path)
        import app.routing
        from Pails.core.routes.Route import Route
        routing = Route().optimize()
        path_helper = routing[1]
        routes = []
        for (route, variables, controller, methods, name) in routing[0]:
            params = {
                'controller': self.__get_controller(controller),
                'methods': methods,
                'param_names': variables,
                'name' : controller,
                'project_path' : self._config.project_path
            }
            routes.append((route, BaseHandler, params))
        settings = {}
        app = Application(routes, **settings)
        app.listen(8888)
        IOLoop.instance().start()
        print 'running server'

    @staticmethod
    def parser(subparser):
        parser = subparser.add_parser('run', help='run server')
        parser.add_argument('environment', nargs='?', default = 'development', help='start with default configuration(development)')
        return parser

    def __get_controller(self, name):
        name = name.replace('/', '.')
        real_name = name.split('.')[-1].capitalize()
        #return __import__('UserController', fromlist='app.controllers.user_controller')
        return __import__("app.controllers.{0:>s}_controller".format(name)).\
            __dict__['controllers'].\
            __dict__['user_controller'].\
            __dict__['UserController']
        #return __import__("app.controllers.{0:>s}_controller.{1:>s}Controller".format(name, real_name))