x = int(input("Enter the first number:"))
y = int(input("Enter the secend number:"))
z = int(input("Enter the third number:"))
if x >= y and x >= z:
    print("The largest number is", x)
elif y >=x and y>=z:
    print("The largest number is", y)
else:
    print("The largest number is", z)