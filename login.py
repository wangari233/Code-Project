username = input("Enter username:")
password = input("Enter password:")
if not username or not password:
    print("Incorrect input")
else:
     if (username == "admin") and (password == "1234"):
      print("Login successful")
     else:
      print("Login failed")
