#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""

from models.base_model import Base
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv

from file_storage import FileStorage

classes = {'User': User, 'Place': Place, 'Review': Review,
           'State': State, 'City': City}

storage = FileStorage()
storage.reload()
