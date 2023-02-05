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

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes=False


@app.royte
