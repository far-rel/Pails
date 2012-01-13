# -*- coding: UTF8 -*-

class RoutingGenerator(object):

    def generate(self, name, *args):
        string = "# -*- coding: UTF8 -*-\n\n"
        string += "from Pails.core.routes import Route\n\n"
        string += "r = Route()"
        return string
  