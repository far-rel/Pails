# -*- coding: UTF8 -*-
from Command import Command
import sys
from Pails.core.config.Settings import Settings

class Routes(Command):

    def __init__(self, config, **params):
        Command.__init__(self, config, **params)
        self._config = Settings(config)

    def __call__(self):
        sys.path.append(self._config.project_path)
        import app.routing
        from Pails.core.routes import Route
        for (route, variables, controller, methods, name) in Route().optimize()[0]:
            for method in methods:
                print "Address => %s Controller => %s Method => %s Action => %s Name => %s" % (route, controller, method, methods[method], name)

    @staticmethod
    def parser(subparser):
        parser = subparser.add_parser('routes', help='Show current routes')
        return parser
