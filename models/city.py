#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel


class City(BaseModel,Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'City'
    
    state_id = Column(String(128))
    name = Column(String(60))
