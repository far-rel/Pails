# -*- coding: UTF8 -*-

from Schema import Schema

class ProjectSchema(Schema):

    def __init__(self):
        self.file_schema = {
            '$name' : {
                'app' : {
                    'controllers' : {
                        '__init__.py' : 'empty'
                    },
                    'fixtures' : {
                    },
                    'models' : {
                        '__init__.py' : 'empty'
                    },
                    'tests' : {
                    },
                    'views' : {
                        'layouts' : {
                            'application.html' : 'layout'
                        }
                    },
                    'routing.py' : 'routing'
                },
                'commands' : {
                    '__init__.py' : 'empty'
                },
                'config' : {
                    'development.ini' : 'config',
                    'production.ini' : 'config'
                },
                'public' : {
                    'images' : {
                    },
                    'javascripts' : {
                    },
                    'stylesheets' : {
                    },
                    'manage.py' : 'manage'
                }
            }
        }
  