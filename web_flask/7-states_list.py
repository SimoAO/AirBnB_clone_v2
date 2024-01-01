#!/usr/bin/python3
""" Starting Flask web application module """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ States list class """
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """ Remove SQLAlchemy class """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
