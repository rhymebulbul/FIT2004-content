def binary_search(array, key):
    lo = 0
    hi = len(array)
    while lo < hi - 1:
        mid = (lo + hi) // 2
        if key >= array[mid]:
            lo = mid
        else:
            hi = mid
    if lo < len(array) and array[lo] == key:
        return lo
    else:
        return None


if __name__ == "__main__":
    test_cases = [
        ([1, 3, 5, 7, 9, 11, 13], 7),      # key in middle
        ([1, 3, 5, 7, 9, 11, 13], 1),      # key at start
        ([1, 3, 5, 7, 9, 11, 13], 13),     # key at end
        ([1, 3, 5, 7, 9, 11, 13], 4),      # key not present
        ([7], 7),                          # single-element, present
        ([7], 3),                          # single-element, not present
        ([], 7),                           # empty array
        ([1, 2, 2, 2, 3], 2),              # duplicates, present
        ([1, 2, 2, 2, 3], 4),              # duplicates, not present
    ]
    for arr, key in test_cases:
        idx = binary_search(arr, key)
        print(f"Array: {arr}, Key: {key} => Index: {idx}")
