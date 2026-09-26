with open("notes.txt", "w") as f:
    f.write("Learning Python file handling\nThis is an appended line\nI love Python")
    


filename = input("Enter the filename: ")
text = input("Enter the text: ")

with open(filename, "w") as f:
    f.write(text)

print("File created successfully!")

with open("notes.txt", "r") as f:
    lines = f.readlines()
    print("Number of lines:", len(lines))

with open("notes.txt", "r") as f:
    for line in f:
        if "Python" in line:
            print(line.strip())

with open("notes.txt", "r") as original:
    content = original.read()

with open("copy.txt", "w") as copy:
    copy.write(content)

print("Copy created successfully!")

with open("notes.txt", "r") as f:
    lines = f.readlines()

with open("reversed.txt", "w") as f:
    for line in reversed(lines):
        f.write(line)

print("Reversed file created!")