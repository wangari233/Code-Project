references = ["TX001", "TX002", "TX003", "TX002", "TX004", "TX001"]
seen = set()
duplicates = set()

for reference in references:
    if reference in seen:
        duplicates.add(reference)
    else:
        seen.add(reference)

print(list(duplicates))  