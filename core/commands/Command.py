# -*- coding:utf-8 -*-

class Command(object):

    def __init__(self):
        '''
            This method may configure command object, call method not take parameters
        '''
        raise NotImplementedError

    def __call__(self):
        '''
            This method implement executing of command
        '''
        raise NotImplementedError
  