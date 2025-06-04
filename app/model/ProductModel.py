class Product:
    def __init__(self, id=None, name=None, price=0.0):
        self.id = id
        self.name = name
        self.price = price

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_price(self, price):
        self.price = price
