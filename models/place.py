#!/usr/bin/python3
""" Place Module for HBNB project """

import models
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv

# Define association table for many-to-many relationship between Place and Amenity
place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60), ForeignKey("places.id"), primary_key=True, nullable=False),
                      Column("amenity_id", String(60), ForeignKey("amenities.id"), primary_key=True, nullable=False))

class Place(BaseModel, Base):
    """A place to stay"""

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", cascade="all,delete", backref="place")
    amenities = relationship("Amenity", secondary=place_amenity, viewonly=False)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            """Returns the list of Reviews associated with the Place"""
            return [review for review in models.storage.all(Review).values() if review.place_id == self.id]

        @property
        def amenities(self):
            """Returns the list of Amenities associated with the Place"""
            return [amenity for amenity in models.storage.all(Amenity).values() if amenity.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, value):
            """Sets the Amenities of the Place"""
            if isinstance(value, Amenity):
                self.amenity_ids.append(value.id)
