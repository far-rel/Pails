# -*- coding: UTF8 -*-
from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader

from tornado.web import RequestHandler

class BaseHandler(RequestHandler):

    def initialize(self, controller, methods, param_names, name, project_path, url_helper):
        self.__controller = controller
        self.__methods = methods
        self.__param_names = param_names
        self.__name = name
        self.__env = Environment(loader = FileSystemLoader(project_path + '/app/views'))
        self.__url_helper = url_helper
    
    def get(self, *args):
        self.process_request('GET', args)

    def post(self, *args):
        self.process_request('POST', args)

    def put(self, *args):
        self.process_request('PUT', args)

    def delete(self, *args):
        self.process_request('DELETE', args)

    def process_request(self, method, args):
        params = self.__parse_arguments(self.request.arguments, self.request.files)
        params.update(dict(zip(self.__param_names, args)))
        if params['format'] is None:
            params['format'] = 'html'
        controller = self.__controller()
        controller.set_parameters(params)
        controller.set_path(self.__url_helper)
        controller.__getattribute__(self.__methods[method])()
        redirect_address = controller.get_redirect()
        if not redirect_address is None:
            self.redirect(redirect_address)
        else:
            view = controller.get_view()
            render_params = controller.get_render_parameters()
            render_params.update({ 'path' : self.__url_helper })
            if view is None:
                view = self.__name + '/' + self.__methods[method]
            elif view.find('/') == -1:
                view = self.__name + '/' + view
            temp = self.__env.get_template(view + '.' + params['format'])
            self.write(temp.render(render_params))
        
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