# -*- coding:utf-8 -*-
import logging
import argparse
from argparse import ArgumentParser
from core.commands import Run

log = logging.getLogger(__name__)

class PailsManager(object):
	
    def __init__(self):
        self._command = {}
	
    def __call__(self):
        argument_config = {
		    'description' : 'Manager to controll Pails application',
		    'epilog' : 'For more information visit url https://github.com/far-rel/Pails',
		}
        # general commands
        opt = ArgumentParser(**argument_config)
        opt.add_argument('--list','-l', action='store_const', const = 'list', help='list of available commands')

        subparsers = opt.add_subparsers(help='name of command to execute')
        run_parser = subparsers.add_parser('run [production,develop,custom]', help='run server')
        start_parser = subparsers.add_parser('start', help = 'run server')

        #parse parameters
        args = vars(opt.parse_args())
        # execute command by name
        command = args['command']
        if command in self._command:
            comm = self._command[command](**args)
            comm()
        else:
            # if command not exist print help
            opt.print_help()
		
    def register(self, action, command_object):
        if action in self._command.keys():
            log.info('command %s has been ovveriden' % action)
        self._command[action] = command_object
		
    @property
    def avaible(self):
        return self._command.keys()


manager = PailsManager()
manager.register('run',Run)
manager.register('start',Run)
