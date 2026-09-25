try:
    alpha = int("abc")
except ValueError:
    print("Invalid number")
except Exception:
    print("Something else went wrong")    