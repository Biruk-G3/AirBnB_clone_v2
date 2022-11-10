#!/usr/bin/python3
"""Starts Flask web app
Listening on 0.0.0.0:5000
Route '/' displays "Hello HBNB!"
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """prints HBNB"""
    return "HBNB"

@app.route('/c/<string:text>', strict_slash=False)
def c_text(text):
    """prints C followed by <text> content"""
    text = text.replace("_", " ")
    return "C %s" % text

@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_text(text="is cool"):
    """prints Python is cool"""
    text = text.replace("_", " ")
    return "Python %s" % text

@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """display n if integer"""
    return "%i is a number" %

if __name__ == "__main__":
    app.run(host="0.0.0.0")
