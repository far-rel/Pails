# -*- coding: UTF8 -*-
from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader

from tornado.web import RequestHandler

class BaseHandler(RequestHandler):

    def initialize(self, controller, methods, param_names, name, project_path):
        self.__controller = controller
        self.__methods = methods
        self.__param_names = param_names
        self.__name = name
        self.__env = Environment(loader = FileSystemLoader(project_path + '/app/views'))
    
    def get(self, *args):
        params = self.__parse_arguments(self.request.arguments, self.request.files)
        params.update(dict(zip(self.__param_names, args)))
        if params['format'] is None:
            params['format'] = 'html'
        controller = self.__controller()
        controller.set_parameters(params)
        controller.__getattribute__(self.__methods['GET'])()
        temp = self.__env.get_template(self.__name + '/' + self.__methods['GET'] + '.html')
        self.write(temp.render(controller.get_render_parameters()))

    def post(self, *args):
        params = dict(zip(self.__param_names, args))
        self.__controller().__getattribute__(self.__methods['PUT'])()

    def put(self, *args):
        params = dict(zip(self.__param_names, args))
        self.__controller().__getattribute__(self.__methods['PUT'])()

    def delete(self, *args):
        params = dict(zip(self.__param_names, args))
        self.__controller().__getattribute__(self.__methods['DELETE'])()

    def __parse_arguments(self, arguments, files):
        params = {}
        for name in arguments:
            self.__parse_argument(name, arguments[name], params)
        for name in files:
            self.__parse_argument(name, files[name], params)
        return params

    def __parse_argument(self, name, value, params):
        name_parts = []
        current_part = ""
        for letter in name:
            if letter == '[':
                name_parts.append(current_part)
                current_part = ''
            elif  letter == ']':
                pass
            else:
                current_part += letter
        name_parts.append(current_part)
        i = 0
        current_param = params
        for part in name_parts:
            if i == len(name_parts) - 1:
                current_param[part] = value
            else:
                if part not in current_param:
                    current_param[part] = {}
                current_param = current_param[part]
            i += 1