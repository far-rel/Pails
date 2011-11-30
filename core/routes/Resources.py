# -*- coding:UTF8 -*-

from ActionSet import ActionSet


class Resources(object):

    def __init__(self, name, without = None, only = None, controller_string = None):
        self.__name = name
        self.__without = without
        self.__only = only
        if controller_string is None:
            self.__controller_string = name
        else:
            self.__controller_string = controller_string
        self.__member = ActionSet()
        self.__collection = ActionSet()
        self.__route_map = []
        
    def resources(self, name, without = None, only = None, controller_string = None):
        r = Resources(name, without, only, controller_string)
        self.__route_map.append(r)
        return r
        
    def resource(self, name, without = None, only = None, controller_string = None):
        from Resource import Resource
        r = Resource(name, without, only, controller_string)
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
            yield ('{0:>s}/[\D\d]*'.format(self.__name), ['id'], self.__controller_string, methods)
        if self.__include('index'):
            yield (self.__name, [], self.__controller_string, { 'GET' : 'index' })
        if self.__include('new'):
            yield ('{0:>s}/new'.format(self.__name), [], self.__controller_string, {'GET' : 'new' })
        if self.__include('edit'):
            yield ('{0:>s}/[\D\d]*/edit'.format(self.__name), ['id'], self.__controller_string, {'GET' : 'edit' })
        for route, variables, controller, methods in self.__collection:
            yield ( '{0:>s}/{1:>s}'.format(self.__name, route), variables, self.__controller_string, methods )
        for route, variables, controller, methods in self.__member:
            variables.insert(0, 'id')
            yield ( '{0:>s}/[\D\d]*/{1:>s}'.format(self.__name, route),
                    variables, self.__controller_string, methods )
        for item in self.__route_map:
            for route, variables, controller, methods in item:
                var_name = 'id'
                while var_name in variables:
                    var_name = self.__name + '_' + var_name
                variables.insert(0, var_name)
                yield ( '{0:>s}/[\D\d]*/{1:>s}'.format(self.__name, route), variables, controller, methods )
