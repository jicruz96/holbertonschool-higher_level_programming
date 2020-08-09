#!/usr/bin/python3
""" defines State class for MySQLdb integration """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ 
    Representation of states table

    Args:
        * id (int): represents id column
        * name (str): represents name column
    """

    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    def __init__(self, name, id=None):
        self.id = id
        self.name = name
