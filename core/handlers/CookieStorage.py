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

    def remove(self, key, handler):
        handler.clear_cookie('_session_{0:>s}'.format(key))
        if key in self.new_values:
            del self.new_values[key]

    def remove_all(self, handler):
        for cookie in handler.request.cookies:
            if cookie.startwith('_session_'):
                handler.clear_cookie(cookie)