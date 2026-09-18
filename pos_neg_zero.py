user_input = input("Enter a number to check whether it is positive, negative or zero:")
if not user_input:
    print("No input entered")
elif user_input.isalpha:
  print("You entered a letter")
else:
    try:
        number = int(user_input)
        if number > 0:
         print("Positive")
        elif number < 0:
         print("Negative")
        else:
         print("Zero")
    except ValueError:
     print("Invalid input. Please enter a whole number.")
