# -*- coding: UTF8 -*-

class CookieSet(object):

    def __init__(self, handler):
        self.__handler = handler

    def __getitem__(self, item):
        return self.__handler.get_secure_cookie(item)

    def __setitem__(self, key, value):
        self.__handler.set_secure_cookie(key, value)

    def __delitem__(self, key):
        self.__handler.clear_cookie(key)
