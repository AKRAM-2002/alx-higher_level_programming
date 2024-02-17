#!/usr/bin/python3
"""Model City 
"""
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class City(Base):
    """City class that represents the cities table in the database."""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))