def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(array, lo, hi):
    if hi > lo:
        mid = (lo + hi) // 2
        left_sorted = merge_sort(array[lo:mid+1], 0, mid-lo)
        right_sorted = merge_sort(array[mid+1:hi+1], 0, hi-mid-1)
        merged = merge(left_sorted, right_sorted)
        return merged
    else:
        return [array[lo]]


if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    sorted_arr = merge_sort(arr, 0, len(arr)-1)
    print("Sorted array:", sorted_arr)

