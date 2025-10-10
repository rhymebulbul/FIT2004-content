# Radix Sort implementation for non-negative integers
# Time Complexity: O(d*(n+b)), where d is the number of digits, n is the number of elements, b is the base (10 for decimal)
# Auxiliary Space: O(n + b)

def get_digit(number, base, digit):
    # Returns the digit at the given place (1-based, rightmost is 1)
    return (number // (base ** (digit - 1))) % base

def radix_pass(arr, base, digit):
    n = len(arr)
    counter = [0] * base  # O(base)
    position = [0] * base  # O(base)
    temp = [0] * n  # O(n)

    # Step 1: Count occurrences
    for i in range(n):  # O(n)
        d = get_digit(arr[i], base, digit)
        counter[d] += 1

    # Step 2: Compute positions (1-based in pseudocode, 0-based in Python)
    position[0] = 0
    for v in range(1, base):  # O(base)
        position[v] = position[v - 1] + counter[v - 1]

    # Step 3: Place elements in temp array (stable)
    for i in range(n):  # O(n)
        d = get_digit(arr[i], base, digit)
        temp[position[d]] = arr[i]
        position[d] += 1

    # Step 4: Copy back
    for i in range(n):  # O(n)
        arr[i] = temp[i]

def radix_sort(arr, base=10):
    if not arr:
        return arr
    max_val = max(arr)
    digits = 1
    while max_val >= base ** digits:
        digits += 1
    for digit in range(1, digits + 1):  # 1-based digit positions
        radix_pass(arr, base, digit)
    return arr

if __name__ == "__main__":
    test_cases = [
        [],
        [1],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        [3, 1, 4, 1, 5, 9, 2, 6],
        [7, 7, 7, 7],
        [0, 2, 0, 2, 1],
        [100, 50, 200, 25, 75],
        [0],
        [170, 45, 75, 90, 802, 24, 2, 66],
    ]
    for arr in test_cases:
        arr_copy = arr.copy()
        radix_sort(arr_copy)
        print(f"Original: {arr}\nSorted:   {arr_copy}\n")
