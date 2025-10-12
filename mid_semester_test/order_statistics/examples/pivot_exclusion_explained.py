"""
Understanding What Gets Excluded After Partitioning
"""

print("="*70)
print("WHAT DO WE EXCLUDE AFTER PARTITIONING?")
print("="*70)
print()
print("Key concept: We exclude the INDEX where the pivot landed,")
print("             not the VALUE of the pivot itself!")
print()
print("="*70)

print("\n\n" + "#"*70)
print("# ROUND 1 DETAILED ANALYSIS")
print("#"*70)

print("\nBEFORE partitioning:")
A_before = [2,3,7,8,4,9,1,10,6,5]
print(f"  Array: {A_before}")
print(f"  Indices: 0  1  2  3  4  5  6  7  8  9")
print(f"  Search range: [0, 9]")
print(f"  Pivot: A[0] = 2")

print("\nAFTER partitioning:")
A_after = [1, 2, 7, 8, 4, 9, 3, 10, 6, 5]
print(f"  Array: {A_after}")
print(f"  Indices: 0  1  2  3  4  5  6  7  8  9")
print(f"             ^")
print(f"         pivot at index 1")

print("\nPartition result: j = 1")
print(f"  - The value 2 is now at INDEX 1 (its final sorted position)")
print(f"  - We exclude INDEX 1 from future searches")
print(f"  - Why? Because it's already in the correct position!")

print("\nTarget: k = 3")
print(f"  Since j=1 < k=3, search RIGHT of the pivot")

print("\nNew search range calculation:")
print(f"  - Start: j+1 = 1+1 = 2 (exclude index 1 where pivot landed)")
print(f"  - End: 9 (unchanged)")
print(f"  - New range: [2, 9]")

print("\nWhat's in the new range?")
print(f"  Indices: 2  3  4  5  6  7  8  9")
print(f"  Values:  7  8  4  9  3 10  6  5")
print(f"           ^")
print(f"      Next pivot = A[2] = 7 (first element of new range)")

print("\n" + "="*70)
print("IMPORTANT DISTINCTION:")
print("="*70)
print("  We exclude: INDEX 1 (the position where pivot ended up)")
print("  NOT excluding: All elements with value 2")
print()
print("  If there were another element with value 2 elsewhere in")
print("  the array, it would still be in the search range!")
print("="*70)

print("\n\n" + "#"*70)
print("# ROUND 2 DETAILED ANALYSIS")
print("#"*70)

print("\nBEFORE partitioning:")
print(f"  Array: {A_after}")
print(f"  Indices: 0  1  2  3  4  5  6  7  8  9")
print(f"  Search range: [2, 9]")
print(f"  Pivot: A[2] = 7")

print("\nAFTER partitioning:")
A_after_2 = [1, 2, 3, 5, 4, 6, 7, 10, 9, 8]
print(f"  Array: {A_after_2}")
print(f"  Indices: 0  1  2  3  4  5  6  7  8  9")
print(f"                      ^")
print(f"                 pivot at index 6")

print("\nPartition result: j = 6")
print(f"  - The value 7 is now at INDEX 6 (its final sorted position)")
print(f"  - We exclude INDEX 6 from future searches")

print("\nTarget: k = 3")
print(f"  Since j=6 > k=3, search LEFT of the pivot")

print("\nNew search range calculation:")
print(f"  - Start: 2 (unchanged from previous lo)")
print(f"  - End: j-1 = 6-1 = 5 (exclude index 6 where pivot landed)")
print(f"  - New range: [2, 5]")

print("\nWhat's in the new range?")
print(f"  Indices: 2  3  4  5")
print(f"  Values:  3  5  4  6")
print(f"           ^")
print(f"      Next pivot = A[2] = 3 (first element of new range)")

print("\n" + "="*70)
print("PATTERN:")
print("="*70)
print("After each partition at index j:")
print("  1. Pivot value is now at INDEX j (final position)")
print("  2. INDEX j is excluded from further searches")
print("  3. If j < k: new range is [j+1, hi]")
print("  4. If j > k: new range is [lo, j-1]")
print("  5. Next pivot is ALWAYS first element (leftmost) of new range")
print("="*70)

print("\n\n" + "#"*70)
print("# VISUAL SUMMARY")
print("#"*70)

print("\nRound 1:")
print("  [2, 3, 7, 8, 4, 9, 1, 10, 6, 5]  ← start")
print("   ^pivot")
print()
print("  [1, 2, 7, 8, 4, 9, 3, 10, 6, 5]  ← after partition")
print("      ^exclude this index (1)")
print("         ^new pivot (index 2)")
print("         [-----search here-----]")

print("\nRound 2:")
print("  [1, 2, 7, 8, 4, 9, 3, 10, 6, 5]  ← start")
print("         ^pivot")
print()
print("  [1, 2, 3, 5, 4, 6, 7, 10, 9, 8]  ← after partition")
print("                  ^exclude this index (6)")
print("         ^new pivot (index 2)")
print("         [------]  search here")

print("\n" + "="*70)
print("ANSWER TO YOUR QUESTION:")
print("="*70)
print("In Round 1:")
print("  - We exclude INDEX 1 (where value 2 ended up)")
print("  - The remaining range starts from INDEX 2 onwards")
print("  - YES, we exclude the position of the pivot value 2")
print("  - But we're excluding the INDEX, not the VALUE")
print("="*70)
