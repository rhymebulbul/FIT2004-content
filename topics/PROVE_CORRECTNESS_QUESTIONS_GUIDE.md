# FIT2004 "Prove Correctness of This Algorithm" Questions Guide

This guide documents **all types of correctness proof questions** you might encounter in FIT2004 exams, based on lecture slides, course notes, applied solutions, and past exam analysis.

**Last Updated:** 2025-10-26
**Source:** lecture/, course_notes/, applied_solutions/, exams/

---

## Table of Contents

1. [What is an Algorithm Correctness Proof?](#what-is-an-algorithm-correctness-proof)
2. [Types of Correctness Proof Questions](#types-of-correctness-proof-questions)
3. [Proof Technique 1: Loop Invariants](#proof-technique-1-loop-invariants)
4. [Proof Technique 2: Exchange Arguments (Greedy)](#proof-technique-2-exchange-arguments-greedy)
5. [Proof Technique 3: Cut Property / Cycle Property (MST)](#proof-technique-3-cut-property--cycle-property-mst)
6. [Proof Technique 4: Induction](#proof-technique-4-induction)
7. [Proof Technique 5: Contradiction](#proof-technique-5-contradiction)
8. [Past Exam Questions by Algorithm Type](#past-exam-questions-by-algorithm-type)
9. [Common Mistakes to Avoid](#common-mistakes-to-avoid)
10. [Exam Strategy and Templates](#exam-strategy-and-templates)

---

## What is an Algorithm Correctness Proof?

**Definition:** A correctness proof demonstrates that an algorithm:
1. **Terminates** (eventually stops)
2. **Produces the correct output** for all valid inputs
3. **Satisfies its specification** (does what it claims to do)

**Why it matters:**
- Worth 3-4 marks per question in exams
- Appears in "Common" frequency (most final exams)
- Tests deep understanding, not just memorization

---

## Types of Correctness Proof Questions

Based on past exam analysis, you might be asked to:

### Type 1: Loop Invariant Proofs (Most Common)
**Frequency:** Every exam
**Marks:** 3-4
**Appears in:** Analysis of Algorithms section

**Example algorithms:**
- Counting algorithms
- Accumulation loops
- Sorting algorithms (Selection Sort, Insertion Sort, Binary Search)
- Modular arithmetic loops

**See:** [LOOP_INVARIANT_QUESTIONS_GUIDE.md](LOOP_INVARIANT_QUESTIONS_GUIDE.md) for full coverage

---

### Type 2: Greedy Algorithm Correctness (Common)
**Frequency:** Common
**Marks:** 3-4
**Appears in:** Applications section, MST algorithms

**Example algorithms:**
- Interval scheduling
- Dijkstra's algorithm
- Prim's algorithm
- Kruskal's algorithm
- Activity selection

**Proof technique:** Exchange argument / "Stays ahead" argument

---

### Type 3: Graph Algorithm Correctness (Common)
**Frequency:** Common
**Marks:** 2-4
**Appears in:** Graph traversal, cycle detection

**Example algorithms:**
- Two-coloring
- Cycle detection (directed vs undirected)
- Shortest cycle finding
- Connected components counting

**Proof technique:** Properties of DFS/BFS, contradiction

---

### Type 4: MST Algorithm Variants (Occasional)
**Frequency:** Occasional
**Marks:** 3-4
**Appears in:** Greedy algorithms section

**Example:**
- Reverse Kruskal's algorithm (remove heavy edges)
- Bottleneck path correctness

**Proof technique:** Cut property, cycle property, invariants

---

### Type 5: Divide and Conquer Correctness (Rare)
**Frequency:** Rare
**Marks:** 2-3
**Appears in:** Divide and Conquer section

**Example algorithms:**
- K-wise merge
- Fixed point search

**Proof technique:** Induction on problem size

---

## Proof Technique 1: Loop Invariants

**When to use:** Iterative algorithms with loops

**Structure:** Three parts (see LOOP_INVARIANT_QUESTIONS_GUIDE.md)
1. **Initialization:** Invariant holds before first iteration
2. **Maintenance:** If true before iteration k, remains true before k+1
3. **Termination:** Invariant at termination proves correctness

### Example: Counting Occurrences

**Past Exam:** Applied Solutions Week 3, Problem 7

**Algorithm:**
```python
function COUNT(A[1..n], target):
    count = 0
    i = 1
    while i ≤ n:
        if A[i] = target:
            count = count + 1
        i = i + 1
    return count
```

**Correctness Proof:**

**Invariant:** At the start of iteration i, `count` equals the number of occurrences of `target` in `A[1..i-1]`.

**Initialization:** At i=1, count=0. The invariant states "count equals occurrences in A[1..0]" (empty list). Since the sum of an empty list is 0, the invariant holds.

**Maintenance:** Assume invariant holds at start of iteration k, so count = occurrences in A[1..k-1] = c.
- If A[k] = target: count becomes c+1, which equals occurrences in A[1..k]
- If A[k] ≠ target: count stays c, which equals occurrences in A[1..k]

Therefore, invariant holds at start of iteration k+1.

**Termination:** Loop terminates when i = n+1. By the invariant, count = occurrences in A[1..n] = A. This proves correctness.

---

## Proof Technique 2: Exchange Arguments (Greedy)

**When to use:** Greedy algorithms that make locally optimal choices

**Structure:**
1. **Greedy choice property:** Show that greedy choice is always safe
2. **Exchange argument:** Show you can swap greedy solution into optimal solution without losing optimality
3. **Optimal substructure:** Show that after greedy choice, remaining problem has same property

### Example: Interval Scheduling

**Past Exam:** Exam s1.json, Question 20 (3 marks)
**Applied Solutions:** Week 6, Problem 7

**Problem:** Choose maximum number of compatible (non-overlapping) requests

**Algorithm:**
```
function INTERVAL_SCHEDULING(requests[1..N]):
    Sort requests by finish time (ascending)
    ACCEPTED = []
    for each request r in sorted order:
        if r is compatible with ACCEPTED:
            ACCEPTED.append(r)
    return ACCEPTED
```

**Correctness Proof (Exchange Argument):**

Let i₁, i₂, ..., iₘ be the requests selected by the greedy algorithm (in time order).

**Claim:** This is an optimal solution (maximum size).

**Proof by contradiction:**

Suppose there exists a larger compatible subset j₁, j₂, ..., jₙ with n > m.

**Lemma (Stays Ahead):** For k = 1, 2, ..., m, we have f(iₖ) ≤ f(jₖ)
(where f(i) = finish time of request i)

**Proof of Lemma (by induction on k):**

*Base case (k=1):*
The greedy algorithm selects i₁ as the request with earliest finish time. Therefore f(i₁) ≤ f(j₁).

*Inductive step:*
Assume f(iₖ) ≤ f(jₖ). We need to show f(iₖ₊₁) ≤ f(jₖ₊₁).

Since j₁, ..., jₙ is compatible, jₖ₊₁ starts after jₖ finishes: s(jₖ₊₁) ≥ f(jₖ).

By the inductive hypothesis: f(iₖ) ≤ f(jₖ).

Therefore: s(jₖ₊₁) ≥ f(jₖ) ≥ f(iₖ).

This means jₖ₊₁ is compatible with i₁, ..., iₖ. The greedy algorithm considers all compatible requests and selects the one with earliest finish time. Therefore:

f(iₖ₊₁) ≤ f(jₖ₊₁) ✓

**Main Proof:**

By the lemma, f(iₘ) ≤ f(jₘ).

Since n > m, there exists request jₘ₊₁. Since j₁, ..., jₙ is compatible:

s(jₘ₊₁) ≥ f(jₘ) ≥ f(iₘ)

This means jₘ₊₁ is compatible with i₁, ..., iₘ. But the greedy algorithm would have selected jₘ₊₁ (or something with earlier finish time), which contradicts the fact that it stopped at iₘ.

Therefore, no larger compatible subset exists, and the greedy algorithm is optimal. ✓

**Key Insight:** We proved the greedy solution "stays ahead" of any other solution, showing it can't be beaten.

---

## Proof Technique 3: Cut Property / Cycle Property (MST)

**When to use:** MST algorithms (Prim's, Kruskal's) and variants

### Example 1: Reverse Kruskal's Algorithm

**Applied Solutions:** Week 6, Problem 5

**Algorithm:** Remove edges in decreasing weight order while keeping graph connected

```
function REVERSE_KRUSKAL(G = (V, E)):
    Sort E by weight (descending: heaviest first)
    T = E
    for each edge e in non-increasing order:
        if T - {e} is connected:
            T = T - {e}
    return T
```

**Correctness Proof:**

**Invariant:** At each iteration, T is a superset of some MST of G.

**Initialization:** T = E contains all edges, so it's definitely a superset of any MST.

**Maintenance:**

Suppose T is a superset of some MST M. Let e be the next edge considered.

*Case 1:* e ∉ M
Then T - {e} is still a superset of M. Invariant holds.

*Case 2:* e ∈ M
Removing e from M creates two disconnected subtrees. Since removing e from T doesn't disconnect T, e must be in some cycle in T. This cycle contains another edge e' ≠ e connecting the two subtrees.

Since e is the heaviest edge whose removal doesn't disconnect T, and e' also doesn't disconnect T (it's in a cycle with e):

w(e') ≤ w(e)

Create M' by removing e from M and adding e':

w(M') = w(M) - w(e) + w(e') ≤ w(M)

Since M is an MST: w(M') ≥ w(M)

Therefore: w(M') = w(M)

So M' is also an MST, and M' ⊆ T - {e}. Invariant holds.

**Termination:**

The algorithm produces a connected graph (never removes disconnecting edges) with no cycles (would remove cycle-creating edges). Therefore, it's a spanning tree.

By the invariant, this spanning tree is a superset of some MST. Since all spanning trees have the same number of edges (V-1), it must BE an MST.

Therefore, the algorithm correctly produces an MST. ✓

---

### Example 2: MST with Negative Weights

**Applied Solutions:** Week 6, Problem 2

**Question:** Can Prim's and Kruskal's work with negative weights?

**Answer:** YES

**Correctness Argument:**

1. **Prim's and Kruskal's greedily select minimum weight edges**
   - Whether weights are positive or negative doesn't matter
   - Still selecting smallest available weights

2. **Proofs don't assume non-negative weights**
   - Cut property: Lightest edge crossing cut is in some MST
   - Cycle property: Heaviest edge in cycle is not in any MST
   - Both properties hold regardless of sign

3. **Alternative proof:** Add constant to all edges
   - Add k to each edge to make all weights non-negative
   - MST of modified graph has same edges as original
   - Therefore, correctness extends to negative weights

**Note:** This differs from Dijkstra's, which **requires** non-negative weights!

---

## Proof Technique 4: Induction

**When to use:** Recursive algorithms, divide-and-conquer

### Example: Union-Find "Union by Size" Complexity

**Applied Solutions:** Week 6, Problem 8 (Supplementary)

**Lemma to Prove:** For any disjoint-set tree with union-by-size heuristic:

size(r) ≥ 2^(height(r))

where r = root, size(r) = number of nodes, height(r) = tree height

**Proof by Induction:**

**Base Case:**

Initially, every tree is a single node:
- size(r) = 1
- height(r) = 0
- 2^0 = 1

Therefore: size(r) ≥ 2^(height(r)) ✓

**Inductive Step:**

Assume lemma holds after k unions. Consider the (k+1)-th union merging trees rooted at s and r.

WLOG, assume size(r) ≥ size(s), so s goes under r.

*Case 1: height(r) > height(s)*

After merge:
- size'(r) ≥ size(r) ≥ 2^(height(r)) [by hypothesis]
- height'(r) = height(r) [taller tree doesn't change height]

Therefore: size'(r) ≥ 2^(height'(r)) ✓

*Case 2: height(r) ≤ height(s)*

After merge:
- size'(r) = size(r) + size(s) ≥ 2 × size(s) [since size(r) ≥ size(s)]
- By hypothesis: size(s) ≥ 2^(height(s))
- Therefore: size'(r) ≥ 2 × 2^(height(s)) = 2^(height(s)+1)
- height'(r) = height(s) + 1 [shorter tree goes under taller]

Therefore: size'(r) ≥ 2^(height'(r)) ✓

By induction, the lemma holds for all unions. ✓

**Consequence:** height(r) ≤ log₂(V), so union operations take O(log V).

---

## Proof Technique 5: Contradiction

**When to use:** Showing something is impossible, or proving uniqueness

### Example: Bottleneck Paths in MST

**Applied Solutions:** Week 6, Problem 4(b)

**Claim:** All paths in an MST M are bottleneck paths in G.

**Proof by Contradiction:**

Let s, t be any two vertices. Since M is a tree, there's a **unique** path p from s to t in M.

**Suppose (for contradiction)** p is NOT a bottleneck path.

Then there exists another s-t path p' in G such that:

max(edge weights in p') < max(edge weights in p)

Let e be the heaviest edge on p. Remove e from M, creating two disconnected subtrees.

Since p' connects s to t in G, at least one edge on p' must cross between these subtrees. Call this edge e'.

Since every edge on p' is lighter than e:

w(e') < w(e)

Now add e' back to M, reconnecting the two subtrees. This creates a spanning tree M' with:

w(M') = w(M) - w(e) + w(e') < w(M)

But M was a **minimum** spanning tree, so no spanning tree can be lighter. **Contradiction!**

Therefore, p must be a bottleneck path. ✓

---

## Past Exam Questions by Algorithm Type

### Loop Invariant Proofs

| Exam | Question | Algorithm | Marks | Proof Required |
|------|----------|-----------|-------|----------------|
| **s1.json** | Q2 | Modular sum checking | 4 | Full proof (init, maintenance, termination) |
| **s2.json** | Q3-4 | Sum of elements with factor m | 3 | Select invariant (1) + prove (2) |
| **s3.json** | Q2 | Count elements with factor m | 2 | MCQ on invariant properties |
| **Applied Week 3** | Prob 7 | Counting occurrences | - | Full loop invariant proof |
| **Applied Week 3** | Prob 8 | Insertion sort (reverse order) | - | Write invariant |
| **Applied Week 3** | Prob 9 | Binary search variants | - | Invariants for first/last occurrence |

**Common patterns:**
- Accumulation (sum, count)
- Modular arithmetic
- Searching algorithms
- Sorting algorithms

---

### Greedy Algorithm Correctness

| Exam | Question | Algorithm | Marks | Proof Technique |
|------|----------|-----------|-------|-----------------|
| **s1.json** | Q20 | Interval scheduling | 3 | Exchange argument |
| **Applied Week 6** | Prob 7 | Interval scheduling | - | "Stays ahead" proof |
| **25-1.json** | Q9 | Prim's/Kruskal's properties | - | Correctness reasoning |

**Common patterns:**
- Interval scheduling
- Greedy choice property
- Exchange argument
- Optimal substructure

---

### Graph Algorithm Correctness

| Applied Solutions | Problem | Algorithm | Proof Type |
|-------------------|---------|-----------|------------|
| **Week 5** | Prob 1 | Two-coloring (bipartite) | DFS correctness |
| **Week 5** | Prob 3(b) | Cycle detection (directed) | DFS with states |
| **Week 5** | Prob 6 | Shortest cycle | Multiple BFS correctness |
| **Week 5** | Prob 7 | Count cycle components | DFS with degree check |
| **Week 5** | Prob 10 | Undirected cycle O(V) | Complexity proof |

**Common patterns:**
- DFS/BFS properties
- State-based graphs
- Cycle properties

---

### MST Algorithm Correctness

| Applied Solutions | Problem | Algorithm | Proof Type |
|-------------------|---------|-----------|------------|
| **Week 6** | Prob 2 | MST with negative weights | Correctness argument |
| **Week 6** | Prob 4(b) | Bottleneck paths in MST | Proof by contradiction |
| **Week 6** | Prob 5 | Reverse Kruskal's | Invariant proof |
| **Week 6** | Prob 8 | Union-Find complexity | Proof by induction |

**Common patterns:**
- Cut/cycle properties
- Exchange arguments
- Invariant maintenance

---

## Common Mistakes to Avoid

### Mistake 1: Not Proving All Three Parts (Loop Invariants)

❌ **Wrong:** Only proving maintenance, skipping initialization and termination

✅ **Correct:** Always prove:
1. Initialization
2. Maintenance (inductive step)
3. Termination (use invariant to show correctness)

---

### Mistake 2: Vague "It's Obvious" Arguments

❌ **Wrong:** "The greedy algorithm clearly works because it picks the best choice."

✅ **Correct:** Use formal exchange argument:
- Define optimal solution O
- Show greedy solution G can be transformed to match O
- Prove transformation doesn't decrease optimality

---

### Mistake 3: Circular Reasoning

❌ **Wrong:** "The algorithm is correct because it produces the correct output."

✅ **Correct:** Prove correctness from **first principles**:
- Start with algorithm specification
- Use invariants/properties to show it meets specification
- Don't assume what you're trying to prove

---

### Mistake 4: Forgetting Edge Cases

❌ **Wrong:** Only proving for "typical" cases

✅ **Correct:** Consider:
- Empty input
- Single element
- All elements equal
- Boundary conditions

---

### Mistake 5: Not Using Proof by Contradiction Properly

❌ **Wrong:** "Suppose the algorithm is wrong. Then it's wrong. Contradiction."

✅ **Correct:**
1. Assume negation of what you want to prove
2. Derive a logical contradiction
3. Conclude original statement must be true

**Example:** "Suppose MST M doesn't contain minimum edge e crossing cut S. Then adding e creates a cycle. This cycle has an edge e' also crossing S with w(e') ≥ w(e). Replacing e' with e gives lighter spanning tree. But M was minimum. Contradiction!"

---

## Exam Strategy and Templates

### Template 1: Loop Invariant Proof (4 marks)

**Time:** 8-12 minutes

**Structure:**
```
(a) Invariant: [State property in terms of loop variable]

(b) Proof:

Initialization: [Show invariant holds before first iteration]
- At [initial value], [invariant statement]
- This is true because [reasoning]

Maintenance: [Show invariant preserved]
- Assume invariant holds at iteration k: [restate with k]
- After loop body executes: [explain what happens]
- Therefore, at iteration k+1: [show invariant still holds]

(c) Termination: [Use invariant to prove correctness]
- Loop terminates when [condition]
- By invariant: [state invariant at termination]
- This equals [desired result], proving correctness
```

---

### Template 2: Exchange Argument (Greedy) (3-4 marks)

**Time:** 10-15 minutes

**Structure:**
```
Greedy Choice Property:
- Greedy selects [describe choice]
- This is safe because [reasoning]

Exchange Argument:
- Let G = greedy solution, O = optimal solution
- If O ≠ G, find first difference at position k
- Replace O's choice at k with G's choice
- Show w(O') = w(O) [or w(O') ≥ w(O)]
- Therefore, greedy choice doesn't lose optimality

Optimal Substructure:
- After greedy choice, remaining problem is [describe]
- Apply same reasoning recursively
- Greedy algorithm produces optimal solution ✓
```

---

### Template 3: MST Invariant Proof (3-4 marks)

**Time:** 10-15 minutes

**Structure:**
```
Invariant: [At each iteration, T is superset of some MST]

Initialization:
- Initially, T = [starting configuration]
- Contains [all edges / no edges]
- Clearly superset of some MST

Maintenance:
- Assume T is superset of MST M
- Consider next edge e
- Case 1: e ∉ M → T-{e} still contains M
- Case 2: e ∈ M → [use cut/cycle property to find e']
  - Show can replace e with e' in M
  - Get M' with w(M') = w(M)
  - M' ⊆ T after operation

Termination:
- Final T is [connected / has no cycles]
- By invariant, T is superset of some MST
- All spanning trees have V-1 edges
- Therefore, T IS an MST ✓
```

---

### Template 4: Proof by Contradiction (2-3 marks)

**Time:** 6-10 minutes

**Structure:**
```
Claim: [What you want to prove]

Proof by Contradiction:

Suppose (for contradiction) that [negation of claim].

Then [derive consequences]:
- [Step 1: logical consequence]
- [Step 2: another consequence]
- [Step 3: reach contradiction with known fact]

But [state the contradiction explicitly].

Therefore, our assumption was wrong, and [original claim] must be true. ✓
```

---

## Quick Reference: When to Use Each Technique

| Algorithm Type | Primary Proof Technique | Secondary Technique |
|---------------|------------------------|---------------------|
| **Iterative loops** | Loop invariants | - |
| **Greedy algorithms** | Exchange argument | Optimal substructure |
| **MST algorithms** | Cut/cycle property | Invariant |
| **Recursive algorithms** | Induction | - |
| **Graph traversal** | DFS/BFS properties | Contradiction |
| **"Is this possible?"** | Contradiction | Counterexample |
| **Uniqueness claims** | Contradiction | - |

---

## Exam Time Management

### 2-mark proof (short):
- **Time:** 4-5 minutes
- **Strategy:** Write key steps, brief justification

### 3-mark proof (medium):
- **Time:** 8-10 minutes
- **Strategy:** Full structure, but concise explanations

### 4-mark proof (full):
- **Time:** 10-15 minutes
- **Strategy:** Complete proof with all steps justified
- Don't skip initialization or termination!

---

## Practice Strategy

### Week 1-2: Master Loop Invariants
- Practice: Applied Week 3, Problems 7-11
- Focus: Counting, accumulation, binary search

### Week 3-4: Learn Exchange Arguments
- Practice: Applied Week 6, Problem 7 (interval scheduling)
- Practice: Exam s1.json Q20

### Week 5-6: MST Proofs
- Practice: Applied Week 6, Problems 2, 4, 5
- Focus: Cut property, invariants

### Week 7+: Mixed Practice
- Practice: Past exam correctness questions
- Time yourself (2-3 min/mark)

---

## Summary: Must-Know Proofs

### Absolutely Must Know:
1. ✅ **Loop invariant structure** (init, maintenance, termination)
2. ✅ **Exchange argument** for greedy algorithms
3. ✅ **Cut property** for MST algorithms

### Should Know:
4. ⚠️ Proof by induction (recursive algorithms)
5. ⚠️ Proof by contradiction (uniqueness, impossibility)
6. ⚠️ DFS/BFS correctness properties

### Nice to Know:
7. 📌 Complexity proofs (amortized analysis)
8. 📌 Optimal substructure (DP/greedy)

---

**Good luck with your exam preparation!**

Remember: **Understanding > Memorization**. Practice writing proofs from scratch, not just reading solutions!