year_input = input("Enter year:")
if not year_input:
    print("Incorrect input")
else:
    try:
        year = int(year_input)    
        if (year % 4 ==0) and (year % 100 != 0) or (year % 400 == 0):
         print("Leap year")
        else:
         print("Common year")
    except ValueError:
     print("Invalid input:Please enter a whole number.")
   
