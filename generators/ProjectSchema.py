# -*- coding: UTF8 -*-

class ProjectSchema(object):

    def __init__(self):
        self.file_schema = {
            '{0:>s}' : {
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
                'libs' : {

                },
                'public' : {
                    'images' : {
                    },
                    'javascripts' : {
                    },
                    'stylesheets' : {
                    },
                },
                'manage.py' : 'manage'
            }
        }
  