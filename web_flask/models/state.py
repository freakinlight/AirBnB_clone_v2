from models import storage
from sqlalchemy import Column, String
from models.base_model import BaseModel
from models.city import City


class State(BaseModel):
    """State class represents state details in the HBNB project,
    linking cities to states."""
    name = Column(String(128), nullable=False)

    @property
    def cities(self):
        """Returns a list of City instances with state_id equal to the current
        State.id.
        """
        city_list = []
        all_cities = storage.all(City)
        for city in all_cities.values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
