count = 0    #count is a global variable

def increment():
    global count
    count += 5
    print(count, end=" ")

increment()
print(count)
