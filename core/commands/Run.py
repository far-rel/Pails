# -*- coding:utf-8 -*-
import sys
from Command import Command
from tornado.ioloop import IOLoop
from tornado.web import Application, StaticFileHandler
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
        routes.append(('/public/(.*)', StaticFileHandler, {'path' : self._config.project_path + '/' + 'public/'}))
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
        controller_class = __import__('app.controllers.{0:>s}_controller'.format(name)).__dict__['controllers']
        i = 0
        subnames = name.split('.')
        for subname in subnames:
            if i == len(subnames) - 1:
                controller_class = controller_class.__dict__['{0:>s}_controller'.format(subname)].__dict__['{0:>s}Controller'.format(subname.capitalize())]
            else:
                controller_class = controller_class.__dict__[subname]
            i+=1
        return controller_class