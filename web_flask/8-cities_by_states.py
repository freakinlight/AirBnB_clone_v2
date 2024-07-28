from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ Displays states and their cities from the database. """
    states = storage.all("State").values()
    # Ensure states are sorted and cities are accessed depending on the storage type.
    for state in states:
        state.cities = sorted(state.cities, key=lambda x: x.name) if hasattr(state, 'cities') else sorted([city for city in storage.all("City").values() if city.state_id == state.id], key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=sorted(states, key=lambda x: x.name))

@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown."""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
