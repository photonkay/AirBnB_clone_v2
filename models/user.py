#!/usr/bin/python3
"""This module defines a class User"""

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from models.base_model import BaseModel

Base = declarative_base()

class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", cascade="all,delete", backref="user")
    reviews = relationship("Review", cascade="all,delete", backref="user")
