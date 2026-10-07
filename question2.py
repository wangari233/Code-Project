products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 25},
    {"name": "Keyboard", "price": 75},
    {"name": "Monitor", "price": 300}
]
expensive_products = []
for product in products:
    if product["price"] > 50:
        expensive_products.append(product["name"])
        print(expensive_products)