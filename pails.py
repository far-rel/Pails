#!/usr/bin/env python
# -*- coding: UTF8 -*-

import os, sys
from generators.Schema import Schema

if __name__ == '__main__':
    cwd = os.getcwd()
    if len(sys.argv) > 1:
        project_name = sys.argv[1]
        if not os.path.exists(os.path.join(cwd, project_name)):
            Schema('default', 'project').generate(cwd, project_name)
        else:
            print "Couldn't initialize new project. Directory taken"
    else:
        print "Project name not specified"