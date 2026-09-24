# Create a shopping cart using a list of dictionaries:
# cart = [
#     {"name": "Laptop", "price": 60000, "quantity": 1},
#     {"name": "Mouse", "price": 1000, "quantity": 2},
#     {"name": "Keyboard", "price": 2500, "quantity": 1}
# ]
# Implement functions to:
# add_product()
# remove_product()
# update_quantity()
# calculate_subtotal()
# calculate_discount()
# calculate_final_amount()
# display_cart()

cart = [
    {"name": "Laptop", "price": 60000, "quantity": 1},
    {"name": "Mouse", "price": 1000, "quantity": 2},
    {"name": "Keyboard", "price": 2500, "quantity": 1}
]

def add_product(name, price, quantity):
    for product in cart:
        if product["name"] == name:
            print("Product is already in the cart.")
            return

    product = {"name": name, "price": price, "quantity": quantity}
    cart.append(product)
    print("Successfully added to the cart.")

add_product("Headphones", 1500, 1)

def remove_product(name):
    for product in cart:
        if product["name"] == name:
            cart.remove(product)
            print("Successfully removed from the cart.")
            return
    print("Product not found in the cart.")

product = input("Enter product to remove from the cart: ")
remove_product(product)

def update_quantity(name, quantity):
    for product in cart:
        if product["name"] == name:
            product["quantity"] = quantity
            print("Successfully updated the quantity.")
            return
    print("Product not found in the cart.")

product = input("Enter product name to update quantity: ")
new_quantity = int(input("Enter new quantity: "))
update_quantity(product, new_quantity)


def calculate_subtotal():
    subtotal = 0
    for product in cart:
        amount = product["price"] * product["quantity"]
        subtotal += amount
    return subtotal

print("Subtotal:", calculate_subtotal())

def calculate_discount(subtotal):
    discount = 0
    if subtotal >= 50000:
        discount = subtotal * 0.1
    elif subtotal >= 30000:
        discount = subtotal * 0.05
    return discount

print("Discount:", calculate_discount(calculate_subtotal()))

def calculate_final_amount():
    subtotal = calculate_subtotal()
    discount = calculate_discount(subtotal)
    final_amount = subtotal - discount
    return final_amount

print("Final Amount:", calculate_final_amount())


def display_cart():
    print("Shopping Cart:")
    for product in cart:
        print("Name: ", product["name"], ", Price: ", product["price"], ", Quantity: ", product["quantity"])

display_cart()