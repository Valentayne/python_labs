class Shop:
    def __init__(self, shop_name, store_type, number_of_units=0):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = number_of_units

    def describe_shop(self):
        return f"Shop: {self.shop_name}, Type: {self.store_type}"

    def open_shop(self):
        return f"The online shop '{self.shop_name}' is open!"

    def set_number_of_units(self, number):
        self.number_of_units = number

    def increment_number_of_units(self, amount):
        self.number_of_units += amount
