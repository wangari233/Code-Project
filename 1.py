import json
data = json.loads('{"name": "Alice", "age": 20, "course": "Cyber Security"}')
print(data["name"])

student = {"id": 101, "name": "Bob", "grade": "A"}
json_string = json.dumps(student)
print(json_string)

with open("students.json", "w") as f:
    json.dump(student, f, indent = 4)