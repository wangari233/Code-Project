def two_sum_sorted(nums, target):
    
    indexed = sorted(enumerate(nums), key=lambda x: x[1])
    left, right = 0, len(indexed) - 1

    while left < right:
        s = indexed[left][1] + indexed[right][1]
        if s == target:
            return sorted([indexed[left][0], indexed[right][0]])
        elif s < target:
            left += 1
        else:
            right -= 1
    return []

print(two_sum_sorted([2, 7, 11, 15], 9))  