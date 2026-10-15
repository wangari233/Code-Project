import json

FILE = "products.json"

def load_products():
    try:
        with open(FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return[]

def save_products(products):
    with open(FILE, "w") as file:
        json.dump(products, file, indent=4)

def add_product(product_id, name, category, price, quantity):
    products = load_products()
    for p in products:
        if p["id"] == product_id:
            print("Error: Product ID already exists!")
            return
    products.append({
            "id": product_id,
            "name": name,
            "category": category,
            "price": price,
            "quantity": quantity
        })
    save_products(products)
    print("Products added successfully!")     

def increase_stock(product_id, amount):
    products = load_products()
    for p in products:
        if p["id"] == product_id:
            p["quantity"] += amount
            save_products(products)
            print("Stock increased!")
            return
    print("Products not found.")

def decrease_stock(product_id, amount):
    products = load_products()
    for p in products:
        if p["id"] == product_id:
            if p["quantity"] - amount < 0:
                print("Error: Not enough stock!")
                return
            p["quantity"] -= amount
            save_products(products)
            print("Stock decreased!")            
            return
    print("Product not found.")

def find_out_of_stock():
    products = load_products()
    return [p for p in products if p["quantity"] == 0]

def find_below_threshold(threshold):
    products = load_products()
    return [p for p in products if p ["quantity"] < threshold]

def find_most_expensive():
    products = load_products()
    return max(products, key=lambda p: p["price"], default=None)               

def find_cheapest():
    products = load_products()
    return min(products, key=lambda p: p["price"], default=None)

def calculate_total_value():
    products = load_products()
    return sum(p["price"] * p["quantity"] for p in products)

def group_by_category():
    products = load_products()
    categories = {}
    for p in products:
        categories.setdefault(p["category"], []).append(p)
    return categories

def main():
    def view_products():
        products = load_products()
        if not products:
            print("No products found.")
            return

        for product in products:
            print(product)


    while True:
        print("\n--- Inventory Management System ---")
        print("1. Add Product")
        print("2. View Products")   
        ...
        print("14. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            pid = input("Enter product ID: ")
            name = input("Enter name: ")
            category = input("Enter category: ")
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))
            add_product(pid, name, category, price, quantity)

        elif choice == "2":
            view_products()

        elif choice == "14":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()                

