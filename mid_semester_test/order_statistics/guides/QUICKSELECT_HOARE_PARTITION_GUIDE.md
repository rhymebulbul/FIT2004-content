# QuickSelect with Hoare's Partition - Step-by-Step Guide

## Overview
This guide provides a systematic approach to solving QuickSelect problems using Hoare's partition algorithm, particularly for quiz/test questions that ask about array state after N rounds of partitioning.

## Key Concepts

### What is QuickSelect?
- Algorithm to find the kth order statistic (element at index k in sorted array)
- Uses partitioning like QuickSort, but only searches one side
- Average O(n), worst case O(n²) with bad pivots

### What is Hoare's Partition?
- In-place partitioning algorithm
- Pivot is typically the **first element** of the subarray
- Creates two unsorted regions: left side ≤ pivot, right side ≥ pivot

## Critical Rules to Remember

### 1. Pivot Selection
- **Always the FIRST element** of the current subarray being partitioned
- Pivot is **excluded from the initial scan** (scanning starts at lo+1)

### 2. Pointer Initialization
- `i = lo + 1` (starts AFTER the pivot)
- `j = hi` (starts at the end of subarray)

### 3. Pointer Movement
- `i` moves **RIGHT** → (stops when `A[i] >= pivot`)
- `j` moves **LEFT** ← (stops when `A[j] <= pivot`)

### 4. When Pointers Cross
- Condition: `i >= j` (meaning `j < i`, so j is to the LEFT of i)
- When this happens, partitioning is complete

### 5. Final Pivot Swap
- **Always swap pivot with A[j]** (NOT A[i]!)
- Why j? Because `A[j] <= pivot` (safe to swap)
- Why not i? Because `A[i] >= pivot` (would break partition)
- The pivot moves to index j (its final sorted position)

### 6. Partition Guarantees
- Elements at indices `lo` to `j-1`: all **< pivot**
- Element at index `j`: **the pivot itself** (in final position)
- Elements at indices `j+1` to `hi`: all **> pivot**
- **IMPORTANT:** Elements on each side are **NOT sorted** among themselves!

### 7. Next Search Range
After pivot lands at index j, compare j with target k:

- **If j == k:** FOUND! We're done
- **If j < k:** Search RIGHT → new range: `[j+1, hi]`, new pivot: `A[j+1]`
- **If j > k:** Search LEFT → new range: `[lo, j-1]`, new pivot: `A[lo]`

**Key:** We exclude index j because the pivot is now in its final position!

---

## Step-by-Step Algorithm

### Hoare Partition Pseudocode
```
function hoare_partition(A, lo, hi):
    pivot = A[lo]           # First element is pivot
    i = lo + 1              # Start after pivot
    j = hi                  # Start at end

    while i <= j:
        # Move i right while A[i] < pivot
        while i <= j and A[i] < pivot:
            i = i + 1

        # Move j left while A[j] > pivot
        while i <= j and A[j] > pivot:
            j = j - 1

        # If pointers haven't crossed, swap
        if i < j:
            swap A[i] and A[j]
            i = i + 1
            j = j - 1

    # Pointers crossed, swap pivot with A[j]
    swap A[lo] and A[j]
    return j                # Pivot is now at index j
```

### QuickSelect Pseudocode
```
function quickselect(A, k):
    lo = 0
    hi = len(A) - 1

    while True:
        j = hoare_partition(A, lo, hi)

        if j == k:
            return A[k]     # Found!
        elif j < k:
            lo = j + 1      # Search right
        else:
            hi = j - 1      # Search left
```

---

## Solving Quiz/Test Questions: Step-by-Step Method

### Problem Template
Given an array and target k, find the array state after N rounds of partitioning (or when kth element is found, whichever comes first).

### Solution Steps

#### Step 1: Set Up Initial State
```
- Write down the array with indices
- Identify k (target position)
- Note: pivot is always first element of search range
```

#### Step 2: For Each Round

**A. Identify Current State**
- Current search range [lo, hi]
- Current pivot = A[lo]

**B. Initialize Pointers**
- i = lo + 1 (after pivot)
- j = hi

**C. Scan and Swap**
```
Repeat:
  1. Move i right until A[i] >= pivot (or i > j)
  2. Move j left until A[j] <= pivot (or i > j)
  3. If i < j:
     - Swap A[i] and A[j]
     - Increment i, decrement j
  4. If i >= j:
     - Stop (pointers crossed)
```

**D. Final Pivot Swap**
- Swap A[lo] (pivot) with A[j]
- Pivot is now at index j

**E. Update Array State**
- Write down the new array

**F. Decide Next Step**
- If j == k: DONE (found kth element)
- If j < k: new range = [j+1, hi]
- If j > k: new range = [lo, j-1]

#### Step 3: Verify Answer
- Check each answer option against your final array state

---

## Worked Example: The Quiz Question

### Problem
```
Array: [2, 3, 7, 8, 4, 9, 1, 10, 6, 5]
Find: 4th order statistic (k=3)
Method: QuickSelect with Hoare's partition, pivot = first element
Question: Array state after 2 rounds of partitioning?
```

### Solution

#### ROUND 1

**Initial State:**
```
Array: [2, 3, 7, 8, 4, 9, 1, 10, 6, 5]
Index:  0  1  2  3  4  5  6  7  8  9
Range: [0, 9]
Pivot: A[0] = 2
```

**Partition Process:**
```
i = 1, j = 9

Iteration 1:
  - i=1: A[1]=3 >= 2, STOP
  - j: scan left... j=6: A[6]=1 <= 2, STOP
  - i < j, so SWAP A[1] ↔ A[6]
  - Array: [2, 1, 7, 8, 4, 9, 3, 10, 6, 5]
  - Move: i=2, j=5

Iteration 2:
  - i=2: A[2]=7 >= 2, STOP
  - j: scan left... all elements > 2 until j=1
  - j=1: A[1]=1 <= 2, STOP
  - i >= j (2 >= 1), POINTERS CROSSED!
```

**Final Pivot Swap:**
```
Swap A[0]=2 with A[1]=1
Array: [1, 2, 7, 8, 4, 9, 3, 10, 6, 5]
Partition index: j = 1
```

**Decision:**
```
j=1 < k=3, so search RIGHT
New range: [2, 9]
Next pivot: A[2] = 7
```

---

#### ROUND 2

**Initial State:**
```
Array: [1, 2, 7, 8, 4, 9, 3, 10, 6, 5]
Index:  0  1  2  3  4  5  6  7  8  9
Range: [2, 9]
Pivot: A[2] = 7
```

**Partition Process:**
```
i = 3, j = 9

Iteration 1:
  - i=3: A[3]=8 >= 7, STOP
  - j=9: A[9]=5 <= 7, STOP
  - i < j, so SWAP A[3] ↔ A[9]
  - Array: [1, 2, 7, 5, 4, 9, 3, 10, 6, 8]
  - Move: i=4, j=8

Iteration 2:
  - i=4: A[4]=4 < 7, move right... i=5
  - i=5: A[5]=9 >= 7, STOP
  - j=8: A[8]=6 <= 7, STOP
  - i < j, so SWAP A[5] ↔ A[8]
  - Array: [1, 2, 7, 5, 4, 6, 3, 10, 9, 8]
  - Move: i=6, j=7

Iteration 3:
  - i=6: A[6]=3 < 7, move right... i=7
  - i=7: A[7]=10 >= 7, STOP
  - j=7: A[7]=10 > 7, move left... j=6
  - j=6: A[6]=3 <= 7, STOP
  - i >= j (7 >= 6), POINTERS CROSSED!
```

**Final Pivot Swap:**
```
Swap A[2]=7 with A[6]=3
Array: [1, 2, 3, 5, 4, 6, 7, 10, 9, 8]
Partition index: j = 6
```

**Decision:**
```
j=6 > k=3, so would search LEFT next
New range would be: [2, 5]
But we stop here (2 rounds complete)
```

---

### Final Answer

**Array after 2 rounds:** `[1, 2, 3, 5, 4, 6, 7, 10, 9, 8]`

**Checking options:**
- a. A[3]=5? → **TRUE** ✓
- b. A[8]=6? → FALSE (A[8]=9)
- c. A[9]=8? → **TRUE** ✓
- d. A[0]=2? → FALSE (A[0]=1)
- e. A[4]=4? → **TRUE** ✓
- f. A[5]=7? → FALSE (A[5]=6)

**Correct answers: a, c, e**

---

## Common Mistakes to Avoid

1. **Starting i at lo instead of lo+1**
   - WRONG: i = lo (includes pivot in scan)
   - RIGHT: i = lo+1 (excludes pivot from scan)

2. **Swapping pivot with A[i] instead of A[j]**
   - WRONG: swap A[lo] with A[i] (breaks partition!)
   - RIGHT: swap A[lo] with A[j] (maintains partition)

3. **Forgetting to exclude pivot index from next range**
   - WRONG: if j < k, new range [j, hi]
   - RIGHT: if j < k, new range [j+1, hi]

4. **Thinking partition sorts the subarrays**
   - WRONG: expecting sorted subarrays after partition
   - RIGHT: subarrays are NOT sorted, only relatively ordered

5. **Using wrong comparison operators**
   - i stops when A[i] >= pivot (not >)
   - j stops when A[j] <= pivot (not <)

6. **Forgetting to move pointers after swap**
   - After swapping A[i] and A[j], increment i and decrement j

7. **Not tracking array changes carefully**
   - Every swap changes the array permanently (in-place)
   - Write down array state after each swap

---

## Quick Reference Card

### Initialization
```
pivot = A[lo]
i = lo + 1
j = hi
```

### Scanning Rules
```
i moves RIGHT → stops when A[i] >= pivot
j moves LEFT ← stops when A[j] <= pivot
```

### Swap Conditions
```
If i < j: swap A[i] and A[j], then i++, j--
If i >= j: STOP, pointers crossed
```

### Final Step
```
Swap pivot A[lo] with A[j]
Return j as partition index
```

### Next Range Decision
```
if j == k: FOUND!
if j < k: search [j+1, hi]
if j > k: search [lo, j-1]
```

### Partition Guarantees
```
A[lo...j-1]: all < pivot
A[j]: pivot (final position)
A[j+1...hi]: all > pivot
NOT sorted within each region!
```

---

## Practice Tips

1. **Draw the array with indices** - Visual representation helps track changes
2. **Write every swap** - Don't skip steps mentally
3. **Mark pivot position clearly** - Track where it moves
4. **Use a table** for complex traces:
   ```
   Round | Range | Pivot | Swaps | Final j | Next Range
   ```
5. **Verify partition property** after each round:
   - All elements left of j are <= pivot
   - All elements right of j are >= pivot

6. **Double-check pointer crossing condition** - Common source of errors

7. **Remember: j not i for final swap** - Most common mistake!

---

## Additional Notes

### Why Hoare's Partition?
- Fewer swaps than other partition schemes
- In-place (no extra space)
- Works well with duplicate elements

### Complexity
- **Per partition:** O(n) where n is subarray size
- **QuickSelect overall:**
  - Average: O(n)
  - Worst: O(n²) with bad pivot choices

### Variations
- Some implementations use different pivot selections (median-of-three, random)
- This guide assumes **first element as pivot** (most common in course materials)
- Some implementations increment/decrement before comparison vs after
- Always follow the specific algorithm given in your course!

---

## Summary Checklist

Before submitting an answer, verify:
- [ ] Pivot was first element of each subarray
- [ ] Started i at lo+1 (not lo)
- [ ] Swapped with A[j] (not A[i])
- [ ] Tracked all swaps correctly
- [ ] Applied final pivot swap
- [ ] Excluded pivot index from next range
- [ ] Counted rounds correctly
- [ ] Checked all answer options against final array

---

## Related Topics

- QuickSort (uses partitioning repeatedly)
- Order Statistics (finding median, percentiles)
- Lomuto Partition (alternative partition scheme)
- Randomized QuickSelect (improves average case)

---

*Created for FIT2004 mid-semester test preparation*
