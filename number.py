numbers = input("Enter numbers separated by spaces").split()
if not numbers:
    print("No numbers entered")
else:
   found = False
for num in numbers:
    try:
         number = int(num)
         if number > 10:
             print(number)
             found = True
    except ValueError:
     print(f"Skipping invalid input: '{num}'")
if not found:
     print("None")

             

        


      

