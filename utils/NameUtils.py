# -*- coding: UTF8 -*-

import inflect
import re

def name_to_class(name):
    name_splited = convert(name).split('_')
    new_name = ''
    for part in name_splited:
        new_name += part.capitalize()
    return new_name

def convert(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def name_to_table_name(name):
    return pluralize(convert(name))

def pluralize(name):
    p = inflect.engine()
    return p.plural(name)
