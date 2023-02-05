#!/usr/bin/python3
"""
starts a Flask web application on 0.0.0.0:5000
	Routes:
		/states_list: displays HTML page:(inside the tag BODY)
			- H1 tag: "States"
			- UL tag: with the list of all State objects present in
					DBStorage sorted by name(A->Z)
				- LI tag: description of one
						State: <state.id>: <B><state.name></B>
"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes=False


@app.route('/states_list')
def states_list():
	states = storage.all("State")
	return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exc):
	storage.close()


if __name__ == "__main__":
	app.run(host="0.0.0.0")
