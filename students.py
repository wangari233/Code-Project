students = [
    {"name": "Alice", "age": 17},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 16},
    {"name": "Diana", "age": 22}
]
result = {student["name"]: student["age"] for student in students if student["age"] >= 18}
print(result)