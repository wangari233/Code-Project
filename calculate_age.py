from datetime import date
current_year = date.today().year
birth_year = int(input("Enter your year of birth:"))
age = current_year - birth_year
print(f"You are approximately{age} years old.")