# -*- coding: UTF8 -*-

class Namespace(object):

    def __init__(self, name):
        self.__route_map = []
        self.__name = name

    def resources(self, name, without = None, only = None, controller_string = None):
        from Resources import Resources
        r = Resources(name, without, only, controller_string)
        self.__route_map.append(r)
        return r

    def resource(self, name, without = None, only = None, controller_string = None):
        from Resource import Resource
        r = Resource(name, without, only, controller_string)
        self.__route_map.append(r)
        return r

    def __iter__(self):
        for item in self.__route_map:
            for route, variables, controller, methods in item:
                yield ('{0:>s}/{1:>s}'.format(self.__name, route), variables, controller, methods)