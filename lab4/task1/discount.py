from lab2.task8.shop import Shop


class Discount(Shop):
    def __init__(self, shop_name, store_type, number_of_units=0, discount_products=None):
        super().__init__(shop_name, store_type, number_of_units)
        self.discount_products = discount_products if discount_products is not None else []

    def get_discounts_products(self):
        return self.discount_products