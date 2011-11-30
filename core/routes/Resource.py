# -*- coding:UTF8 -*-

from ActionSet import ActionSet

class Resource(object):

    def __init__(self, name, without = None, only = None, controller_string = None):
        self.__name = name
        self.__without = without
        self.__only = only
        if controller_string is None:
            self.__controller_string = name
        else:
            self.__controller_string = controller_string
        self.__member = ActionSet()
        self.__route_map = []
        
    def resources(self, name, without = None, only = None, controller_string = None):
        from Resources import Resources
        r = Resources(name, without, only, controller_string)
        self.__route_map.append(r)
        return r
        
    def resource(self, name, without = None, only = None, controller_string = None):
        r = Resource(name, without, only, controller_string)
        self.__route_map.append(r)
        return r

    def member(self):
        return self.__member

    def __include(self, name):
        if not self.__only is None:
            return (name == self.__only or name in self.__only)
        elif not self.__without is None:
            return (name != self.__without or not name in self.__without)
        else:
            return True

    def __iter__(self):
        methods = { }
        if self.__include('show'):
            methods['GET'] = 'show'
        if self.__include('create'):
            methods['POST'] = 'create'
        if self.__include('update'):
            methods['PUT'] = 'update'
        if self.__include('destroy'):
            methods['DELETE'] = 'destroy'
        if len(methods) > 0:
            yield (self.__name, [], self.__controller_string, methods)
        if self.__include('edit'):
            yield ('{0:>s}/edit'.format(self.__name), [], self.__controller_string, {'GET' : 'edit' })
        if self.__include('new'):
            yield ('{0:>s}/new'.format(self.__name), [], self.__controller_string, {'GET' : 'new' })
        for item in self.__member:
            for route, variables, controller, methods in item:
                yield ( '{0:>s}/{1:>s}'.format(self.__name, route), variables, self.__controller_string, methods )
        for item in self.__route_map:
            for route, variables, controller, methods in item:
                yield ( '{0:>s}/{1:>s}'.format(self.__name, route), variables, controller, methods )

