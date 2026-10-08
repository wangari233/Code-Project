
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Hello, how many vowels are in this sentence?"))
print(count_vowels("My name is Rita."))

sentence = "list comprehensions are powerful"
result = [char for char in sentence if char.lower() not in "aeiou"]
print(result)

