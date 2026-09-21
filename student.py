student_name = input("Enter your name:")
student_score = int(input("Enter your score:"))
if student_score >= 90:
    print(f"Hello {student_name}, you scored an A!")
elif student_score >= 80:
    print(f"Hello {student_name}, you scored a B!")
elif student_score >= 70:
    print(f"Hello {student_name}, you scored a C!")
elif student_score >=60:
    print(f"Hello {student_name}, you scored a D!")
else:
    print(f"Hello {student_name}, you scored an F!")
    