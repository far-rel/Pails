# -*- coding: UTF8 -*-

class Route(object):

    def __init__(self):
        pass
        
    def resources(self, name, without = [], only = [], controller_string = None):
        pass
        
    def resource(self, name, without = [], only = [], controller_string = None):
        pass
        
    def match(self, regexp, controller_string):
        pass
        
    def root(self, controller_string):
        pass
