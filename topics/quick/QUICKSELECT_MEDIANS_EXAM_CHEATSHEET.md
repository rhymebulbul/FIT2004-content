# Quickselect, Quicksort & Median of Medians - Exam Cheatsheet

**Purpose:** Comprehensive guide covering all quickselect/quicksort/partition/median problems that appear in FIT2004 exams

---

## Table of Contents
1. [Core Concepts & Complexity](#core-concepts--complexity)
2. [Common Exam Question Patterns](#common-exam-question-patterns)
3. [Partition Schemes Deep Dive](#partition-schemes-deep-dive)
4. [Median of Medians (Critical!)](#median-of-medians-critical)
5. [Applied Problem Patterns](#applied-problem-patterns)
6. [Common Mistakes & Pitfalls](#common-mistakes--pitfalls)
7. [Quick Reference Formulas](#quick-reference-formulas)

---

## Core Concepts & Complexity

### Quickselect Algorithm
**Purpose:** Find the k-th smallest element in O(n) average time

**Key Properties:**
- Does NOT sort the entire array
- Partitions around pivot until k-th element found
- Best/Average: O(n), Worst: O(n²)

**Basic Structure:**
```python
def quickselect(A, k, lo, hi):
    while True:
        if lo == hi:
            return A[lo]
        pivot = choose_pivot(A, lo, hi)
        lt, gt = partition(A, lo, hi, pivot)
        if k < lt:
            hi = lt - 1
        elif k > gt:
            lo = gt + 1
        else:
            return A[k]
```

### Quicksort Algorithm
**Purpose:** Sort entire array using divide-and-conquer

**Complexity:**
- **Best case:** O(n log n) - balanced partitions (T(n) = 2T(n/2) + O(n))
- **Average case:** O(n log n) - random pivots
- **Worst case:** O(n²) - always choosing min/max pivot (T(n) = T(n-1) + O(n))

**Not stable** (unless using special 3-way stable partition)

---

## Common Exam Question Patterns

### Pattern 1: Median of Medians Justification ⭐⭐⭐
**CRITICAL - Worth 2+ marks, commonly appears**

**Question Type:** "Justify why Quickselect using median-of-medians achieves O(n) worst-case"

**What NOT to do (0.5/2 marks):**
- ❌ "It picks a pivot in the 30-70 percentile"
- ❌ Just stating the recurrence without explanation
- ❌ Mentioning the 70-30 split without justification

**Full Answer Template (2/2 marks):**

1. **State the guarantee:**
   - Median of medians guarantees pivot within 30th-70th percentile
   - This ensures at least 30% of elements eliminated per recursion

2. **Show the recurrence:**
   ```
   T(n) = T(n/5)      [finding median of medians]
        + T(7n/10)    [recursive call on larger partition]
        + O(n)        [partitioning work]
   ```

3. **Prove O(n) using geometric series:**
   ```
   Work per level: n + 0.9n + 0.81n + 0.729n + ...
                 = n(1 + 0.9 + 0.9² + 0.9³ + ...)
                 = n · (1/(1-0.9))
                 = 10n
                 = O(n)
   ```

4. **Key insight:**
   - Don't need EXACT median, just "good enough" to eliminate constant fraction
   - Any constant fraction α > 0 eliminated gives O(n) via geometric series
   - MoM adds O(n) overhead, which doesn't affect overall O(n) complexity

**Why it works:**
- If we eliminate at least α fraction: T(n) = T((1-α)n) + O(n)
- Forms geometric series: n + (1-α)n + (1-α)²n + ... ≤ n/(1-(1-α)) = O(n)

---

### Pattern 2: Percentile/Order Statistic Selection ⭐⭐⭐
**CRITICAL - Appears in almost every exam, master this pattern!**

**Common in:** s1-Q5 (interviewing applicants), s2-Q4, s3-Q5

**Question Type:** "Find top X%, bottom Y%, or specific percentiles and partition into groups"

---

#### 🔥 UNIVERSAL SOLUTION FORMULA - MEMORIZE THIS! 🔥

**Step 1:** Use Quickselect to find threshold positions
**Step 2:** Linear scan to collect groups
**Result:** Always O(n) time!

```python
# UNIVERSAL TEMPLATE - Works for ANY percentile question!
def partition_by_percentiles(A, n):
    # Step 1: Find thresholds using Quickselect - O(n) EACH
    threshold_pos_1 = int(percentile_1 * n)
    quickselect(A, threshold_pos_1, 0, n-1)  # O(n)

    threshold_pos_2 = int(percentile_2 * n)
    quickselect(A, threshold_pos_2, 0, n-1)  # O(n)

    # Step 2: Partition into groups - O(n)
    group_1 = A[0:threshold_pos_1]
    group_2 = A[threshold_pos_1:threshold_pos_2]
    group_3 = A[threshold_pos_2:n]

    # Total: O(n) + O(n) + O(n) = O(n) ✓
    return group_1, group_2, group_3
```

---

#### 🚨 CRITICAL PERCENTILE POSITION FORMULAS 🚨

**ALWAYS 0-indexed arrays - MEMORIZE THESE:**

```python
# Top X% → threshold at (1 - X/100) position!
top_10_percent_threshold  = int(0.9 * n)   # Top 10% = above 90th percentile
top_20_percent_threshold  = int(0.8 * n)   # Top 20% = above 80th percentile
top_25_percent_threshold  = int(0.75 * n)  # Top 25% = above 75th percentile

# Bottom X% → threshold at (X/100) position
bottom_10_percent_threshold = int(0.1 * n)   # Bottom 10%
bottom_30_percent_threshold = int(0.3 * n)   # Bottom 30%
bottom_50_percent_threshold = int(0.5 * n)   # Bottom 50% (median)

# Specific percentiles
median_pos = n // 2                          # 50th percentile
p25_pos = int(0.25 * n)                      # 25th percentile
p75_pos = int(0.75 * n)                      # 75th percentile
p80_pos = int(0.8 * n)                       # 80th percentile
p90_pos = int(0.9 * n)                       # 90th percentile
```

---

#### ⚠️ COMMON TRAP - DO NOT FALL FOR THIS! ⚠️

**WRONG THINKING (costs you marks!):**
```python
# ❌ "Top 20% means position 0.2n" - WRONG!
top_20_pos = int(0.2 * n)  # This gives BOTTOM 20%!
```

**CORRECT THINKING:**
```python
# ✓ "Top 20% = elements ABOVE 80th percentile"
top_20_threshold_pos = int(0.8 * n)  # Elements from [0.8n : n] are top 20%
```

**Memory trick:** "Top X% excludes the bottom (100-X)%"

---

#### 📋 COMPLETE WORKED EXAMPLE

**Question:** "Partition n applicants by score: reject bottom 60%, waitlist middle 30%, accept top 10%"

**Solution:**
```python
def partition_applicants(scores):
    n = len(scores)

    # Find 60th percentile threshold (reject below this)
    reject_threshold_pos = int(0.6 * n)
    quickselect(scores, reject_threshold_pos, 0, n-1)  # O(n)

    # Find 90th percentile threshold (accept above this)
    accept_threshold_pos = int(0.9 * n)
    quickselect(scores, accept_threshold_pos, 0, n-1)  # O(n)

    # Collect groups
    rejected = scores[0:reject_threshold_pos]                    # 60%
    waitlist = scores[reject_threshold_pos:accept_threshold_pos] # 30%
    accepted = scores[accept_threshold_pos:n]                    # 10%

    return rejected, waitlist, accepted
    # Time: O(n) + O(n) + O(n) = O(n) ✓
```

**Verification:**
- Bottom 60%: indices [0, 0.6n) → 0.6n elements ✓
- Middle 30%: indices [0.6n, 0.9n) → 0.3n elements ✓
- Top 10%: indices [0.9n, n) → 0.1n elements ✓
- Total: 60% + 30% + 10% = 100% ✓

---

#### 🎯 EXAM STRATEGY - ANSWER ANY PERCENTILE QUESTION

**When you see percentile/threshold questions:**

1. **Identify percentile boundaries**
   - "Top X%" → threshold at (1 - X/100)n
   - "Bottom Y%" → threshold at (Y/100)n

2. **Calculate k positions (0-indexed)**
   - Write them down: k₁ = ..., k₂ = ...

3. **Write Quickselect calls**
   - One call per threshold: `quickselect(A, k, 0, n-1)`

4. **Partition with slicing**
   - Group i: `A[k_{i-1} : k_i]`

5. **State complexity**
   - "k Quickselect calls: k × O(n) = O(n) for constant k"
   - "Linear scan: O(n)"
   - "Total: O(n)" ✓

---

#### 💡 WHY MULTIPLE QUICKSELECT CALLS STAY O(n)

```
Quickselect call 1:  O(n)
Quickselect call 2:  O(n)  [works on whole array, not subset!]
Quickselect call 3:  O(n)
Linear partitioning: O(n)

Total = O(n) + O(n) + O(n) + O(n) = O(4n) = O(n)
```

**Key insight:** Constants don't matter in Big-O!
- O(2n) = O(n)
- O(5n) = O(n)
- As long as it's O(kn) where k is constant, it's O(n)

---

#### ✅ PATTERN WORKS FOR ALL VARIATIONS

1. **Two-way split:** "Accept top 30%, reject rest"
   - One Quickselect at 70th percentile → O(n)

2. **Three-way split:** "Reject 50%, waitlist 40%, accept 10%"
   - Two Quickselect calls (50th, 90th) → O(n)

3. **Multi-way split:** "Partition into k groups"
   - (k-1) Quickselect calls → O(kn) = O(n) if k constant

4. **Dynamic thresholds:** "Find k closest to median"
   - Find median first, then k-th smallest distance → O(n)
   - See Pattern B (lines 352-381)

---

#### 🔑 KEY TAKEAWAYS - WRITE THESE IN YOUR EXAM

1. **Multiple Quickselect calls = still O(n) total** (if constant number)
2. **Top X% = threshold at position (1-X/100)n** ← DON'T CONFUSE THIS!
3. **Bottom X% = threshold at position (X/100)n**
4. **Always verify percentages sum to 100%** in multi-way partitions
5. **Quickselect doesn't sort** - it just places k-th element correctly

---

#### 📝 PRACTICE CHECKLIST

Before the exam, make sure you can:
- [ ] Convert "top 20%" to correct array position (0.8n)
- [ ] Convert "bottom 30%" to correct array position (0.3n)
- [ ] Write Quickselect calls for multiple thresholds
- [ ] Explain why multiple calls stay O(n)
- [ ] Partition array correctly after Quickselect
- [ ] Verify percentages add up to 100%

**This pattern alone can earn you 3-5 marks per exam - MASTER IT!**

---

### Pattern 3: Modified Insertion Sort with Binary Search
**Common in:** s1-Q4, s3-Q4, mid-sem feedback

**Question:** "Binary search for position, then shift elements"

**Analysis:**
- **Comparisons:** O(n log n) - binary search for each of n elements
- **Time complexity:** O(n²) - shifting elements dominates
- **Why?** Even though finding position is O(log n), inserting requires O(n) shifts

```
for i = 2 to n:                    # n iterations
    binary_search(A[1..i-1], A[i]) # O(log n) comparisons
    shift_elements()                # O(n) time - DOMINATES!
```

**Common trap:** Thinking binary search makes it O(n log n) overall - NO! Shifts still O(n) per iteration.

---

### Pattern 4: Partition Scheme Analysis

#### Hoare's Partition
**Properties:**
- In-place, few swaps
- Two pointers move towards each other
- All elements ≤ pivot on left, ≥ pivot on right
- Returns partition index j (not necessarily pivot's final position)
- Recursion: `quicksort(A, lo, j)` and `quicksort(A, j+1, hi)`

**NOT stable, suffers from clustering with many duplicates**

#### Dutch National Flag (3-way Partition)
**Properties:**
- Three regions: < pivot, = pivot, > pivot
- Returns (lt, gt) - boundaries of equal region
- Excellent for arrays with duplicates
- Recursion: `quicksort(A, lo, lt-1)` and `quicksort(A, gt+1, hi)`

**Key advantage:** Skips elements equal to pivot in future recursions

---

### Pattern 5: K-Partitioning ⭐
**From:** Week 4 Applied Problem 5

**Question:** "Partition array into k regions using k pivots"

**Two solutions:**

**O(nk) - Naive:**
```python
def k_partition_naive(A, pivots):
    pivots.sort()  # O(k log k)
    j = 0
    for i in range(k):
        j = partition(A[j:], pivots[i]) + 1  # k calls, O(n) total
    # Total: O(nk)
```

**O(n log k) - Divide & Conquer:**
```python
def k_partition_fast(A, pivots):
    pivots.sort()  # O(k log k)
    k_partition_recursive(A, pivots)

def k_partition_recursive(A, pivots):
    if len(pivots) == 0 or len(A) == 0:
        return
    mid = len(pivots) // 2
    j = partition(A, pivots[mid])  # O(n) work at this level
    k_partition_recursive(A[0:j], pivots[0:mid])
    k_partition_recursive(A[j+1:], pivots[mid+1:])
```

**Analysis:**
- Log k levels of recursion
- Each level does O(n) partitioning work
- Total: O(n log k + k log k) = O(n log k) since typically n > k

**Why can't we go faster than O(n log k)?**
- If k = n (all elements as pivots), this becomes sorting
- Sorting has Ω(n log n) lower bound
- Therefore k-partitioning is Ω(n log k)

---

### Pattern 6: Weighted Median
**From:** Week 4 Applied Problem 7

**Concept:** Find element where cumulative weight ≈ 1/2

**Modified Quickselect:**
```python
def weighted_quickselect(array, weights, target_weight):
    if hi <= lo:
        return array[lo]

    pivot = array[lo]
    j = partition(array, weights, pivot)  # Partition both arrays together

    left_weight = sum(weights[lo:j])
    pivot_weight = weights[j]

    if left_weight > target_weight:
        return weighted_quickselect(array[lo:j], weights[lo:j], target_weight)
    elif left_weight + pivot_weight >= target_weight:
        return array[j]
    else:
        return weighted_quickselect(array[j+1:hi], weights[j+1:hi],
                                   target_weight - left_weight - pivot_weight)
```

**Key:** Adjust target weight when recursing right

---

## Median of Medians (Critical!)

### Why It's Important
- Guarantees O(n) worst-case for Quickselect
- **Most tested concept** in quickselect questions
- Common 2-mark written question

### The Algorithm

**Step-by-step:**
1. Divide array into groups of 5
2. Find median of each group (via sorting) - O(1) per group
3. Recursively find median of these medians
4. Use this as pivot for Quickselect

### The Guarantee

**70-30 Split Proof:**
- There are ⌈n/5⌉ groups
- Half of group medians are ≤ MoM
- Each of those groups has 3 elements ≤ its median
- So at least (⌈n/5⌉/2) × 3 ≈ 3n/10 elements ≤ MoM
- Similarly, 3n/10 elements ≥ MoM
- **Therefore:** MoM guarantees 30-70 split

### Complexity Analysis

**Recurrence:**
```
T(n) = T(n/5)        [find MoM recursively]
     + T(7n/10)      [worst case partition on 70%]
     + O(n)          [partitioning + finding group medians]
```

**Solving via recursion tree:**
```
Level 0: n
Level 1: n/5 + 7n/10 = 9n/10
Level 2: (9/10)²n
Level 3: (9/10)³n
...
Total = n(1 + 9/10 + (9/10)² + ...) = n/(1-0.9) = 10n = O(n)
```

**Key insight:** As long as coefficient of n in recursion < 1, series converges to O(n)

### Why Groups of 5?

Groups of 3 don't work:
```
T(n) = T(n/3) + T(2n/3) + O(n)
     = n + n + n + ... = O(n log n)  ❌
```

Groups of 5 work:
```
T(n) = T(n/5) + T(7n/10) + O(n)
     = O(n)  ✓
```

Groups of 7, 9, etc. also work but more overhead.

---

## Applied Problem Patterns

### Pattern A: Lock and Key Matching
**From:** Week 4 Applied Problem 2

**Setup:**
- n locks and n keys (each matches exactly one)
- Can try key in lock: larger/smaller/fits
- Cannot compare two keys or two locks directly

**Solution:** Modified Quicksort
```python
def match_locks_keys(locks, keys):
    if len(locks) <= 1:
        return

    # Step 1: Pick random key as pivot
    pivot_key = keys[random_index]

    # Step 2: Partition locks using pivot key
    # Try pivot key in each lock to classify smaller/equal/larger
    j_lock = partition_locks(locks, pivot_key)
    matching_lock = locks[j_lock]

    # Step 3: Use matching lock to partition keys
    j_key = partition_keys(keys, matching_lock)

    # Step 4: Recurse on smaller and larger sets
    match_locks_keys(locks[:j_lock], keys[:j_key])
    match_locks_keys(locks[j_lock+1:], keys[j_key+1:])
```

**Complexity:** O(n log n) average (like Quicksort)

**Key insight:** Can't compare directly, but can use intermediary to partition both

---

### Pattern B: K Closest to Median
**From:** Week 4 Applied Problem 3

**Question:** Find k numbers closest to median

**Solution:**
```python
def k_closest_to_median(A, k):
    n = len(A)

    # Step 1: Find median in O(n)
    median = quickselect(A, n//2, 0, n-1)

    # Step 2: Transform array to absolute differences (virtual, no extra space)
    # For each A[i], consider |A[i] - median|

    # Step 3: Find k-th smallest absolute difference in O(n)
    # Use modified Quickselect that compares |A[i] - median| values
    kth_diff = modified_quickselect(A, k, median)

    # Step 4: Collect all elements with |A[i] - median| ≤ kth_diff
    result = [A[i] for i in range(n) if abs(A[i] - median) <= kth_diff]

    return result[:k]  # In case of ties
```

**Complexity:** O(n) + O(n) + O(n) = O(n)

**Space:** O(1) auxiliary (transform is virtual)

---

### Pattern C: Mergesort + Insertion Sort Hybrid
**From:** Week 4 Applied Problem 4

**Question:** Mergesort until subproblems size k, then insertion sort

**Analysis:**
```
Mergesort levels until size k: log₂(n/k) levels
Work per level: O(n)
Total Mergesort: O(n log(n/k))

Number of subproblems at size k: n/k
Insertion sort per subproblem: O(k²)
Total Insertion: O(n/k × k²) = O(nk)

Total complexity: O(nk + n log(n/k))
```

**Optimal k:** Set k = O(log n) for O(n log n) total

---

### Pattern D: Pivot Strategy Analysis
**From:** Week 4 Applied Problem 6

**Question:** Quicksort using average as pivot - what's worst case?

**Answer:** Still O(n²)!

**Counter-example:** Factorial sequence [1!, 2!, 3!, ..., n!]
```
Average of [1!, 2!, ..., n!] ≈ n!/n = (n-1)!
```
- Average is second-largest element
- Unbalanced split: (n-2) vs 1
- Recurrence: T(n) = T(n-2) + O(n) = O(n²)

**Lesson:** Choosing pivot by average (not median) doesn't guarantee balanced splits

---

### Pattern E: Two Sorted Arrays - Kth Element
**From:** Week 4 Applied Problem 9

**Question:** Find k-th element of union of two sorted arrays

**Solution:** Nested binary search
```python
def kth_of_two_sorted(a, b, k):
    # Binary search on array a
    # For each position i in a, use binary search on b
    # to count how many elements in b are < a[i]

    # order(a[i]) = i + count(b[j] < a[i]) + 1

    # Binary search on order function to find element with order = k
    # If not in a, swap and search in b
```

**Complexity:** O(log m × log n)

**Why:** Binary search on a (O(log m)) × binary search on b for each (O(log n))

---

## Common Mistakes & Pitfalls

### Mistake 1: Confusing Comparisons vs Time Complexity
**Example:** Binary insertion sort
- Comparisons: O(n log n) ✓
- Time: O(n²) ✓ (due to shifts)

**Don't say:** "O(n log n) time because binary search"

### Mistake 2: Incomplete MoM Explanation
**Don't say:** "MoM gives 70-30 split" (only 0.5/2 marks)

**Do say:**
1. MoM guarantees eliminating 30% per recursion
2. This gives recurrence T(n) = T(7n/10) + T(n/5) + O(n)
3. Geometric series: n + 0.9n + 0.81n + ... = n/(1-0.9) = O(n)
4. Finding MoM adds O(n) overhead which doesn't affect total

### Mistake 3: Thinking Quickselect Sorts
**Wrong:** "Quickselect sorts the array then returns k-th element"

**Right:** "Quickselect partitions until k-th element found, NO full sorting"

### Mistake 4: Off-by-One in Percentiles
**Finding top 20%:** Position is ⌈0.8n⌉ or ⌊0.8n⌋, not 0.2n!
- Top 20% = elements > 80th percentile
- Use `k = int(0.8 * n)` for the threshold position

### Mistake 5: Hoare vs DNF Partition Confusion
**Hoare returns j:**
- Recurse on [lo, j] and [j+1, hi]

**DNF returns (lt, gt):**
- Recurse on [lo, lt-1] and [gt+1, hi]
- Skip [lt, gt] (all equal to pivot)

---

## Quick Reference Formulas

### Complexities
| Algorithm | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| Quicksort | O(n log n) | O(n log n) | O(n²) | O(log n) |
| Quickselect | O(n) | O(n) | O(n²) | O(1) |
| MoM Select | O(n) | O(n) | **O(n)** | O(log n) |

### Recurrences
```
Balanced Quicksort:     T(n) = 2T(n/2) + O(n) = O(n log n)
Unbalanced Quicksort:   T(n) = T(n-1) + O(n) = O(n²)
Quickselect (average):  T(n) = T(3n/4) + O(n) = O(n)
Median of Medians:      T(n) = T(n/5) + T(7n/10) + O(n) = O(n)
```

### Geometric Series
```
If T(n) = T(αn) + O(n) where α < 1:
T(n) = n + αn + α²n + α³n + ...
     = n(1 + α + α² + α³ + ...)
     = n · 1/(1-α)
     = O(n)
```

**Examples:**
- α = 0.75: converges to 4n
- α = 0.9: converges to 10n
- α = 0.5: converges to 2n

### Percentile Positions (0-indexed)
```
Median (50th):     k = n // 2
Top 10%:          k = int(0.9 * n)
Bottom 25%:        k = int(0.25 * n) - 1
80th percentile:   k = int(0.8 * n)
```

---

## Exam Strategy Checklist

When you see a quickselect/partition problem:

- [ ] **Identify the pattern**: percentile, k-closest, matching, partitioning?
- [ ] **Determine required complexity**: O(n), O(n log n), O(n log k)?
- [ ] **Choose pivot strategy**: random (average case) or MoM (worst case)?
- [ ] **If MoM question**: Prepare full 4-part explanation
- [ ] **Check partition scheme**: Hoare, DNF, or custom?
- [ ] **Count Quickselect calls**: Multiple calls still O(n) if on shrinking input
- [ ] **Don't forget**: Quickselect doesn't sort!

---

## Practice Problem Checklist

Make sure you can solve:
- ✓ s1-Q4: MoM justification (2 marks)
- ✓ s1-Q5: Percentile selection with Quickselect (3 marks)
- ✓ s3-Q3: Radix sort base analysis
- ✓ Mid-sem Q3: Clustering with MST (conceptually related to partitioning)
- ✓ Week 4 Applied: All problems 1-7

---

## Final Tips

1. **For MoM questions:** Always include geometric series proof
2. **For percentile questions:** Sketch the array and mark positions
3. **For complexity questions:** Separate comparisons from total time
4. **For partition questions:** Know when to use Hoare vs DNF
5. **Practice writing:** MoM explanation until you can do it in 3 minutes

**Remember:** Quickselect + MoM is worth understanding deeply - it appears in almost every exam!