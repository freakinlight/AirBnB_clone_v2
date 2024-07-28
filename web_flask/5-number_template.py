#!/usr/bin/python3
"""
A Flask web application that listens on 0.0.0.0, port 5000.
The application includes multiple routes
and displays an HTML page for integer inputs.
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Displays 'Hello HBNB!' """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Displays 'HBNB' """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ Displays 'C ' followed by the value of the text variable. """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """ Displays 'Python ' followed by the value of the text variabl. """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """ Displays 'n is a number' only if n is an integer. """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Display a HTML page only if n is an integer. """
    return render_template('5-number.html', number=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
