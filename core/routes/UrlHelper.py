# -*- coding: UTF8 -*-

class UrlHelper(object):

    def __init__(self):
        self.__routes = {}

    def append(self, item):
        self.__routes[self.__url_to_name(item)] = self.__url_to_formatted_url(item)

    def __getattr__(self, item):
        print self.__routes
        base_url = self.__routes[item]
        def name_to_url(*args, **kwargs):
            url = base_url
            for arg in args:
                param = None
                try:
                    param = arg.parametrize()
                except AttributeError:
                    try:
                        param = arg.id
                    except AttributeError:
                        param = str(arg)
                url = url.replace(':param', param, 1)
            if 'format' in kwargs:
                url = url.replace(':format', '.' + kwargs['format'])
            else:
                url = url.replace(':format', '')
            return url
        return name_to_url

    def __url_to_formatted_url(self, url):
        return url.replace('[\D\d]*', ':param').replace('(.[a-z0-9]+)?', ':format')

    def __url_to_name(self, url):
        name = url[1:].replace('/', '_').replace('[\D\d]*', '').replace('(.[a-z0-9]+)?', '')
        new_name = name.replace('__', '_')
        while new_name != name:
            name = new_name
            new_name = name.replace('__', '_')
        name = new_name
        if name.endswith('_'):
            name = name[:-1]
        return name