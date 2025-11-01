# FIT2004 Loop Invariant Questions Guide

This guide documents **all types of loop invariant questions** you might encounter in FIT2004 exams, based on lecture slides, course notes, and past exam analysis.

**Last Updated:** 2025-10-26
**Source:** lecture/, course_notes/, exams/

---

## Table of Contents

1. [What is a Loop Invariant?](#what-is-a-loop-invariant)
2. [Loop Invariant Proof Structure](#loop-invariant-proof-structure)
3. [Question Type 1: MCQ - Select the Correct Invariant](#question-type-1-mcq---select-the-correct-invariant)
4. [Question Type 2: Write Your Own Invariant](#question-type-2-write-your-own-invariant)
5. [Question Type 3: Prove the Invariant Holds](#question-type-3-prove-the-invariant-holds)
6. [Question Type 4: Use Invariant to Prove Correctness](#question-type-4-use-invariant-to-prove-correctness)
7. [Question Type 5: Full Proof (All Three Steps)](#question-type-5-full-proof-all-three-steps)
8. [Common Algorithms with Loop Invariants](#common-algorithms-with-loop-invariants)
9. [Common Mistakes to Avoid](#common-mistakes-to-avoid)
10. [Exam Strategy and Templates](#exam-strategy-and-templates)

---

## What is a Loop Invariant?

**Definition:** A loop invariant is a property/statement that:
- Holds **before** the first iteration of a loop
- If true before an iteration, remains true **after** that iteration
- When the loop terminates, helps prove the algorithm's **correctness**

**Purpose:** Loop invariants are used to prove that an algorithm works correctly using a proof technique similar to mathematical induction.

---

## Loop Invariant Proof Structure

Every loop invariant proof has **three parts**:

### 1. **Initialization (Base Case)**
- **What to show:** The invariant is true before the first iteration (when the loop starts)
- **When:** Typically at `i=0`, `i=1`, or when the loop control variable is initialized
- **Template:** "At initialization, [loop variable] = [initial value]. The invariant states [invariant]. This is true because [reasoning]."

### 2. **Maintenance (Inductive Step)**
- **What to show:** If the invariant is true before iteration k, it remains true before iteration k+1
- **Template:** "Assume the invariant holds at the start of iteration k. After executing the loop body, [explain what happens]. Therefore, when i increments to k+1, the invariant still holds."

### 3. **Termination (Use Invariant to Prove Correctness)**
- **What to show:** When the loop terminates, the invariant (combined with the termination condition) proves the algorithm is correct
- **Template:** "The loop terminates when [termination condition]. At this point, the invariant states [invariant]. Combined with the termination condition, this proves [correctness claim]."

---

## Question Type 1: MCQ - Select the Correct Invariant

**Format:** Given an algorithm, select the correct loop invariant from multiple choices.

**Marks:** 1-2 marks

**Frequency:** Common (appears in most exams)

---

### Example 1: Sum of Elements with Factor m

**Exam:** Past Exam 2, Question 3 (1 mark)

**Algorithm:**
```python
def myfunc(L[1...n], m):
    x = 0
    loop i from 1 to n:
        # loop invariant here
        if L[i] % m == 0:
            x = x + L[i]
    return x
```

**Question:** What is a useful loop invariant for this algorithm?

**Options:**
- A. x is the sum of all numbers in list L[1...i] % m
- B. x is the sum of all numbers in list L[1...i-1] % m
- **C. x is the sum of all numbers with factor m in list L[1...i-1]** ✓
- D. x is the sum of all numbers with factor m in list L
- E. x is a list of all numbers in list L[1...i-1] % m
- F. x is the sum of all numbers with factor m in list L[1...i]

**Correct Answer:** C

**Why C is correct:**
- At initialization (i=1): x=0, representing sum of L[1...0] (empty list) - TRUE ✓
- The invariant must hold **BEFORE** processing L[i] in each iteration
- After processing L[i], the invariant shifts to include the newly processed element

**Why others are wrong:**
- **A, B, E:** The `%m` notation doesn't represent a list of remainders; x stores actual sums
- **D:** Doesn't include iterator, not specific to loop state
- **F:** Would be false at initialization (x=0 but L[1] might have factor m)

**Key Insight:** The invariant should describe the state **at the START of each iteration**, not after processing the current element.

---

### Example 2: Count Elements with Factor m

**Exam:** Past Exam 3, Question 2 (2 marks)

**Algorithm:**
```python
function myFunc(L[1...n], m):
  x = 0
  i = 1
  while i <= n:
    # loop invariant here
    if L[i] % m == 0:
      x = x + 1
    else:
      x = x + 0
    i = i + 1
  return x
```

**Given invariant:** `x is the number of items with a factor of m in list L[1...i-1]`

**Question:** Which statements are TRUE?

**Options:**
- A. The loop invariant should be: x is the number of items with factor m in L[1...i]
- **B. The invariant at i=n+1 implies correctness** ✓
- C. The invariant at i=n implies correctness
- **D. The following invariant holds just before line 10: x is the number of items with factor m in L[1...i]** ✓

**Correct Answers:** B and D

**Explanation:**
- **B is correct:** Loop terminates when `i=n+1`, at which point the invariant `x counts L[1...n]` proves correctness
- **D is correct:** Just before `i=i+1`, x has been updated to include L[i], so x now counts L[1...i]
- **A is wrong:** The invariant at the START of the iteration is L[1...i-1], not L[1...i]
- **C is wrong:** Loop doesn't terminate at i=n; it terminates at i=n+1

**Key Insight:** Pay attention to when the loop terminates and when invariants hold!

---

## Question Type 2: Write Your Own Invariant

**Format:** Given an algorithm, write down a useful loop invariant.

**Marks:** 1-2 marks

**Frequency:** Very common

---

### Example 1: Modular Arithmetic Sum

**Exam:** Past Exam 1, Question 2a (part of 4-mark question)

**Algorithm:**
```python
def sum_factor(L, m):
    n = len(L)
    s = 0
    for i in range(n):
        s = (s + L[i]) % m
    return s == 0
```

**Question:** (a) Write down a useful invariant for this algorithm.

**Answer:** `s = sum(L[0..i-1]) % m` at the beginning of loop iteration i

**Explanation:**
- At the start of the i-th iteration, `s` holds the remainder when the sum of the first i-1 elements is divided by m
- This relates the current state (s) to what has been processed (L[0..i-1])

---

### Example 2: Selection Sort

**From:** Course Notes, Chapter 1

**Algorithm:**
```python
function SELECTION_SORT(array[1..n]):
  for i = 1 to n:
    min = i
    for j = i+1 to n:
      if array[j] < array[min]: min = j
    swap(array[i], array[min])
```

**Invariant (at start of iteration i):**
1. `array[1..i-1]` is sorted
2. `∀x ∈ array[1..i-1], ∀y ∈ array[i..n], x ≤ y`

**Translation:** Everything before position i is sorted, and everything before i is less than or equal to everything from i onwards.

---

### Example 3: Binary Search

**From:** Course Notes, Chapter 1 + Lecture 1

**Algorithm:**
```python
function BINARY_SEARCH(array[1..n], key):
  lo = 1; hi = n + 1
  while lo < hi - 1:
    mid = floor((lo + hi) / 2)
    if key >= array[mid]: lo = mid
    else: hi = mid
  if array[lo] == key: return lo
  else: return null
```

**Invariant (maintained at every iteration if key ∈ array):**
1. `array[lo] ≤ key`
2. If `hi ≠ n + 1`, then `array[hi] > key`

**Implication:** If the key exists, it lies within the range `[lo..hi)`

---

### Example 4: Insertion Sort

**From:** Course Notes, Chapter 1

**Algorithm:**
```python
function INSERTION_SORT(array[1..n]):
  for i = 2 to n:
    key = array[i]
    j = i - 1
    while j > 0 and array[j] > key:
      array[j + 1] = array[j]
      j = j - 1
    array[j + 1] = key
```

**Invariant (at start of iteration i):** `array[1..i-1]` is sorted

---

## Question Type 3: Prove the Invariant Holds

**Format:** Show that the given invariant is true on loop entry and each time the loop runs.

**Marks:** 2-3 marks

**Frequency:** Common

---

### Example: Justify Loop Invariant

**Exam:** Past Exam 2, Question 4 (2 marks)

**Algorithm:**
```python
def myfunc(L[1...n], m):
    x = 0
    loop i from 1 to n:
        if L[i] % m == 0:
            x = x + L[i]
    return x
```

**Given Invariant:** `x is the sum of all numbers with factor m in list L[1...i-1]`

**Question:** Justify that the loop invariant you have chosen is true each time the loop runs and when it terminates.

**Answer (Full Proof Structure):**

### **Initialization:**
At `i=1`, `x=0`. The invariant states "x is the sum of numbers with factor m in L[1...0]" (empty list). This is **true** since 0 is the sum of no numbers.

### **Maintenance:**
Assume at iteration k (i=k), the invariant holds: x represents the sum of numbers with factor m in L[1...k-1].

The if condition checks if L[k] has factor m:
- **If yes:** `x = x + L[k]` (add L[k] to sum)
- **If no:** x remains unchanged

Either way, after the conditional executes, x represents the sum of numbers with factor m in L[1...k].

When i increments to k+1, the invariant holds for the next iteration.

### **Termination:**
The loop terminates when `i = n+1`. At this point, x has not changed since the last iteration, so the invariant still holds:

`x represents the sum of numbers with factor m in L[1...n] = L`

This proves the correctness of the result.

---

## Question Type 4: Use Invariant to Prove Correctness

**Format:** Use the invariant (assumed to be proven) to argue that the algorithm is correct.

**Marks:** 1-2 marks

**Frequency:** Common

---

### Example: Modular Arithmetic Correctness

**Exam:** Past Exam 1, Question 2c (part of 4-mark question)

**Algorithm:**
```python
def sum_factor(L, m):
    n = len(L)
    s = 0
    for i in range(n):
        s = (s + L[i]) % m
    return s == 0
```

**Given Invariant (proven):** `s = sum(L[0..i-1]) % m` at the beginning of iteration i

**Question:** (c) Now use your invariant to argue that the algorithm is correct.

**Answer:**

The for loop terminates when `i=n`. At this point, by the invariant:

```
s = sum(L[0..n-1]) % m = sum(L) % m
```

The function returns `(s == 0)`, which is **True** if and only if `sum(L) % m == 0`, meaning m divides sum(L).

This matches the specification exactly: the algorithm returns True iff m is a factor of sum(L).

**Key Concepts:**
- Modular arithmetic properties: `(a + b) % m = ((a % m) + b) % m`
- Loop termination analysis
- Using invariant at termination to prove correctness

---

## Question Type 5: Full Proof (All Three Steps)

**Format:** Write invariant, prove initialization, maintenance, and termination.

**Marks:** 3-4 marks

**Frequency:** Common (appears as a combined question)

This is the combination of Question Types 2, 3, and 4.

---

### Full Example: Modular Sum Algorithm

**Exam:** Past Exam 1, Question 2 (4 marks total)

**Algorithm:**
```python
def sum_factor(L, m):
    n = len(L)
    s = 0
    for i in range(n):
        s = (s + L[i]) % m
    return s == 0
```

**Full Answer:**

### **(a) Loop Invariant: (1 mark)**

`s = sum(L[0..i-1]) % m` at the beginning of loop iteration i

### **(b) Proof of Invariant: (2 marks)**

**Initialization:**
At loop entry, `i=0`. The invariant states: `s = sum(L[0..-1]) % m` (empty list).
Since the sum of an empty list is 0, and `0 % m = 0`, and `s=0`, the invariant holds.

**Maintenance (by induction):**
Assume the invariant holds at the start of iteration k, so `s = sum(L[0..k-1]) % m`.

After the loop body executes:
```
s = (s + L[k]) % m
  = (sum(L[0..k-1]) % m + L[k]) % m        [by invariant assumption]
  = (sum(L[0..k-1]) + L[k]) % m            [by modular arithmetic property]
  = sum(L[0..k]) % m
```

This is exactly what the invariant requires at the start of iteration k+1. ✓

### **(c) Correctness Proof: (1 mark)**

**Termination:**
The for loop terminates when `i=n`. At this point, by the invariant:
```
s = sum(L[0..n-1]) % m = sum(L) % m
```

The function returns `(s == 0)`, which is True if and only if `sum(L) % m == 0`, meaning m divides sum(L).

This matches the specification exactly. ✓

---

## Common Algorithms with Loop Invariants

### 1. Binary Search

**Invariant:** If `key` exists in the array, it lies within range `[lo..hi)`

**Key Properties:**
- `array[lo] ≤ key`
- If `hi ≠ n+1`, then `array[hi] > key`

**Termination:** When `lo = hi - 1`, the search space has narrowed to a single element

---

### 2. Selection Sort

**Invariant (at start of iteration i):**
1. `array[1..i-1]` is sorted
2. All elements in `array[1..i-1]` are ≤ all elements in `array[i..n]`

**Termination:** When `i=n`, the entire array `array[1..n]` is sorted

---

### 3. Insertion Sort

**Invariant (at start of iteration i):** `array[1..i-1]` is sorted (but not necessarily containing the smallest i-1 elements)

**Termination:** When `i=n+1`, array `[1..n]` is sorted

---

### 4. Accumulation Loops

**Common Pattern:** Summing or counting elements with a property

**Invariant Template:** `accumulator = [function of elements processed so far]`

**Examples:**
- Sum: `sum = total of L[1..i-1]`
- Count: `count = number of elements in L[1..i-1] satisfying property P`
- Product: `product = product of L[1..i-1]`

---

### 5. Search Loops

**Common Pattern:** Finding an element or index

**Invariant Template:** `[property holds for all elements checked so far]`

**Example (Linear Search):**
- Invariant: `key ∉ array[1..i-1]` (key not found in elements checked so far)
- Termination: Either found key at position i, or searched entire array

---

## Common Mistakes to Avoid

### Mistake 1: Wrong Index Range

❌ **Wrong:** `x is the sum of L[1..i]` (when invariant should hold at START of iteration)

✅ **Correct:** `x is the sum of L[1..i-1]` (describes state before processing L[i])

**Why:** Invariant must be true **before** processing the current element.

---

### Mistake 2: Not Checking Initialization

❌ **Wrong:** Skipping the initialization step or not verifying it with actual values

✅ **Correct:** Explicitly show the invariant holds when the loop starts (i=0, i=1, etc.)

**Example:**
- At `i=1`, `x=0`, invariant says "x is sum of L[1..0]" (empty list = 0) ✓

---

### Mistake 3: Confusing Termination Condition

❌ **Wrong:** "Loop terminates at `i=n`" (when it actually terminates at `i=n+1`)

✅ **Correct:** Carefully check when the loop condition becomes false

**Example:**
- `while i <= n` terminates when `i=n+1`
- `for i = 1 to n` terminates when `i=n+1` (after processing i=n)

---

### Mistake 4: Not Using Modular Arithmetic Properties

❌ **Wrong:** `(a % m + b) % m` without justification

✅ **Correct:** Explicitly state: "By modular arithmetic property: `(a % m + b) % m = (a + b) % m`"

**Key Properties to Know:**
- `(a + b) % m = ((a % m) + (b % m)) % m`
- `(a * b) % m = ((a % m) * (b % m)) % m`

---

### Mistake 5: Vague Inductive Step

❌ **Wrong:** "After the loop runs, the invariant still holds."

✅ **Correct:** "Assume invariant holds at iteration k. [Explain what loop body does]. Therefore, invariant holds at iteration k+1."

**Be Specific:** Show exactly how the loop body preserves the invariant.

---

### Mistake 6: Not Relating Invariant to Correctness

❌ **Wrong:** "The loop terminates, so the algorithm is correct."

✅ **Correct:** "The loop terminates when `i=n+1`. By the invariant, x = [value]. This equals [desired result], proving correctness."

**Key:** Connect the invariant at termination to the algorithm's specification.

---

## Foundational Knowledge to Avoid Mistakes 1-3

This section provides the **core conceptual understanding** needed to avoid the most common mistakes. If you consistently make Mistakes 1-3, you need to master these fundamentals.

---

### Understanding Mistake 1: Wrong Index Range

**Root Cause:** Not understanding **when** the loop invariant is evaluated during loop execution.

#### **Core Concept: Loop Execution Timeline**

```
┌─────────────┐
│ Before Loop │ Variables initialized (i=1, x=0, etc.)
└─────────────┘
       ↓
┌─────────────┐
│  Check i<=n │ Is loop condition true?
└─────────────┘
       ↓ YES
┌─────────────┐
│  INVARIANT  │ ◄── Invariant must be TRUE HERE (before processing L[i])
│   HOLDS     │     This is the "start of iteration i"
└─────────────┘
       ↓
┌─────────────┐
│  Loop Body  │ Process L[i], update x, etc.
└─────────────┘
       ↓
┌─────────────┐
│  Increment  │ i = i + 1
└─────────────┘
       ↓
    (repeat)
```

**Key Insight:** The invariant describes the state **BEFORE** the loop body executes, which means **BEFORE** processing `L[i]`.

#### **Mental Model: "Work Done So Far"**

The invariant answers: "What work has been **completed** before processing the current element?"

**Example:**
```python
x = 0
for i = 1 to n:
    # ◄── CHECKPOINT: What is true HERE?
    if L[i] % m == 0:
        x = x + L[i]
```

**At the checkpoint (start of iteration i):**
- You **have** processed: L[1], L[2], ..., L[i-1]
- You **haven't** processed: L[i] (about to do it now)
- Therefore: invariant = "x is the sum of elements with factor m in L[1..i-1]"

**Not L[1..i]** because L[i] hasn't been processed yet!

#### **Concrete Example with i=3:**

```python
# Assume n=5, L=[2,4,3,6,5], m=2
x = 0
i = 1: x = x + L[1] = 2    # After: x=2 (represents L[1])
i = 2: x = x + L[2] = 6    # After: x=6 (represents L[1..2])
i = 3: # ◄── AT THIS POINT (before processing L[3]):
       # x = 6 = sum of L[1..2] (i-1 = 2)
       # L[3]=3 not yet added
       # Invariant: x = sum of L[1..i-1] = L[1..2] ✓
       x remains 6 (L[3]=3 has no factor 2)
```

#### **Practice Drill:**

For **any** loop, identify the checkpoint and ask:
1. "Has L[i] been processed at the START of iteration i?" → **NO**
2. "What's the last element that was processed?" → **L[i-1]**
3. "Therefore, the invariant refers to..." → **L[1..i-1]**

#### **Exception: Invariants After Loop Body**

Some questions ask about invariants **just before the increment** (after loop body):

```python
for i = 1 to n:
    if L[i] % m == 0:
        x = x + L[i]
    # ◄── HERE, x = sum of L[1..i] (just processed L[i])
    # But the "official" loop invariant is still L[1..i-1]
```

**Important:** Unless explicitly stated otherwise, "loop invariant" refers to the state **at the start** of the iteration.

---

### Understanding Mistake 2: Not Checking Initialization

**Root Cause:** Not verifying the base case with **concrete values**.

#### **Core Concept: Induction Base Case**

Loop invariants are **induction proofs** in disguise:

| Mathematical Induction | Loop Invariant |
|------------------------|----------------|
| Prove P(0) or P(1) | **Initialization**: Prove invariant holds when loop starts |
| Assume P(k), prove P(k+1) | **Maintenance**: Assume true at iteration k, prove true at k+1 |
| Conclude P(n) | **Termination**: Invariant at loop exit proves correctness |

**Just like induction, you MUST verify the base case explicitly.**

#### **How to Check Initialization**

**Step-by-step process:**

1. **Identify initial values:** What is i? What are other variables (x, sum, count)?
2. **State the invariant with those values:** Substitute the initial i into the invariant
3. **Check if it's true:** Use actual values, not hand-waving

**Example:**

```python
x = 0
for i = 1 to n:
    if L[i] % m == 0:
        x = x + L[i]
```

**Invariant:** "x is the sum of numbers with factor m in L[1..i-1]"

**Initialization Check:**

1. **Initial values:** i=1, x=0
2. **Invariant at i=1:** "x is the sum of numbers with factor m in L[1..0]"
3. **Is it true?**
   - L[1..0] is an **empty range** (no elements)
   - Sum of empty list = **0**
   - x = **0**
   - Therefore: 0 = 0 ✓ **TRUE**

#### **Empty Set Semantics: What You Must Know**

| Property | Empty Set Value | Why |
|----------|----------------|-----|
| Sum of empty list | 0 | Identity element for addition |
| Product of empty list | 1 | Identity element for multiplication |
| Count of empty list | 0 | No elements to count |
| "Key not in empty list" | TRUE (vacuously) | No elements to contradict |
| "All elements in empty list satisfy P" | TRUE (vacuously) | No counterexamples |

**Common initialization patterns:**

```python
sum = 0      # Sum of L[1..0] = 0 ✓
count = 0    # Count of L[1..0] = 0 ✓
product = 1  # Product of L[1..0] = 1 ✓
found = False # Key not found in L[1..0] ✓
```

#### **Common Initialization Mistakes**

❌ **Mistake:** "At i=1, x=0, so the invariant holds" (no justification)

✅ **Correct:**
```
At i=1, x=0.
The invariant states: "x is the sum of L[1..0]" (empty range).
The sum of zero elements is 0.
Since x=0, the invariant holds. ✓
```

#### **Practice Drill:**

For every invariant you write:
1. Write down initial values: "At loop entry, i=___, x=___"
2. Substitute into invariant: "The invariant claims: ___"
3. Evaluate the claim: "This means ___ (with concrete values)"
4. Verify: "Since ___, this is TRUE ✓"

---

### Understanding Mistake 3: Confusing Termination Condition

**Root Cause:** Not understanding when loops actually **exit**.

#### **Core Concept: Last Iteration vs. Termination**

**Critical distinction:**
- **Last iteration processed:** The last value of i for which the loop body executes
- **Termination value:** The value of i when the loop condition becomes false

**These are different!**

#### **Loop Termination Table (Memorize This)**

| Loop Structure | Last Processed | Termination Value | Invariant at Termination |
|----------------|----------------|-------------------|--------------------------|
| `for i = 1 to n` | i = n | i = n+1 | Describes L[1..n] |
| `while i <= n` (i starts at 1) | i = n | i = n+1 | Describes L[1..n] |
| `for i in range(n)` (0-indexed) | i = n-1 | i = n | Describes L[0..n-1] |
| `while i < n` (i starts at 0) | i = n-1 | i = n | Describes L[0..n-1] |
| `while lo < hi - 1` | lo = hi-2 | lo = hi-1 | Search space narrowed |

#### **Why This Matters for Correctness**

The invariant **at termination** is what proves the algorithm works!

**Example:**

```python
x = 0
for i = 1 to n:
    if L[i] % m == 0:
        x = x + L[i]
return x
```

**Invariant:** "x is the sum of numbers with factor m in L[1..i-1]"

**Common Wrong Reasoning:**
> "The loop terminates at i=n, so by the invariant, x = sum of L[1..n-1]."
>
> **This is WRONG!** You're missing L[n]!

**Correct Reasoning:**
> "The loop processes i=1,2,...,n, then increments i to n+1 and checks the condition.
> Since n+1 > n, the condition fails and the loop exits **at i=n+1**.
> By the invariant: x = sum of numbers with factor m in L[1..n].
> This is the entire list L, proving correctness. ✓"

#### **Manual Trace Method**

When unsure, **trace the last 2 iterations manually:**

**Example: `for i = 1 to n` where n=3**

```
Iteration i=2:
  - Check: 2 <= 3? YES
  - Execute body (process L[2])
  - Increment: i = 3

Iteration i=3:
  - Check: 3 <= 3? YES
  - Execute body (process L[3])  ◄── Last element processed
  - Increment: i = 4

Iteration i=4:
  - Check: 4 <= 3? NO  ◄── Loop exits
  - Termination value: i = 4 (not 3!)
```

**At termination:** i=4, and invariant "x = sum of L[1..i-1]" means x = sum of L[1..3] = entire list ✓

#### **Common Termination Patterns**

**1-indexed loops (1 to n):**
```python
for i = 1 to n:
    process(L[i])
# Terminates at i = n+1
# Invariant: describes L[1..n]
```

**0-indexed loops (0 to n-1):**
```python
for i in range(n):  # i = 0, 1, ..., n-1
    process(L[i])
# Terminates at i = n
# Invariant: describes L[0..n-1]
```

**While loops:**
```python
i = 1
while i <= n:
    process(L[i])
    i = i + 1
# Terminates at i = n+1
```

#### **Practice Drill:**

For each loop type, manually trace:
1. What is the last value processed? (last i where body executes)
2. After that iteration, what is i? (after increment)
3. What condition is checked? (i <= n, i < n, etc.)
4. At what value of i does the loop exit? (termination value)

---

### Conceptual Integration: How It All Fits Together

**The Three Mistakes Stem From One Problem:** Not having a clear mental model of loop execution.

#### **Complete Mental Model:**

```
BEFORE LOOP:
├─ Variables initialized (i=1, x=0, etc.)
└─ Invariant must hold here (Initialization / Mistake 2)

EACH ITERATION:
├─ START: Invariant holds (describes L[1..i-1]) ◄── Mistake 1
├─ BODY: Process L[i], update variables
└─ END: Increment i

TERMINATION:
├─ Loop exits at i = n+1 (not i=n!) ◄── Mistake 3
└─ Invariant at i=n+1 describes L[1..n] (entire list)
```

#### **Unified Understanding:**

1. **Mistake 1 (Index Range):** Occurs because you don't visualize the timeline (invariant holds **before** processing)
2. **Mistake 2 (Initialization):** Occurs because you don't verify the base case with concrete values
3. **Mistake 3 (Termination):** Occurs because you confuse "last processed" with "loop exit value"

**All three require:** Precise understanding of **when** things happen during loop execution.

---

### Study Plan: Fixing These Mistakes

#### **Phase 1: Build Mental Model (2-3 hours)**

**Exercise 1: Loop Tracing**
- Take 5 simple loops from the guide
- For each iteration, write down:
  - Current i
  - Current variable values
  - What has been processed (L[1..i-1])
  - What will be processed (L[i])
- Trace through termination to see final i value

**Exercise 2: Initialization Practice**
- For each invariant in the guide, write out:
  - "At i=___, variables are ___"
  - "Invariant claims: ___"
  - "This is true because: ___ (with concrete values)"

**Exercise 3: Termination Analysis**
- For each loop structure, manually trace last 2 iterations
- Identify termination value
- Write what the invariant claims at that value

#### **Phase 2: Pattern Recognition (1-2 hours)**

Memorize these patterns:

**Index Range Patterns:**
- Accumulator invariant: `acc = f(L[1..i-1])` (work done so far)
- Search invariant: `property holds for L[1..i-1]` (checked so far)
- Sorted region: `array[1..i-1] is sorted` (fixed portion)

**Initialization Patterns:**
- `sum/count = 0` → Empty list has sum/count 0
- `product = 1` → Empty list has product 1
- `found = false` → Key not found in empty list

**Termination Patterns:**
- `for i = 1 to n` → exits at i=n+1
- `for i in range(n)` → exits at i=n
- `while i <= n` → exits at i=n+1

#### **Phase 3: Deliberate Practice (2-3 hours)**

**Do MCQ questions from the guide:**
- Question yourself: "Why is A wrong? Is it Mistake 1, 2, or 3?"
- For correct answer: Verify initialization and termination

**Write full proofs:**
- Use the templates in the guide
- Force yourself to check all three: init, maintenance, termination
- Self-grade: Did I specify concrete values? Did I trace termination correctly?

#### **Phase 4: Application (1-2 hours)**

**Work through past exam questions:**
- Before looking at solutions, identify potential Mistakes 1-3
- Write your answer
- Compare with solution
- If wrong, diagnose which mistake you made

---

### Quick Reference: Pre-Answer Checklist

**Before answering ANY loop invariant question, check:**

✅ **Index Range (Mistake 1):**
- [ ] Is the invariant describing state at **START** of iteration?
- [ ] Does it refer to L[1..i-1] (processed) not L[1..i] (not processed yet)?

✅ **Initialization (Mistake 2):**
- [ ] Did I write down initial values (i=?, x=?)?
- [ ] Did I substitute into the invariant?
- [ ] Did I verify with concrete values (empty list = 0, etc.)?

✅ **Termination (Mistake 3):**
- [ ] Did I trace the last iteration manually?
- [ ] What is the termination value? (Usually i=n+1, not i=n)
- [ ] What does the invariant claim at that value?

**If ANY box is unchecked, you risk making Mistakes 1-3!**

---

## Exam Strategy and Templates

### Template 1: Writing an Invariant

**Pattern:** `[variable] = [property of elements processed so far]`

**Examples:**
- Accumulation: `sum = total of L[1..i-1]`
- Counting: `count = number of elements in L[1..i-1] with property P`
- Search range: `if key exists, it's in range [lo..hi)`
- Sorted region: `array[1..i-1] is sorted`

### Template 2: Initialization Proof

```
At initialization, [loop variable] = [initial value].
The invariant states: [invariant].
This is true because [reasoning with concrete values].
```

**Example:**
```
At initialization, i=1 and x=0.
The invariant states: "x is the sum of L[1..0]" (empty range).
This is true because the sum of zero elements is 0, and x=0.
```

### Template 3: Maintenance Proof

```
Assume the invariant holds at the start of iteration k:
[state the invariant with k substituted]

After the loop body executes:
[show step-by-step what happens]

Therefore, at the start of iteration k+1:
[show the invariant now holds with k+1]
```

### Template 4: Termination Proof

```
The loop terminates when [termination condition].
At this point, the invariant states: [invariant at termination].
Combined with the termination condition, this means: [desired result].
This proves the algorithm is correct.
```

---

## Time Management for Exam

### 1-mark MCQ (Select Invariant):
- **Time:** 1-2 minutes
- **Strategy:**
  - Check initialization (does it hold when i=0 or i=1?)
  - Check range (is it i-1 or i?)
  - Eliminate wrong answers quickly

### 2-mark Proof Question:
- **Time:** 4-5 minutes
- **Strategy:**
  - Write clear initialization, maintenance, termination
  - Use bullet points for clarity
  - Don't spend too much time on detailed algebra

### 4-mark Full Proof:
- **Time:** 8-12 minutes
- **Strategy:**
  - Spend 2 minutes thinking about the invariant
  - Write invariant clearly (1 mark)
  - Proof structure (2 marks): init + maintenance
  - Correctness argument (1 mark): termination
  - If stuck, write the structure and partial reasoning for partial credit

---

## Summary: What You Need to Know

### For MCQ Questions (1-2 marks):
✅ Invariant describes state **at start** of iteration (usually `L[1..i-1]`, not `L[1..i]`)
✅ Must be true at initialization (when i=1 or i=0)
✅ Must relate to loop variable (usually includes i-1)

### For Written Proofs (2-4 marks):
✅ **Three-part structure:** Initialization, Maintenance, Termination
✅ **Initialization:** Show it's true when loop starts
✅ **Maintenance:** Show if true at iteration k, remains true at k+1
✅ **Termination:** Use invariant at loop end to prove correctness

### Key Algorithms to Practice:
1. Binary search (range invariant)
2. Selection sort (sorted region + min property)
3. Insertion sort (sorted region)
4. Accumulation loops (sum, count, product)
5. Modular arithmetic loops

### Common Patterns:
- Accumulator: `acc = f(L[1..i-1])`
- Search range: `key ∈ [lo..hi)` if it exists
- Sorted region: `array[1..i-1]` is sorted
- Conditional accumulation: `x = sum/count of elements in L[1..i-1] satisfying property P`

---

**Good luck with your exam preparation!**

Remember: Loop invariants are just **formalized induction proofs**. If you understand induction from discrete mathematics, you already understand loop invariants!