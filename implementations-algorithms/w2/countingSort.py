# Counting Sort Implementation
# Time Complexity: O(n + k), where n is the number of elements and k is the range of input values
# Auxiliary Space Complexity: O(n + k)

def counting_sort(arr):
    if not arr:
        return arr  # O(1)
    max_val = max(arr)  # O(n)
    min_val = min(arr)  # O(n)
    k = max_val - min_val + 1  # O(1)
    count = [0] * k  # O(k)
    output = [0] * len(arr)  # O(n)

    # Count occurrences
    for num in arr:  # O(n)
        count[num - min_val] += 1  # O(1)

    # Accumulate counts
    for i in range(1, k):  # O(k)
        count[i] += count[i - 1]  # O(1)

    # Build output array (stable sort)
    for i in range(len(arr) - 1, -1, -1):  # O(n)
        output[count[arr[i] - min_val] - 1] = arr[i]  # O(1)
        count[arr[i] - min_val] -= 1  # O(1)

    # Copy output to arr
    for i in range(len(arr)):  # O(n)
        arr[i] = output[i]  # O(1)
    return arr

if __name__ == "__main__":
    test_cases = [
        [],  # empty
        [1],  # single element
        [5, 4, 3, 2, 1],  # reverse sorted
        [1, 2, 3, 4, 5],  # already sorted
        [3, 1, 4, 1, 5, 9, 2, 6],  # unsorted with duplicates
        [7, 7, 7, 7],  # all equal
        [0, 2, 0, 2, 1],  # with zero
        [100, 50, 200, 25, 75],  # large values
        [0],  # single zero
    ]
    for arr in test_cases:
        arr_copy = arr.copy()
        counting_sort(arr_copy)
        print(f"Original: {arr}\nSorted:   {arr_copy}\n")

