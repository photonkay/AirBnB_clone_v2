#!/usr/bin/python3
"""starts a Flask web application that listens on 0.0.0.0, port 5000"""

from models import storage
from models.state import State
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """displays a HTML page: (inside the <body> tag)
       -> h1: "States"
       -> ul: list of all 'State' objects present in 'DBStorage'
              sorted by name (A-Z)
            -> li: description of one 'State':
                   "<state.id>: <b><state.name><b>"
                -> ul: list of 'City' objects linked to the 'State'
                       sorted by name (A->Z)
                    -> li: description of one 'City':
                           "<city.id>: <b><city.name></b>"
    """
    states = storage.all(State)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """removes the current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
