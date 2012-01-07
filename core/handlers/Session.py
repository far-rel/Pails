# -*- coding: UTF8 -*-

from CookieStorage import CookieStorage

class Session(object):

    storages = {}

    @staticmethod
    def register(name, cls):
        Session.storages[name] = cls

    def __init__(self, handler, storage_name = 'cookie'):
        self.__handler = handler
        self.__storage = Session.storages[storage_name]()

    def __getitem__(self, item):
        return self.__storage.get(item, self.__handler)

    def __setitem__(self, key, value):
        self.__storage.store(key, value, self.__handler)

Session.register('cookie', CookieStorage)