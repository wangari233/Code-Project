def linear_search(ids, target):
    for i in range(len(ids)):
        if ids[i] == target:
            return i   
    return -1          


ids = [105, 203, 150, 99, 300]
print(linear_search(ids, 150))  


def binary_search(ids, target):
    left, right = 0, len(ids) - 1
    while left <= right:
        mid = (left + right) // 2
        if ids[mid] == target:
            return mid
        elif ids[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


ids_sorted = [99, 105, 150, 203, 300]
print(binary_search(ids_sorted, 150))

