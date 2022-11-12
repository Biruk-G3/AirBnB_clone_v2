#!/usr/bin/python3
""" State Module for HBNB project for AirBNB_clone_v2"""


from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.engine.file_storage import FileStorage
from os import getenv


class State(BaseModel, Base):
    """ State class definition in the next line"""
    __tablename__ = 'states'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade="all, delete")
    else:
        name = ''


    @property
    def cities(self):
        '''returns the list of City instances with state_id
                equals the current State.id
                FileStorage relationship between State and City
        '''
        from models import storage
        related_cities = []
        cities = storage.all(City)
        for city in cities.values():
            if city.state_id == self.id:
                related_cities.append(city)
        return related_cities
