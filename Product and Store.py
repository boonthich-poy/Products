class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class Store:
    def __init__(self):
        self.products = []

    def add_product(self, name, quantity):
        product = Product(name, quantity)
        self.products.append(product)

    def show_products(self):
        for p in self.products:
            print(f"สินค้า: {p.name}, จำนวน: {p.quantity}")

my_store = Store()
my_store.add_product("โฟมล้างหน้า", 30)
my_store.add_product("ทิชชู่", 15)
my_store.show_products()