# Exam 25-2: Question 1 Solution

**Course:** FIT2004 Algorithms and Data Structures
**Institution:** Monash University
**Topic:** Complexity Analysis (Space, Auxiliary Space, Time)
**Question Type:** Multiple Select
**Total Marks:** 3

---

## Question Statement

Consider the code shown below that takes a positive integer n as input. **Select all the correct options** regarding the space, auxiliary space, and time complexities of this code.

```python
def mystery(n):
    if n == 0:
        return 1
    else:
        return 7*mystery(n-1)+1
```

---

## Student's Answer

### Selected Answers

**✗ Selected (1 option only):**
- **time_2**: "The worst-case time complexity is Θ((log N)^c)" - **INCORRECT**

**Missed correct answers:**
1. **space_3**: "The worst-case space complexity is Θ(N)." - NOT SELECTED
2. **aux_space_3**: "The worst-case auxiliary space complexity is Θ(N)." - NOT SELECTED
3. **time_3**: "The worst-case time complexity is Θ(N)." - NOT SELECTED

---

## Detailed Reasoning (Based on Course Materials)

### 1. Time Complexity Analysis

**Recurrence Relation:**
```
T(n) = T(n-1) + O(1)    [recursive call + constant operations]
T(0) = O(1)              [base case]
```

**Solution Method (from course_notes/chap_one.json):**

According to **Section 1.2 Complexity Analysis**, the common recurrence pattern for linear recursion is:
- **Relation:** `T(n) = T(n-1) + a`
- **Solution:** `T(n) = a·n + b`
- **Complexity:** **O(n) - Linear**

**From mid_semester_test/analysis/RECURRENCE_RELATIONS_GUIDE.md:**

> Type 1: Subtracting a Constant - T(n) = T(n-c) + f(n)
>
> If f(n) = O(1) = O(n^0), then T(n) = O(n^1) = **O(n)**
>
> **Why?** You make roughly n/c recursive calls, and at each call you do work proportional to n^k.

**Expansion proof:**
```
T(n) = T(n-1) + c
     = [T(n-2) + c] + c = T(n-2) + 2c
     = [T(n-3) + c] + 2c = T(n-3) + 3c
     ...
     = T(0) + n·c
     = O(n)
```

**Answer:** ✓ **time_3: Θ(N)** is CORRECT

**Why NOT logarithmic?**

From **RECURRENCE_RELATIONS_GUIDE.md**, logarithmic complexity O(log n) occurs with:
- Pattern: `T(n) = T(n/2) + O(1)` (dividing by 2, not subtracting 1)
- Example: Binary search

The key difference:
- **Linear recursion** (n → n-1 → n-2 → ... → 0) makes **n calls** → O(n)
- **Divide-and-conquer** (n → n/2 → n/4 → ... → 1) makes **log n calls** → O(log n)

---

### 2. Space Complexity Analysis

**From lecture/l1.json - Complexity Definitions:**

> **space_complexity:** "Total amount of space taken by algorithm as function of input size"

**Analysis:**
- **Input space:** The integer `n` itself takes O(1) space (single integer)
- **Recursion stack space:** The function makes recursive calls from n down to 0
  - Maximum recursion depth = n
  - Each call frame stores: return address, parameter n, local computation
  - Space per frame = O(1)
  - Total stack space = depth × space per frame = n × O(1) = O(n)

**Total space = O(1) [input] + O(n) [call stack] = O(n)**

**Answer:** ✓ **space_3: Θ(N)** is CORRECT

---

### 3. Auxiliary Space Complexity Analysis

**From lecture/l1.json - Auxiliary Space Definition:**

> **auxiliary_space_complexity:** "Amount of space taken by algorithm EXCLUDING space taken by input"
>
> **Important note:** "In this unit, in-place means O(1) auxiliary space, including recursion stack"

**From lecture/l1.json - Recursion Space Example:**

Under "power_functions" section:
> ```
> power1_recursive:
>   space_analysis:
>     recursion_depth: O(n)
>     local_space: O(1) per call
>     analysis: "Total space = local space * maximum recursion depth = O(1) * O(n)"
>     complexity: O(n)
>   auxiliary_space: "O(n) - recursion depth"
>   in_place: false
> ```

**Common Mistake (from lecture/l1.json):**

> **mistake_3:**
> - Error: "Forgetting recursion uses space"
> - Correction: "Recursive calls create stack frames - count this in space complexity"

**Analysis for mystery(n):**
- Input space (integer n) = O(1) - **EXCLUDED from auxiliary space**
- Recursion call stack = O(n) - **INCLUDED in auxiliary space**
- No additional data structures created

**Auxiliary space = O(n) due to recursion depth**

**Answer:** ✓ **aux_space_3: Θ(N)** is CORRECT

---

## Why Other Options Are Wrong

### Space Complexity Options

- **space_1:** Θ(1) - ❌ **Incorrect**
  - Ignores the recursion call stack which grows to depth n

- **space_2:** Θ((log N)^c) - ❌ **Incorrect**
  - Would require divide-and-conquer pattern like T(n) = T(n/2) + O(1)
  - This function uses linear recursion T(n) = T(n-1) + O(1)

- **space_4:** Θ(N·(log N)^c) - ❌ **Incorrect**
  - Too large; function only uses linear space

- **space_5:** Θ(N²) - ❌ **Incorrect**
  - Would require each recursive call to use O(n) space

### Auxiliary Space Options

- **aux_space_1:** Θ(1) - ❌ **Incorrect**
  - Common mistake: forgetting to count recursion stack
  - Course material explicitly warns about this (lecture/l1.json mistake_3)

- **aux_space_2:** Θ((log N)^c) - ❌ **Incorrect**
  - Same reasoning as space_2

- **aux_space_4, aux_space_5** - ❌ **Incorrect**
  - Too large for this linear recursion pattern

### Time Complexity Options

- **time_1:** Θ(1) - ❌ **Incorrect**
  - Function makes n recursive calls, not constant

- **time_2:** Θ((log N)^c) - ❌ **Incorrect**
  - **Common confusion:** Mixing up linear recursion with divide-and-conquer
  - From RECURRENCE_RELATIONS_GUIDE.md:
    - `T(n) = T(n-1) + O(1)` → O(n) [Linear recursion - what we have]
    - `T(n) = T(n/2) + O(1)` → O(log n) [Binary search pattern]

- **time_4:** Θ(N·(log N)^c) - ❌ **Incorrect**
  - Too large; would need pattern like T(n) = 2T(n/2) + O(n) (merge sort)

- **time_5:** Θ(N²) - ❌ **Incorrect**
  - Would need pattern like T(n) = T(n-1) + O(n)

---

## Key Insights from Course Materials

### From course_notes/chap_one.json

1. **Linear recursion pattern:**
   - `T(n) = T(n-1) + a` solves to `T(n) = a·n + b`
   - Result: **O(n) time complexity**

2. **Why the constant 7 doesn't matter:**
   - The multiplication `7*mystery(n-1)` is a constant-time operation
   - Big-Θ notation ignores constant factors
   - Only the number of recursive calls matters: n calls

### From lecture/l1.json

3. **Space vs Auxiliary Space:**
   - Space complexity = input space + auxiliary space
   - Auxiliary space = extra space excluding input
   - **Critical:** Recursion stack counts as auxiliary space

4. **Recursion depth determines space:**
   - Each recursive call adds a stack frame
   - Stack frame contains: return address, parameters, local variables
   - Total space = recursion depth × space per frame

### From mid_semester_test/analysis/RECURRENCE_RELATIONS_GUIDE.md

5. **Recurrence pattern recognition:**
   - Subtract constant → one degree higher in complexity
   - `T(n) = T(n-1) + O(1)` → bump O(1) = O(n^0) to O(n^1) = **O(n)**

6. **Mental check method:**
   - "How many times does the function call itself?" → n times
   - "How much work per call?" → O(1)
   - "Total work?" → n × O(1) = **O(n)**

---

## Marking Scheme

**Total Marks Available:** 3
**Marks Awarded:** **0/3** ✗

**Grading Criteria:** All three correct options (space_3, aux_space_3, time_3) must be selected for full marks.

**Result:** Only selected time_2 (incorrect). Did not select any of the three correct options. **Zero marks awarded.**

---

## Summary Table

| Complexity Type | Student Selected | Correct Answer | Correct? | Marks |
|----------------|------------------|----------------|----------|-------|
| Time | time_2 (Θ((log N)^c)) | time_3 (Θ(N)) | ✗ No | 0/1 |
| Space | (not selected) | space_3 (Θ(N)) | ✗ No | 0/1 |
| Auxiliary Space | (not selected) | aux_space_3 (Θ(N)) | ✗ No | 0/1 |
| **TOTAL** | | | | **0/3** |

---

## References

1. **course_notes/chap_one.json** - Section 1.2: Complexity Analysis
   - Common recurrence relations and their solutions
   - Linear recurrence pattern: T(n) = T(n-1) + a → O(n)

2. **lecture/l1.json** - Complexity Definitions and Common Mistakes
   - Space complexity vs auxiliary space complexity definitions
   - Recursion stack space analysis
   - Common mistake: forgetting recursion uses space

3. **mid_semester_test/analysis/RECURRENCE_RELATIONS_GUIDE.md**
   - Type 1 recurrences (subtracting constants)
   - Mental calculation methods for exam
   - Pattern recognition for complexity classes
