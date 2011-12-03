# -*- coding: UTF8 -*-

from Pails.exceptions.routes import RoutingDefinitionException

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
        routes = []
        for route in Route.__route_map:
            routes.append(route)
        i = 0
        to_remove = []
        to_insert = {}
        for route in routes:
            j = 0
            for other_route in routes:
                if i != j:
                    if route[0] == other_route[0] and\
                       route[1] == other_route[1] and\
                       route[2] == other_route[2]:
                        merge = dict(route[3])
                        merge.update(other_route[3])
                        if len(merge) != len(route[3]) + len(other_route[3]):
                            to_remove.append(j)
                            to_insert[i] = (route[0], route[1], route[2], merge)
                        else:
                            pass
                j += 1
            i+= 1



    def __iter__(self):
        for item in Route.__route_map:
            for route, variables, controller, methods in item:
                variables.append('format')
                yield ('/{0:>s}(.[a-z0-9]+)?'.format(route), variables, controller, methods)
