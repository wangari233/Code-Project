numbers = input("Enter numbers separated by spaces:").split()
unique = []
for num in numbers:
    num = int(num)
    if num not in unique:
        unique.append(num)
print("List without duplicates:", unique)
