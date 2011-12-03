# -*- coding:utf-8 -*-

from ConfigParser import ConfigParser
from ConfigParser import NoOptionError, NoSectionError

class SettingsParser(object):

    def __init__(self, project_path, file_path):
        # at this moment just parse global section
        self.project_path = project_path
        self._config = ConfigParser()
        try:
            # try open file and read config object
            with file(file_path) as f:
                self._config.readfp(f)
        except IOError:
            raise IOError("No config file found in '%s'" % file_path)
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