#!/usr/bin/python3
"""improve the file model_state.py and save as relationship_state.py"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()
"""instances"""


class State(Base):
    """the class"""
    __tablename__ = 'state'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")
