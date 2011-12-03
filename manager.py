# -*- coding:utf-8 -*-
import logging
import argparse
from argparse import ArgumentParser
from core.commands import Run
from core.commands import Routes
from core.config import SettingsParser
import os, sys

log = logging.getLogger(__name__)

class PailsManager(object):

    def __init__(self, default = 'development'):
        self._command = {}
        self._parsers = {}
        # http://docs.python.org/library/sys.html#sys.path
        # As initialized upon program startup, the first item of this list, path[0],
        # is the directory containing the script that was used to invoke the Python interpreter.
        self._project_path = sys.path[0]
        config_path = os.path.join(self._project_path,'config')
        # find all config files
        config_filter = lambda x: (x.endswith('.ini') or x.endswith('.cfg')) and True or False
        self._available_config = filter(config_filter,os.listdir(config_path))
        self._config_file = None
        try:
            # find default config file
            self._config_file = filter(lambda x: x.startswith(default) and True or False, self._available_config)[0]
        except IndexError:
            raise ValueError('File %(name)s.ini or %(name)s.cfg not found in your config directory' % {'name' : default})
        # loading config object from file
        self.settings = SettingsParser(self._project_path,os.path.join(config_path,self._config_file))


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
            comm = self._command[command](self.settings,**args)
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
manager.register('start',Run)
manager.register('routes', Routes)
