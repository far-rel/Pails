# -*- coding: UTF8 -*-

from Pails.exceptions.routes import RoutingDefinitionException
from UrlHelper import UrlHelper

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
        m = Match('', controller, action, 'GET', name = 'root')
        Route.__route_map.append(m)

    def optimize(self):
        routes = []
        for route in self:
            routes.append(route)
        i = 0
        to_remove = []
        to_insert = {}
        for route in routes:
            j = 0
            for other_route in routes:
                if i != j and i not in to_remove and j not in to_remove:
                    if route[0] == other_route[0] and\
                       route[1] == other_route[1] and\
                       route[2] == other_route[2]:
                        first_dict = route[3]
                        second_dict = other_route[3]
                        if i in to_insert:
                            first_dict = to_insert[i][3]
                        if j in to_insert:
                            second_dict = to_insert[j][3]
                        merge = dict(first_dict)
                        merge.update(second_dict)
                        if len(merge) == len(first_dict) + len(second_dict):
                            to_remove.append(j)
                            to_insert[i] = (route[0], route[1], route[2], merge, route[4])
                            if j in to_insert:
                                del to_insert[j]
                        else:
                            raise RoutingDefinitionException('Method defined twice')
                    elif route[0] == other_route[0] and\
                       route[1] == other_route[1] and\
                       route[2] != other_route[2]:
                        raise RoutingDefinitionException('Same routes with different controllers')
                    elif route[0] == other_route[0] and\
                       route[1] != other_route[1]:
                        raise RoutingDefinitionException('Same routes with different variables')
                j += 1
            i+= 1
        for insert in to_insert:
            routes[insert] = to_insert[insert]
        for remove in to_remove:
            routes.remove(routes[remove])
        helper = UrlHelper()

        for route in routes:
            if route[4] is not None:
                helper.append(route[4], route[0])
        return (routes, helper)

    def __iter__(self):
        for item in Route.__route_map:
            for route, variables, controller, methods, name in item:
                variables.append('format')
                yield ('/{0:>s}(.[a-z0-9]+)?'.format(route), variables, controller, methods, name)
