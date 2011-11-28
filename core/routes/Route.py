# -*- coding: UTF8 -*-

#from routes.Match import Match


class Route(object):

    def __init__(self):
        self.__route_map = []
        
    def resources(self, name, without = [], only = [], controller_string = None):
        from Resources import Resources
        r = Resources(name, without, only, controller_string)
        self.__route_map.append(r)
        return r
        
    def resource(self, name, without = [], only = [], controller_string = None):
        from Resource import Resource
        r = Resource(name, without, only, controller_string)
        self.__route_map.append(r)
        return r
        
    def match(self, regexp, controller_string):
#        m = Match(name, without, only, controller_string)
#        return m
        pass
        
    def root(self, controller_string):
        pass

    def __iter__(self):
        for item in self.__route_map:
            for route, variables, controller, methods in item:
                yield ('/' + route, variables, controller, methods)
