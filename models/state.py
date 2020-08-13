#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relatioship('City', backref='state', cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """ Getter returns the list of City instances
            with state_id equals to the current State.id
            """
            return [city for city in models.storage.all(City)
                    .values() if city.state_id == self.id]