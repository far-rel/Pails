# -*- coding: UTF8 -*-

class UrlHelper(object):

    def __init__(self):
        self.__routes = {}

    def append(self, name, url):
        self.__routes[name] = self.__url_to_formatted_url(url)

    def __getattr__(self, item):
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

    