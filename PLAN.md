What am I building? I am building a Simple Inventory Management System that allows a shop keeper to manage products. Each product has an ID, name, category, price and quantity. The system supports adding, viewing, searching, updating, deleting, stock management and reporting.
How will I break the problem into smaller parts?
*Data Handling
  . Load products from storage.
  . Save products to storage.

*Core Operations 
  . Add, view, search, update, delete products.

*Stock Management
  . Increase/decrease stock.
  . Prevent negative stock.

*Reports
  . Out-of-stock products.
  . Products below threshold.
  . Most expensive/cheapest product.
  . Total inventory value.
  . Group by category.

*User Interface
  . Menu-driven loop for interaction.
  . Input validation and error handling.

How will I represent a product?
A product will be represented as a dictionary with keys:
{
    "id": "P001",
    "name": "Milk",
    "category": "Dairy",
    "price": 50.0,
    "quantity": 20
}  

Which data structures will I use and why?
*List of dictionaries:
  . Easy to iterate, search and update.
  . Flexible for JSON persistence.
Example:
products = [
    {"id": "P001", "name": "Milk", "category": "Dairy", "price": 50.0, "quantity": 20},
    {"id": "P002", "name": "Bread", "category": "Bakery", "price": 30.0, "quantity": 15}
]

How will I persist the information?
Use a JSON file called products.json
  . It is human-readable.
  . It is easy to load and save with json module.
  . It ensures data remains after restarting the application.

What edge cases have I identified?
Adding a product with an existing ID to prevent duplicates.
Decreasing stock below zero to block operation.
Searching for a product that doesn't exist to return "not found".
Invalid input types for example, string instead of number for price or quantity.
Empty inventory file to handle gracefully.
Large inventory to ensure functions still work efficiently.
How will I test the application?
*Unit testing styel(manual at first):
  . Add products to check file contents.
  . Update product to verify changes.
  . Delete product to confirm removal.
  . Decrease stock to ensure no negatives.
  . Reports to check correctness.
*Scenario testing:
  . Start with empty file.
  . Add multiple categories.
  . Try invalid inputs.
  . Simulate shop operations(add, sell, restock)  
