# -*- coding: UTF8 -*-

import inflect

def name_to_class(name):
    return name

def name_to_table_name(name):
    return name

def pluralize(name):
    p = inflect.engine()
    return p.plural(name)
