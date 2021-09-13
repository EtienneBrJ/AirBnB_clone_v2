#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
        list of State sorted by the name
"""
from models import storage
from models.state import State
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ Display a list of all State objects """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """ Close the current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
