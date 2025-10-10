# Selection Sort Implementation
# Time Complexity: O(n^2) in all cases (best, average, worst)
# Auxiliary Space Complexity: O(1) (in-place)

def selection_sort(arr):
    n = len(arr)  # O(1)
    for i in range(n):  # O(n)
        min_idx = i  # O(1)
        for j in range(i+1, n):  # O(n) in total for all i
            # Compare arr[j] and arr[min_idx]: O(1)
            if arr[j] < arr[min_idx]:
                min_idx = j  # O(1)
        # Swap arr[i] and arr[min_idx] if needed: O(1)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    # Total time complexity: O(n^2)
    # Total auxiliary space: O(1)
    return arr

if __name__ == "__main__":
    test_cases = [
        [],  # empty
        [1],  # single element
        [5, 4, 3, 2, 1],  # reverse sorted
        [1, 2, 3, 4, 5],  # already sorted
        [3, 1, 4, 1, 5, 9, 2, 6],  # unsorted with duplicates
        [7, 7, 7, 7],  # all equal
    ]
    for arr in test_cases:
        arr_copy = arr.copy()
        selection_sort(arr_copy)
        print(f"Original: {arr}\nSorted:   {arr_copy}\n")

