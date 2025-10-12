"""
QuickSelect with Hoare's Partition - Interactive Tracer
Use this to trace through any QuickSelect problem step-by-step

Usage:
    python3 quickselect_tracer.py

Modify the PROBLEM SETUP section below with your array, k value, and number of rounds.
"""

def hoare_partition_trace(A, lo, hi, round_num):
    """
    Traces one round of Hoare's partition with detailed output
    """
    pivot = A[lo]
    i = lo + 1
    j = hi

    print(f"\n{'='*70}")
    print(f"ROUND {round_num} - PARTITIONING")
    print(f"{'='*70}")
    print(f"Range: [{lo}, {hi}]")
    print(f"Pivot: A[{lo}] = {pivot}")
    print(f"Array: {A}")
    print(f"Index:  {' '.join(f'{idx:2}' for idx in range(len(A)))}")
    print(f"\nInitial pointers: i={i} (after pivot), j={j}")

    iteration = 0
    while i <= j:
        iteration += 1
        print(f"\n--- Iteration {iteration} ---")

        # Move i right
        print(f"Moving i right (while A[i] < {pivot}):")
        while i <= j and A[i] < pivot:
            print(f"  i={i}: A[{i}]={A[i]} < {pivot}, continue...")
            i += 1
        if i <= j:
            print(f"  i={i}: A[{i}]={A[i]} >= {pivot}, STOP")

        # Move j left
        print(f"Moving j left (while A[j] > {pivot}):")
        while i <= j and A[j] > pivot:
            print(f"  j={j}: A[{j}]={A[j]} > {pivot}, continue...")
            j -= 1
        if i <= j:
            print(f"  j={j}: A[{j}]={A[j]} <= {pivot}, STOP")

        # Check if crossed
        if i < j:
            print(f"\ni < j ({i} < {j}), so SWAP A[{i}]={A[i]} ↔ A[{j}]={A[j]}")
            A[i], A[j] = A[j], A[i]
            print(f"Array: {A}")
            i += 1
            j -= 1
            print(f"Move pointers: i={i}, j={j}")
        else:
            print(f"\ni >= j ({i} >= {j}), POINTERS CROSSED!")
            break

    # Final pivot swap
    print(f"\n{'*'*70}")
    print(f"FINAL PIVOT SWAP:")
    print(f"Swap pivot A[{lo}]={A[lo]} with A[{j}]={A[j]}")
    A[lo], A[j] = A[j], A[lo]
    print(f"Array: {A}")
    print(f"Index:  {' '.join(f'{idx:2}' for idx in range(len(A)))}")
    print(f"\nPivot {pivot} is now at index j={j}")
    print(f"Elements at indices {lo} to {j-1}: all < {pivot}")
    print(f"Element at index {j}: {pivot} (in final position)")
    print(f"Elements at indices {j+1} to {hi}: all > {pivot}")
    print(f"{'*'*70}")

    return j


def quickselect_n_rounds(A, k, max_rounds):
    """
    Performs QuickSelect for max_rounds (or until found)
    """
    A = A.copy()  # Work on a copy
    lo, hi = 0, len(A) - 1
    round_num = 0

    print("="*70)
    print("QUICKSELECT TRACER")
    print("="*70)
    print(f"Original array: {A}")
    print(f"Target: {k+1}th order statistic (index k={k})")
    print(f"Sorted array would be: {sorted(A)}")
    print(f"Looking for value: {sorted(A)[k]}")
    print(f"Maximum rounds: {max_rounds}")

    while round_num < max_rounds:
        round_num += 1
        j = hoare_partition_trace(A, lo, hi, round_num)

        print(f"\n{'='*70}")
        print(f"END OF ROUND {round_num}")
        print(f"{'='*70}")
        print(f"Current array: {A}")
        print(f"Partition index j={j}, target k={k}")

        if j == k:
            print(f"\n🎉 FOUND! j == k ({j} == {k})")
            print(f"The {k+1}th order statistic is {A[k]}")
            return A, j, True
        elif j < k:
            print(f"\nj < k ({j} < {k}), search RIGHT")
            print(f"New range: [{j+1}, {hi}]")
            print(f"Next pivot will be: A[{j+1}] = {A[j+1]}")
            lo = j + 1
        else:
            print(f"\nj > k ({j} > {k}), search LEFT")
            print(f"New range: [{lo}, {j-1}]")
            print(f"Next pivot will be: A[{lo}] = {A[lo]}")
            hi = j - 1

        if round_num < max_rounds:
            input("\nPress Enter to continue to next round...")

    return A, None, False


def verify_options(A, options):
    """
    Verifies answer options against the final array
    """
    print("\n" + "="*70)
    print("VERIFYING ANSWER OPTIONS")
    print("="*70)
    print(f"Final array: {A}")
    print(f"Index:       {' '.join(f'{idx:2}' for idx in range(len(A)))}")
    print()

    for label, (idx, expected) in options.items():
        actual = A[idx]
        is_correct = (actual == expected)
        symbol = "✓" if is_correct else "✗"
        status = "TRUE" if is_correct else "FALSE"
        print(f"{label}. A[{idx}]={expected}? → A[{idx}]={actual} {symbol} {status}")


# =============================================================================
# PROBLEM SETUP - MODIFY THESE VALUES FOR YOUR PROBLEM
# =============================================================================

# The quiz problem
ARRAY = [2, 3, 7, 8, 4, 9, 1, 10, 6, 5]
K = 3  # 4th order statistic (0-indexed)
MAX_ROUNDS = 2  # Stop after this many rounds

# Answer options to check (format: 'label': (index, expected_value))
OPTIONS = {
    'a': (3, 5),   # A[3]=5?
    'b': (8, 6),   # A[8]=6?
    'c': (9, 8),   # A[9]=8?
    'd': (0, 2),   # A[0]=2?
    'e': (4, 4),   # A[4]=4?
    'f': (5, 7),   # A[5]=7?
}

# =============================================================================
# RUN THE TRACER
# =============================================================================

if __name__ == "__main__":
    final_array, partition_idx, found = quickselect_n_rounds(ARRAY, K, MAX_ROUNDS)

    print("\n\n" + "#"*70)
    print("# FINAL RESULTS")
    print("#"*70)
    print(f"\nArray after {MAX_ROUNDS} rounds: {final_array}")

    if found:
        print(f"Element found at index {partition_idx}: {final_array[partition_idx]}")
    else:
        print(f"Stopped after {MAX_ROUNDS} rounds (not yet found)")

    if OPTIONS:
        verify_options(final_array, OPTIONS)

    print("\n" + "="*70)
    print("TRACE COMPLETE")
    print("="*70)
