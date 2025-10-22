# Recurrence Relations Quick Reference Guide

**For FIT2004 Exams: Pattern Recognition Without Hand Calculation**

---

## The Master Theorem (One Formula to Rule Them All)

For recurrences of the form: **T(n) = aT(n/b) + f(n)**

### Step 1: Calculate the Critical Exponent
```
c_crit = log_b(a)
```
This is the ONLY calculation you need!

### Step 2: Compare f(n) with n^c_crit

#### **Basic Form**: When f(n) = n^c (pure polynomial)

| Condition | Result           | Meaning |
|-----------|------------------|---------|
| **c < c_crit** | **Θ(n^c_crit)**  | Recursion dominates |
| **c = c_crit** | **Θ(n^c log n)** | Tied - add logarithm |
| **c > c_crit** | **Θ(n^c)**       | Work per level dominates |
| **c > c_crit** | **Θ(n^c log n)** | and f(n) contains log(n) |
#### **Extended Form**: When f(n) = n^c · log^k(n) (polynomial WITH log factors)

**If f(n) = n^c_crit · log^k(n)** where k ≥ 0, then:
```
T(n) = Θ(n^c_crit · log^(k+1) n)
```

**Recognition Rule**: If you see log(n) multiplied in f(n):
- First check if the polynomial part equals n^c_crit
- If YES, multiply the log power by adding 1
- If NO, use basic Master Theorem

**Examples**:
- f(n) = **n log n**, c_crit = 1 → f(n) = n^1 · log^1(n) → **Θ(n log² n)**
- f(n) = **n² log n**, c_crit = 2 → f(n) = n^2 · log^1(n) → **Θ(n² log² n)**
- f(n) = **n log³ n**, c_crit = 1 → f(n) = n^1 · log^3(n) → **Θ(n log⁴ n)**

---

## Quick log_b(a) Reference Table

**Memorize these common values:**

| a | b | log_b(a) | Memory Trick |
|---|---|----------|--------------|
| 2 | 2 | **1** | "Half and double → linear leaves" |
| 3 | 2 | **≈1.59** | "Karatsuba multiplication" |
| 4 | 2 | **2** | "2² = 4 → quadratic" |
| 8 | 2 | **3** | "2³ = 8 → cubic" |
| 1 | 2 | **0** | "No branching → logarithmic" |
| 2 | 4 | **0.5** | "√4 = 2 → square root" |
| 9 | 3 | **2** | "3² = 9 → quadratic" |

**Quick Formula**: log_b(a) asks "**b to what power equals a?**"
- Example: log₄(2) → "4^? = 2" → 4^0.5 = 2 → **0.5**

---

## Common Patterns - Instant Recognition

### Divide-and-Conquer Recurrences

| Recurrence | c_crit | f(n) exponent | Compare | Answer | Algorithm Example |
|------------|--------|---------------|---------|--------|-------------------|
| T(n) = 2T(n/2) + n | 1 | 1 | 1 = 1 | **Θ(n log n)** | Merge Sort |
| T(n) = 2T(n/2) + n² | 1 | 2 | 2 > 1 | **Θ(n²)** | - |
| T(n) = 2T(n/2) + 1 | 1 | 0 | 0 < 1 | **Θ(n)** | - |
| T(n) = T(n/2) + n | 0 | 1 | 1 > 0 | **Θ(n)** | - |
| T(n) = T(n/2) + 1 | 0 | 0 | 0 = 0 | **Θ(log n)** | Binary Search |
| T(n) = 3T(n/2) + n | 1.59 | 1 | 1 < 1.59 | **Θ(n^1.59)** | Karatsuba |
| T(n) = 4T(n/2) + n | 2 | 1 | 1 < 2 | **Θ(n²)** | Naive multiplication |
| T(n) = 2T(n/4) + n | 0.5 | 1 | 1 > 0.5 | **Θ(n)** | Exam Q2 |
| T(n) = 2T(n/2) + n³ | 1 | 3 | 3 > 1 | **Θ(n³)** | Exam Q1 |

### Subtraction Recurrences

| Recurrence | Summation Pattern | Answer | Example |
|------------|------------------|--------|---------|
| T(n) = T(n-1) + 1 | 1+1+1+...+1 (n times) | **Θ(n)** | Linear scan |
| T(n) = T(n-1) + n | n+(n-1)+(n-2)+...+1 | **Θ(n²)** | Selection/Insertion Sort |
| T(n) = T(n-2) + n² | n²+(n-2)²+(n-4)²+... | **Θ(n³)** | Mid-semester exam |
| T(n) = 2T(n-1) + 1 | 2⁰+2¹+2²+...+2^n | **Θ(2^n)** | Exponential growth |

**Key Pattern**:
- Subtracting by constant k → you do f(n) work roughly n/k times
- If f(n) = n^p, answer is usually Θ(n^(p+1))

---

## Exam Strategy Flowchart

```
┌─────────────────────────────────┐
│ Look at the recurrence          │
└────────┬────────────────────────┘
         │
         ▼
    Is it T(n) = aT(n/b) + f(n)?
         │
    ┌────┴────┐
   YES        NO (subtraction form)
    │          │
    ▼          ▼
Calculate    Use summation
log_b(a)     pattern table
    │
    ▼
What is f(n)?
Write as n^c
    │
    ▼
Compare c to log_b(a)
    │
    ├─ c < log_b(a) → Θ(n^log_b(a))
    ├─ c = log_b(a) → Θ(n^c log n)
    └─ c > log_b(a) → Θ(n^c)
```

---

## Worked Examples from Past Exams

### Example 1: T(n) = 2T(n/2) + n³

**Step 1**: Identify form
- a = 2, b = 2, f(n) = n³

**Step 2**: Calculate c_crit
- c_crit = log₂(2) = 1

**Step 3**: Compare
- f(n) = n³, so c = 3
- 3 > 1 (Case 3: work dominates)

**Answer**: **Θ(n³)** ✓

---

### Example 2: T(n) = 2T(n/4) + n

**Step 1**: Identify form
- a = 2, b = 4, f(n) = n

**Step 2**: Calculate c_crit
- c_crit = log₄(2) = 0.5
- (Because 4^0.5 = 2)

**Step 3**: Compare
- f(n) = n¹, so c = 1
- 1 > 0.5 (Case 3: work dominates)

**Answer**: **Θ(n)** ✓

---

### Example 3: T(n) = T(n-2) + n², T(0) = T(1) = b

**Step 1**: Recognize subtraction form

**Step 2**: Sum pattern
- Even n: n² + (n-2)² + (n-4)² + ... + 2²
- Odd n: n² + (n-2)² + (n-4)² + ... + 1²

**Step 3**: Estimate sum
- Roughly n/2 terms
- Each term is O(n²)
- But they're decreasing squares: ≈ ∫n² dx = n³/3

**Answer**: **Θ(n³)** ✓

---

### Example 4: T(n) = 3T(n/2) + n

**Step 1**: Identify form
- a = 3, b = 2, f(n) = n

**Step 2**: Calculate c_crit
- c_crit = log₂(3) ≈ 1.585

**Step 3**: Compare
- f(n) = n¹, so c = 1
- 1 < 1.585 (Case 1: recursion dominates)

**Answer**: **Θ(n^1.585)** (Karatsuba multiplication) ✓

---

### Example 5: T(n) = 2T(n/2) + cn log n (EXTENDED MASTER THEOREM)

**Step 1**: Identify form
- a = 2, b = 2, f(n) = n log n

**Step 2**: Calculate c_crit
- c_crit = log₂(2) = 1

**Step 3**: Recognize log factor in f(n)
- f(n) = n log n = n^1 · log^1(n)
- Polynomial part: n^1
- Log power: k = 1

**Step 4**: Check if polynomial matches c_crit
- Polynomial = n^1
- c_crit = 1
- ✓ They match! Use extended form

**Step 5**: Apply Extended Master Theorem
- f(n) = n^c_crit · log^k(n) where c_crit = 1, k = 1
- Result: T(n) = Θ(n^c_crit · log^(k+1) n)
- Result: T(n) = Θ(n^1 · log^(1+1) n)

**Answer**: **Θ(n log² n)** or **Θ(n log n log n)** ✓

**Why NOT Θ(n log n)?**
- At each recursion level, work is multiplied by log of that level's size
- Level 0: n log(n)
- Level 1: n log(n/2) = n(log n - 1)
- Level 2: n log(n/4) = n(log n - 2)
- Total: n[log n + (log n - 1) + ... + 1] ≈ n × (log n)²/2 = Θ(n log² n)

---

## Common Traps to Avoid

### ❌ Trap 1: Confusing a and b
```
T(n) = 2T(n/4) + n
```
- ❌ Wrong: log₂(4) = 2
- ✅ Right: log₄(2) = 0.5
- **Remember**: It's log_**b**(a), not log_a(b)

### ❌ Trap 2: Forgetting the log in Case 2
```
T(n) = 2T(n/2) + n
```
- log₂(2) = 1, and c = 1, so c = c_crit
- ❌ Wrong: Θ(n)
- ✅ Right: Θ(n log n)

### ❌ Trap 3: Miscounting recursive calls
```
POWER(x, p):
  if p even: return POWER(x, p/2) * POWER(x, p/2)
```
- This makes **TWO** recursive calls!
- T(p) = 2T(p/2) + 1 → Θ(p), NOT Θ(log p)
- Fix: Store result once → T(p) = T(p/2) + 1 → Θ(log p)

### ❌ Trap 4: Missing the log factor in f(n)
```
T(n) = 2T(n/2) + n log n
```
- ❌ Wrong: "c_crit = 1, c = 1, so c = c_crit → Θ(n log n)"
- ✅ Right: "f(n) has a log factor! → Extended Master Theorem → Θ(n log² n)"
- **Key**: If f(n) contains log(n), you CANNOT just compare exponents directly
- **Rule**: When f(n) = n^c_crit · log^k(n), answer is Θ(n^c_crit · log^(k+1) n)

---

## What NOT to Do on Exams

❌ **Don't** telescope unless explicitly asked to prove/derive
❌ **Don't** draw full recursion trees
❌ **Don't** expand more than 2-3 levels to verify
❌ **Don't** waste time on exact constants

✅ **DO** recognize pattern immediately
✅ **DO** calculate log_b(a) once
✅ **DO** compare and match to table
✅ **DO** state final answer with Θ notation

---

## The 30-Second Exam Method

1. **Identify**: Is it T(n) = aT(n/b) + f(n)?
2. **Calculate**: log_b(a) = ? (one calculation)
3. **Extract**: f(n) = n^c, what is c?
4. **Compare**:
   - c < log_b(a) → **Θ(n^log_b(a))**
   - c = log_b(a) → **Θ(n^c log n)**
   - c > log_b(a) → **Θ(n^c)**
5. **Write**: "Therefore, T(n) = Θ(...)"

---

## Additional Notes

### When Master Theorem Doesn't Apply

If f(n) is not a simple polynomial:
- f(n) = n log n → Use substitution or recursion tree
- f(n) = n/log n → Advanced analysis needed
- Multiple non-recursive terms → Analyze separately

For exam purposes, **all questions will fit Master Theorem or simple summation patterns**.

### Quickselect Special Case

```
T(n) = T(n/2) + n  (average case, always recurse on one side)
```
- This is NOT T(n) = 2T(n/2) + n
- Answer: Θ(n), not Θ(n log n)
- Summation: n + n/2 + n/4 + ... = 2n = Θ(n)

---

## Practice Checklist

Before the exam, verify you can instantly recognize:

**Basic Master Theorem:**
- [ ] T(n) = 2T(n/2) + n → Θ(n log n)
- [ ] T(n) = T(n/2) + 1 → Θ(log n)
- [ ] T(n) = 3T(n/2) + n → Θ(n^1.59)
- [ ] T(n) = 2T(n/4) + n → Θ(n)
- [ ] T(n) = 2T(n/2) + n³ → Θ(n³)

**Extended Master Theorem (with log factors):**
- [ ] T(n) = 2T(n/2) + n log n → Θ(n log² n) ⚠️ NOT Θ(n log n)!
- [ ] T(n) = 4T(n/2) + n² log n → Θ(n² log² n)

**Subtraction Recurrences:**
- [ ] T(n) = T(n-1) + n → Θ(n²)
- [ ] T(n) = T(n-2) + n² → Θ(n³)

**Key Values to Memorize:**
- [ ] log₂(2) = 1
- [ ] log₄(2) = 0.5
- [ ] log₂(3) ≈ 1.59
- [ ] log₂(4) = 2

---

## Summary: The Only Thing to Remember

### For T(n) = aT(n/b) + n^c:

**Step 1**: Find **log_b(a)**

**Step 2**: Compare **c** to **log_b(a)**:

---

### ⭐ CASE 1: c < log_b(a) → Answer is **Θ(n^log_b(a))** (Recursion Dominates)

**When**: The recursive calls grow faster than the work at each level

**Example 1**: T(n) = 3T(n/2) + n
- a = 3, b = 2, so log₂(3) ≈ 1.59
- f(n) = n¹, so c = 1
- Compare: 1 < 1.59 ✓
- **Answer: Θ(n^1.59)**
- **Why**: We're making 3 recursive calls (lots of branching), but only doing linear work. The tree has n^1.59 leaves, which dominates.

**Example 2**: T(n) = 4T(n/2) + n
- a = 4, b = 2, so log₂(4) = 2
- f(n) = n¹, so c = 1
- Compare: 1 < 2 ✓
- **Answer: Θ(n²)**
- **Why**: 4 recursive calls create a tree with n² leaves. Linear work per level is overwhelmed by quadratic leaf count.

**Example 3**: T(n) = 2T(n/2) + 1
- a = 2, b = 2, so log₂(2) = 1
- f(n) = 1 = n⁰, so c = 0
- Compare: 0 < 1 ✓
- **Answer: Θ(n)**
- **Why**: We do constant work but create n leaves (since we double at each level). The leaves dominate.

**Intuition**: Too many recursive calls → the leaves overwhelm the work done at each level → count the leaves (n^log_b(a))

---

### ⭐ CASE 2: c = log_b(a) → Answer is **Θ(n^c log n)** (Perfectly Balanced)

**When**: Work per level and recursive structure are perfectly balanced

**Example 1**: T(n) = 2T(n/2) + n  [Merge Sort]
- a = 2, b = 2, so log₂(2) = 1
- f(n) = n¹, so c = 1
- Compare: 1 = 1 ✓
- **Answer: Θ(n log n)**
- **Why**: At each of the log(n) levels, we do exactly n work total. Level 0: n, Level 1: 2×(n/2)=n, Level 2: 4×(n/4)=n, etc.

**Example 2**: T(n) = T(n/2) + 1  [Binary Search]
- a = 1, b = 2, so log₂(1) = 0
- f(n) = 1 = n⁰, so c = 0
- Compare: 0 = 0 ✓
- **Answer: Θ(n⁰ log n) = Θ(log n)**
- **Why**: Constant work at each of log(n) levels → log(n) total.

**Example 3**: T(n) = 4T(n/2) + n²
- a = 4, b = 2, so log₂(4) = 2
- f(n) = n², so c = 2
- Compare: 2 = 2 ✓
- **Answer: Θ(n² log n)**
- **Why**: Each level does n² work, there are log(n) levels → n² log n total.

**Intuition**: Work per level stays the same across all log(n) levels → multiply by log(n)

---

### ⭐ CASE 3: c > log_b(a) → Answer is **Θ(n^c)** (Work Dominates)

**When**: The work at the root level is so large it dominates everything below

**Example 1**: T(n) = 2T(n/2) + n³
- a = 2, b = 2, so log₂(2) = 1
- f(n) = n³, so c = 3
- Compare: 3 > 1 ✓
- **Answer: Θ(n³)**
- **Why**: Root does n³ work, children do 2×(n/2)³ = n³/4 work, grandchildren do n³/16, etc. The series n³(1 + 1/4 + 1/16 + ...) = n³ × (4/3) = Θ(n³). Root dominates!

**Example 2**: T(n) = 2T(n/4) + n
- a = 2, b = 4, so log₄(2) = 0.5
- f(n) = n¹, so c = 1
- Compare: 1 > 0.5 ✓
- **Answer: Θ(n)**
- **Why**: Root does n work, children do 2×(n/4) = n/2, grandchildren n/4, etc. Sum: n(1 + 1/2 + 1/4 + ...) = 2n = Θ(n). Root dominates!

**Example 3**: T(n) = T(n/2) + n
- a = 1, b = 2, so log₂(1) = 0
- f(n) = n¹, so c = 1
- Compare: 1 > 0 ✓
- **Answer: Θ(n)**
- **Why**: Root does n work, child does n/2, grandchild n/4, etc. Sum: n + n/2 + n/4 + ... = 2n = Θ(n).

**Intuition**: Work decreases geometrically as you go down → the root level (or top few levels) dominate → just take f(n)

---

## Subtraction Recurrences Explained

### Pattern 1: T(n) = T(n-1) + c (constant) → **Θ(n)**

**Example**: Counting from 1 to n
```
T(n) = T(n-1) + 1
```
**Expansion**:
- T(n) = T(n-1) + 1
- T(n-1) = T(n-2) + 1
- T(n-2) = T(n-3) + 1
- ...
- T(1) = 0

**Sum**: 1 + 1 + 1 + ... + 1 (n times) = **n**

**Answer: Θ(n)**

**Real Example**: Linear search - constant work at each step, n steps total.

---

### Pattern 2: T(n) = T(n-1) + n (linear) → **Θ(n²)**

**Example**: Selection Sort
```
T(n) = T(n-1) + n
```
**Expansion**:
- T(n) = T(n-1) + n
- T(n-1) = T(n-2) + (n-1)
- T(n-2) = T(n-3) + (n-2)
- ...
- T(1) = 0

**Sum**: n + (n-1) + (n-2) + ... + 2 + 1 = **n(n+1)/2 = Θ(n²)**

**Answer: Θ(n²)**

**Real Example**: Selection sort outer loop runs n times, inner loop does n, n-1, n-2, ... work.

---

### Pattern 3: T(n) = T(n-2) + n² (quadratic, skip by 2) → **Θ(n³)**

**Example**: Mid-semester exam question
```
T(n) = T(n-2) + n², T(0) = T(1) = b
```
**Expansion** (for even n):
- T(n) = T(n-2) + n²
- T(n-2) = T(n-4) + (n-2)²
- T(n-4) = T(n-6) + (n-4)²
- ...
- T(2) = T(0) + 4
- T(0) = b

**Sum**: n² + (n-2)² + (n-4)² + ... + 4² + 2²

**How many terms?** n/2 terms

**Each term ≈ O(n²)**, but they decrease. This is like integrating:
∫₀ⁿ x² dx = n³/3

**Answer: Θ(n³)**

**Why n³ not n² × (n/2)?** The squares form a sum dominated by the integral approximation, which adds another factor of n.

---

### Pattern 4: T(n) = 2T(n-1) + c (doubling) → **Θ(2^n)**

**Example**: Exponential growth
```
T(n) = 2T(n-1) + 1, T(0) = 1
```
**Expansion**:
- T(n) = 2T(n-1) + 1
- T(n-1) = 2T(n-2) + 1
- T(n-2) = 2T(n-3) + 1
- ...

**Substitute back**:
- T(n) = 2[2T(n-2) + 1] + 1 = 4T(n-2) + 2 + 1
- T(n) = 4[2T(n-3) + 1] + 3 = 8T(n-3) + 4 + 2 + 1
- T(n) = 2ⁿT(0) + (2^(n-1) + 2^(n-2) + ... + 2 + 1)
- T(n) = 2ⁿ + (2ⁿ - 1) = **2^(n+1) - 1 = Θ(2^n)**

**Answer: Θ(2^n)**

**Real Example**: Computing all subsets of a set, tree where each node spawns 2 children.

---

## Complete Summary Table

### Divide-and-Conquer: T(n) = aT(n/b) + n^c

| If... | Then... | Example | Answer |
|-------|---------|---------|--------|
| c < log_b(a) | Θ(n^log_b(a)) | T(n) = 3T(n/2) + n | Θ(n^1.59) |
| c = log_b(a) | Θ(n^c log n) | T(n) = 2T(n/2) + n | Θ(n log n) |
| c > log_b(a) | Θ(n^c) | T(n) = 2T(n/2) + n³ | Θ(n³) |

### Subtraction: T(n) = T(n-k) + f(n)

| Recurrence | Sum Pattern | Answer | Example Algorithm |
|------------|-------------|--------|-------------------|
| T(n) = T(n-1) + O(1) | 1+1+1+...(n times) | **Θ(n)** | Linear scan |
| T(n) = T(n-1) + O(n) | n+(n-1)+(n-2)+...+1 | **Θ(n²)** | Selection/Insertion Sort |
| T(n) = T(n-2) + O(n²) | n²+(n-2)²+(n-4)²+... | **Θ(n³)** | Mid-semester exam |
| T(n) = 2T(n-1) + O(1) | 2⁰+2¹+2²+...+2^n | **Θ(2^n)** | Exponential tree |

---

**This handles 95% of exam recurrence questions.**

---

*Good luck on your deferred mid-semester test!*
