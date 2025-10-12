"""
Understanding Pointer Crossing and Next Pivot Selection in QuickSelect
"""

def visualize_pointer_crossing():
    """
    Shows how pointers cross and what that means
    """
    print("="*70)
    print("UNDERSTANDING POINTER CROSSING")
    print("="*70)
    print()
    print("Initial setup:")
    print("  i starts at lo+1 (left side, after pivot)")
    print("  j starts at hi (right side, end of array)")
    print()
    print("During scanning:")
    print("  i moves RIGHT →→→ (looking for elements >= pivot)")
    print("  j moves LEFT ←←← (looking for elements <= pivot)")
    print()
    print("When they CROSS:")
    print("  - i has moved past j")
    print("  - Now: j is to the LEFT of i")
    print("  - Condition: i >= j or equivalently j < i")
    print()
    print("Visual representation:")
    print()
    print("  Before crossing:    [pivot | ... | j | i | ... ]")
    print("                                    ←j   i→")
    print()
    print("  After crossing:     [pivot | ... | j,i | ... ]")
    print("                                    ←j i→")
    print("                       OR")
    print("                       [pivot | ... | j | i | ... ]")
    print("                                      ←j i→")
    print()
    print("  j is now to the LEFT of i!")
    print("="*70)


def explain_pivot_selection():
    """
    Explains how next pivot is chosen
    """
    print("\n\n" + "="*70)
    print("PIVOT SELECTION FOR NEXT ROUND")
    print("="*70)
    print()
    print("Rule: The pivot is ALWAYS the FIRST element of the subarray")
    print()
    print("After partitioning at position j:")
    print("  - Pivot is now at index j (in its correct position)")
    print("  - Compare j with target k")
    print()
    print("Case 1: j < k (target is to the RIGHT)")
    print("  → Search range: [j+1, hi]")
    print("  → New pivot: A[j+1] (first element of right subarray)")
    print()
    print("Case 2: j > k (target is to the LEFT)")
    print("  → Search range: [lo, j-1]")
    print("  → New pivot: A[lo] (first element of left subarray)")
    print()
    print("Case 3: j == k (FOUND!)")
    print("  → No more searching needed")
    print("="*70)


def trace_with_pivot_selection():
    """
    Trace the quiz example showing pivot selection
    """
    print("\n\n" + "#"*70)
    print("# QUIZ EXAMPLE: Tracing Pivot Selection")
    print("#"*70)

    A = [2,3,7,8,4,9,1,10,6,5]
    k = 3

    print(f"\nOriginal array: {A}")
    print(f"Target: k={k} (4th order statistic)")

    # Round 1
    print("\n" + "="*70)
    print("ROUND 1:")
    print("="*70)
    print(f"Search range: [0, 9]")
    print(f"Pivot: A[0] = {A[0]} (first element of subarray)")
    print(f"\nAfter partitioning:")
    print("  - Pointers cross at: i=2, j=1")
    print("  - j is to the LEFT of i ✓")
    print("  - Swap pivot with A[j]: A[0]↔A[1]")
    A = [1, 2, 7, 8, 4, 9, 3, 10, 6, 5]
    print(f"  - Array: {A}")
    print(f"  - Pivot 2 is now at index j=1")
    print(f"\nDecision: j=1 < k=3, so search RIGHT")
    print(f"  New range: [2, 9]")
    print(f"  Next pivot will be: A[2] = {A[2]} ← first element of new range")

    # Round 2
    print("\n" + "="*70)
    print("ROUND 2:")
    print("="*70)
    print(f"Search range: [2, 9]")
    print(f"Pivot: A[2] = {A[2]} (first element of subarray)")
    print(f"\nAfter partitioning:")
    print("  - Pointers cross at: i=7, j=6")
    print("  - j is to the LEFT of i ✓")
    print("  - Swap pivot with A[j]: A[2]↔A[6]")
    A = [1, 2, 3, 5, 4, 6, 7, 10, 9, 8]
    print(f"  - Array: {A}")
    print(f"  - Pivot 7 is now at index j=6")
    print(f"\nDecision: j=6 > k=3, so search LEFT")
    print(f"  New range: [2, 5]")
    print(f"  Next pivot would be: A[2] = {A[2]} ← first element of new range")

    print("\n" + "="*70)
    print("KEY INSIGHTS:")
    print("="*70)
    print("1. When pointers cross: j < i (j is to the left)")
    print("2. We swap pivot with A[j]")
    print("3. Next pivot is ALWAYS the first element of the new search range")
    print("4. Search range excludes the pivot we just placed (it's in final position)")
    print("="*70)


def detailed_crossing_example():
    """
    Show detailed pointer movements until crossing
    """
    print("\n\n" + "#"*70)
    print("# DETAILED EXAMPLE: Round 1 Pointer Movements")
    print("#"*70)

    A = [2, 3, 7, 8, 4, 9, 1, 10, 6, 5]
    pivot = 2

    print(f"\nArray: {A}")
    print(f"Pivot: {pivot} (at index 0)")
    print(f"\nInitial: i=1, j=9")
    print()

    print("Iteration 1:")
    print("  i=1: A[1]=3 >= 2, STOP")
    print("  j=9,8,7,6: scanning left... A[6]=1 <= 2, STOP")
    print("  i=1 < j=6, so swap A[1]↔A[6]")
    A = [2, 1, 7, 8, 4, 9, 3, 10, 6, 5]
    print(f"  Array: {A}")
    print("  Move pointers: i=2, j=5")
    print()

    print("Iteration 2:")
    print("  i=2: A[2]=7 >= 2, STOP")
    print("  j=5,4,3,2,1: scanning left... all > 2, goes to j=1")
    print("  Now: i=2, j=1")
    print("  i >= j (2 >= 1) → POINTERS CROSSED! ✓")
    print()
    print("  Visual:")
    print("  Index:  0   1   2   3   4   5   6   7   8   9")
    print(f"  Array: {A}")
    print("         ^   j   i")
    print("       pivot")
    print()
    print("  j is at index 1, i is at index 2")
    print("  j < i, so j is to the LEFT ✓")
    print()
    print("  Swap pivot A[0]=2 with A[1]=1")
    A[0], A[1] = A[1], A[0]
    print(f"  Final: {A}")


# Run all explanations
visualize_pointer_crossing()
explain_pivot_selection()
trace_with_pivot_selection()
detailed_crossing_example()

print("\n\n" + "="*70)
print("SUMMARY:")
print("="*70)
print("Q1: When pointers cross, is j to the left of i?")
print("A1: YES! When i >= j, that means j < i (j is to the left)")
print()
print("Q2: How do we choose the next pivot?")
print("A2: Always the FIRST element of the new search range")
print("    - If j < k: new range is [j+1, hi], pivot is A[j+1]")
print("    - If j > k: new range is [lo, j-1], pivot is A[lo]")
print("="*70)
