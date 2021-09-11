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
from flask.templating import render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    """ """
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pyiscool(text="is cool"):
    """ """
    return "C {}".format(text.replace("_", " "))


@app.route("/number/<int:intoprint>", strict_slashes=False)
def number(intoprint):
    """ """
    return '{} is a number'.format(intoprint)


@app.route('/number_template/<int:number>', strict_slashes=False)
def display_template(number):
    """ """
    if number:
        return render_template('5-number.html', number=number)


@app.route('/number_odd_or_even/<int:number>', strict_slashes=False)
def display_odd_or_even(number):
    """ """
    if number:
        return render_template('6-number_odd_or_even.html', number=number)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
