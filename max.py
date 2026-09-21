def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b

a = float(int(input("Enter the first number:")))
b = float(int(input("Enter the second number:")))
result = max_of_two(a, b)
print(result)
