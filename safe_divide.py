def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: division by zero")
        return None
    finally:
        print("Operations finished")

print(safe_divide(16, 2))
print(safe_divide(6 / 0))        