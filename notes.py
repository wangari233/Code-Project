with open("notes.txt", "w") as f:
    f.write("Learning Python file handling")

with open("notes.txt", "r") as f:
    content = f.read()
    print(content)

with open("notes.txt", "a") as f:
    f.write("\nThis is an appended line")

with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())        