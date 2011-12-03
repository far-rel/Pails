# -*- coding: UTF8 -*-

class ActionSet(object):

    def __init__(self):
        self.__actions = []
    
    def get(self, name, _as = None):
        get = {
            'name':name,
            'as':_as,
            'method':'GET'
        }
        if _as is None:
            get['as'] = name
        self.__actions.append(get)
        
    def post(self, name, _as = None):
        post = {
            'name':name,
            'as':_as,
            'method':'POST'
        }
        if _as is None:
            post['as'] = name
        self.__actions.append(post)
        
    def put(self, name, _as = None):
        put = {
            'name':name,
            'as':_as,
            'method':'PUT'
        }
        if _as is None:
            put['as'] = name
        self.__actions.append(put)
    
    def delete(self, name, _as = None):
        delete = {
            'name':name,
            'as':_as,
            'method':'DELETE'
        }
        if _as is None:
            delete['as'] = name
        self.__actions.append(delete)

    def __iter__(self):
        for action in self.__actions:
            yield ( action['as'], [], '', { action['method'] : action['name'] } )
