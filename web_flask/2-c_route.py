#!/usr/bin/python3
""" starts a Flask web application:
    display Hello HBNB on 0.0.0.0:5000
    display HBNB on 0.0.0.0:5000/hbnb
    display C <text> on 0.0.0.0:5000/C/<text>
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ """
    return "HBNB"


@app.route("/C/<text>", strict_slashes=False)
def cisfun(text):
    """ """
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
