#!/usr/bin/python3
"""starts a Flask web application that listens on 0.0.0.0, port 5000"""

from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """displays a HTML page like '6-index.html' from static"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
    """removes the current SQLAlchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
