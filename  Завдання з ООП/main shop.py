from shop import Shop
from shop import Discount

store = Shop("Rozetka", "електроніка")

print(store.shop_name)
print(store.store_type)

store.describe_shop()
store.open_shop()

print()

store1 = Shop("Allo", "телефони")
store2 = Shop("Epicentr", "будматеріали")
store3 = Shop("Comfy", "побутова техніка")

store1.describe_shop()
print()
store2.describe_shop()
print()
store3.describe_shop()
print()

store = Shop("Rozetka", "електроніка")
print("Кількість видів товару:", store.number_of_units)

store.number_of_units = 500
print("Після зміни:", store.number_of_units)
print()

store.set_number_of_units(1000)
print("Після set_number_of_units:", store.number_of_units)

store.increment_number_of_units(50)
print("Після increment_number_of_units:", store.number_of_units)
print()

store_discount = Discount("SaleShop", "одяг")
store_discount.discount_products = ["куртка", "джинси", "кросівки"]
store_discount.get_discounts_products()
print()

all_store = Shop("AllStore", "все підряд")
all_store.describe_shop()