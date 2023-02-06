#!/usr/bin/python3
"""
starts a Flask web application on 0.0.0.0:5000
    Routes:
        /hbnb: displays HTML page: with list of State objects
"""

from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb')
def hbnb():
    """ Displays the main HBnB filters HTML page """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    return render_template('100-hbnb.html',
                           states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def teardown(exc):
    """ Removes the current SQLAlchemy session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
