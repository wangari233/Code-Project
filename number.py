numbers = input("Enter numbers separated by spaces:").split()
print("numbers greater than 10")
for num in numbers:
    if int(num) > 10:
        print(num)
