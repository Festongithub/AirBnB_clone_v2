#!/usr/bin/python3
"""script that Starts a flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    displays hello HBNB
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    returns the HNBNB
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_cool(text):
    """
    Displays  c
    """
    return "C " + text.replace('_', ' ')


@app.route('/python/<text>', defaults={'text': 'is cool'},
           strict_slashes=False)
def magic_python(text):
    """
    Displays magicity of python
    """
    return "Python " + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
