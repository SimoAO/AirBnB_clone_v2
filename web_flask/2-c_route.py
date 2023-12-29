#!/usr/bin/python3
""" Starting Flask web application module """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Hello HBNB clss """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ HBNB class """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """ C <text> class """
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
