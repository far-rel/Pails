# -*- coding: UTF8 -*-

class CookieStorage(object):

    def __init__(self):
        self.new_values = {}

    def get(self, key, handler):
        if key in self.new_values:
            return self.new_values[key]
        else:
            return handler.get_secure_cookie('_session_{0:>s}'.format(key))

    def store(self, key, value, handler):
        handler.set_secure_cookie('_session_{0:>s}'.format(key), str(value))
        self.new_values[key] = value