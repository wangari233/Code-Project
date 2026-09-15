score = input("Enter your score:")
if not score:
    print("Incorrect input")
else:
    try:
     user_score = int(score)
     if user_score >= 90:
      print("Grade: A")
     elif user_score >= 80:
      print("Grade: B")
     elif user_score >= 70:
      print("Grade: C")
     elif user_score >= 60:
      print("Grade: D")
     else:
      print("Grade: F")
    except ValueError:
      print("Wrong input. Please enter a whole number")
    
    
    
