from collections import Counter
characters = "aabbcddee"
count = Counter(characters)
for char in characters:          
    if count[char] == 1:
        print(char)     
        break