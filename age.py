user_age = input("How old are you?:")
if not user_age:
    print("Age not entered")
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
        print("Invalid")
        
