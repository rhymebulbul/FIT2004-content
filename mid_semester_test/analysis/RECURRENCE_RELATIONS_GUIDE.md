# Recurrence Relations - Complete Guide for Mid-Semester Test

## General Rules (Master Formulas)

### Type 1: Subtracting a Constant - T(n) = T(n-c) + f(n)

**General Pattern:** If f(n) = O(n^k), then **T(n) = O(n^(k+1))**

| f(n) | Result | Explanation |
|------|--------|-------------|
| O(1) = O(n^0) | O(n^1) = **O(n)** | Linear: sum of constants n times |
| O(n) = O(n^1) | O(n^2) = **O(n²)** | Quadratic: sum 1+2+3+...+n |
| O(n²) = O(n^2) | O(n^3) = **O(n³)** | Cubic: sum 1²+2²+3²+...+n² |
| O(n^k) | **O(n^(k+1))** | Add 1 to the exponent |

**Why?** You make roughly n/c recursive calls, and at each call you do work proportional to n^k. The sum n^k + (n-c)^k + (n-2c)^k + ... ≈ integral of x^k from 0 to n = n^(k+1)/(k+1).

---

### Type 2: Dividing by Constant - T(n) = aT(n/b) + f(n)

Use **Master Theorem**:

Let f(n) = O(n^c) where c is the degree of the polynomial.

#### **🎯 EXAM METHOD: No Calculator Needed!**

**Traditional approach:** Calculate c_critical = log_b(a), then compare c vs c_critical

**⚡ BETTER APPROACH:** Compare **b^c vs a** (eliminates logarithm calculations!)

| Comparison | What it means | Dominating term | Result |
|------------|---------------|-----------------|---------|
| **b^c < a** | c < c_critical | **Recursion wins** | Θ(n^(log_b(a))) |
| **b^c = a** | c = c_critical | **Tied, add log** | Θ(n^c log n) |
| **b^c > a** | c > c_critical | **f(n) wins** | Θ(n^c) |

**Why this works:** Raising both sides of "c vs log_b(a)" by base b gives "b^c vs a"

#### **Mnemonic: "Big Base Power = Big Work"**

- If **b^c > a**: "My work per level (b^c) beats my subproblems (a)" → **work dominates** → **Θ(n^c)**
- If **b^c < a**: "My subproblems (a) beat my work (b^c)" → **recursion dominates** → **Θ(n^(log_b(a)))**
- If **b^c = a**: "Perfectly balanced" → **add log factor** → **Θ(n^c log n)**

#### Common Examples:

| Recurrence | a | b | c | **b^c vs a** | Comparison | Result | Algorithm |
|------------|---|---|---|------------|------------|--------|-----------|
| T(n) = T(n/2) + O(1) | 1 | 2 | 0 | 2^0=1 **vs** 1 | 1=1 | **O(log n)** | Binary search |
| T(n) = 2T(n/2) + O(n) | 2 | 2 | 1 | 2^1=2 **vs** 2 | 2=2 | **O(n log n)** | Merge sort |
| T(n) = 3T(n/2) + O(n) | 3 | 2 | 1 | 2^1=2 **vs** 3 | 2<3 | **O(n^1.58)** | Karatsuba |
| T(n) = T(n/2) + O(n) | 1 | 2 | 1 | 2^1=2 **vs** 1 | 2>1 | **O(n)** | - |
| T(n) = 8T(n/2) + O(n²) | 8 | 2 | 2 | 2^2=4 **vs** 8 | 4<8 | **O(n³)** | - |
| T(n) = 4T(n/2) + O(n²) | 4 | 2 | 2 | 2^2=4 **vs** 4 | 4=4 | **O(n² log n)** | - |
| T(n) = 2T(n/2) + O(n³) | 2 | 2 | 3 | 2^3=8 **vs** 2 | 8>2 | **O(n³)** | - |

#### **Powers You Can Do Mentally (No Calculator!)**

```
2¹=2   2²=4   2³=8   2⁴=16  2⁵=32
3¹=3   3²=9   3³=27  3⁴=81
4¹=4   4²=16  4³=64
5²=25
```

---

## Step-by-Step Solution Method

### Method: Expansion/Unrolling (Works for All Types)

**Example:** T(n) = T(n-2) + c·n² + d with T(0)=T(1)=b

#### Step 1: Expand Several Times
```
T(n) = T(n-2) + c·n² + d
     = [T(n-4) + c·(n-2)² + d] + c·n² + d
     = T(n-4) + c·(n-2)² + c·n² + 2d
     = T(n-6) + c·(n-4)² + c·(n-2)² + c·n² + 3d
```

#### Step 2: Identify Pattern After k Steps
```
T(n) = T(n-2k) + c·[2² + 4² + ... + (n-2)² + n²] + k·d
```

#### Step 3: Determine Base Case
When n - 2k = 0 (even n) or n - 2k = 1 (odd n), so k ≈ n/2

#### Step 4: Evaluate the Sum

The sum is: c·[2² + 4² + 6² + ... + n²]

This is every other square from 1² to n², which is roughly:
- Full sum 1² + 2² + ... + n² = n(n+1)(2n+1)/6 ≈ n³/3
- Our sum (every other) ≈ n³/6

So: c·(n³/6) = **O(n³)**

#### Step 5: Combine All Terms
- Base case: b = O(1)
- Summation: O(n³)
- Linear term: (n/2)·d = O(n)

**Result: T(n) = O(n³)**

---

## Quick Recognition Guide

### Pattern Type 1: T(n) = T(n-c) + n^k

| k | Work at Each Level | Number of Levels | Total |
|---|-------------------|------------------|-------|
| 0 | O(1) | n/c | **O(n)** |
| 1 | O(n) | n/c | **O(n²)** |
| 2 | O(n²) | n/c | **O(n³)** |
| 3 | O(n³) | n/c | **O(n⁴)** |
| k | O(n^k) | n/c | **O(n^(k+1))** |

**Memory Trick:** "Subtract constant → Add one to exponent"

### Pattern Type 2: T(n) = aT(n/b) + O(n)

| a | b | Meaning | Result |
|---|---|---------|--------|
| 1 | 2 | One subproblem, half size | O(n) or O(log n) |
| 2 | 2 | Two subproblems, half size | O(n log n) |
| 4 | 2 | Four subproblems, half size | O(n²) |
| a | b | a subproblems, 1/b size | Use Master Theorem |

---

## Common Mid-Semester Patterns

### Linear Decrements (T(n-1), T(n-2), etc.)

```
T(n) = T(n-1) + 1         → O(n)      [Simple iteration]
T(n) = T(n-1) + n         → O(n²)     [Selection sort]
T(n) = T(n-1) + n²        → O(n³)
T(n) = T(n-2) + 1         → O(n)      [Skip by 2]
T(n) = T(n-2) + n²        → O(n³)     [Your exam question!]
```

### Logarithmic Decrements (T(n/2), T(n/3), etc.)

```
T(n) = T(n/2) + 1         → O(log n)  [Binary search]
T(n) = T(n/2) + n         → O(n)      [Work dominates]
T(n) = 2T(n/2) + n        → O(n log n) [Merge sort]
T(n) = 2T(n/2) + 1        → O(n)      [Recursion dominates]
```

---

## Practice Problems with Solutions

### Problem 1
**Q:** T(n) = T(n-3) + n² with T(0)=T(1)=T(2)=1

**Solution:**
- Pattern: T(n-c) + n^k where k=2
- Rule: O(n^(k+1)) = O(n³)
- **Answer: O(n³)**

### Problem 2
**Q:** T(n) = 4T(n/2) + n with T(1)=1

**Solution (Calculator-Free Method):**
- a=4, b=2, c=1 (since f(n)=n¹)
- Calculate: b^c = 2¹ = 2
- Compare: 2 < 4 (so b^c < a)
- Recursion dominates → Use O(n^(log_b a))
- **Answer: O(n^(log₂ 4)) = O(n²)**

**Old Method (for reference):**
- c_critical = log₂(4) = 2
- Compare c vs c_critical: 1 < 2
- **Answer: O(n²)**

### Problem 3
**Q:** T(n) = T(n-1) + n³ with T(0)=1

**Solution:**
- Pattern: T(n-c) + n^k where k=3
- Rule: O(n^(k+1)) = O(n⁴)
- **Answer: O(n⁴)**

### Problem 4
**Q:** T(n) = 2T(n/2) + n² with T(1)=1

**Solution:**
- Master Theorem: a=2, b=2, d=2
- Compare: 2 vs 2² → 2 < 4, so a < b^d
- Use case 1: O(n^d) = O(n²)
- **Answer: O(n²)**

---

## Exam Strategy

### 30-Second Quick Check
1. **Subtract or divide?**
   - Subtract (n-c): Use Type 1 rule (add 1 to exponent)
   - Divide (n/b): Use Master Theorem

2. **What's f(n)?** (the non-recursive part)
   - Count the highest degree: n², log n, n³, etc.

3. **Apply the formula**
   - Type 1: f(n) = n^k → Answer = n^(k+1)
   - Type 2: Use Master Theorem comparison

### If You Have Time
- Expand 3-4 terms to verify
- Check if the sum makes sense
- Compare with known algorithms (merge sort, binary search)

---

## Formula Sheet (Memorize These!)

### Type 1 (Linear Recurrence)
```
T(n) = T(n-c) + O(n^k) → O(n^(k+1))
```

### Type 2 (Master Theorem) - Calculator-Free Method!
```
T(n) = aT(n/b) + O(n^c)

Step 1: Calculate b^c (easy mental math!)
Step 2: Compare b^c with a

If b^c < a: O(n^(log_b a))  [Recursion dominates]
If b^c = a: O(n^c log n)     [Balanced - add log]
If b^c > a: O(n^c)           [Work dominates]
```

**Example:** T(n) = 8T(n/2) + n²
- b^c = 2² = 4
- Compare: 4 < 8
- Answer: O(n^(log₂ 8)) = O(n³)

### Common Sums
```
1 + 2 + 3 + ... + n = n(n+1)/2 ≈ n²/2 = O(n²)
1² + 2² + 3² + ... + n² = n(n+1)(2n+1)/6 ≈ n³/3 = O(n³)
1 + 2 + 4 + ... + 2^k = 2^(k+1) - 1 ≈ 2^k = O(2^k)
```

---

## Related Topics for Mid-Semester

- **Recurrence from Merge Sort:** T(n) = 2T(n/2) + O(n) = O(n log n) (line 58, examinable_content_mid.txt)
- **Counting Inversions:** Same recurrence as merge sort (line 59)
- **Quickselect Average Case:** T(n) = T(n/2) + O(n) = O(n) (line 92-95)

---

**Last Updated:** October 12, 2025
**Source:** FIT2004 Mid-Semester Examinable Content
