sentence = "list comprehensions are powerful"
result = [char for char in sentence if char.lower() not in "aeiou"]
print(result)
