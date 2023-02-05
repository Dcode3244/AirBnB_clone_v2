#!/usr/bin/python3
""" starts a Flask web application on 0.0.0.0:5000
    Routes:
        /: displays 'Hello HBNB!'
        /hbnb: displays 'HBNB'
        /c/<text>: displays "C", followed by the value of text variable
        /python/<text>: displays "Python followed by the value of text
        /number/<n>: displays "n is a number" only is n is an integer
"""

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    return "HBNB"


@app.route('/c/<text>')
def c(text):
    return "C %s" % text.replace("_", " ")


@app.route('/python')
@app.route('/python/<text>')
def python(text="is cool"):
    return "Python %s" % text.replace("_", " ")


@app.route('/number/<int:n>')
def number(n):
    return "%d is a number" % n


@app.route('/number_template/<int:n>')
def number_template(n):
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
