#!/usr/bin/python3
"""
starts a Flask web application on 0.0.0.0:5000
    Routes:
        /states_list: displays HTML page: with list of State objects
"""

from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exc):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
