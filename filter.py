numbers = [10, 15, 20, 25, 30, 35]
result = filter(lambda x: x % 5 == 0 and x > 20, numbers)
print(list(result))

