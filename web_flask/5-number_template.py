#!/usr/bin/python3
"""script that Starts a flask web application"""

from flask import Flask, render_template

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


@app.route('/python/', defaults={'text': 'is cool'},
           strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def magic_python(text):
    """
    Displays magicity of python
    """
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Displays n as an integer
    """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Renders  a html template
    """
    return render_template('5-number.html', num=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
