#!/usr/bin/python3
"""
A Python script that defines a State class using SQLAlchemy.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """A representation of state class that inherits from Base"""
    __tablename__ = 'states'
    id = Column(
            Integer,
            primary_key=True,
            unique=True,
            autoincrement=True,
            nullable=False)
    name = Column(String(128), nullable=False)
