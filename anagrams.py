def are_anagrams(word1, word2):
    return sorted(word1) == sorted(word2)

print(are_anagrams("listen", "silent"))