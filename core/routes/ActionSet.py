# -*- coding: UTF8 -*-

class ActionSet(object):

    def __init__(self):
        self.actions = []
    
    def get(self, name):
        self.actions.append((name, 'GET'))
        
    def post(self, name):
        self.actions.append((name, 'POST'))
        
    def put(self, name):
        self.actions.append((name, 'PUT'))
    
    def delete(self, name):
        self.actions.append((name, 'DELETE'))
