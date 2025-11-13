# Exam 25-2: Question 2 Solution

**Course:** FIT2004 Algorithms and Data Structures
**Institution:** Monash University
**Topic:** Loop Invariants and Heap Data Structures
**Question Type:** Multiple Choice
**Total Marks:** 3

---

## Question Statement

Given the following pseudocode, which loop invariant is correct?

```python
function MYSTERY(A[1...n], k)
    # Initialise an empty MaxHeap named mh with the k first elements of A
    i = k + 1
    while i ≤ n do
        if A[i] < mh.max_element() then
            mh.pop()
            mh.push(A[i])
        // Loop invariant here
        i = i + 1
    return mh
```

**Heap Operations:**
- `mh.max_element()` - returns maximum element without removing
- `mh.pop()` - removes maximum element
- `mh.push(x)` - inserts element x

### Answer Choices

a) mh contains the i biggest elements of A[1...k]
b) mh contains the k biggest elements of A[1...i+1]
c) mh contains the i biggest elements of A[1...k+i]
**d) mh contains the k smallest elements of A[1...i]** ✓
e) mh contains the k biggest elements of A[1...i]
f) mh contains the i smallest elements of A[1...k]
g) mh contains the i smallest elements of A[1...k+i]
h) mh contains the k smallest elements of A[1...i+1]

---

## My Solution

**Selected Answer: d) mh contains the k smallest elements of A[1...i]**

**Status:** ✓ **CORRECT**
**Marks Awarded:** **3/3**

---

## Detailed Reasoning

### Algorithm Purpose

This algorithm solves the **k-smallest-elements problem**: finding the k smallest elements from an array of n elements using a MaxHeap of size k.

**Key Insight:** Why use a **MaxHeap** to find the **smallest** elements?
- The MaxHeap maintains the k smallest elements seen so far
- The root (maximum) represents the **largest of the k smallest** elements
- This is the threshold: any new element smaller than this belongs in the top k smallest
- We can check and remove the max in O(1) and O(log k) respectively

### Loop Invariant Analysis

**The correct loop invariant is:**
**"mh contains the k smallest elements of A[1...i]"**

Let me prove this satisfies all three requirements of a loop invariant:

#### 1. Initialization (Before loop starts)

**State:** `i = k + 1`, `mh` contains `A[1...k]`

**Check:** Does "mh contains the k smallest elements of A[1...k]" hold?
- YES! mh contains all k elements of A[1...k]
- These are trivially the k smallest (and only) elements of A[1...k]
- ✓ **Invariant holds initially**

#### 2. Maintenance (Loop preserves invariant)

**Assume:** At start of iteration i, "mh contains the k smallest of A[1...i-1]" holds (inductive hypothesis)

**Goal:** Show "mh contains the k smallest of A[1...i]" after processing A[i]

**Case 1:** `A[i] < mh.max_element()`
- A[i] is smaller than the largest element in mh
- This means A[i] belongs in the k smallest of A[1...i]
- We remove the current max (which is now outside the k smallest)
- We insert A[i] (which is now inside the k smallest)
- Result: mh contains the k smallest of A[1...i] ✓

**Case 2:** `A[i] ≥ mh.max_element()`
- A[i] is not smaller than any element in mh
- A[i] is not among the k smallest of A[1...i]
- We don't modify mh (it already contains the k smallest)
- Result: mh contains the k smallest of A[1...i] ✓

- ✓ **Invariant maintained after each iteration**

#### 3. Termination (When loop ends)

**State:** Loop ends when `i = n + 1`

**Invariant says:** "mh contains the k smallest elements of A[1...n]"

**This is exactly what we want!** The algorithm correctly returns the k smallest elements of the entire array.

- ✓ **Invariant proves algorithm correctness**

---

## Why Other Options Are Wrong

### Option a: "mh contains the i biggest elements of A[1...k]"
❌ **Range error** - Only considers first k elements, but i > k
❌ **Size error** - Heap size is k, not i
❌ **Direction error** - Algorithm finds smallest, not biggest

### Option b: "mh contains the k biggest elements of A[1...i+1]"
❌ **Off-by-one error** - At start of iteration i, we've only processed up to i-1
❌ **Direction error** - Algorithm finds smallest, not biggest

### Option c: "mh contains the i biggest elements of A[1...k+i]"
❌ **Size error** - Heap size is k, not i
❌ **Range error** - Range A[1...k+i] doesn't match loop variable
❌ **Direction error** - Algorithm finds smallest, not biggest

### Option e: "mh contains the k biggest elements of A[1...i]"
❌ **Direction error** - This is the critical mistake!
- The algorithm uses a **MaxHeap** and **removes the maximum**
- If we wanted k biggest, we would use a **MinHeap** and remove minimum
- By removing the max when finding smaller elements, we keep the k **smallest**

**From topics/LOOP_INVARIANT_QUESTIONS_GUIDE.md:**
> "Common mistake: Confusing heap type with algorithm purpose"
> - MaxHeap for k smallest (remove max when finding smaller)
> - MinHeap for k largest (remove min when finding larger)

### Option f: "mh contains the i smallest elements of A[1...k]"
❌ **Range error** - Only considers first k elements
❌ **Size error** - Heap contains k elements, not i

### Option g: "mh contains the i smallest elements of A[1...k+i]"
❌ **Size error** - Heap size is k (constant), not i (variable)

### Option h: "mh contains the k smallest elements of A[1...i+1]"
❌ **Off-by-one error** - Should be A[1...i], not A[1...i+1]
- At the invariant point (start of iteration), we haven't processed A[i] yet
- We've only processed A[1...i-1], but with i incremented, the invariant refers to having processed through index i-1

---

## Algorithm Complexity Analysis

### Time Complexity: O(n log k)

**Breakdown:**
- Initialize heap with k elements: O(k log k) using repeated insertions
  - (Can be optimized to O(k) with bottom-up heapify)
- Process remaining (n-k) elements: O((n-k) log k)
  - Each element: O(1) comparison + possibly O(log k) pop + O(log k) push
  - At most O(log k) per element
- **Total:** O(k log k) + O((n-k) log k) = **O(n log k)**

**Why this is efficient:**
- Compare to sorting entire array: O(n log n)
- When k << n, log k << log n, significant improvement
- Example: Finding 10 smallest in 1,000,000 elements
  - This algorithm: O(1M × log 10) ≈ O(1M × 3.3) = O(3.3M) operations
  - Full sort: O(1M × log 1M) ≈ O(1M × 20) = O(20M) operations

### Space Complexity: O(k)

**Heap storage:** O(k) for the MaxHeap
**No additional structures:** Just variables i, and temporary storage
**Total:** **O(k)** auxiliary space

---

## Key Insights from Course Materials

### From topics/LOOP_INVARIANT_QUESTIONS_GUIDE.md

**Three Properties of Loop Invariants:**
1. ✓ Initialization: True before loop starts
2. ✓ Maintenance: If true before iteration, remains true after
3. ✓ Termination: When loop ends, invariant + termination condition → correctness

**Common mistakes to avoid:**
- Off-by-one errors in array ranges
- Forgetting what has been processed at the invariant point
- Confusing the heap type (Max/Min) with algorithm purpose

### From course_notes/ - Heap Properties

**MaxHeap property:**
- Parent ≥ all children
- Root is maximum element
- Access max in O(1)
- Remove max in O(log n)
- Insert in O(log n)

**Why MaxHeap for k-smallest?**
> "To maintain k smallest elements, we need quick access to the largest of these k elements (the 'threshold'). Any element smaller than this threshold replaces it. MaxHeap gives us O(1) access to this threshold."

### From mid_semester_test/ Materials

**Loop Invariant Checking Strategy:**
1. Identify loop variable and its range
2. Determine what has been processed at invariant point
3. Check initialization (typically with smallest/first values)
4. Trace one iteration to verify maintenance
5. Check termination gives desired result

---

## Related Problems and Patterns

### k-Smallest Elements Problem Variants

**1. Using MaxHeap (this algorithm) - O(n log k) time, O(k) space**
- Best when k << n (finding few elements from many)
- Example: Top 10 smallest from 1 million

**2. Using QuickSelect - O(n) average time, O(1) space**
- Best for finding exact k-th smallest (median finding)
- Modifies array in-place

**3. Full Sort - O(n log n) time, O(1) or O(n) space**
- Best when k ≈ n (need most elements sorted)
- Also useful when elements must be in order

### Dual Problem: k-Largest Elements

**Algorithm:** Same structure, but use **MinHeap** instead
```python
function K_LARGEST(A[1...n], k)
    # Initialize MinHeap with first k elements
    for i = k+1 to n:
        if A[i] > mh.min_element():  # Note: > instead of <
            mh.pop()                  # Remove minimum
            mh.push(A[i])
    return mh
```

**Loop Invariant:** "mh contains the k largest elements of A[1...i]"

---

## Exam Strategy Tips

### Quick Recognition Checklist

When analyzing heap-based loop invariants:

1. **Check heap type:**
   - MaxHeap → likely finding smallest elements
   - MinHeap → likely finding largest elements

2. **Check operation:**
   - Removing max/min → replacing it with better candidate
   - Comparing with max/min → it's the threshold

3. **Check size:**
   - Heap size should be constant k, not variable i

4. **Check range:**
   - Should match what's been processed up to loop variable
   - Watch for off-by-one errors

5. **Verify initialization:**
   - What's in heap before loop starts?
   - Does invariant hold at that point?

### Common Traps

❌ **Trap 1:** "MaxHeap finds biggest elements"
- Wrong! MaxHeap provides quick access to max, but algorithm logic determines what we're finding
- This algorithm removes max when finding smaller → keeps smallest

❌ **Trap 2:** "The range should be i+1 because we increment i"
- At the invariant point (start of iteration), i hasn't been processed yet
- The invariant describes state before processing current i

❌ **Trap 3:** "Heap contains i elements"
- Heap size is k (constant), initialized once
- i is just the loop counter

---

## Marking Scheme

**Total Marks Available:** 3
**Marks Awarded:** **3/3** ✓

**Grading Criteria:** Select the single correct loop invariant

**Result:** Correct answer (option d) selected. **Full marks awarded.**

---

## Summary

| Aspect | Answer |
|--------|--------|
| **Correct Loop Invariant** | mh contains the k smallest elements of A[1...i] |
| **Algorithm Purpose** | Find k smallest elements from array |
| **Data Structure** | MaxHeap of size k |
| **Key Insight** | MaxHeap's root = largest of k smallest = threshold |
| **Time Complexity** | O(n log k) |
| **Space Complexity** | O(k) |
| **Student Answer** | Option d ✓ |
| **Marks** | **3/3** |

---

## References

1. **topics/LOOP_INVARIANT_QUESTIONS_GUIDE.md**
   - Three properties of loop invariants
   - Common mistakes in invariant analysis
   - Verification strategies

2. **course_notes/** (Heap chapters)
   - MaxHeap and MinHeap properties
   - k-smallest and k-largest problems
   - Heap operation complexities

3. **mid_semester_test/README.md**
   - Loop invariant checking strategies
   - Heap-based algorithm patterns

4. **Exam file:** exams/25-2.json (question 2)
   - Original problem statement
   - All answer choices with detailed analysis
