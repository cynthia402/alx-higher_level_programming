#!/usr/bin/python3
''' create state class that inherits methods form sqlalchamey'''

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
maindata = MetaData()
Base = declarative_base(metadata=maindata)


class State(Base):
    """ class represent State and inherit Base """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
