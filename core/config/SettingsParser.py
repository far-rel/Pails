# -*- coding:utf-8 -*-

from ConfigParser import ConfigParser
from ConfigParser import NoOptionError, NoSectionError
import sys, os

class SettingsParser(object):

    def __init__(self,default):
        # at this moment just parse global section
        self._config = ConfigParser()
        self._load_avaible_config()
        self.reload_config(default)

    def _load_avaible_config(self):
        # http://docs.python.org/library/sys.html#sys.path
        # As initialized upon program startup, the first item of this list, path[0],
        # is the directory containing the script that was used to invoke the Python interpreter.
        self.project_path = sys.path[0]
        config_path = os.path.join(self.project_path,'config')
        # find all config files
        config_filter = lambda x: (x.endswith('.ini') or x.endswith('.cfg')) and True or False
        self._available_config = filter(config_filter,os.listdir(config_path))


    def _load_file(self, default):
        config_file = None
        try:
            # find default config file
            config_file = filter(lambda x: x.startswith(default) and True or False, self._available_config)[0]
        except IndexError:
            raise ValueError('File %(name)s.ini or %(name)s.cfg not found in your config directory' % {'name' : default})
        config_file = os.path.join(self.project_path,'config',config_file)
        try:
            # try open file and read config object
            with file(config_file) as f:
                self._config.readfp(f)
        except IOError:
            raise IOError("No config file found in '%s'" % config_file)

    def _load_all(self):
        self._default_load()

    def _default_load(self):
        '''
            Load information from global section in config file
            Section global is required
        '''
        try:
            for (option,value) in self._config.items('global'):
                self.__setattr__(option,eval(value))
        except NoSectionError:
            raise NoSectionError('Section global is required in config file')

    def reload_config(self, default):
        self._load_file(default)
        self._load_all()
