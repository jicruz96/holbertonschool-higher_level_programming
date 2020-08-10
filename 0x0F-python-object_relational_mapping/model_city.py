#!/usr/bin/python3
""" defines City class for MySQLdb integration """

from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey
from model_state import Base


class City(Base):
    """
    Representation of cities table

    Args:
        * id (int): represents id column
        * name (str): represents name column
    """

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))

    def __init__(self, name, id=None):
        self.id = id
        self.name = name
