#!/usr/bin/python3
""" Starting Flask web application module """
from flask import Flask, render_template

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


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """ Python <text> class """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ n is a number class """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ number template class """
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """ number odd or even class """
    if n % 2 == 0:
        evod = "even"
    else:
        evod = "odd"
    return render_template("6-number_odd_or_even.html",
            number=n, parity=evod)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
