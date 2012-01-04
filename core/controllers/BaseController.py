# -*- coding: UTF8 -*-

class BaseController(object):

    def __init__(self):
        self._params = {}
        self.__render_called = False
        self.__redirect_called = False
        self._render_parameters = {}
        self._view = None
        self._redirect_address = None

    def render(self, params = {}, view = None):
        if not (self.__render_called or self.__redirect_called):
            self.__render_called = True
            self._render_parameters = params
            self._view = view
        else:
            raise Exception('render or redirect called more than once')

    def redirect(self, address):
        if not (self.__render_called or self.__redirect_called):
            self.__redirect_called = True
            self._redirect_address = address
        else:
            raise Exception('render or redirect called more than once')

    def set_path(self, url_helper):
        self.path = url_helper

    def set_parameters(self, params):
        self._params = params

    def get_render_parameters(self):
        return self._render_parameters

    def get_redirect(self):
        return self._redirect_address

    def get_view(self):
        return self._view
