# -*- coding: UTF8 -*-

class Route(object):

    __route_map = []

    def namespace(self, name):
        from Namespace import Namespace
        n = Namespace(name)
        Route.__route_map.append(n)
        return n

    def resources(self, name, without = None, only = None, controller = None, _as = None):
        from Resources import Resources
        r = Resources(name, without, only, controller, _as)
        Route.__route_map.append(r)
        return r
        
    def resource(self, name, without = None, only = None, controller = None, _as = None):
        from Resource import Resource
        r = Resource(name, without, only, controller, _as)
        Route.__route_map.append(r)
        return r
        
    def match(self, route, controller, action, method = None, _as = None):
        from Match import Match
        m = Match(route, controller, action, method, _as)
        Route.__route_map.append(m)
        return m


    def root(self, controller, action):
        from Match import Match
        m = Match('', controller, action, 'GET')
        Route.__route_map.append(m)

    def optimize(self):
        pass

    def __iter__(self):
        for item in Route.__route_map:
            for route, variables, controller, methods in item:
                variables.append('format')
                yield ('/{0:>s}(.[a-z0-9]+)?'.format(route), variables, controller, methods)
