#!/usr/bin/python3
"""script that Starts a flask web application"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def index():
    """displays hello HBNB"""
    return "Hello HBNB"


if __name__ == '__main__':
    app.run(debug=True)
