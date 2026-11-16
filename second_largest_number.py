def second_largest(lst):
    unique_nums = list(set(lst))
    unique_nums.sort()
    if len(unique_nums) < 2:
        return None
    return unique_nums[-2]

print(second_largest([10, 20, 4, 20, 15]))