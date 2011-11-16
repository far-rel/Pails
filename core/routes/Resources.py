# -*- coding:UTF8 -*-

class Resources(object):

    def __init__(self, name, without = [], only = [], controller_string = None):
        self.member = ActionSet()
        self.collection = ActionSet()
        
    def resources(self, name, without = [], only = [], controller_string = None):
        pass
        
    def resource(self, name, without = [], only = [], controller_string = None):
        pass

