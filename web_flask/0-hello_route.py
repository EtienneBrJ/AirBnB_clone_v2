#!/usr/bin/python3
""" starts a Flask web application:
    display Hello HBNB on 0.0.0.0:5000
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Hello at route /"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
