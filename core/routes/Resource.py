# -*- coding:UTF8 -*-

from ActionSet import ActionSet

class Resource(object):

    def __init__(self, name, without = None, only = None, controller = None, _as = None):
        self.__name = name
        self.__without = without
        self.__only = only
        if controller is None:
            self.__controller = name
        else:
            self.__controller = controller
        if _as is None:
            self.__as = name
        else:
            self.__as = _as
        self.__member = ActionSet()
        self.__route_map = []
        
    def resources(self, name, without = None, only = None, controller = None, _as = None):
        from Resources import Resources
        r = Resources(name, without, only, controller, _as)
        self.__route_map.append(r)
        return r
        
    def resource(self, name, without = None, only = None, controller = None, _as = None):
        r = Resource(name, without, only, controller, _as)
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
            yield (self.__name, [], self.__controller, methods)
        if self.__include('edit'):
            yield ('{0:>s}/edit'.format(self.__name), [], self.__controller, {'GET' : 'edit' })
        if self.__include('new'):
            yield ('{0:>s}/new'.format(self.__name), [], self.__controller, {'GET' : 'new' })
        for item in self.__member:
            for route, variables, controller, methods in item:
                yield ( '{0:>s}/{1:>s}'.format(self.__as, route), variables, self.__controller, methods )
        for item in self.__route_map:
            for route, variables, controller, methods in item:
                yield ( '{0:>s}/{1:>s}'.format(self.__as, route), variables, controller, methods )

