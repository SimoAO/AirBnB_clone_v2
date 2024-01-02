#!/usr/bin/python3
""" Starting Flask web application module """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """ States list class """
    states = storage.all(State)
    return render_template("9-states.html", states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
	""" Cities of a state list class """
	for state in storage.all(State).values():
		if state.id == id:
		    return render_template('9-states.html', states=states, id=id)
	return render_template('9-states.html')


@app.teardown_appcontext
def teardown(exc):
    """ Remove SQLAlchemy class """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
