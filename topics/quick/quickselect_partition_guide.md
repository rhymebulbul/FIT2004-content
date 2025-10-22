# Comprehensive Approach to Solve QuickSelect Partition Problem

## Problem Statement
Given initial array `[2, 3, 7, 8, 4, 9, 1, 10, 6, 5]`, find the 4th order statistic (k_index = 3) using FIT2004 Hybrid Hoare Partition. After **exactly 2 rounds**, determine which statements about the array are true.

---

## APPROACH OVERVIEW

### The Master Strategy
```
1. Understand the algorithm rules precisely
2. Set up a systematic tracking template
3. Execute Round 1 step-by-step
4. Execute Round 2 step-by-step
5. Read final array and check all options
```

---

## STEP 1: Understand FIT2004 Hybrid Hoare Partition Rules

### Algorithm Pseudocode
```python
def fit2004_partition(A, low, high):
    pivot = A[low]  # First element is pivot
    L = low + 1
    R = high

    while L < R:
        # L moves RIGHT until A[L] > pivot (strict >)
        while L <= high and A[L] <= pivot:
            L += 1

        # R moves LEFT until A[R] <= pivot (includes =)
        while R >= low and A[R] > pivot:
            R -= 1

        # If they haven't crossed, swap
        if L < R:
            swap(A[L], A[R])

    # When L >= R, swap pivot with A[R]
    swap(A[low], A[R])
    return R  # Pivot's final position
```

### Critical Rules (MEMORIZE THESE!)
| Rule | Description | Why It Matters |
|------|-------------|----------------|
| **Pivot = A[low]** | Always first element of subarray | Don't pick middle or random! |
| **L stops at >** | `A[L] > pivot` (strict) | Equal values stay on left |
| **R stops at ≤** | `A[R] <= pivot` (includes =) | Handles duplicates properly |
| **Swap with R** | `swap(A[low], A[R])` at end | NOT L! This is crucial |
| **L starts at low+1** | Not low | Pivot is at low initially |
| **R starts at high** | Entire right side | Not high-1 |

---

## STEP 2: Set Up Systematic Tracking Template

### Template for Each Round
```
ROUND X: Partition subarray [low..high]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Initial State:
  Array:  [list the array]
  Pivot:  value (at index X)
  Range:  [low..high]
  L = low+1, R = high

ITERATION 1:
  ┌─ Find L: Scan right until A[L] > pivot
  │   L = ? → A[L] = ? → STOP (reason)
  ├─ Find R: Scan left until A[R] <= pivot
  │   R = ? → A[R] = ? → STOP (reason)
  └─ Check: L < R?
      ├─ YES → Swap A[L] ↔ A[R]
      │   Array after swap: [...]
      └─ NO  → DONE, go to final swap

ITERATION 2: (if L < R still)
  [repeat above]

FINAL SWAP:
  Swap A[low] ↔ A[R]
  Array: [final state]
  Pivot final position: R = ?

DECISION:
  k_index = 3, pivot_index = ?
  Next: recurse on [? .. ?]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## STEP 3: Execute Round 1 [0..9]

### Initial State
```
Array:  [2, 3, 7, 8, 4, 9, 1, 10, 6, 5]
Index:   0  1  2  3  4  5  6   7  8  9

Pivot:  2 (at index 0)
Range:  [0..9]
L = 1, R = 9
```

### Iteration 1: Find L and R

#### Finding L (moves RIGHT until A[L] > pivot=2)
```
L = 1: A[1] = 3
  Is 3 > 2? YES ✓
  STOP at L = 1
```

#### Finding R (moves LEFT until A[R] ≤ pivot=2)
```
R = 9: A[9] = 5
  Is 5 ≤ 2? NO, continue
R = 8: A[8] = 6
  Is 6 ≤ 2? NO, continue
R = 7: A[7] = 10
  Is 10 ≤ 2? NO, continue
R = 6: A[6] = 1
  Is 1 ≤ 2? YES ✓
  STOP at R = 6
```

#### Check and Swap
```
L = 1, R = 6
L < R? YES → Swap A[1] ↔ A[6]

Before: [2, 3, 7, 8, 4, 9, 1, 10, 6, 5]
         └───────swap───────┘
After:  [2, 1, 7, 8, 4, 9, 3, 10, 6, 5]
```

### Iteration 2: Find L and R again

#### Finding L (continue from L=1, move right until A[L] > pivot=2)
```
L = 2: A[2] = 7
  Is 7 > 2? YES ✓
  STOP at L = 2
```

#### Finding R (continue from R=6, move left until A[R] ≤ pivot=2)
```
R = 6: A[6] = 3
  Is 3 ≤ 2? NO, continue
R = 5: A[5] = 9
  Is 9 ≤ 2? NO, continue
R = 4: A[4] = 4
  Is 4 ≤ 2? NO, continue
R = 3: A[3] = 8
  Is 8 ≤ 2? NO, continue
R = 2: A[2] = 7
  Is 7 ≤ 2? NO, continue
R = 1: A[1] = 1
  Is 1 ≤ 2? YES ✓
  STOP at R = 1
```

#### Check L and R
```
L = 2, R = 1
L < R? NO (2 > 1) → STOP iterations
```

### Final Swap
```
Swap A[low] ↔ A[R]
Swap A[0] ↔ A[1]

Before: [2, 1, 7, 8, 4, 9, 3, 10, 6, 5]
         └─swap─┘
After:  [1, 2, 7, 8, 4, 9, 3, 10, 6, 5]

Pivot 2 is now at index 1 (its final sorted position)
```

### QuickSelect Decision
```
Target: k_index = 3 (find 4th smallest)
Pivot ended at: index 1

Compare:
  k_index (3) vs pivot_index (1)
  3 > 1 → Target is to the RIGHT of pivot

Next action: Recurse on subarray [2..9]
```

---

## STEP 4: Execute Round 2 [2..9]

### Initial State
```
Array:  [1, 2, 7, 8, 4, 9, 3, 10, 6, 5]
Index:   0  1  2  3  4  5  6   7  8  9

Working on subarray [2..9]:
        [7, 8, 4, 9, 3, 10, 6, 5]

Pivot:  7 (at index 2)
Range:  [2..9]
L = 3, R = 9
```

### Iteration 1: Find L and R

#### Finding L (moves RIGHT until A[L] > pivot=7)
```
L = 3: A[3] = 8
  Is 8 > 7? YES ✓
  STOP at L = 3
```

#### Finding R (moves LEFT until A[R] ≤ pivot=7)
```
R = 9: A[9] = 5
  Is 5 ≤ 7? YES ✓
  STOP at R = 9
```

#### Check and Swap
```
L = 3, R = 9
L < R? YES → Swap A[3] ↔ A[9]

Before: [1, 2, 7, 8, 4, 9, 3, 10, 6, 5]
                  └──────swap──────┘
After:  [1, 2, 7, 5, 4, 9, 3, 10, 6, 8]
```

### Iteration 2: Find L and R again

#### Finding L (continue from L=3, move right until A[L] > pivot=7)
```
L = 4: A[4] = 4
  Is 4 > 7? NO, continue
L = 5: A[5] = 9
  Is 9 > 7? YES ✓
  STOP at L = 5
```

#### Finding R (continue from R=9, move left until A[R] ≤ pivot=7)
```
R = 8: A[8] = 6
  Is 6 ≤ 7? YES ✓
  STOP at R = 8
```

#### Check and Swap
```
L = 5, R = 8
L < R? YES → Swap A[5] ↔ A[8]

Before: [1, 2, 7, 5, 4, 9, 3, 10, 6, 8]
                        └──swap──┘
After:  [1, 2, 7, 5, 4, 6, 3, 10, 9, 8]
```

### Iteration 3: Find L and R again

#### Finding L (continue from L=5, move right until A[L] > pivot=7)
```
L = 6: A[6] = 3
  Is 3 > 7? NO, continue
L = 7: A[7] = 10
  Is 10 > 7? YES ✓
  STOP at L = 7
```

#### Finding R (continue from R=8, move left until A[R] ≤ pivot=7)
```
R = 7: A[7] = 10
  Is 10 ≤ 7? NO, continue
R = 6: A[6] = 3
  Is 3 ≤ 7? YES ✓
  STOP at R = 6
```

#### Check L and R
```
L = 7, R = 6
L < R? NO (7 > 6) → STOP iterations
```

### Final Swap
```
Swap A[low] ↔ A[R]
Swap A[2] ↔ A[6]

Before: [1, 2, 7, 5, 4, 6, 3, 10, 9, 8]
             └────swap───┘
After:  [1, 2, 3, 5, 4, 6, 7, 10, 9, 8]

Pivot 7 is now at index 6 (its final sorted position)
```

### QuickSelect Decision
```
Target: k_index = 3
Pivot ended at: index 6

Compare:
  k_index (3) vs pivot_index (6)
  3 < 6 → Target is to the LEFT of pivot

Next action: Would recurse on [2..5]
But quiz stops after 2 rounds!
```

---

## STEP 5: Read Final Array and Check Options

### Final Array After 2 Rounds
```
[1, 2, 3, 5, 4, 6, 7, 10, 9, 8]
 0  1  2  3  4  5  6   7  8  9
```

### Systematic Option Checking

| Option | Statement | Index | Actual Value | Match? | Result |
|--------|-----------|-------|--------------|--------|--------|
| **a** | A[3] = 5 | 3 | 5 | ✓ | **TRUE** ✅ |
| **b** | A[8] = 6 | 8 | 9 | ✗ | **FALSE** ❌ |
| **c** | A[9] = 8 | 9 | 8 | ✓ | **TRUE** ✅ |
| **d** | A[0] = 2 | 0 | 1 | ✗ | **FALSE** ❌ |
| **e** | A[4] = 4 | 4 | 4 | ✓ | **TRUE** ✅ |
| **f** | A[5] = 7 | 5 | 6 | ✗ | **FALSE** ❌ |

### Answer: **a, c, e**

---

## VERIFICATION CHECKLIST

### ✓ Round 1 Verification
```
✅ Pivot was 2 (first element)
✅ L started at 1, R started at 9
✅ L stopped at first element > 2 (which was 3 at index 1)
✅ R stopped at first element ≤ 2 (which was 1 at index 6)
✅ Swapped A[1] ↔ A[6]
✅ L and R crossed (L=2, R=1)
✅ Swapped pivot with A[R]: A[0] ↔ A[1]
✅ Pivot 2 ended at index 1
✅ Result: [1, 2, 7, 8, 4, 9, 3, 10, 6, 5]
```

### ✓ Round 2 Verification
```
✅ Subarray was [2..9]
✅ Pivot was 7 (at index 2)
✅ L started at 3, R started at 9
✅ First swap: A[3]=8 ↔ A[9]=5
✅ Second swap: A[5]=9 ↔ A[8]=6
✅ L and R crossed (L=7, R=6)
✅ Swapped pivot with A[R]: A[2] ↔ A[6]
✅ Pivot 7 ended at index 6
✅ Result: [1, 2, 3, 5, 4, 6, 7, 10, 9, 8]
```

### ✓ Option Checking
```
✅ Wrote out final array with indices
✅ Checked each option systematically
✅ Verified a, c, e are true
✅ Verified b, d, f are false
```

---

## COMMON MISTAKES TO AVOID

### ❌ Mistake 1: Wrong Stopping Conditions
```
WRONG: L stops at A[L] >= pivot  ✗
RIGHT: L stops at A[L] > pivot   ✓

WRONG: R stops at A[R] < pivot   ✗
RIGHT: R stops at A[R] <= pivot  ✓
```

### ❌ Mistake 2: Swapping with Wrong Pointer
```
WRONG: swap(A[low], A[L]) at end  ✗
RIGHT: swap(A[low], A[R]) at end  ✓
```

### ❌ Mistake 3: Not Updating L/R After Swap
```
WRONG: Check L < R immediately after swap
RIGHT: Continue moving L right and R left after swap
```

### ❌ Mistake 4: Wrong Initial Values
```
WRONG: L = low, R = high-1       ✗
RIGHT: L = low+1, R = high       ✓
```

### ❌ Mistake 5: Forgetting Subarray Context
```
Round 2 works on [2..9], not [0..9]!
Pivot is at index 2, not index 0!
```

---

## EXAM STRATEGY

### Time Management
```
1. Read problem carefully         (1 min)
2. Set up template               (1 min)
3. Execute Round 1               (3-4 min)
4. Execute Round 2               (3-4 min)
5. Check all options             (2 min)
Total:                           ~10-12 min
```

### During Execution
- ✅ **Write down** each array state
- ✅ **Draw boxes** around elements being swapped
- ✅ **Label** L and R positions clearly
- ✅ **Double-check** stopping conditions
- ✅ **Verify** final swap is with A[R]

### If You Make a Mistake
- Don't erase everything!
- Mark where you went wrong
- Restart from last correct state
- Common recovery: after Round 1

---

## PRACTICE TIPS

1. **Do it manually 5+ times** with different arrays
2. **Memorize the stopping rules**: L stops at >, R stops at ≤
3. **Always track indices** explicitly
4. **Check your work** by verifying pivot placement makes sense
5. **Practice writing neatly** - exam pressure causes sloppy work

---

## Related Problems

**Reference**: Week 3 Quiz Question 2 (`/Users/rhymebulbul/repo/FIT2004-content/weekly_quiz/q3.json`)

This comprehensive guide shows exactly how to systematically trace through the FIT2004 Hybrid Hoare Partition algorithm to reach the correct answers. The key is being methodical, tracking every step, and not rushing through the pointer movements!
