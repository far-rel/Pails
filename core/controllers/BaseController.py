# -*- coding: UTF8 -*-

class BaseController(object):

    def set_parameters(self, params):
        self._params = params

    def _set_render_parameters(self, params):
        self._render_parameters = params

    def get_render_parameters(self):
        try:
            return self._render_parameters
        except AttributeError:
            return {}