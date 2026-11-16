def most_frequent(lst):
    freq = {}
    for num in lst:
        freq[num] = freq.get(num, 0) + 1
    return max(freq, key=freq.get)

print(most_frequent([1, 2, 2, 3, 3, 3, 4]))