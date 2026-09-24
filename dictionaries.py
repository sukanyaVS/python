# Create an inventory using a list of dictionaries:
# products = [
#     {"id": 1, "name": "Laptop", "price": 60000, "quantity": 5},
#     {"id": 2, "name": "Mouse", "price": 1000, "quantity": 20},
#     {"id": 3, "name": "Keyboard", "price": 2500, "quantity": 10}
# ]
# Implement:
# Display all products.
# Search product by ID.
# Add a new product.
# Update product quantity.
# Update product price.
# Find products with quantity less than 10.
# Calculate the total inventory value.


products = [
    {"id": 1, "name": "Laptop", "price": 60000, "quantity": 5},
    {"id": 2, "name": "Mouse", "price": 1000, "quantity": 20},
    {"id": 3, "name": "Keyboard", "price": 2500, "quantity": 10}
]

for product in products:
    print("ID:", product["id"])
    print("Name:", product["name"])
    print("Price:", product["price"])
    print("Quantity:", product["quantity"])
    print("=======================")

product_id = int(input("Enter product ID to search: "))

for product in products:
    if product["id"] == product_id:
        print("Product found:")
        print("ID:", product["id"])
        print("Name:", product["name"])
        print("Price:", product["price"])
        print("Quantity:", product["quantity"])
        break
else:
    print("Product not found.")

new_product_id = int(input("Enter new product ID: "))
new_product_name = input("Enter new product name: ")
new_product_price = float(input("Enter new product price: "))
new_product_quantity = int(input("Enter new product quantity: "))

new_product = {
    "id": new_product_id,
    "name": new_product_name,
    "price": new_product_price,
    "quantity": new_product_quantity
}

products.append(new_product)
print("Product added successfully.")

prod_id = int(input("Enter product ID to update quantity: "))
for product in products:
    if product["id"] == prod_id:
        new_quantity = int(input("Enter new quantity: "))
        product["quantity"] = new_quantity
        print("Quantity updated successfully.")
        break
else:
    print("Product not found.")

prod_price = int(input("Enter product ID to update price: "))
for product in products:
    if product["id"] == prod_price:
        new_price = float(input("Enter new price: "))
        product["price"] = new_price
        print("Price updated successfully.")
        break
else:
    print("Product not found.")    


filtered_products = []
for product in products:
    if product["quantity"] < 10:
        filtered_products.append(product)

print("Products with quantity less than 10:")
for product in filtered_products:
    print("ID:", product["id"])
    print("Name:", product["name"])
    print("Price:", product["price"])
    print("Quantity:", product["quantity"])
    print("=======================")


total_inventory_value = 0
for product in products:
    total_value = product["price"] * product["quantity"]
    total_inventory_value += total_value
    print("ID:", product["id"])
    print("Name:", product["name"])
    print("Total Inventory Value:", total_value)
    print("=======================")

print("Total Inventory Value:", total_inventory_value)