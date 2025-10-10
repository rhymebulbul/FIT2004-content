def merge_and_count_split_inv(left, right):
    result = []
    i = j = 0
    split_inversions = 0
    n1 = len(left)
    n2 = len(right)
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            split_inversions += n1 - i
    result.extend(left[i:])
    result.extend(right[j:])
    return result, split_inversions


def sort_and_count_inv(array, lo, hi):
    if lo == hi:
        return [array[lo]], 0
    else:
        mid = (lo + hi) // 2
        left_sorted, inv_left = sort_and_count_inv(array, lo, mid)
        right_sorted, inv_right = sort_and_count_inv(array, mid + 1, hi)
        merged, inv_split = merge_and_count_split_inv(left_sorted, right_sorted)
        return merged, inv_left + inv_right + inv_split


if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 4, 5],            # sorted, 0 inversions
        [5, 4, 3, 2, 1],            # reverse, 10 inversions
        [2, 4, 1, 3, 5],            # 3 inversions
        [1],                        # single element, 0 inversions
        [],                         # empty, 0 inversions
        [3, 1, 2],                  # 2 inversions
        [1, 20, 6, 4, 5],           # 5 inversions
    ]
    for arr in test_cases:
        if arr:
            sorted_arr, inv_count = sort_and_count_inv(arr, 0, len(arr)-1)
        else:
            sorted_arr, inv_count = [], 0
        print(f"Array: {arr}\nSorted: {sorted_arr}\nInversions: {inv_count}\n")

