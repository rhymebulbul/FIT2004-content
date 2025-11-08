# QuickSelect - Find k-th smallest element (0-indexed)
# Time Complexity: O(n) average case, O(n²) worst case
# Space Complexity: O(log n) average case for recursion stack, O(n) worst case
# Based on FIT2004 Course Notes Chapter 4 and Lecture 3

import random


def hoare_partition(A, lo, hi):
    """
    Hoare's partition scheme - in-place partitioning

    Partitions array A[lo..hi] around pivot (chosen as first element)
    Returns index j where:
    - All elements A[lo..j] <= pivot
    - All elements A[j+1..hi] >= pivot

    Time Complexity: O(hi - lo + 1) = O(n) for subarray size n
    Space Complexity: O(1)

    Note: Pivot is A[lo], excluded from initial scan
    """
    pivot = A[lo]
    i = lo + 1  # Start after pivot
    j = hi      # Start at end

    while i <= j:
        # Move i right while A[i] < pivot
        while i <= j and A[i] < pivot:
            i += 1

        # Move j left while A[j] > pivot
        while i <= j and A[j] > pivot:
            j -= 1

        # If pointers haven't crossed, swap elements
        if i < j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1

    # Swap pivot into correct position
    A[lo], A[j] = A[j], A[lo]
    return j


def dnf_partition(A, lo, hi, pivot_val):
    """
    Dutch National Flag (3-way) partition

    Partitions array into three regions:
    - A[lo..lt-1]: elements < pivot_val
    - A[lt..gt]: elements == pivot_val
    - A[gt+1..hi]: elements > pivot_val

    Returns: (lt, gt) - boundaries of equal region

    Time Complexity: O(hi - lo + 1) = O(n)
    Space Complexity: O(1)

    Advantage: Handles duplicates efficiently
    """
    lt = lo
    i = lo
    gt = hi

    while i <= gt:
        if A[i] < pivot_val:
            A[lt], A[i] = A[i], A[lt]
            lt += 1
            i += 1
        elif A[i] > pivot_val:
            A[i], A[gt] = A[gt], A[i]
            gt -= 1
        else:  # A[i] == pivot_val
            i += 1

    return lt, gt


def quickselect_random(A, k, lo=0, hi=None):
    """
    QuickSelect with random pivot selection
    Finds k-th smallest element (0-indexed)

    Algorithm:
    1. Choose random pivot
    2. Partition array using DNF partition
    3. If k in equal region, return pivot value
    4. If k < left boundary, recurse left
    5. If k > right boundary, recurse right

    Time Complexity:
    - Average case: O(n) - Expected linear time
    - Worst case: O(n²) - If pivot consistently bad

    Space Complexity: O(log n) average for recursion

    Args:
        A: List of comparable elements (modified in-place)
        k: Index of desired order statistic (0-indexed)
        lo: Start of range (default 0)
        hi: End of range (default len(A)-1)

    Returns:
        k-th smallest element
    """
    if hi is None:
        hi = len(A) - 1

    while True:
        # Base case: single element
        if lo == hi:
            return A[lo]

        # Choose random pivot value
        pivot_index = random.randint(lo, hi)
        pivot_val = A[pivot_index]

        # Partition using DNF (3-way partition)
        lt, gt = dnf_partition(A, lo, hi, pivot_val)

        # Check which region k falls into
        if k < lt:
            # k-th element in left region (< pivot)
            hi = lt - 1
        elif k > gt:
            # k-th element in right region (> pivot)
            lo = gt + 1
        else:
            # k-th element in middle region (== pivot)
            return A[k]


def median_of_medians(A, lo, hi):
    """
    Median of Medians - finds approximate median in O(n)

    Algorithm:
    1. Divide array into groups of 5
    2. Find median of each group
    3. Recursively find median of these medians

    Guarantees pivot quality: between 30th and 70th percentile

    Time Complexity: O(n)
    Recurrence: T(n) = T(n/5) + T(7n/10) + O(n) = O(n)

    Space Complexity: O(n) for medians array
    """
    n = hi - lo + 1

    # Base case: sort small groups directly
    if n <= 5:
        sorted_group = sorted(A[lo:hi+1])
        return sorted_group[n // 2]

    # Divide into groups of 5 and find medians
    medians = []
    i = lo
    while i <= hi:
        group_end = min(i + 4, hi)
        group = sorted(A[i:group_end+1])
        medians.append(group[len(group) // 2])
        i += 5

    # Recursively find median of medians
    return median_of_medians(medians, 0, len(medians) - 1)


def quickselect_mom(A, k, lo=0, hi=None):
    """
    QuickSelect with Median-of-Medians pivot selection
    Guarantees O(n) worst-case time complexity

    Uses median-of-medians to select pivot that guarantees
    balanced partition (at most 70% of elements on one side)

    Time Complexity: O(n) worst-case
    Space Complexity: O(n) for median-of-medians computation

    Note: Slower in practice than random pivot due to constant factors
    """
    if hi is None:
        hi = len(A) - 1

    while True:
        # Base case: single element
        if lo == hi:
            return A[lo]

        # Choose pivot using median-of-medians
        pivot_val = median_of_medians(A, lo, hi)

        # Partition using DNF (3-way partition)
        lt, gt = dnf_partition(A, lo, hi, pivot_val)

        # Check which region k falls into
        if k < lt:
            hi = lt - 1
        elif k > gt:
            lo = gt + 1
        else:
            return A[k]


def find_median(A):
    """
    Finds median of array A using QuickSelect

    Time Complexity: O(n) average case
    """
    n = len(A)
    k = (n - 1) // 2 if n % 2 == 1 else n // 2
    return quickselect_random(A.copy(), k)


if __name__ == "__main__":
    print("="*70)
    print("QUICKSELECT ALGORITHM DEMONSTRATION")
    print("="*70)

    # Test 1: Basic quickselect with random pivot
    print("\nTest 1: Find k-th smallest elements")
    print("-" * 70)
    A = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    print(f"Array: {A}")
    print(f"Sorted: {sorted(A)}")

    for k in [0, 2, 4, 6, 9]:
        A_copy = A.copy()
        result = quickselect_random(A_copy, k)
        expected = sorted(A)[k]
        status = "✓" if result == expected else "✗"
        print(f"  k={k}: quickselect={result}, expected={expected} {status}")

    # Test 2: Finding median
    print("\n" + "="*70)
    print("Test 2: Finding Median")
    print("-" * 70)
    test_arrays = [
        [5, 3, 8, 1, 9],
        [10, 20, 30, 40],
        [7],
        [2, 3, 7, 8, 4, 9, 1, 10, 6, 5]
    ]

    for arr in test_arrays:
        median = find_median(arr)
        sorted_arr = sorted(arr)
        expected = sorted_arr[len(arr) // 2] if len(arr) % 2 == 0 else sorted_arr[len(arr) // 2]
        print(f"Array: {arr}")
        print(f"  Median: {median}, Expected: {expected}")

    # Test 3: Median of Medians
    print("\n" + "="*70)
    print("Test 3: QuickSelect with Median-of-Medians (Deterministic)")
    print("-" * 70)
    B = [50, 80, 90, 10, 30, 20, 70, 60]
    print(f"Array: {B}")
    print(f"Sorted: {sorted(B)}")

    for k in [0, 3, 5, 7]:
        B_copy = B.copy()
        result = quickselect_mom(B_copy, k)
        expected = sorted(B)[k]
        status = "✓" if result == expected else "✗"
        print(f"  k={k}: mom_select={result}, expected={expected} {status}")

    # Test 4: Edge cases
    print("\n" + "="*70)
    print("Test 4: Edge Cases")
    print("-" * 70)

    # Single element
    C = [42]
    result = quickselect_random(C.copy(), 0)
    print(f"Single element [42], k=0: {result} {'✓' if result == 42 else '✗'}")

    # All duplicates
    D = [5, 5, 5, 5, 5]
    result = quickselect_random(D.copy(), 2)
    print(f"All duplicates [5,5,5,5,5], k=2: {result} {'✓' if result == 5 else '✗'}")

    # Already sorted
    E = [1, 2, 3, 4, 5]
    result = quickselect_random(E.copy(), 2)
    print(f"Already sorted [1,2,3,4,5], k=2: {result} {'✓' if result == 3 else '✗'}")

    # Reverse sorted
    F = [5, 4, 3, 2, 1]
    result = quickselect_random(F.copy(), 2)
    print(f"Reverse sorted [5,4,3,2,1], k=2: {result} {'✓' if result == 3 else '✗'}")

    # Test 5: Performance comparison (conceptual)
    print("\n" + "="*70)
    print("ALGORITHM COMPARISON")
    print("="*70)
    print("Random Pivot QuickSelect:")
    print("  - Average case: O(n)")
    print("  - Worst case: O(n²)")
    print("  - Fastest in practice")
    print("  - Expected linear time with high probability")
    print()
    print("Median-of-Medians QuickSelect:")
    print("  - Worst case: O(n) guaranteed")
    print("  - Higher constant factors")
    print("  - Slower in practice")
    print("  - Theoretical importance: proves O(n) selection possible")
    print()
    print("Sorting then selecting:")
    print("  - O(n log n) - always slower than selection for single query")
    print("="*70)