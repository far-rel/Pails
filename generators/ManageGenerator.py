# -*- coding: UTF8 -*-

class ManageGenerator(object):

    def generate(self, name, *args):
        indent = "    "
        string = "#!/usr/bin/env python\n"
        string += "# -*- coding:utf-8 -*-\n\n"
        string += "''' example manage.py in project environment '''\n\n"
        string += "from Pails.manager import manager\n\n"
        string += "if __name__ == \"__main__\":\n"
        string += "{0:>s}manager()".format(indent)
        return string
  