#!/usr/bin/env python
# -*- coding: UTF8 -*-

import os, sys

if __name__ == '__main__':
    cwd = os.getcwd()
    project_name = sys.argv[1]
    try:
        os.mkdir(os.path.join(cwd, project_name))
    except OSError:
        print "Couldn't initialize new project. Directory taken"