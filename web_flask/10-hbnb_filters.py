#!/usr/bin/python3
"""
starts a Flask web application on 0.0.0.0:5000
    Routes:
        /hbnb_filters: displays HBnB HTML page
"""

from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def hbnb_filters():
    """ Displays the main HBnB filters HTML page """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
    """ Removes the current SQLAlchemy session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
