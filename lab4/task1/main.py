from lab4.task1.shop import Shop
from lab4.task1.discount import Discount

store = Shop("TechWorld", "Electronics")
print(store.shop_name)
print(store.store_type)
print(store.describe_shop())
print(store.open_shop())

store1 = Shop("FashionHub", "Clothing")
store2 = Shop("BookCorner", "Books")
store3 = Shop("GadgetZone", "Gadgets")
for s in [store1, store2, store3]:
    print(s.describe_shop())

store = Shop("TechWorld", "Electronics")
print(store.number_of_units)
store.number_of_units = 50
print(store.number_of_units)

store.set_number_of_units(100)
print(store.number_of_units)
store.increment_number_of_units(25)
print(store.number_of_units)

store_discount = Discount("SaleShop", "Mixed", discount_products=["Laptop", "Phone", "Tablet"])
print(store_discount.get_discounts_products())

all_store = Shop("AllStore", "General")
print(all_store.open_shop())