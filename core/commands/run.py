# -*- coding:utf-8 -*-
from command import Command

class Run(Command):

    def __init__(self, **params):
        pass

    def __call__(self):
        print 'running server'
  