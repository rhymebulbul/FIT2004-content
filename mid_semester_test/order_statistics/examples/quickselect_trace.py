"""
QuickSelect with Hoare's Partition - Trace Analysis
Finding the 4th order statistic (index 3) in A = [2,3,7,8,4,9,1,10,6,5]
"""

def hoare_partition(A, lo, hi):
    """
    Hoare's partition scheme with pivot as first element
    Returns partition index j
    """
    pivot = A[lo]
    i = lo - 1
    j = hi + 1

    print(f"\n  Partitioning indices {lo}-{hi}, pivot = {pivot}")
    print(f"  Array before: {A}")

    while True:
        # Move i right until A[i] >= pivot
        while True:
            i += 1
            if A[i] >= pivot:
                break

        # Move j left until A[j] <= pivot
        while True:
            j -= 1
            if A[j] <= pivot:
                break

        print(f"  i={i} (A[i]={A[i]}), j={j} (A[j]={A[j]})")

        if i >= j:
            print(f"  Returning j={j}")
            return j

        # Swap
        A[i], A[j] = A[j], A[i]
        print(f"  Swapped A[{i}] and A[{j}]: {A}")


def quickselect_trace(A, k):
    """
    QuickSelect to find kth order statistic (0-indexed)
    Traces first 2 rounds of partitioning
    """
    A = A.copy()  # Work on a copy
    lo, hi = 0, len(A) - 1
    round_num = 0

    while round_num < 2:
        round_num += 1
        print(f"\n{'='*60}")
        print(f"ROUND {round_num}:")
        print(f"Searching for index {k} in range [{lo}, {hi}]")

        j = hoare_partition(A, lo, hi)

        print(f"\nArray after partition: {A}")
        print(f"Partition index j = {j}")

        if j == k:
            print(f"\nFound! The {k+1}th order statistic is at index {j}")
            return A, True
        elif j > k:
            print(f"j > k, search left side")
            hi = j
        else:
            print(f"j < k, search right side")
            lo = j + 1

    return A, False


# Original array
A = [2,3,7,8,4,9,1,10,6,5]
k = 3  # 4th order statistic (0-indexed)

print("="*60)
print("QuickSelect Analysis")
print("="*60)
print(f"Initial array: {A}")
print(f"Looking for 4th order statistic (index {k})")
print(f"Sorted array would be: {sorted(A)}")
print(f"So we're looking for the value: {sorted(A)[k]}")

final_array, found = quickselect_trace(A, k)

print(f"\n{'='*60}")
print(f"FINAL STATE AFTER 2 ROUNDS:")
print(f"{'='*60}")
print(f"Array: {final_array}")
print(f"")

# Check each option
options = {
    'a': (3, 5, "A[3]=5"),
    'b': (8, 6, "A[8]=6"),
    'c': (9, 8, "A[9]=8"),
    'd': (0, 2, "A[0]=2"),
    'e': (4, 4, "A[4]=4"),
    'f': (5, 7, "A[5]=7"),
}

print("Checking options:")
for opt, (idx, expected, desc) in options.items():
    actual = final_array[idx]
    is_correct = actual == expected
    print(f"  {opt}. {desc}: A[{idx}]={actual}, {'✓ TRUE' if is_correct else '✗ FALSE'}")
