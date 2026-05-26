class Shop():

    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = 0

    def describe_shop(self):
        print("Назва: " + self.shop_name)
        print("Тип: " + self.store_type)

    def open_shop(self):
        print(self.shop_name + " - онлайн-магазин відкритий!")

    def set_number_of_units(self, number):
        self.number_of_units = number

    def increment_number_of_units(self, amount):
        self.number_of_units = self.number_of_units + amount

class Discount(Shop):

    def __init__(self, shop_name, store_type):
        super().__init__(shop_name, store_type)
        self.discount_products = []

    def get_discounts_products(self):
        print("Товари зі знижкою:")
        for product in self.discount_products:
            print("- " + product)