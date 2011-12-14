# -*- coding: UTF8 -*-

class Namespace(object):

    def __init__(self, name, _as = None):
        self.__route_map = []
        self.__name = name
        if _as is None:
            self.__as = name
        else:
            self.__as = _as

    def resources(self, name, without = None, only = None, controller = None, _as = None):
        from Resources import Resources
        r = Resources(name, without, only, controller, _as)
        self.__route_map.append(r)
        return r

    def resource(self, name, without = None, only = None, controller = None, _as = None):
        from Resource import Resource
        r = Resource(name, without, only, controller, _as)
        self.__route_map.append(r)
        return r

    def __iter__(self):
        for item in self.__route_map:
            for route, variables, controller, methods, name in item:
                yield ('{0:>s}/{1:>s}'.format(self.__as, route), variables,
                       '{0:>s}/{1:>s}'.format(self.__as, controller), methods, '{0:>s}_{1:>s}'.format(self.__name, name))