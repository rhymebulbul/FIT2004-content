"""
Understanding Unsorted Elements After Partitioning

Key Question: What about elements between the pivot's original position
and where it gets swapped to? Are they sorted?
"""

print("="*70)
print("PARTITION DOES NOT FULLY SORT!")
print("="*70)
print()
print("Key Insight:")
print("  Partitioning only guarantees a RELATIVE ordering around the pivot:")
print("  - Elements LEFT of pivot are <= pivot")
print("  - Elements RIGHT of pivot are >= pivot")
print("  - But elements on EACH SIDE are NOT necessarily sorted!")
print("="*70)

print("\n\n" + "#"*70)
print("# ROUND 1 ANALYSIS: What's really happening?")
print("#"*70)

print("\nBEFORE partitioning:")
A_before = [2, 3, 7, 8, 4, 9, 1, 10, 6, 5]
print(f"  Array: {A_before}")
print(f"  Index:  0  1  2  3  4  5  6  7  8  9")
print(f"  Pivot: A[0] = 2")

print("\nDuring partitioning:")
print("  - i starts at 1, j starts at 9")
print("  - i=1 stops at A[1]=3 (>= 2)")
print("  - j=6 stops at A[6]=1 (<= 2)")
print("  - Swap A[1] and A[6]: [2, 1, 7, 8, 4, 9, 3, 10, 6, 5]")
print("  - Pointers cross: i=2, j=1")

print("\nBEFORE final pivot swap:")
A_mid = [2, 1, 7, 8, 4, 9, 3, 10, 6, 5]
print(f"  Array: {A_mid}")
print(f"  Index:  0  1  2  3  4  5  6  7  8  9")
print(f"          ^  ^")
print(f"       pivot j")

print("\nWhat do we know at this point?")
print("  - Elements from index 1 to 1 (just A[1]=1) are <= 2 ✓")
print("  - Elements from index 2 to 9 are >= 2 ✓")
print("  - A[1]=1 is <= pivot (safe to swap)")

print("\nFinal pivot swap: A[0] ↔ A[1]")
A_after = [1, 2, 7, 8, 4, 9, 3, 10, 6, 5]
print(f"  Array: {A_after}")
print(f"  Index:  0  1  2  3  4  5  6  7  8  9")

print("\nAfter swap, what do we have?")
print("  LEFT side (indices 0 to 0): [1]")
print("    → All elements <= 2? YES (1 <= 2)")
print("    → Are they sorted? YES (only one element)")
print()
print("  PIVOT at index 1: 2")
print()
print("  RIGHT side (indices 2 to 9): [7, 8, 4, 9, 3, 10, 6, 5]")
print("    → All elements >= 2? YES")
print("    → Are they sorted? NO! (7, 8, 4... not in order)")
print()
print("  ⚠️  The RIGHT side is NOT sorted, but that's OK!")

print("\n" + "="*70)
print("IN ROUND 1: There are no unsorted elements BETWEEN pivot and j")
print("because j=1 is adjacent to pivot at index 0!")
print("="*70)

print("\n\n" + "#"*70)
print("# EXAMPLE WITH LARGER GAP: What if j was farther away?")
print("#"*70)

print("\nLet's create a different example where j is NOT adjacent to pivot:")
print()

# Custom example
A_custom = [5, 2, 8, 9, 7, 3, 1, 10, 6, 4]
print("Example array: [5, 2, 8, 9, 7, 3, 1, 10, 6, 4]")
print("Index:          0  1  2  3  4  5  6  7  8  9")
print("Pivot: A[0] = 5")
print()

print("After Hoare's partition (simulated):")
print("  - Scan from left: find elements >= 5")
print("  - Scan from right: find elements <= 5")
print("  - Swap them")
print("  - Eventually pointers cross, say at i=5, j=4")
print()

A_example = [3, 2, 4, 1, 5, 7, 8, 10, 6, 9]
print("Array might look like:")
print(f"  {A_example}")
print("  Index: 0  1  2  3  4  5  6  7  8  9")
print("                    ^")
print("                    j=4")
print()

print("BEFORE final pivot swap (pivot still at index 0):")
print("  Elements at indices 1-4: [2, 4, 1, 5]")
print("  Are they <= pivot 5? Let's check:")
print("    2 <= 5? YES")
print("    4 <= 5? YES")
print("    1 <= 5? YES")
print("    5 <= 5? YES")
print("  Are they SORTED? NO! [2, 4, 1, 5] is not sorted")
print()
print("  ⚠️  Elements between pivot and j are NOT sorted!")
print("  ✓  But they ARE all <= pivot")

print("\nAFTER swapping pivot with j:")
print("  Swap A[0]=5 with A[4]=5: (happens to be same value)")
print("  Now indices 0-3 contain: [3, 2, 4, 1]")
print("  Are these sorted? NO!")
print("  Are they all < 5? YES!")

print("\n" + "="*70)
print("KEY UNDERSTANDING:")
print("="*70)
print("1. Partitioning creates two UNSORTED regions:")
print("   - Left: elements <= pivot (but not sorted among themselves)")
print("   - Right: elements >= pivot (but not sorted among themselves)")
print()
print("2. Elements between the original pivot position and j:")
print("   - Are GUARANTEED to be <= pivot")
print("   - Are NOT guaranteed to be sorted")
print()
print("3. This is fine because:")
print("   - QuickSelect recursively searches within one region")
print("   - It will partition that region again")
print("   - Eventually finding the kth element")
print("="*70)

print("\n\n" + "#"*70)
print("# BACK TO THE QUIZ: Round 1 Detailed")
print("#"*70)

A_before = [2, 3, 7, 8, 4, 9, 1, 10, 6, 5]
print(f"\nBefore: {A_before}")
print("Index:   0  1  2  3  4  5  6  7  8  9")

print("\nPartition invariants DURING scanning:")
print("  - We maintain: scanned left portion has elements <= pivot")
print("  - We maintain: scanned right portion has elements >= pivot")

print("\nAfter swap A[1]↔A[6]:")
A_during = [2, 1, 7, 8, 4, 9, 3, 10, 6, 5]
print(f"  {A_during}")
print("  Index: 0  1  2  3  4  5  6  7  8  9")
print()
print("  Check elements from index 1 to j=1:")
print("    A[1]=1 <= 2? YES ✓")
print()
print("  Check elements from index 2 to 9:")
print("    All >= 2? Let's see: [7,8,4,9,3,10,6,5]")
print("    7>=2?YES, 8>=2?YES, 4>=2?YES, 9>=2?YES,")
print("    3>=2?YES, 10>=2?YES, 6>=2?YES, 5>=2?YES ✓")

print("\nFinal swap pivot with j:")
A_after = [1, 2, 7, 8, 4, 9, 3, 10, 6, 5]
print(f"  {A_after}")
print("  Index: 0  1  2  3  4  5  6  7  8  9")

print("\nIn this specific case:")
print("  - There's only ONE element to the left of pivot (index 0)")
print("  - So there are NO elements 'between' pivot and j")
print("  - j=1 is immediately adjacent to the pivot position!")

print("\n" + "="*70)
print("ANSWER TO YOUR QUESTION:")
print("="*70)
print("Q: What if there were unsorted elements between the swapped")
print("   element (at j) and the pivot?")
print()
print("A: They would be UNSORTED, and that's PERFECTLY FINE!")
print("   - Partition only guarantees they're <= pivot")
print("   - It doesn't sort them")
print("   - In Round 1, j=1 is adjacent to pivot at 0, so no gap anyway")
print("   - If there was a gap, those elements would be <= pivot")
print("     but not necessarily sorted")
print("="*70)
