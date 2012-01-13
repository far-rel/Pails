# -*- coding: utf-8 -*-

from SettingsParser import SettingsParser

class Settings(object):
    __obj = None

    def __init__(self, default = 'development'):
        if Settings.__obj is None:
            Settings.__obj = SettingsParser(default)

        self.__dict__['_Settings__obj'] = Settings.__obj

    def __getattr__(self, attr):
        return getattr(self.__obj, attr)

    def __setattr__(self, attr, value):
        return setattr(self.__obj, attr, value)