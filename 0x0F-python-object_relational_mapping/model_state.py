#!/usr/bin/python3
""" Creating the class definition of a state """

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()


class State(Base):
    """Creating state class inherintace of Base"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                nullable=False)
    name = Column(String(128), nullable=False)
