from lab2.task8.shop import Shop


class Discount(Shop):
    def __init__(self, shop_name, store_type, discount_products):
        super().__init__(shop_name, store_type)
        self.discount_products = discount_products

    def get_discount_products(self):
        print("Discount products:")
        for product in self.discount_products:
            print(f"- {product}")