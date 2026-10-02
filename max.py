words = ["hello", "world", "python", "programming", "ai"]
def count_vowels(s):
    return sum(char in "aeiou" for char in s.lower())
result = max(words, key=count_vowels)
print(result)