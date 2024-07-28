def close(self):
    """Closes the current SQLAlchemy session."""
    self.__session.remove()
