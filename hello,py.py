# ==========================================
# 1. DECLARING VARIABLES & NAMING CONVENTIONS
# ==========================================
# Use snake_case (lowercase with underscores) for variable names.
# Must start with a letter or underscore, not a number.

user_name = "Alex"      # Valid snake_case variable
total_score = 95        # Valid snake_case variable
_is_active = True       # Valid variable starting with underscore


# ==========================================
# 2. HOW THE print() FUNCTION WORKS
# ==========================================
# Basic print statement
print("Hello, World!")

# Printing multiple items separated by space
print("User:", user_name, "| Score:", total_score)

# Using f-strings (formatted strings)
print(f"Welcome back {user_name}! Your total score is {total_score}.")


# ==========================================
# 3. COMMON DATA TYPES IN PYTHON
# ==========================================
age = 25                # Integer (int)
price = 19.99           # Floating-point number (float)
greeting = "Hello"      # String (str)
is_student = False      # Boolean (bool)
skills = ["Python", "SQL", "Git"]  # List (list)


# ==========================================
# 4. HOW type() AND isinstance() WORK
# ==========================================
# type() returns the exact data type of an object
print(type(age))        # Output: <class 'int'>
print(type(price))      # Output: <class 'float'>
print(type(greeting))   # Output: <class 'str'>

# isinstance() checks if an object is of a specified type (returns True or False)
print(isinstance(age, int))          # Output: True
print(isinstance(greeting, int))     # Output: False

# Checking against multiple possible types
print(isinstance(price, (int, float)))  # Output: True