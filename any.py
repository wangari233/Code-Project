numbers = [-10, -5, -2, 4, -8]
if any(x > 0 for x in numbers):
    print("True")   #positive number exists
else:
    print("False")   #no positive number exists