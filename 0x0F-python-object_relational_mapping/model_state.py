#!/usr/bin/python3
""" contains the class definition of a State and an instance Base """
from sqlalchemy import Column, String, Integer, MetaData
from sqlalchemy.ext.declarative import declarative_base

m_metadata = MetaData()
Base = declarative_base(metadata=m_metadata)


class State(Base):
    """ clase State an instance Base class
    Attributes:
        id(int): primary key
        name(str): name of state
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
