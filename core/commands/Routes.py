# -*- coding: UTF8 -*-
from Command import Command

class Routes(Command):

    def __call__(self):
        import project.routes #This needs to be replaced by import projects routes file to setup route maps
        from Pails.core.routes.Route import Route
        for (route, variables, controller, methods) in Route():
            for method in methods:
                print "Address => %s Controller => %s Method => %s Actions => %s" % (route, controller, method, methods[method])

    @staticmethod
    def parser(subparser):
        pass