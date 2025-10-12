"""
Hoare's Partition: Understanding the Final Pivot Swap

Key Question: After pointers cross, which element do we swap with the pivot?
Answer: We swap the pivot with the element at position j
"""

def explain_partition_invariants():
    """
    Explains why we swap with j (not i) after pointers cross
    """
    print("="*70)
    print("HOARE'S PARTITION INVARIANTS")
    print("="*70)
    print()
    print("Setup:")
    print("  - Pivot is at A[lo] (first position)")
    print("  - i starts at lo+1 (excludes pivot)")
    print("  - j starts at hi (last position)")
    print()
    print("During scanning:")
    print("  - i moves right, stops when A[i] >= pivot")
    print("  - j moves left, stops when A[j] <= pivot")
    print("  - If i < j, swap and continue")
    print()
    print("When pointers CROSS (i >= j):")
    print("  - All elements from lo+1 to j are <= pivot")
    print("  - All elements from j+1 to hi are > pivot")
    print("  - Position j is the RIGHTMOST element <= pivot")
    print()
    print("Final Pivot Swap:")
    print("  - Swap A[lo] (pivot) with A[j]")
    print("  - This puts pivot in its CORRECT sorted position")
    print("  - Now: A[lo...j-1] < pivot, A[j] = pivot, A[j+1...hi] > pivot")
    print()
    print("Why j and not i?")
    print("  - j points to an element <= pivot (safe to swap)")
    print("  - i points to an element >= pivot (would break partition)")
    print()
    print("="*70)


def trace_with_explanation(A, lo, hi):
    """
    Trace partition with detailed explanation of final swap
    """
    pivot = A[lo]
    i = lo + 1
    j = hi

    print(f"\nPARTITION: [{lo}, {hi}], pivot = A[{lo}] = {pivot}")
    print(f"Array: {A}")
    print(f"Starting: i={i}, j={j}")

    # Simplified scanning
    while i <= j:
        while i <= j and A[i] < pivot:
            i += 1
        while i <= j and A[j] > pivot:
            j -= 1

        if i < j:
            print(f"\nSwap A[{i}]={A[i]} ↔ A[{j}]={A[j]}")
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1

    print(f"\n" + "="*70)
    print("POINTERS CROSSED!")
    print(f"i={i}, j={j}")
    print(f"Array: {A}")
    print(f"\nPartition state:")
    print(f"  A[{lo+1}...{j}]: ", A[lo+1:j+1] if j >= lo+1 else "empty", f" (all <= {pivot})")
    print(f"  A[{j+1}...{hi}]: ", A[j+1:hi+1] if j+1 <= hi else "empty", f" (all > {pivot})")
    print(f"\nElement at j: A[{j}]={A[j]}")
    print(f"  → This is <= {pivot}, so SAFE to swap with pivot")

    if i <= hi:
        print(f"\nElement at i: A[{i}]={A[i]}")
        print(f"  → This is >= {pivot}, so NOT safe to swap with pivot")

    print(f"\n>>> Swap PIVOT A[{lo}]={A[lo]} with A[{j}]={A[j]} <<<")
    A[lo], A[j] = A[j], A[lo]
    print(f"Result: {A}")
    print(f"Pivot {pivot} is now at index {j}")
    print("="*70)

    return j, A


# Demo with the quiz examples
print("="*70)
print("UNDERSTANDING THE FINAL PIVOT SWAP")
print("="*70)

explain_partition_invariants()

print("\n\n" + "#"*70)
print("# EXAMPLE 1: Round 1 from the quiz")
print("#"*70)
A1 = [2, 1, 7, 8, 4, 9, 3, 10, 6, 5]  # State before pivot swap
print("\nBefore final swap (pointers already crossed):")
j1, result1 = trace_with_explanation(A1.copy(), 0, 9)

print("\n\n" + "#"*70)
print("# EXAMPLE 2: Round 2 from the quiz")
print("#"*70)
A2 = [1, 2, 7, 5, 4, 6, 3, 10, 9, 8]  # State before pivot swap
print("\nBefore final swap (pointers already crossed):")
j2, result2 = trace_with_explanation(A2.copy(), 2, 9)

print("\n\n" + "="*70)
print("KEY TAKEAWAY:")
print("="*70)
print("After pointers cross, we ALWAYS swap the pivot with A[j] because:")
print("  1. j is the rightmost position of elements <= pivot")
print("  2. A[j] <= pivot (by definition)")
print("  3. This places the pivot in its correct sorted position")
print("  4. Maintains partition: left side < pivot < right side")
print("="*70)
