numbers = input("Enter numbers separated by spaces to determine whether numbers are greater than 10:").split()
if not numbers:
    print("No numbers entered")
else:
   found = False
for num in numbers:
    try:
         number = int(num)
         if number > 10:
             print(f"{number} is greater than 10")
             found = True
    except ValueError:
     print(f"Skipping invalid input: '{num}'")
if not found:
     print("None")

             

        


      

