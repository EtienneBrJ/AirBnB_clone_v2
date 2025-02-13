#!/usr/bin/python3
""" starts a Flask web application:
    display Hello HBNB on 0.0.0.0:5000
    display HBNB on 0.0.0.0:5000/hbnb
    display C <text> on 0.0.0.0:5000/C/<text>
    display Python <text> on 0.0.0.0:5000/Python/<text>
        with a default text: is cool
    display n on 0.0.0.0:5000/<n>

"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Display Hello HBNB """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Display Hello HBNB """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    """ Display Hello HBNB """
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pyiscool(text="is cool"):
    """ Display Hello HBNB """
    return "C {}".format(text.replace("_", " "))


@app.route("/number/<int:intoprint>", strict_slashes=False)
def number(intoprint):
    """ Display Hello HBNB """
    return '{} is a number'.format(intoprint)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
