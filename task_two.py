from collections import Counter

refs = ["TX001", "TX002", "TX003", "TX002", "TX004", "TX001"]
freq = Counter(refs)
print(dict(freq))
