# -*- coding:UTF8 -*-

from ActionSet import ActionSet


class Resources(object):

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
        self.__collection = ActionSet()
        self.__route_map = []
        
    def resources(self, name, without = None, only = None, controller = None, _as = None):
        r = Resources(name, without, only, controller, _as)
        self.__route_map.append(r)
        return r
        
    def resource(self, name, without = None, only = None, controller = None, _as = None):
        from Resource import Resource
        r = Resource(name, without, only, controller, _as)
        self.__route_map.append(r)
        return r

    def member(self):
        return self.__member

    def collection(self):
        return self.__collection

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
            yield ('{0:>s}/[\D\d]*'.format(self.__as), ['id'],
                   self.__controller, methods, self.__name)
        if self.__include('index'):
            yield (self.__as, [], self.__controller, { 'GET' : 'index' },
                   '{0:>s}s'.format(self.__name))
        if self.__include('new'):
            yield ('{0:>s}/new'.format(self.__as), [], self.__controller,
                       {'GET' : 'new' }, '{0:>s}_new'.format(self.__name))
        if self.__include('edit'):
            yield ('{0:>s}/[\D\d]*/edit'.format(self.__as), ['id'], self.__controller,
                       {'GET' : 'edit' }, '{0:>s}_edit'.format(self.__name))
        for route, variables, controller, methods, name in self.__collection:
            yield ( '{0:>s}/{1:>s}'.format(self.__name, route), variables, self.__controller,
                    methods, '{0:>s}s_{1:>s}'.format(self.__name, name) )
        for route, variables, controller, methods, name in self.__member:
            variables.insert(0, 'id')
            yield ( '{0:>s}/[\D\d]*/{1:>s}'.format(self.__as, route),
                    variables, self.__controller, methods, '{0:>s}_{1:>s}'.format(self.__name, name) )
        for item in self.__route_map:
            for route, variables, controller, methods, name in item:
                var_name = 'id'
                while var_name in variables:
                    var_name = self.__name + '_' + var_name
                variables.insert(0, var_name)
                yield ( '{0:>s}/[\D\d]*/{1:>s}'.format(self.__as, route), variables, controller,
                        methods, '{0:>s}_{1:>s}'.format(self.__name, name) )
