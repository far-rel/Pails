# -*- coding: UTF8 -*-

class ActionSet(object):

    def __init__(self):
        self.__actions = []
    
    def get(self, name):
        self.__actions.append((name, 'GET'))
        
    def post(self, name):
        self.__actions.append((name, 'POST'))
        
    def put(self, name):
        self.__actions.append((name, 'PUT'))
    
    def delete(self, name):
        self.__actions.append((name, 'DELETE'))

    def __iter__(self):
        for name, method in self.__actions:
            print name, [], None, { method : name }
            yield ( name, [], None, { method : name } )
