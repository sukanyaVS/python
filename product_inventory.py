import csv
from pathlib import Path


FILE_NAME = Path(__file__).with_name("products.csv")
FIELDNAMES = ["product_id", "product_name", "category", "price", "quantity", "supplier_name"]


def load_products():
    try:
        with FILE_NAME.open("r", newline="", encoding="utf-8") as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        print(f"{FILE_NAME.name} file not found. Starting with an empty inventory.")
        return []
    except (csv.Error, OSError) as error:
        print(f"Could not read {FILE_NAME.name}: {error}")
        return []


def save_products(products):
    try:
        with FILE_NAME.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(products)
    except OSError as error:
        print(f"Could not save {FILE_NAME.name}: {error}")


def find_product_by_id(products, product_id):
    for product in products:
        if product.get("product_id") == product_id:
            return product
    return None


def display_products(products):
    if not products:
        print("No products found.")
        return

    print("\n===== Product Inventory =====")
    for product in products:
        print(
            "ID:", product["product_id"],
            "Name:", product["product_name"],
            "Category:", product["category"],
            "Price:", product["price"],
            "Quantity:", product["quantity"],
            "Supplier:", product["supplier_name"],
        )


def search_products(products):
    search_term = input("Enter a category or product name: ").strip().lower()
    if not search_term:
        print("Search term cannot be empty.")
        return

    matches = [
        product
        for product in products
        if search_term in product["category"].lower()
        or search_term in product["product_name"].lower()
    ]
    display_products(matches)


def add_product(products):
    product_id = input("Enter product ID: ").strip()
    if not product_id:
        print("Product ID cannot be empty.")
        return
    if find_product_by_id(products, product_id):
        print("A product with this ID already exists.")
        return

    product_name = input("Enter product name: ").strip()
    category = input("Enter category: ").strip()
    supplier_name = input("Enter supplier name: ").strip()
    try:
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Price must be a number and quantity must be a whole number.")
        return

    if price < 0 or quantity < 0:
        print("Price and quantity cannot be negative.")
        return
    if not product_name or not category or not supplier_name:
        print("Product name, category, and supplier name are required.")
        return

    products.append({
        "product_id": product_id,
        "product_name": product_name,
        "category": category,
        "price": str(price),
        "quantity": str(quantity),
        "supplier_name": supplier_name,
    })
    save_products(products)
    print("Product added successfully.")


def update_product(products):
    product_id = input("Enter product ID: ").strip()
    product = find_product_by_id(products, product_id)
    if product is None:
        print("Product not found.")
        return

    choice = input("Update price or quantity? ").strip().lower()
    try:
        if choice == "price":
            new_value = float(input("Enter new price: "))
            if new_value < 0:
                raise ValueError
            product["price"] = str(new_value)
        elif choice == "quantity":
            new_value = int(input("Enter new quantity: "))
            if new_value < 0:
                raise ValueError
            product["quantity"] = str(new_value)
        else:
            print("Choose either price or quantity.")
            return
    except ValueError:
        print("Enter a valid non-negative numeric value.")
        return

    save_products(products)
    print("Product updated successfully.")


def delete_product(products):
    product_id = input("Enter product ID to delete: ").strip()
    product = find_product_by_id(products, product_id)
    if product is None:
        print("Product not found.")
        return

    products.remove(product)
    save_products(products)
    print("Product deleted successfully.")


def main():
    products = load_products()

    while True:
        print("\n===== Product Inventory Management =====")
        print("1. Add product")
        print("2. Display all products")
        print("3. Search by category or product name")
        print("4. Update price or quantity")
        print("5. Delete product")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_product(products)
        elif choice == "2":
            display_products(products)
        elif choice == "3":
            search_products(products)
        elif choice == "4":
            update_product(products)
        elif choice == "5":
            delete_product(products)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1 to 6.")


if __name__ == "__main__":
    main()