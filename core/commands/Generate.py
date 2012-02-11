# -*- coding: UTF8 -*-

from Command import Command
from Pails.core.config.Settings import Settings
from Pails.generators.Schema import Schema

class Generate(Command):

    def __init__(self, config, **params):
        Command.__init__(self, config, **params)
        print params
        self._config = Settings(config)
        self.params = params

    def __call__(self):
        Schema('default', self.params['resource_type']).generate(
            self._config.project_path,
            self.params['resource_name'],
            *self.params['fields']
        )

    @staticmethod
    def parser(subparser):
        parser = subparser.add_parser('generate', help='Generates named resources')
        parser.add_argument('resource_type', help='Resource type to generate')
        parser.add_argument('resource_name', help='Resource name')
        parser.add_argument('fields', metavar='field', nargs='*', help='List of fields')
        return parser