# -*- coding: UTF8 -*-

class Route(object):

    __route_map = []

    def namespace(self, name):
        from Namespace import Namespace
        n = Namespace(name)
        Route.__route_map.append(n)
        return n

    def resources(self, name, without = None, only = None, controller_string = None):
        from Resources import Resources
        r = Resources(name, without, only, controller_string)
        Route.__route_map.append(r)
        return r
        
    def resource(self, name, without = None, only = None, controller_string = None):
        from Resource import Resource
        r = Resource(name, without, only, controller_string)
        Route.__route_map.append(r)
        return r
        
    def match(self, route, controller_string, action, method = None):
        from Match import Match
        m = Match(route, controller_string, action, method)
        Route.__route_map.append(m)
        return m


    def root(self, controller_string, action):
        from Match import Match
        m = Match('', controller_string, action, 'GET')
        Route.__route_map.append(m)

    def __iter__(self):
        for item in Route.__route_map:
            for route, variables, controller, methods in item:
                yield ('/{0:>s}'.format(route), variables, controller, methods)
