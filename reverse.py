def reverse_and_flip(words: list[str]) -> list[str]:
    return [word[::-1] for word in reversed(words)]
print(reverse_and_flip(["hello", "world", "python"]))
    