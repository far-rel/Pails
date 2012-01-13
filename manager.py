# -*- coding:utf-8 -*-
import logging
import argparse
from argparse import ArgumentParser
from core.commands import Run
from core.commands import Routes

log = logging.getLogger(__name__)

class PailsManager(object):

    def __init__(self, default = 'development'):
        self._command = {}
        self._parsers = {}
        self._default = default

    def __call__(self):
        argument_config = {
		    'description' : 'Manager to control Pails application',
		    'epilog' : 'For more information visit url https://github.com/far-rel/Pails',
		}
        # general commands
        opt = ArgumentParser(**argument_config)
        opt.add_argument('--list','-l', action='store_const', const = 'list', help='list of available commands')

        subparsers = opt.add_subparsers(dest = 'sub_name', help='name of command to execute')
        for obj in self._command.values():
            obj.parser(subparsers)
        #parse parameters
        args = vars(opt.parse_args())
        command = args['sub_name']
        # execute command by name
        if command in self._command:
            comm = self._command[command](self._default,**args)
            comm()
        else:
            # if command not exist print help
            opt.print_help()

    def register(self, action, command_object):
        if action in self._command.keys():
            log.info('command %s has been overridden' % action)
        self._command[action] = command_object

    @property
    def available(self):
        return self._command.keys()


manager = PailsManager()
manager.register('run',Run)
manager.register('routes', Routes)
