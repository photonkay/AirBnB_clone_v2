#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""

from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


classes = {'User': User, 'Place': Place, 'Review': Review,
           'State': State, 'City': City}


class DBStorage:
    def __init__(self):
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        self.reload()
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine, checkfirst=True)

    def all(self, cls=None):
        objects = {}
        for cls_name, cls in classes.items():
            if cls is None or cls_name == cls.__name__:
                query = self.__session.query(cls)
                for obj in query.all():
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    objects[key] = obj
        return objects

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        self.__session.close()
