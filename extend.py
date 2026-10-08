def merge_and_clean(data: list) -> list:
    merged = []
    for item in data:
        if isinstance(item, list):
            merged.extend(item)
        else:
            merged.append(item)
    return merged

def clean_unique(data: list) -> list:
    cleaned = []
    seen = set()
    for item in merge_and_clean(data):
        if item not in seen:
            seen.add(item)
            cleaned.append(item)
    return cleaned
input_list = [1, 2, [3, 4], 2, [5, 3], 6, [7]]
print(merge_and_clean(input_list))