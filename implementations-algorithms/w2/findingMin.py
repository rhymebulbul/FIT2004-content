def find_min(array):
    if not array:
        raise ValueError("Array must have at least one element.")
    min_val = array[0]
    index = 1
    N = len(array)
    while index < N:
        if array[index] < min_val:
            min_val = array[index]
        index += 1
    return min_val


if __name__ == "__main__":
    test_cases = [
        [3, 1, 4, 1, 5, 9, 2, 6],    # typical unsorted
        [10],                        # single element
        [-5, -1, -10, 0],            # negatives
        [7, 7, 7, 7],                # all equal
        [100, 50, 200, 25, 75],      # mixed
    ]
    for arr in test_cases:
        print(f"Array: {arr}\nMin: {find_min(arr)}\n")

