# -*- coding:utf8 -*-

from Pails.exceptions.routes import InvalidMethodException
import re

class Match(object):

    def __init__(self, route, controller, action, method = None, name = None):
        self.__route = route
        self.__controller = controller
        self.__action = action
        self.__name = name
        if method is None:
            self.__method = 'GET'
        else:
            if method in ['GET', 'POST', 'PUT', 'DELETE']:
                self.__method = method
            else:
                raise InvalidMethodException('{0:>s} is invalid method'.format(method))

    def __iter__(self):
        expression = re.compile(r':[_a-z]+[_a-z0-9]*')
        matches = re.findall(expression, self.__route)
        variables = [m.replace(':', '') for m in matches]
        route = re.sub(expression, '[\D\d]*', self.__route)
        yield (route, variables, self.__controller, { self.__method : self.__action }, self.__name )
