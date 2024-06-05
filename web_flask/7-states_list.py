#!/usr/bin/python3

"""
imports list of states
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def db_teardown(exception=None):
    """
    SQL alchemy session teardonw
    """
    if storage is not None:
        storage.close()


@app.route('/states_list')
def list_states(n=None):
    """
    display list in HTML format
    """
    states = storag.all('State')
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(debug=True)
