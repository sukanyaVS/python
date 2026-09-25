class Product:

    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_details(self):
        print("Product ID:", self.product_id)
        print("Name:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)




product1 = Product(101, "Laptop", 60000, 2)
product1.display_details()
product2 = Product(102, "Mouse", 500, 5)
product3 = Product(103, "Keyboard", 2500, 1)
product4 = Product(104, "Monitor", 15000, 2)

class ShoppingCart:

    def __init__(self):
        self.products = []

    def add_product(self, product):
       self.products.append(product)

    def total_value(self):
        total = 0

        for product in self.products:
            total += product.price * product.quantity

        return total    

    def display_cart(self):

        print("\n===== Shopping Cart =====")

        if not self.products:
            print("Cart is empty.")
            return

        for product in self.products:
            print(
                "ID:", product.product_id,
                "Name:", product.name,
                "Price:", product.price,
                "Quantity:", product.quantity
            )

        print("Total Value:", self.total_value())   

    def remove_product(self, product_id, quantity=1):

        for product in self.products:

            if product.product_id == product_id:

                if quantity >= product.quantity:
                    self.products.remove(product)
                else:
                    product.quantity -= quantity

                return

        print("Product not found.")    

    def __add__(self, other):

            new_cart = ShoppingCart()

            for product in self.products:
                new_cart.add_product(product)

            for product in other.products:
                new_cart.add_product(product)

            return new_cart    

    def __sub__(self, product_id):

        self.remove_product(product_id)

        return self        

    def __len__(self):

        total_quantity = 0

        for product in self.products:
            total_quantity += product.quantity

        return total_quantity  

    def __gt__(self, other):

        return self.total_value() > other.total_value()    


cart1 = ShoppingCart()
cart1.add_product(product1)
cart1.display_cart()
cart1.remove_product(101, 2)

cart2 = ShoppingCart()
cart2.add_product(product2)     
cart2.display_cart()

print("\n===== Merged Cart =====")
cart3 = cart1 + cart2
cart3.display_cart()

cart1 = cart1 - 101
cart1.display_cart()
print("Total products in Cart 1:", len(cart1))


if cart1 > cart2:
    print("Cart 1 has greater total value.")
else:
    print("Cart 2 has greater or equal total value.")

