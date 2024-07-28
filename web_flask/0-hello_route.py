#!/usr/bin/python3
"""
A simple Flask application to serve the 'Hello HBNB!' message.
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Returns the 'Hello HBNB!' message.
    """
    return 'Hello HBNB!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
