#!/usr/bin/python3
""" Starting Flask web application module """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
	""" HBnB filters class """
	states = storage.all(State)
	amenities = storage.all(Amenity)
	return render_template("10-hbnb_filters.html",
            states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
    """ Remove SQLAlchemy class """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
