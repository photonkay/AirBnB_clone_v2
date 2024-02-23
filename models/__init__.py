#!/usr/bin/python3
""" Module to handle storage for hbnb project """

from os import getenv

# Check the value of the environment variable HBNB_TYPE_STORAGE
HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')

if HBNB_TYPE_STORAGE == 'db':
    # If HBNB_TYPE_STORAGE is set to 'db', use DBStorage
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    # If HBNB_TYPE_STORAGE is not set or set to anything other than 'db', use FileStorage
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
