"""
QuickSelect with Hoare's Partition - CORRECT IMPLEMENTATION
Pivot is first element and excluded from initial scan
"""

def hoare_partition_correct(A, lo, hi):
    """
    Hoare's partition with pivot as first element
    - Pivot is excluded from scanning
    - At the end, swap pivot into correct position
    """
    pivot = A[lo]
    i = lo + 1  # Start AFTER pivot
    j = hi      # Start at end

    print(f"\n{'='*70}")
    print(f"PARTITION: range [{lo}, {hi}], pivot = A[{lo}] = {pivot}")
    print(f"Array: {A}")
    print(f"Initial: i={i} (after pivot), j={j}")
    print(f"{'='*70}")

    iteration = 0
    while i <= j:
        iteration += 1
        print(f"\nIteration {iteration}:")

        # Move i right while A[i] < pivot
        print(f"  Moving i right (while A[i] < {pivot}):")
        while i <= j and A[i] < pivot:
            print(f"    i={i}, A[{i}]={A[i]} < {pivot}, move right...")
            i += 1
        if i <= j:
            print(f"    i={i}, A[{i}]={A[i]} >= {pivot} ✓ STOP")

        # Move j left while A[j] > pivot
        print(f"  Moving j left (while A[j] > {pivot}):")
        while i <= j and A[j] > pivot:
            print(f"    j={j}, A[{j}]={A[j]} > {pivot}, move left...")
            j -= 1
        if i <= j:
            print(f"    j={j}, A[{j}]={A[j]} <= {pivot} ✓ STOP")

        # If pointers haven't crossed, swap
        if i < j:
            print(f"\n  i < j ({i} < {j}), SWAP A[{i}] ↔ A[{j}]")
            print(f"  Before swap: A[{i}]={A[i]}, A[{j}]={A[j]}")
            A[i], A[j] = A[j], A[i]
            print(f"  After swap:  A[{i}]={A[i]}, A[{j}]={A[j]}")
            print(f"  Array now: {A}")
            i += 1
            j -= 1
        else:
            print(f"\n  i >= j ({i} >= {j}), pointers crossed")
            break

    # Swap pivot with element at j
    print(f"\nPartitioning complete. Now swap PIVOT A[{lo}]={A[lo]} with A[{j}]={A[j]}")
    print(f"  Before pivot swap: {A}")
    A[lo], A[j] = A[j], A[lo]
    print(f"  After pivot swap:  {A}")
    print(f"  Pivot now at index {j}")

    return j


def quickselect_correct_trace(A, k):
    """
    QuickSelect with correct Hoare partition for 2 rounds
    """
    A = A.copy()
    lo, hi = 0, len(A) - 1
    round_num = 0

    while round_num < 2:
        round_num += 1
        print(f"\n\n{'#'*70}")
        print(f"# ROUND {round_num}")
        print(f"{'#'*70}")
        print(f"Goal: Find 4th order statistic (index k={k})")
        print(f"Current search range: [{lo}, {hi}]")
        print(f"Array: {A}")

        j = hoare_partition_correct(A, lo, hi)

        print(f"\n{'='*70}")
        print(f"ROUND {round_num} SUMMARY:")
        print(f"{'='*70}")
        print(f"Array after partitioning: {A}")
        print(f"Pivot is now at index: j={j}")
        print(f"All elements at indices 0 to {j-1} are < pivot")
        print(f"All elements at indices {j+1} to {len(A)-1} are > pivot")

        if j == k:
            print(f"\nFOUND! j == k ({j} == {k})")
            print(f"The 4th order statistic is A[{k}] = {A[k]}")
            return A, True
        elif j > k:
            print(f"\nj > k ({j} > {k}), search LEFT half")
            hi = j - 1
        else:
            print(f"\nj < k ({j} < {k}), search RIGHT half")
            lo = j + 1

    return A, False


# Original problem
A = [2,3,7,8,4,9,1,10,6,5]
k = 3

print("="*70)
print("QUICKSELECT ANALYSIS: Finding 4th Order Statistic")
print("="*70)
print(f"Original array: {A}")
print(f"Target: 4th order statistic (index k={k})")
print(f"Sorted array: {sorted(A)}")
print(f"Answer should be: {sorted(A)[k]}")
print(f"\nPivot selection: FIRST element of subarray (excluded from scan)")
print(f"Partitioning: Hoare's algorithm with pivot swap at end")

final_array, found = quickselect_correct_trace(A, k)

print(f"\n\n{'#'*70}")
print(f"# FINAL RESULT AFTER 2 ROUNDS")
print(f"{'#'*70}")
print(f"Final array state: {final_array}")
print(f"\nVerifying answer choices:")
print(f"  a. A[3]=5? → A[3]={final_array[3]} {'✓' if final_array[3]==5 else '✗'}")
print(f"  b. A[8]=6? → A[8]={final_array[8]} {'✓' if final_array[8]==6 else '✗'}")
print(f"  c. A[9]=8? → A[9]={final_array[9]} {'✓' if final_array[9]==8 else '✗'}")
print(f"  d. A[0]=2? → A[0]={final_array[0]} {'✓' if final_array[0]==2 else '✗'}")
print(f"  e. A[4]=4? → A[4]={final_array[4]} {'✓' if final_array[4]==4 else '✗'}")
print(f"  f. A[5]=7? → A[5]={final_array[5]} {'✓' if final_array[5]==7 else '✗'}")
