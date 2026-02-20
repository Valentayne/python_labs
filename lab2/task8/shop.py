class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = 0

    def describe_shop(self):
        print(f"Shop name: {self.shop_name}")
        print(f"Store type: {self.store_type}")

    def open_shop(self):
        print("The online shop is open!")

    def set_number_of_units(self, number):
        self.number_of_units = number

    def increment_number_of_units(self, increment):
        self.number_of_units += increment