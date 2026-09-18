try:
    n = int(input("Enter a positive integer to determine the sum of all numbers from 1 to n:"))
    if n < 1: 
        print("Input incorrect. Please enter a number greater than 0.")
    else:
        total = 0
        counter = 1
        while counter <= n:
            total = total + counter
            counter = counter + 1
        print("The sum of numbers from 1 to", n, "is:", total)
except ValueError:
    print("Invalid input. Please enter a valid integer")

            