user_age = input("How old are you?:")
if not user_age:
    print("Age not entered")
elif user_age.replace(".", "", 1).isdigit and "." in user_age:
     print("You entered a decimal number")
elif user_age.isalpha:
     print("You entered a number in words or you entered something not related to a number")       
else:
    age = int(user_age)
    try:
        if age < 13:
            print("Child")
        elif age <= 19:
            print("Teenager")
        else:
            print("Adult")
    except ValueError:
        print("Invalid input")
        
