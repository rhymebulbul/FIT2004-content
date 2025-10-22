# K-Partitioning: Comprehensive Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Problem Definition](#problem-definition)
3. [Understanding K-Partitioning vs Sorting](#understanding-k-partitioning-vs-sorting)
4. [Solution 1: O(nk) Sequential Approach](#solution-1-onk-sequential-approach)
5. [Solution 2: O(n log k) Divide-and-Conquer](#solution-2-on-log-k-divide-and-conquer)
6. [Lower Bound: Why We Can't Do Better](#lower-bound-why-we-cant-do-better)
7. [Practical Applications](#practical-applications)
8. [Complete Examples](#complete-examples)

---

## Introduction

K-partitioning is a generalization of the standard partitioning subroutine used in Quicksort. While standard partitioning uses one pivot to split an array into two regions, k-partitioning uses k pivots to split an array into k+1 regions.

**Key Insight**: K-partitioning is fundamentally different from sorting. It only guarantees that elements are in the correct regions relative to pivots, but does NOT sort elements within those regions.

---

## Problem Definition

### Standard Quicksort Partitioning (1 pivot)

**Input**:
- An array of n elements
- One pivot element p

**Output**:
- Array rearranged so all elements ≤ p come before all elements > p
- Creates **2 regions**

**Example**:
```
Input:  [3, 7, 1, 9, 2, 5], pivot = 5

Output: [3, 1, 2, 5] | [7, 9]
           ≤ 5       |  > 5
        (Region 1)   | (Region 2)
```

### K-Partitioning (k pivots)

**Input**:
- An array of n elements
- k pivot elements p₁, p₂, ..., pₖ (not necessarily sorted)

**Output**:
- Array rearranged into **k+1 regions**:
  - Region 1: all elements ≤ p₁
  - Region 2: all elements > p₁ and ≤ p₂
  - Region 3: all elements > p₂ and ≤ p₃
  - ...
  - Region k+1: all elements > pₖ

**Example**:
```
Input:  [3, 7, 1, 9, 2, 5], pivots = [7, 3]

Step 1: Sort pivots → [3, 7]

Step 2: K-partition:
Output: [3, 1, 2] | [7, 5] | [9]
           ≤ 3    | ≤7, >3 | >7
       (Region 1) |(Region 2)|(Region 3)
```

### Visual Pattern: k pivots → k+1 regions

```
k = 1:  | ≤p₁ | >p₁ |                                    (2 regions)

k = 2:  | ≤p₁ | >p₁, ≤p₂ | >p₂ |                        (3 regions)

k = 3:  | ≤p₁ | >p₁, ≤p₂ | >p₂, ≤p₃ | >p₃ |            (4 regions)

k = n:  | ≤p₁ | >p₁, ≤p₂ | ... | >pₙ₋₁, ≤pₙ | >pₙ |   (n+1 regions)
```

---

## Understanding K-Partitioning vs Sorting

### Critical Distinction: Pivots vs Array Elements

**STEP 1: Sort ONLY the k pivots** (NOT the array)

The pivots themselves need to be sorted to determine the order of regions, but this does NOT affect the array elements yet.

```
Array:  [3, 7, 1, 9, 2, 5, 8, 4, 6]  ← Still unsorted
Pivots: [7, 3]                        ← Unsorted

After sorting ONLY pivots:
Array:  [3, 7, 1, 9, 2, 5, 8, 4, 6]  ← Still unchanged!
Pivots: [3, 7]                        ← Now sorted
```

**STEP 2: Partition the array into regions**

Now we rearrange array elements based on the sorted pivots.

### K-Partitioning Result (NOT fully sorted)

```
After k-partitioning with pivots [3, 7]:

[3, 1, 2] | [7, 5, 4, 6] | [9, 8]
   ≤ 3    |  >3 and ≤7   |  > 7

✓ Elements are in correct REGIONS
✗ Within each region, elements are NOT sorted
```

**Observations**:
- Region 1: `[3, 1, 2]` - NOT sorted (correct order would be `[1, 2, 3]`)
- Region 2: `[7, 5, 4, 6]` - NOT sorted (correct order would be `[4, 5, 6, 7]`)
- Region 3: `[9, 8]` - NOT sorted (correct order would be `[8, 9]`)

### Full Sorting Result

```
After full sorting:

[1, 2, 3] | [4, 5, 6, 7] | [8, 9]
   ≤ 3    |  >3 and ≤7   |  > 7

✓ Elements are in correct REGIONS
✓ Within each region, elements ARE sorted
```

### Comparison Table

| Property | K-Partitioning | Full Sorting |
|----------|---------------|--------------|
| Regions separated correctly | ✓ | ✓ |
| Elements within regions sorted | ✗ | ✓ |
| Time Complexity | O(n log k) | O(n log n) |
| Work Required | Less | More |

### Why This Matters: Complexity Savings

When k << n (k is much smaller than n), k-partitioning is significantly faster:

**Example with n = 1,000,000 elements:**
- **k = 10 pivots**:
  - K-partitioning: O(n log k) = O(1,000,000 × 3.3) ≈ 3.3 million operations
  - Full sorting: O(n log n) = O(1,000,000 × 20) ≈ 20 million operations
  - **Speedup: ~6x faster**

- **k = 100 pivots**:
  - K-partitioning: O(n log k) = O(1,000,000 × 6.6) ≈ 6.6 million operations
  - Full sorting: O(n log n) ≈ 20 million operations
  - **Speedup: ~3x faster**

---

## Solution 1: O(nk) Sequential Approach

### Algorithm Description

The simplest approach applies 2-way partitioning sequentially, k times:

1. Sort the k pivots: O(k log k)
2. Partition entire array around p₁
3. Partition the right portion around p₂
4. Partition the right-right portion around p₃
5. Continue for all k pivots

### Pseudocode

```
function K_PARTITION(a[1..n], p[1..k]):
    // Step 1: Sort the pivots
    sort(p[1..k])                           // O(k log k)

    // Step 2: Sequential partitioning
    j = 1                                    // Start index
    for i = 1 to k:
        // Partition subarray a[j..n] using pivot p[i]
        j = partition(a[j..n], p[i]) + 1    // O(n) worst case

    // Note: partition() is the standard 2-way partition function
    // that returns the final position of the pivot
```

### Step-by-Step Example

**Input**: Array `[9, 2, 7, 4, 1, 8, 3, 6, 5]`, Pivots `[3, 7]`

**Step 1**: Sort pivots → `[3, 7]`

**Step 2**: Partition around p₁ = 3
```
Initial:  [9, 2, 7, 4, 1, 8, 3, 6, 5]
          ↑ (j = 1, scan entire array)

After:    [2, 1, 3] | [9, 7, 4, 8, 6, 5]
                   ↑
                  j = 4 (start of right portion)
```

**Step 3**: Partition a[4..9] around p₂ = 7
```
Before:   [2, 1, 3] | [9, 7, 4, 8, 6, 5]
                      ↑ (j = 4, scan from here)

After:    [2, 1, 3] | [7, 4, 6, 5] | [9, 8]
                                   ↑
                                  j = 8
```

**Final Result**: `[2, 1, 3] | [7, 4, 6, 5] | [9, 8]`

### Complexity Analysis

**Time Complexity**: O(nk + k log k) = O(nk)

Breaking it down:
- **Sorting pivots**: O(k log k)
- **Partition 1**: O(n) - scan entire array
- **Partition 2**: O(n) worst case - might scan n-1 elements
- **Partition 3**: O(n) worst case - might scan n-2 elements
- ...
- **Partition k**: O(n) worst case

**Worst case**: Each partition scans nearly the entire array
- Total partition cost: k × O(n) = O(nk)
- Total: O(k log k) + O(nk) = O(nk) (since n ≥ k)

**Space Complexity**: O(1) auxiliary space (in-place partitioning)

### Why This is Inefficient

The problem is that we're potentially doing O(n) work k times sequentially. Even though each partition works on a smaller portion, in the worst case (when all elements are greater than all pivots), we scan almost the entire array k times.

---

## Solution 2: O(n log k) Divide-and-Conquer

### Key Insight

Instead of partitioning sequentially, use a **divide-and-conquer** strategy on the pivots themselves:
- Partition by the **middle pivot**
- Recursively k-partition the left half with the left pivots
- Recursively k-partition the right half with the right pivots

This creates a **binary tree structure** with depth log k, where each level does O(n) total work.

### Pseudocode

```
function K_PARTITION(a[1..n], p[1..k]):
    // Base case
    if k == 0 or n == 0:
        return

    // Find middle pivot
    mid = k / 2

    // Partition around middle pivot
    j = partition(a[1..n], p[mid])          // O(n)

    // Recursively partition left and right
    K_PARTITION(a[1..j-1], p[1..mid-1])     // Left half, left pivots
    K_PARTITION(a[j+1..n], p[mid+1..k])     // Right half, right pivots

// Note: Assumes pivots are sorted before first call
// Initial call: sort(p), then K_PARTITION(a, p)
```

### Recursion Tree Example

**Input**: Array of size n, Pivots `[2, 4, 6, 8]` (k=4, already sorted)

```
Level 0:  Partition entire array (size n) around p[2] = 4
          |
          +-- Array split into [≤4] and [>4]
          |
          Work: O(n)

Level 1:  Partition [≤4] around p[1]=2  +  Partition [>4] around p[3]=6
          |                                  |
          +-- [≤2] and [≤4]                 +-- [≤6] and [>6]
          |
          Work: O(left_size) + O(right_size) = O(n) total

Level 2:  Partition [>6] around p[4]=8
          |
          +-- [≤8] and [>8]
          |
          Work: O(right_size) ≤ O(n)

Final: [≤2] | [≤4] | [≤6] | [≤8] | [>8]
```

### Detailed Walk-through

**Setup**: Array `[9, 2, 7, 4, 1, 8, 3, 6, 5]`, Pivots `[2, 4, 6, 8]` (sorted)

#### Level 0 (mid = 2, pivot = 4)
```
Partition around 4:

[9, 2, 7, 4, 1, 8, 3, 6, 5]
             ↓
[2, 4, 1, 3] | [9, 7, 8, 6, 5]
    ≤ 4      |      > 4

Left subarray: [2, 4, 1, 3], Left pivots: [2]
Right subarray: [9, 7, 8, 6, 5], Right pivots: [6, 8]
```

#### Level 1 Left (mid = 0, pivot = 2)
```
Partition [2, 4, 1, 3] around 2:

[2, 4, 1, 3]
 ↓
[2, 1] | [4, 3]
  ≤ 2  |  > 2

No more pivots for further partitioning
```

#### Level 1 Right (mid = 0, pivot = 6)
```
Partition [9, 7, 8, 6, 5] around 6:

[9, 7, 8, 6, 5]
          ↓
[6, 5] | [9, 7, 8]
 ≤ 6   |   > 6

Right subarray: [9, 7, 8], Right pivots: [8]
```

#### Level 2 Right-Right (mid = 0, pivot = 8)
```
Partition [9, 7, 8] around 8:

[9, 7, 8]
       ↓
[7, 8] | [9]
 ≤ 8   | > 8
```

#### Final Result
```
[2, 1] | [4, 3] | [6, 5] | [7, 8] | [9]
  ≤ 2  |  ≤ 4   |  ≤ 6   |  ≤ 8   | > 8
```

### Complexity Analysis

**Recursion Depth**: O(log k)
- Each recursive level divides k by 2
- Depth = ⌈log₂ k⌉

**Work Per Level**: O(n)
- Level 0: Partition entire array once → O(n)
- Level 1: Partition left portion + right portion = O(n) total
  - Even though we partition two smaller pieces, their sizes sum to n
- Level 2: Partition up to 4 pieces, but total size ≤ n
- **Key insight**: At each level, we touch each array element at most once

**Proof of O(n) work per level**:
```
Level i: Partition 2^i subarrays, but their total size = n
         Work = O(n₁ + n₂ + ... + n₂ᵢ) where Σnⱼ ≤ n
         Therefore, work = O(n)
```

**Total Time Complexity**:
- Sorting pivots: O(k log k)
- Partitioning: O(n) × O(log k) = O(n log k)
- **Total**: O(k log k + n log k) = **O(n log k)** (since k ≤ n)

**Space Complexity**:
- O(log k) for recursion stack
- O(1) auxiliary space for partitioning

### Comparison: Sequential vs Divide-and-Conquer

| Aspect | Sequential O(nk) | Divide-and-Conquer O(n log k) |
|--------|------------------|-------------------------------|
| Approach | Partition k times sequentially | Binary recursion on pivots |
| Tree depth | k levels | log k levels |
| Work per level | O(n) | O(n) |
| Total work | k × O(n) = O(nk) | log k × O(n) = O(n log k) |
| When better | Never (always worse or equal) | Always (when k > 1) |

**Example savings**:
- k = 100, n = 10,000
  - Sequential: 100 × 10,000 = 1,000,000 operations
  - D&C: 6.6 × 10,000 ≈ 66,000 operations
  - **~15x speedup**

---

## Lower Bound: Why We Can't Do Better

### The Argument

**Claim**: We cannot do k-partitioning faster than O(n log k) in the comparison model.

**Proof by Reduction to Sorting**:

Consider the **special case where k = n** (use all n elements as pivots).

#### What happens when k = n?

Given array `[5, 2, 8, 1, 9]` and pivots `[1, 2, 5, 8, 9]` (all elements):

After k-partitioning with k = n:
```
[1] | [2] | [5] | [8] | [9]
≤1  | ≤2  | ≤5  | ≤8  | ≤9
(but>0) (but>1) (but>2) (but>5) (but>8)
```

**This is exactly a sorted array!**

Since each region contains only elements in a specific range, and we have n pivots creating n+1 regions, most regions will be empty or contain single elements. The array is now sorted.

#### The Contradiction

1. **Sorting lower bound**: Any comparison-based sorting algorithm requires Ω(n log n) comparisons
2. **If k-partitioning could be done in o(n log k)**:
   - When k = n, we'd have an algorithm running in o(n log n)
   - This would sort n elements faster than the sorting lower bound
3. **This is impossible!**

Therefore, k-partitioning **cannot** be done faster than Ω(n log k).

### Why O(n log k) is Optimal

Our divide-and-conquer algorithm achieves O(n log k), which matches the lower bound Ω(n log k).

**Conclusion**: O(n log k) is **optimal** in the comparison model.

### Information-Theoretic Perspective

**Decision tree argument**:
- With k pivots, we need to determine which of k+1 regions each element belongs to
- This requires Ω(log(k+1)) comparisons per element on average
- For n elements: Ω(n log k) total comparisons

---

## Practical Applications

### 1. Multi-Way Quicksort

Standard quicksort partitions into 2 parts. Multi-way quicksort uses k pivots to partition into k+1 parts, reducing recursion depth.

**Benefit**: Better cache performance, reduced recursion overhead.

### 2. Approximate Sorting / Bucketing

When exact sorting isn't needed, k-partitioning can place elements into approximate buckets.

**Use case**:
- Grouping students by grade ranges: F, D, C, B, A
- Pivots: [50, 60, 70, 80]
- Creates 5 grade buckets without fully sorting

### 3. Parallel Processing

K-partitioning naturally divides data into k+1 independent regions that can be processed in parallel.

**Use case**:
- Distribute data across k+1 processors
- Each processor handles one region independently

### 4. Database Query Optimization

Range queries can use k-partitioning to quickly filter data into relevant ranges.

**Example**: Find all transactions between $100-$500, $500-$1000, $1000+
- Pivots: [100, 500, 1000]
- K-partition once, then process relevant regions

### 5. Selection Algorithms

Finding the k smallest/largest elements can be accelerated using k-partitioning.

**Approach**:
- Use order statistics to find the kth smallest element
- K-partition around it
- Return the left region

---

## Complete Examples

### Example 1: Small Array, Few Pivots

**Input**:
```
Array:  [8, 3, 5, 1, 9, 2, 7, 4, 6]
Pivots: [4, 7]
```

**Step 1: Sort pivots**
```
Pivots: [4, 7]  (already sorted)
```

**Step 2: Apply divide-and-conquer k-partition**

**Recursion Level 0**: Partition around mid pivot = 4
```
[8, 3, 5, 1, 9, 2, 7, 4, 6]
             ↓ (pivot = 4)
[3, 1, 2, 4] | [8, 5, 9, 7, 6]
    ≤ 4      |      > 4
```

**Recursion Level 1**:
- Left: No more pivots, done
- Right: Partition [8, 5, 9, 7, 6] around pivot = 7

```
[8, 5, 9, 7, 6]
          ↓ (pivot = 7)
[5, 7, 6] | [8, 9]
   ≤ 7    |  > 7
```

**Final Result**:
```
[3, 1, 2, 4] | [5, 7, 6] | [8, 9]
    ≤ 4      |  ≤7, >4   |  > 7

Region 1 (≤4):  [3, 1, 2, 4]  ← NOT sorted internally
Region 2 (4-7): [5, 7, 6]     ← NOT sorted internally
Region 3 (>7):  [8, 9]        ← NOT sorted internally
```

**Verification**:
- ✓ All elements in Region 1 are ≤ 4
- ✓ All elements in Region 2 are > 4 AND ≤ 7
- ✓ All elements in Region 3 are > 7
- ✗ Elements within regions are NOT sorted

---

### Example 2: Larger Array, More Pivots

**Input**:
```
Array:  [15, 3, 9, 8, 5, 2, 7, 1, 6, 11, 4, 13, 10, 12, 14]
Pivots: [4, 8, 12]
```

**Step 1: Sort pivots**
```
Pivots: [4, 8, 12]  (already sorted)
```

**Step 2: Divide-and-conquer k-partition**

**Level 0**: mid = 1, pivot = 8
```
Original: [15, 3, 9, 8, 5, 2, 7, 1, 6, 11, 4, 13, 10, 12, 14]
                        ↓
Result:   [3, 5, 2, 7, 1, 6, 4, 8] | [15, 9, 11, 13, 10, 12, 14]
                 ≤ 8                 |           > 8

Left portion:  [3, 5, 2, 7, 1, 6, 4, 8]
Left pivots:   [4]

Right portion: [15, 9, 11, 13, 10, 12, 14]
Right pivots:  [12]
```

**Level 1 Left**: mid = 0, pivot = 4
```
[3, 5, 2, 7, 1, 6, 4, 8]
          ↓
[3, 2, 1, 4] | [5, 7, 6, 8]
    ≤ 4      |  ≤8, >4
```

**Level 1 Right**: mid = 0, pivot = 12
```
[15, 9, 11, 13, 10, 12, 14]
                     ↓
[9, 11, 10, 12] | [15, 13, 14]
   ≤12, >8      |     > 12
```

**Final Result**:
```
[3, 2, 1, 4] | [5, 7, 6, 8] | [9, 11, 10, 12] | [15, 13, 14]
    ≤ 4      |  >4, ≤8      |   >8, ≤12       |     > 12

Region 1 (≤4):   {1, 2, 3, 4}     ← contains these, unsorted
Region 2 (4-8):  {5, 6, 7, 8}     ← contains these, unsorted
Region 3 (8-12): {9, 10, 11, 12}  ← contains these, unsorted
Region 4 (>12):  {13, 14, 15}     ← contains these, unsorted
```

**Complexity for this example**:
- n = 15, k = 3
- Tree depth: ⌈log₂ 3⌉ = 2 levels
- Work per level: O(15)
- Total: 2 × 15 = 30 operations (approximately)

**vs Sequential approach**:
- Would do 3 partitions: 15 + 15 + 15 = 45 operations (approximately)

---

### Example 3: Demonstrating k = n (Becomes Sorting)

**Input**:
```
Array:  [5, 2, 8, 1, 9]
Pivots: [1, 2, 5, 8, 9]  (all elements, sorted)
```

**K-partition with k = 5**:

Using divide-and-conquer:

**Level 0**: mid = 2, pivot = 5
```
[5, 2, 8, 1, 9]
 ↓
[2, 1, 5] | [8, 9]
   ≤ 5    |  > 5
```

**Level 1 Left**: mid = 0, pivot = 2
```
[2, 1, 5]
 ↓
[1, 2] | [5]
 ≤ 2   | ≤5, >2
```

**Level 1 Right**: mid = 0, pivot = 8
```
[8, 9]
 ↓
[8] | [9]
≤8  | >8
```

**Level 2 Left-Left**: mid = 0, pivot = 1
```
[1, 2]
 ↓
[1] | [2]
≤1  | ≤2, >1
```

**Final Result**:
```
[1] | [2] | [5] | [8] | [9]
≤1  | ≤2  | ≤5  | ≤8  | ≤9
    |but>1|but>2|but>5|but>8
```

**This is a fully sorted array!**

**Complexity**:
- K-partitioning: O(n log n) = O(5 log 5) ≈ O(11.6) operations
- This matches the sorting lower bound
- Therefore, we cannot do better than O(n log k) for k-partitioning

---

## Summary

### Key Takeaways

1. **K-partitioning ≠ Sorting**
   - K-partitioning only separates elements into k+1 regions
   - Elements within regions remain unsorted
   - This is what makes it faster than sorting when k << n

2. **Two Algorithms**
   - **Sequential O(nk)**: Simple but inefficient, partitions k times
   - **Divide-and-conquer O(n log k)**: Optimal, uses binary recursion on pivots

3. **Optimality**
   - O(n log k) is the best possible in the comparison model
   - Proven by reduction: when k = n, k-partitioning becomes sorting
   - Our divide-and-conquer algorithm achieves this optimal bound

4. **Practical Benefits**
   - When k << n: Significantly faster than sorting
   - Useful for bucketing, multi-way partitioning, parallel processing
   - Natural fit for divide-and-conquer and parallel algorithms

### Complexity Quick Reference

| Algorithm | Time Complexity | Space Complexity | When to Use |
|-----------|----------------|------------------|-------------|
| Sequential | O(nk) | O(1) | Never (always suboptimal) |
| Divide-and-Conquer | O(n log k) | O(log k) | Always (optimal) |
| Sorting | O(n log n) | O(log n) or O(n) | When full ordering needed |

### When k << n (e.g., k = 10, n = 10,000)
- K-partition: O(10,000 × 3.3) ≈ 33,000 operations
- Sort: O(10,000 × 13.3) ≈ 133,000 operations
- **Speedup: ~4x**

### When k ≈ n (e.g., k = n = 10,000)
- K-partition: O(10,000 × 13.3) ≈ 133,000 operations
- Sort: O(10,000 × 13.3) ≈ 133,000 operations
- **Same complexity** (k-partitioning becomes sorting)

---

## Additional Notes

### Stability
Standard k-partitioning (like quicksort partitioning) is **not stable**. Elements with equal values may be reordered. To maintain stability, use a stable partitioning method or track original indices.

### In-Place vs Out-of-Place
The algorithms described use in-place partitioning (O(1) extra space for partitioning, O(log k) for recursion). Out-of-place versions using extra arrays can be simpler to implement but require O(n) additional space.

### Practical Implementation Considerations
- **Pivot selection**: In practice, pivots might be selected as sample quantiles
- **Small subarrays**: Use insertion sort for tiny regions (optimization)
- **Cache efficiency**: Multi-way partitioning can improve cache locality
- **Parallelization**: The divide-and-conquer tree naturally parallelizes

### Related Algorithms
- **Quickselect**: O(n) average case for finding kth element
- **3-way partitioning**: Used in quicksort for handling duplicates
- **Multi-pivot quicksort**: Uses k pivots to reduce recursion depth
- **Radix sort**: Can be viewed as k-partitioning with k = radix size

---

*This guide covers the theoretical and practical aspects of k-partitioning for FIT2004. For implementation examples, see `implementations-algorithms/` directory.*
