
count = 0    #count is a global variable

def increment():
    global count
    count += 5
    print(count, end=" ")

increment()
print(count)

scores = [7, 8, 9, 7, 10, 7, 6]
count = scores.count(7)
print(count)

