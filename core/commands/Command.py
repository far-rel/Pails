# -*- coding:utf-8 -*-

class Command(object):

    def __init__(self, config, **params):
        '''
            This method may configure command object, call method not take parameters
        '''
        self._config = config

    def __call__(self):
        '''
            This method implement executing of command
        '''
        raise NotImplementedError

    @staticmethod
    def parser(subparser):
        '''
            This method return subparser to command line in manager
        '''
        subparser.add('example',help = 'command')
  