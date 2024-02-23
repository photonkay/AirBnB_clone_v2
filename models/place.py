#!/usr/bin/python3
""" Place Module for HBNB project """

import models
from models.base_model import BaseModel
from models.base_model import Base
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Column, String, Integer, Float, Table
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", cascade="all,delete", backref="place")
    amenities = relationship("Amenity", secondary="place_amenity")

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            """returns the list of Reviews"""
            reviews = []
            all_reviews = models.storage.all(Review)
            for review in all_reviews.values():
                if self.id == review.place_id:
                    reviews.append(review)
            return reviews

        @property
        def amenities(self):
            """ndeaa"""
            amenity_list = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            """ndeaa"""
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
