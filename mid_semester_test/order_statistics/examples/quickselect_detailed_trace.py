"""
QuickSelect with Hoare's Partition - DETAILED STEP-BY-STEP TRACE
Shows every pointer movement and swap
"""

def hoare_partition_detailed(A, lo, hi):
    """
    Hoare's partition with detailed tracing
    """
    pivot = A[lo]
    i = lo - 1
    j = hi + 1

    print(f"\n{'='*70}")
    print(f"PARTITION: range [{lo}, {hi}], pivot = A[{lo}] = {pivot}")
    print(f"Array: {A}")
    print(f"Initial: i={i}, j={j}")
    print(f"{'='*70}")

    iteration = 0
    while True:
        iteration += 1
        print(f"\nIteration {iteration}:")

        # Move i right until A[i] >= pivot
        print(f"  Moving i right (looking for A[i] >= {pivot}):")
        while True:
            i += 1
            print(f"    i={i}, A[{i}]={A[i]}", end="")
            if A[i] >= pivot:
                print(f" >= {pivot} ✓ STOP")
                break
            else:
                print(f" < {pivot}, continue...")

        # Move j left until A[j] <= pivot
        print(f"  Moving j left (looking for A[j] <= {pivot}):")
        while True:
            j -= 1
            print(f"    j={j}, A[{j}]={A[j]}", end="")
            if A[j] <= pivot:
                print(f" <= {pivot} ✓ STOP")
                break
            else:
                print(f" > {pivot}, continue...")

        print(f"\n  Result: i={i} (A[{i}]={A[i]}), j={j} (A[{j}]={A[j]})")

        if i >= j:
            print(f"  i >= j ({i} >= {j}), PARTITIONING COMPLETE")
            print(f"  Returning partition index j={j}")
            return j

        # Swap
        print(f"  i < j, so SWAP A[{i}] ↔ A[{j}]")
        print(f"  Before swap: A[{i}]={A[i]}, A[{j}]={A[j]}")
        A[i], A[j] = A[j], A[i]
        print(f"  After swap:  A[{i}]={A[i]}, A[{j}]={A[j]}")
        print(f"  Array now: {A}")


def quickselect_detailed_trace(A, k):
    """
    QuickSelect with detailed tracing for 2 rounds
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

        j = hoare_partition_detailed(A, lo, hi)

        print(f"\n{'='*70}")
        print(f"ROUND {round_num} SUMMARY:")
        print(f"{'='*70}")
        print(f"Array after partitioning: {A}")
        print(f"Partition index: j={j}")
        print(f"Elements at index 0-{j} are <= pivot")
        print(f"Elements at index {j+1}-{hi} can be > pivot")

        if j == k:
            print(f"\nFOUND! j == k ({j} == {k})")
            print(f"The 4th order statistic is A[{k}] = {A[k]}")
            return A, True
        elif j > k:
            print(f"\nj > k ({j} > {k}), search LEFT half")
            hi = j
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
print(f"\nPivot selection: Always the FIRST element of the subarray")
print(f"Partitioning: Hoare's algorithm (in-place)")

final_array, found = quickselect_detailed_trace(A, k)

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

print(f"\n{'='*70}")
print("CORRECT ANSWERS: b and e")
print(f"{'='*70}")
