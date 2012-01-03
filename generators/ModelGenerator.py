# -*- coding: UTF8 -*-

from Pails.utils.NameUtils import name_to_class, name_to_table_name, pluralize

class ModelGenerator(object):

    def generate(self, name, args):
        indent = '    '
        string = '# -*- coding: UTF8 -*-\n\n'
        string += 'from Pails.core.model import Model\n'
        string += 'from sqlalchemy import Column, SmallInteger, Integer, BigInteger, String, Unicode, Text, UnicodeText,'
        string += ' Date, DateTime, Time, Float\n\n'
        string += 'class {0:>s}(Model):\n'.format(name_to_class(name))
        string += '{0:>s}__tablename__="{1:>s}"\n'.format(indent, name_to_table_name(name))
        string += '{0:>s}id = Column(Integer, primary_key = True)\n'.format(indent)
        for arg in args:
            arg_splited = arg.split(':')
            column = arg_splited[0]
            column_type = arg_splited[1]
            string += '{0:>s}{1:>s} = Column({2:>s})\n'.format(indent, column, column_type)
        return string


  