#!/usr/bin/python3
"""Start link class to table in database 
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class State(Base):
    """State class that represents the states table in the database."""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)