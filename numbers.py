numbers = input("Enter a number from 1 to 10:")
while numbers == "":
    print("Input incorrect. Please try again!")
    numbers = input("Enter a number from 1 to 10:")
numbers = int(numbers)
print(f"You have entered {numbers}")