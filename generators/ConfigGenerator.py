# -*- coding: UTF8 -*-

from hashlib import md5
import time

class ConfigGenerator(object):

    def generate(self, name, *args):
        string = "[global]\n\n"
        string += "admin_email = \"login@example.net\"\n"
        string += "host = \"example.net\"\n"
        string += "port = 8080\n"
        string += "session_storage = \"cookie\"\n"
        string += "cookie_secret = \"{0:>s}\"\n".format(md5(str(time.time())))
        string += "serve_static = True\n"
        return string
  