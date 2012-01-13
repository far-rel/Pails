# -*- coding: UTF8 -*-

class LayoutGenerator(object):

    def generate(self, name, *args):
        indent = "    "

        string = "<!DOCTYPE html>\n"
        string += "<html>\n"
        string += "{0:>s}<head>\n".format(indent)
        string += "{0:>s}<title>\n".format(indent*2)
        string += "{0:>s}{1:>s}\n".format(indent*3, name)
        string += "{0:>s}</title>\n".format(indent*2)
        string += "{0:>s}</head>\n".format(indent)
        string += "{0:>s}<body>\n".format(indent)
        string += "{0:>s}{{% block content %}}\n".format(indent*2)
        string += "{0:>s}{{% endblock %}}\n".format(indent*2)
        string += "{0:>s}</body>\n".format(indent)
        string += "</html>\n"
        return string
  