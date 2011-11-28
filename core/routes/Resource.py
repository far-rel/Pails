# -*- coding:UTF8 -*-

from Resources import Resources
from ActionSet import ActionSet

class Resource(object):

    def __init__(self, name, without = [], only = [], controller_string = None):
        self.__name = name
        self.__without = without
        self.__only = only
        if controller_string is None:
            self.__controller_string = name
        else:
            self.__controller_string = controller_string
        self.__member = ActionSet()
        self.__route_map = []
        
    def resources(self, name, without = [], only = [], controller_string = None):
        r = Resources(name, without, only, controller_string)
        self.__route_map.append(r)
        return r
        
    def resource(self, name, without = [], only = [], controller_string = None):
        r = Resource(name, without, only, controller_string)
        self.__route_map.append(r)
        return r

    def __iter__(self):
        methods = {
            'GET': 'show',
            'POST': 'create',
            'PUT': 'update',
            'DELETE': 'destroy'
        }
        yield (self.__name, [], None, methods)
        yield (self.__name + '/edit', [], None, {'GET' : 'edit' })
        yield (self.__name + '/new', [], None, {'GET' : 'new' })
        for item in self.__member:
            for route, variables, controller, methods in item:
                yield ( self.__name + '/' + route, variables, controller, methods )
        for item in self.__route_map:
            for route, variables, controller, methods in item:
                yield ( self.__name + '/' + route, variables, controller, methods )

