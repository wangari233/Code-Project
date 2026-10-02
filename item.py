def get_item(lst, index):
    try:
        return lst[index]
    except IndexError:
        print("Index out of range")
        return None
    finally:
        print("Lookup finished")

print(get_item([10, 20, 30], 1))
print(get_item([10, 20, 30], 5))
print(get_item([], 0))      