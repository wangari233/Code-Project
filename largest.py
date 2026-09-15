x = input("Enter the first number:")
y = input("Enter the secend number:")
z = input("Enter the third number:")
if not x or not y or not z:
    print("Number not entered")
else:
    try: 
       x = int(x)
       y = int(y)
       z = int(z)
    

       if x >= y and x >= z:
        print("The largest number is", x)
       elif y >=x and y>=z:
        print("The largest number is", y)
       else:
        print("The largest number is", z)
    except ValueError:
      print("Invalid")