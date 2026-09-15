user_input = input("Enter a number:")
if not user_input:
    print("No input entered")
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
