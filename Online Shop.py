class Product:
    def __init__(self, name, description, price, online_shop):
        self.name = name
        self.description = description
        self.price = price
        self.online_shop = online_shop 


class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.cart = []        
        self.past_orders = [] 


class OnlineShop:
    def __init__(self):
        self.name = "Narak Shop"
        self.url = "www.Narak Shop.com"
        self.products = []  

    def addingItemsToCart(self, customer, product, quantity):
        customer.cart.append({
            "product": product,
            "quantity": quantity
        })
        print(f"เพิ่ม {product.name} x{quantity} ลงตะกร้าของ {customer.name} แล้ว")

    def checkout(self, customer):
        if not customer.cart:
            print("ตะกร้าว่าง ไม่สามารถชำระเงินได้")
            return

        order_id = len(customer.past_orders) + 1
        order = {
            "order_id": order_id,
            "items": customer.cart.copy()
        }
        customer.past_orders.append(order)
        customer.cart.clear()
        print(f"{customer.name} ชำระเงินเรียบร้อย (Order ID: {order_id})")

    def orderTracking(self, customer, order_id):
        for order in customer.past_orders:
            if order["order_id"] == order_id:
                print(f"พบคำสั่งซื้อ {order_id} ของ {customer.name}:")
                for item in order["items"]:
                    print(f"- {item['product'].name} x{item['quantity']}")
                return
        print("ไม่พบคำสั่งซื้อ")

shop = OnlineShop()

p1 = Product("โฟมล้างหน้า", "เซนกะ เพอร์เฟ็ควิป แอคเน่โฟม ", 199, shop)
p2 = Product("ทิชชู่", "ทิชชู่กระดาษนุ่ม", 79, shop)

shop.products.extend([p1, p2])

c1 = Customer("Narak", "NarakShop@example.com", "Bangkok")

shop.addingItemsToCart(c1, p1, 2)
shop.addingItemsToCart(c1, p2, 1)

shop.checkout(c1)

shop.orderTracking(c1, 1)