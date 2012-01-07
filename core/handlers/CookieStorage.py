# -*- coding: UTF8 -*-

class CookieStorage(object):

    def __init__(self):
        pass

    def get(self, key, handler):
        return handler.get_secure_cookie('_session_{0:>s}'.format(key))

    def store(self, key, value, handler):
        handler.set_secure_cookie('_session_{0:>s}'.format(key), str(value))