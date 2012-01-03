# -*- coding: UTF8 -*-

from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import create_session

engine = create_engine('')
Base = declarative_base(bind=engine)
session = create_session()

class Model(Base):

    def save(self):
        if self.valid():
            session.add(self)
            session.commit()
            return True
        else:
            return False

    def update_attributes(self, **kwargs):
        if self.valid():
            session.add(self)
            session.commit()
            return True
        else:
            return False

    def valid(self):
        try:
            self.__validators
        except AttributeError:
            self.__validators = []
        valid_flag = True
        for validator in self.__validators:
            pass
        return valid_flag

  