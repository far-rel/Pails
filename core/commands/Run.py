# -*- coding:utf-8 -*-
from Command import Command

class Run(Command):

    def __init__(self, config, **params):
        Command.__init__(self, config, **params)

    def __call__(self):
        print 'running server'

    @staticmethod
    def parser(subparser):
        parser = subparser.add_parser('run', help='run server')
        parser.add_argument('environment', nargs='?', default = 'development', help='start with default configuration(development)')
        return parser