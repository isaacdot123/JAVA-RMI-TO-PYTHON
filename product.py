import Pyro5.api

@Pyro5.api.expose
class Product:
    """A remote Product. Public methods below can be invoked by clients."""

    def __init__(self, name, description, price):
        # Attributes (ProductImpl's fields). Underscore-prefixed so they are
        # NOT exposed remotely; clients must use the getters below.
        self._name = name
        self._description = description
        self._price = price

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description

    def get_price(self):
        return self._price