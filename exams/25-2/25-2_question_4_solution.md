# Exam 25-2: Question 4 Solution

**Course:** FIT2004 Algorithms and Data Structures
**Institution:** Monash University
**Topic:** Dynamic Programming - Minimum Operations
**Question Type:** Numerical Answer
**Total Marks:** 3

---

## Question Statement

Consider the problem in which you are given as input a positive integer to be used as the starting value, and you want to return the minimum number of operations to go from the starting value to 1 given that the allowed operations are:

### Allowed Operations

1. **Subtract 1**
   - Constraint: none
   - Always available

2. **Divide by 2**
   - Constraint: current value is divisible by 2 over the integers
   - Only available when current value is even

3. **Divide by 3**
   - Constraint: current value is divisible by 3 over the integers
   - Only available when current value is divisible by 3

### Notation

**MIN_OP(n)** = the minimum number of operations to go from n to 1

### Specific Question

Calculate: **x = MIN_OP(10) + MIN_OP(14) + MIN_OP(15)**

What is the value of x? (Just type the numerical answer)

---

## My Solution

**Submitted Answer: 12**

**Status:**  **INCORRECT**
**Correct Answer:** **11**
**Marks Awarded:** **0/3**

---

## Dynamic Programming Solution Framework

### Algorithm Type
Dynamic Programming (can be solved bottom-up or top-down with memoization)

### State Definition
- **State:** MIN_OP(n)
- **Meaning:** Minimum operations to reduce n to 1

### Base Case
```
MIN_OP(1) = 0
```
**Explanation:** Already at target, no operations needed

### Recurrence Relation

**General Form:**
```
MIN_OP(n) = 1 + min(available_operations)
```

**Specific Cases:**

| Condition | Formula | Available Choices |
|-----------|---------|-------------------|
| n divisible by both 2 and 3 (i.e., by 6) | MIN_OP(n) = 1 + min(MIN_OP(n-1), MIN_OP(n/2), MIN_OP(n/3)) | 3 choices |
| n divisible by 2 only | MIN_OP(n) = 1 + min(MIN_OP(n-1), MIN_OP(n/2)) | 2 choices |
| n divisible by 3 only | MIN_OP(n) = 1 + min(MIN_OP(n-1), MIN_OP(n/3)) | 2 choices |
| n not divisible by 2 or 3 | MIN_OP(n) = 1 + MIN_OP(n-1) | 1 choice |

### Implementation (Bottom-Up)

```python
def min_operations_to_one(n):
    """
    Compute minimum operations to reduce n to 1
    Operations: -1, /2 (if even), /3 (if divisible by 3)
    """
    # DP array: dp[i] = min operations to reach 1 from i
    dp = [0] * (n + 1)

    # Base case
    dp[1] = 0

    # Build up from 2 to n
    for i in range(2, n + 1):
        # Option 1: Subtract 1 (always available)
        dp[i] = 1 + dp[i - 1]

        # Option 2: Divide by 2 (if even)
        if i % 2 == 0:
            dp[i] = min(dp[i], 1 + dp[i // 2])

        # Option 3: Divide by 3 (if divisible by 3)
        if i % 3 == 0:
            dp[i] = min(dp[i], 1 + dp[i // 3])

    return dp[n]

# Calculate the answer
x = min_operations_to_one(10) + min_operations_to_one(14) + min_operations_to_one(15)
print(f"x = {x}")
```

---

## Detailed Computation

### Complete DP Table (1 to 15)

Let me build the complete table:

| n | Divisible by | Available Operations | Calculation | MIN_OP(n) | Optimal Path |
|---|--------------|---------------------|-------------|-----------|--------------|
| 1 | - | - | Base case | **0** | - |
| 2 | 2 | -1, /2 | min(1+0, 1+0) | **1** | 2→1 |
| 3 | 3 | -1, /3 | min(1+1, 1+0) | **1** | 3→1 |
| 4 | 2 | -1, /2 | min(1+1, 1+1) | **2** | 4→2→1 |
| 5 | - | -1 | 1+2 | **3** | 5→4→2→1 |
| 6 | 2,3 | -1, /2, /3 | min(1+3, 1+1, 1+1) | **2** | 6→3→1 or 6→2→1 |
| 7 | - | -1 | 1+2 | **3** | 7→6→3→1 |
| 8 | 2 | -1, /2 | min(1+3, 1+2) | **3** | 8→4→2→1 |
| 9 | 3 | -1, /3 | min(1+3, 1+1) | **2** | 9→3→1 |
| **10** | **2** | **-1, /2** | **min(1+2, 1+3)** | **3** | **10→9→3→1** |
| 11 | - | -1 | 1+3 | **4** | 11→10→9→3→1 |
| 12 | 2,3 | -1, /2, /3 | min(1+4, 1+2, 1+2) | **3** | 12→6→3→1 or 12→4→2→1 |
| 13 | - | -1 | 1+3 | **4** | 13→12→6→3→1 |
| **14** | **2** | **-1, /2** | **min(1+4, 1+2)** | **4** | **14→7→6→3→1** |
| **15** | **3** | **-1, /3** | **min(1+4, 1+3)** | **4** | **15→5→4→2→1** |

### Step-by-Step Computation

#### MIN_OP(10)

```
10 is even (divisible by 2)
Options:
  - Subtract 1: 10 → 9, then MIN_OP(9) = 2
    Total: 1 + 2 = 3
  - Divide by 2: 10 → 5, then MIN_OP(5) = 3
    Total: 1 + 3 = 4

MIN_OP(10) = min(3, 4) = 3
Optimal path: 10 → 9 → 3 → 1
```

**Verification:**
- 10 → 9 (subtract 1)
- 9 → 3 (divide by 3)
- 3 → 1 (divide by 3)
- **Total: 3 operations** 

#### MIN_OP(14)

```
14 is even (divisible by 2)
Options:
  - Subtract 1: 14 → 13, then MIN_OP(13) = 4
    Total: 1 + 4 = 5
  - Divide by 2: 14 → 7, then MIN_OP(7) = 3
    Total: 1 + 3 = 4

MIN_OP(14) = min(5, 4) = 4
Optimal path: 14 → 7 → 6 → 3 → 1
```

**Verification:**
- 14 → 7 (divide by 2)
- 7 → 6 (subtract 1)
- 6 → 3 (divide by 2) or 6 → 2 (divide by 3)
- 3 → 1 (divide by 3) or 2 → 1 (divide by 2)
- **Total: 4 operations** 

#### MIN_OP(15)

```
15 is divisible by 3
Options:
  - Subtract 1: 15 → 14, then MIN_OP(14) = 4
    Total: 1 + 4 = 5
  - Divide by 3: 15 → 5, then MIN_OP(5) = 3
    Total: 1 + 3 = 4

MIN_OP(15) = min(5, 4) = 4
Optimal path: 15 → 5 → 4 → 2 → 1
```

**Verification:**
- 15 → 5 (divide by 3)
- 5 → 4 (subtract 1)
- 4 → 2 (divide by 2)
- 2 → 1 (divide by 2)
- **Total: 4 operations** 

### Final Answer

```
x = MIN_OP(10) + MIN_OP(14) + MIN_OP(15)
x = 3 + 4 + 4
x = 11
```

**Correct Answer: 11**
**My Answer: 12**
**Error: +1** (likely miscounted one of the values)

---

## Why Greedy Doesn't Work

### Greedy Approach (INCORRECT)
"Always divide when possible"

**Counterexample with n=10:**

Greedy path:
```
10 → 5 (divide by 2)
5 → 4 (subtract 1)
4 → 2 (divide by 2)
2 → 1 (divide by 2)
Total: 4 operations
```

Optimal path:
```
10 → 9 (subtract 1)
9 → 3 (divide by 3)
3 → 1 (divide by 3)
Total: 3 operations 
```

**Lesson:** Sometimes subtracting first sets up better division opportunities later. This is why dynamic programming is necessary.

---

## Complexity Analysis

### Time Complexity

| Approach | Time Complexity | Explanation |
|----------|-----------------|-------------|
| Naive Recursive | O(3^n) | Each call can make up to 3 recursive calls |
| Top-down with Memoization | O(n) | Each state computed once, constant work per state |
| **Bottom-up DP** | **O(n)** | Single loop from 2 to n, constant work per iteration |

### Space Complexity

| Approach | Space Complexity | Explanation |
|----------|------------------|-------------|
| Top-down with Memoization | O(n) | Memoization array + recursion stack |
| **Bottom-up DP** | **O(n)** | DP array only |
| Space-optimized | O(1) | If only computing specific values without storing all |

---

## Common Mistakes

### Mistake 1: Forgetting divisibility constraints
**Error:** Attempting to divide by 2 or 3 without checking divisibility
**Correction:** Always check `n % 2 == 0` before dividing by 2, `n % 3 == 0` before dividing by 3

### Mistake 2: Not considering all operations
**Error:** Only trying division operations when available
**Correction:** Subtraction is ALWAYS available and must be considered

### Mistake 3: Off-by-one errors in counting operations
**Error:** Counting states instead of transitions
**Correction:** Each operation is a transition. Path 10→9→3→1 has 3 transitions, not 4 states

### Mistake 4: Greedy approach
**Error:** Always choosing division over subtraction
**Correction:** Use DP to explore all possibilities. Sometimes subtraction first is better.

### Mistake 5: Computational errors
**Error:** Miscalculating one of the MIN_OP values (my mistake!)
**Correction:** Build complete DP table systematically, verify each step

---

## Edge Cases

### Case 1: n = 1
- **Result:** 0 operations (base case)
- **Path:** Already at target

### Case 2: n is a power of 2 (e.g., 8, 16, 32)
- **Observation:** Can repeatedly divide by 2 efficiently
- **Example:** 8 → 4 → 2 → 1 (3 operations)
- **Formula:** MIN_OP(2^k) = k

### Case 3: n is a power of 3 (e.g., 9, 27, 81)
- **Observation:** Can repeatedly divide by 3 efficiently
- **Example:** 9 → 3 → 1 (2 operations)
- **Formula:** MIN_OP(3^k) = k

### Case 4: n is prime and > 3
- **Observation:** Must subtract 1 first, then proceed from n-1
- **Example:** MIN_OP(7) = 1 + MIN_OP(6) = 1 + 2 = 3

### Case 5: n is divisible by 6
- **Observation:** Three operations available, must choose optimally
- **Example:** MIN_OP(6) = min(1+MIN_OP(5), 1+MIN_OP(3), 1+MIN_OP(2)) = min(4, 2, 2) = 2

---

## Related Problems

### Similar DP Problems

1. **Coin Change (Minimum Coins)**
   - Given coin denominations, find minimum coins to make amount
   - Similar recurrence structure: MIN_COINS(n) = 1 + min over all coins

2. **Fibonacci Numbers**
   - Classic DP example with overlapping subproblems
   - Shows memoization benefits

3. **Climbing Stairs**
   - Minimum cost to reach top
   - Similar choice structure at each step

### Problem Variations

1. **Different set of allowed operations**
   - E.g., Can also multiply by 2
   - Same DP approach, different recurrence

2. **Finding the actual sequence of operations**
   - Store parent pointers in DP table
   - Backtrack from n to 1 to reconstruct path

3. **Weighted operations (different costs)**
   - E.g., Subtraction costs 1, division costs 2
   - Modify recurrence to account for costs

4. **Multiple target values**
   - Compute MIN_OP for multiple starting values
   - Can reuse DP table if computing max value first

---

## Problem-Solving Strategy

### Step-by-Step Approach

1. **Start with base case:** MIN_OP(1) = 0

2. **Build up values systematically** for small n:
   - MIN_OP(2) = 1
   - MIN_OP(3) = 1
   - MIN_OP(4) = 2
   - ...continue to 15

3. **For each n, consider which operations are valid:**
   - Check divisibility by 2 and 3
   - Compute min over available choices

4. **Compute required values:**
   - MIN_OP(10), MIN_OP(14), MIN_OP(15)

5. **Sum the three values**

### Mental Calculation Tips

For small values during exams:
- Recognize powers of 2 and 3 immediately
- Work backwards from n to 1, exploring paths
- Use memoization on scratch paper for values you compute

---

## Verification Approach

### Methods to Verify Answer

1. **Build complete DP table from 1 to max(10, 14, 15) = 15**
   - Systematic, less error-prone
   - Can verify intermediate values

2. **Trace back optimal paths**
   - Verify each path actually uses computed number of operations
   - Check that all operations are valid

3. **Cross-check with alternative computation**
   - Top-down vs bottom-up should give same answer
   - Recursive with memoization as verification

4. **Test boundary cases**
   - MIN_OP(1) should be 0
   - MIN_OP(2) should be 1
   - MIN_OP(3) should be 1

---

## Marking Scheme

**Total Marks Available:** 3
**Marks Awarded:** **0/3**

**Grading Criteria:** All-or-nothing for correct numerical answer

**Student Answer:** 12
**Correct Answer:** 11
**Difference:** +1 (likely miscounted one of the three values)

**Feedback:** Incorrect. Student answered 12, correct answer is 11 (3+4+4). Ensure systematic computation and verification of each MIN_OP value.

---

## Summary

| Value | Computation | MIN_OP | Optimal Path |
|-------|-------------|--------|--------------|
| **10** | min(1+MIN_OP(9), 1+MIN_OP(5)) = min(3,4) | **3** | 10→9→3→1 |
| **14** | min(1+MIN_OP(13), 1+MIN_OP(7)) = min(5,4) | **4** | 14→7→6→3→1 |
| **15** | min(1+MIN_OP(14), 1+MIN_OP(5)) = min(5,4) | **4** | 15→5→4→2→1 |
| **x** | 3 + 4 + 4 | **11** | - |

**My Answer:** 12 
**Correct Answer:** 11 
**Score:** 0/3

---

## Key Takeaways

1. **DP is necessary** - Greedy doesn't work for this problem
2. **Build systematically** - Use bottom-up DP table to avoid errors
3. **Verify each step** - Check intermediate values
4. **Consider all operations** - Subtraction is always available
5. **Watch for computation errors** - Double-check arithmetic in exams

---

## References

1. **course_notes/** (Dynamic Programming chapters)
   - DP problem recognition
   - Recurrence relation formulation
   - Bottom-up vs top-down approaches

2. **implementations-algorithms/w6/**
   - `coinChangeBottomUp.py` - Similar DP structure
   - `coinChangeTopDown.py` - Memoization example

3. **Exam file:** exams/25-2/25-2_part1.json (question 4)
   - Original problem statement
   - Expected solution with detailed computation
