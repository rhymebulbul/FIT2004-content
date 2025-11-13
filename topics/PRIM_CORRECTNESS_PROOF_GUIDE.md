# Prim's Algorithm Correctness Proof - Exam Guide

**Topic:** Greedy Algorithms - Prim's Minimum Spanning Tree
**Proof Type:** Loop Invariant + Exchange Argument
**Difficulty:** Medium
**Exam Time:** 5-7 minutes for full proof

---

## Table of Contents
1. [Theorem Statement](#theorem-statement)
2. [Proof Structure Overview](#proof-structure-overview)
3. [Detailed Proof Steps](#detailed-proof-steps)
4. [Visual Understanding](#visual-understanding)
5. [Common Mistakes](#common-mistakes)
6. [Memorization Checklist](#memorization-checklist)
7. [Practice Template](#practice-template)

---

## Theorem Statement

**Theorem:** Correctness of Prim's Algorithm

Given a **connected, undirected graph** G = (V, E) with edge weights, Prim's algorithm correctly produces a minimum spanning tree.

**Key requirements:**
- Graph must be connected
- Edge weights can be any real numbers (negative weights OK, unlike Dijkstra)

**Complexity:** O(|E| log |V|) using binary heap priority queue

---

## Proof Structure Overview

### Type of Proof
- **Primary method:** Loop invariant (invariant maintenance)
- **Secondary method:** Exchange argument (constructing alternative MST)

### The Invariant
**At every iteration, the current set of selected edges T is a subset of some minimum spanning tree of G.**

### What Makes Prim's Different from Dijkstra's Proof
- Dijkstra: Uses **induction + contradiction** (prove distances are correct)
- Prim: Uses **invariant + exchange argument** (prove edges belong to some MST)

### Proof Flow Diagram
```
[Invariant Statement]
    ↓
[Base Case: T is empty]
    ↓
[Inductive Hypothesis: T ⊆ some MST M]
    ↓
[Algorithm adds edge e = (u,v)]
    ↓
[Case 1: M contains e → Done]
    ↓
[Case 2: M doesn't contain e]
    ↓
[Find edge (x,y) in M to replace]
    ↓
[Construct M' = M ∪ {e} \ {(x,y)}]
    ↓
[Prove w(e) ≤ w(x,y)]
    ↓
[Show M' is also MST]
    ↓
[Conclude T ∪ {e} ⊆ M']
```

---

## Detailed Proof Steps

### Step 1: Understanding Prim's Algorithm

**What Prim's does:**
```python
T = ∅               # Selected edges (initially empty)
S = {start_vertex}  # Vertices in current tree
Priority Queue Q    # Contains (vertex, key) where key = lightest edge to tree

while Q is not empty:
    u = extract_min(Q)  # u has lightest edge to current tree
    S = S ∪ {u}
    Let e = (v, u) be the edge connecting u to tree (where v ∈ T)
    T = T ∪ {e}         # Add edge to MST

    # Update keys for neighbors
    for each neighbor w of u:
        if w ∉ S and weight(u,w) < key[w]:
            key[w] = weight(u,w)
```

**Key difference from Dijkstra:**
- **Dijkstra key:** dist[v] = total distance from source to v
- **Prim key:** key[v] = weight of **single lightest edge** connecting v to current tree

---

### Step 2: The Invariant Statement

**Invariant:** At every iteration of Prim's algorithm, the current set of selected edges T is a subset of some minimum spanning tree M of G.

**What this means:**
- We can always find at least one MST that contains ALL edges in T
- As we add edges to T, this property is maintained
- When T becomes a spanning tree, T itself IS an MST

**Key phrase for exam:**
> "We prove correctness by showing that in every iteration, the current set T of selected edges is a subset of some minimum spanning tree."

---

### Step 3: Base Case

**Initial state:** T = ∅ (empty set)

**Proof:**
- The empty set is a subset of every MST
- Therefore T ⊆ M for any MST M
- Invariant holds trivially

**Key phrase for exam:**
> "Initially T is empty, so T is a subset of every MST of G, and the invariant holds."

---

### Step 4: Inductive Hypothesis

**Assume:** At some iteration, T is a subset of some minimum spanning tree M.

We write: **T ⊆ M** where M is an MST

**Key phrase for exam:**
> "Suppose that at some iteration, T is a subset of some MST M. We denote this MST by M."

---

### Step 5: Inductive Step - Setup

**What happens next:**
- Prim's algorithm selects edge e = (u, v) where:
  - u ∈ T (u is in the current tree)
  - v ∉ T (v is NOT in the current tree)
  - e has the **lightest weight** among all edges connecting T to vertices outside T

**Goal:** Prove T ∪ {e} is a subset of some MST

**Two cases to consider:**
1. **Case 1:** M contains e → Easy case
2. **Case 2:** M does not contain e → Need exchange argument

**Key phrase for exam:**
> "Let e = (u,v) denote the lightest edge that connects some u ∈ T to some v ∉ T. Prim's adds e to T. We consider two cases."

---

### Step 6: Case 1 - Easy Case

**Case 1:** M already contains edge e

**Proof:**
- T ⊆ M (by inductive hypothesis)
- e ∈ M (by case assumption)
- Therefore T ∪ {e} ⊆ M
- Invariant holds!

**Key phrase for exam:**
> "If M contains e, then T ∪ {e} is a subset of M, so the invariant holds."

---

### Step 7: Case 2 - Exchange Argument Setup

**Case 2:** M does not contain edge e

This is the **core of the proof**.

**Strategy:**
- We'll construct a NEW MST M' that contains T ∪ {e}
- We do this by adding e to M and removing a different edge

**Why this works:**
- M is a tree → adding edge e creates a cycle
- Remove an edge from the cycle → get a new tree M'
- Pick the right edge to remove → M' has same weight as M → M' is also MST

**Key phrase for exam:**
> "Otherwise, suppose M does not contain e. We need to prove that there exists some other MST M' such that T ∪ {e} is a subset of M'."

---

### Step 8: Finding the Path in M

**Key observation:** M is a spanning tree, so it contains a path from u to v.

Let **p** be the path in M from u to v.

**Visual:**
```
In MST M:
u ----path p----> v

Path p consists of edges (because e is not in M)
```

**Why this matters:**
- u ∈ T (u is in current tree)
- v ∉ T (v is outside current tree)
- Path p connects them → at least one edge on p must "cross" from T to outside T

**Key phrase for exam:**
> "Since M is a tree, it contains a path p from u to v."

---

### Step 9: Finding the Edge (x,y) to Exchange

**Critical step:** Find edge (x,y) on path p where x ∈ T and y ∉ T

**How to find it:**
- Start at u (u ∈ T) and follow path p toward v (v ∉ T)
- Since we start inside T and end outside T, we must cross the boundary
- Let (x,y) be the **first edge** on path p where:
  - x ∈ T (still inside current tree)
  - y ∉ T (crossed to outside)

**Visual:**
```
Path p in M:  u → ... → x → y → ... → v
              └─ in T ─┘   └─ not in T ─┘
                         ↑
                    first edge crossing boundary
```

**Why this edge exists:**
- Since T is a subset of M, and we're traversing edges in M
- The first part of path p stays within T
- But eventually we must reach y (which is outside T)
- (x,y) is the boundary edge

**Key phrase for exam:**
> "Since u and v are not connected in T, at least one edge on path p is not in T. Let (x,y) be the first edge on path p from u to v that is not contained in T. Since (x,y) is the first edge not in T, we have x ∈ T and y ∉ T."

---

### Step 10: Constructing the New MST M'

**Step 1: Remove edge (x,y) from M**

Since M is a tree, removing (x,y) disconnects M into two components:
- M₁: Component containing x
- M₂: Component containing y

**Step 2: Add edge e = (u,v) to reconnect**

Since u ∈ T and x ∈ T, both u and x are in M₁
Since v ∉ T and y ∉ T, both v and y are in M₂

Adding edge e = (u,v) reconnects M₁ and M₂

**New tree:**
```
M' = M ∪ {e} \ {(x,y)}
M' = (M₁ ∪ M₂ ∪ {e})
```

**Key phrase for exam:**
> "Since M is a tree, removing edge (x,y) disconnects M into two components M₁ and M₂. Adding edge (u,v) reconnects them to form a new spanning tree M' = M ∪ {(u,v)} \ {(x,y)}."

---

### Step 11: The Weight Comparison - KEY INSIGHT

**Goal:** Prove w(M') ≤ w(M), which means M' is also an MST

**Weight of M':**
```
w(M') = w(M) - w(x,y) + w(u,v)
w(M') = w(M) - w(x,y) + w(e)
```

**The crucial comparison:** w(e) vs w(x,y)

**Why w(e) ≤ w(x,y):**

Remember how Prim's chooses edge e:
- e = (u,v) is the **lightest edge** connecting T to a vertex outside T
- (x,y) is also an edge connecting T (vertex x) to outside T (vertex y)
- If w(x,y) < w(e), Prim's would have chosen (x,y) instead of e
- Therefore: **w(e) ≤ w(x,y)**

**THIS IS THE HEART OF THE PROOF!**

**Computing weight difference:**
```
w(M') - w(M) = w(e) - w(x,y) ≤ 0

Therefore: w(M') ≤ w(M)
```

**Key phrase for exam:**
> "Since (u,v) is the lightest edge connecting T to a new vertex, it is no heavier than (x,y), otherwise Prim's would have picked (x,y) instead since x ∈ T and y ∉ T. In other words, w(u,v) ≤ w(x,y), which implies w(u,v) - w(x,y) ≤ 0."

---

### Step 12: Concluding M' is an MST

**What we know:**
1. M is an MST → w(M) is minimum
2. M' is a spanning tree → w(M') ≥ w(M) (by definition of MST)
3. We just proved: w(M') ≤ w(M)

**Combining 2 and 3:**
```
w(M) ≤ w(M') ≤ w(M)

Therefore: w(M') = w(M)
```

**Conclusion:** Since M' has the same weight as MST M, **M' is also an MST**

**Key phrase for exam:**
> "So the total weight of M' is w(M') = w(M) + w(u,v) - w(x,y) ≤ w(M). But since M is a minimum spanning tree, w(M) ≤ w(M'), and hence w(M) = w(M'). We conclude that M' is also a minimum spanning tree."

---

### Step 13: Completing the Inductive Step

**What we've shown:**
- Started with T ⊆ M (an MST)
- Prim's adds edge e to get T ∪ {e}
- We constructed M' (another MST) that contains T ∪ {e}

**Therefore:** T ∪ {e} ⊆ M'

**Invariant maintained!**

**Key phrase for exam:**
> "Since T ∪ {e} is a subset of M', we have shown that the invariant is maintained."

---

### Step 14: Final Correctness Argument

**Part 1: Prim's produces a spanning tree**

**Why no cycles:**
- Prim's only adds edges from tree to NEW vertices
- Never creates cycles

**Why it spans all vertices:**
- Graph is connected
- Algorithm continues until no more vertices can be added
- Therefore visits every vertex

**Part 2: The spanning tree is minimum**

**When algorithm terminates:**
- T is a spanning tree
- By invariant: T ⊆ some MST M
- Spanning trees have exactly |V| - 1 edges
- T has |V| - 1 edges, M has |V| - 1 edges
- Since T ⊆ M and both have same number of edges: **T = M**

**Therefore T itself is an MST!**

**Key phrase for exam:**
> "First, we argue that Prim's produces a spanning tree. Whenever Prim's adds an edge to the MST, it does so to a newly added vertex, which means it can never create a cycle. Since the graph is connected, Prim's will visit every vertex and hence produce a spanning tree. Therefore when the algorithm terminates, T is a spanning tree, and by the invariant above, T is a subset of some minimum spanning tree. Since all spanning trees contain the same number of edges (|V|-1), T itself must be a minimum spanning tree."

---

## Visual Understanding

### The Big Picture

```
ITERATION i:

Current tree T (vertices):  {s, a, b, c}
Current edges in T:         {(s,a), (a,b), (b,c)}

Candidate edges leaving T:
  (c, d): weight 5  ← LIGHTEST (Prim's picks this)
  (a, e): weight 7
  (b, f): weight 9

Some MST M contains: {(s,a), (a,b), (b,c), ...}
                     └──── all of T ────┘

After adding (c,d):
New T edges: {(s,a), (a,b), (b,c), (c,d)}

Either:
  - M already has (c,d) → T still ⊆ M ✓
  - M doesn't have (c,d) → Exchange to create M' ✓
```

### The Exchange Argument Visualized

```
BEFORE EXCHANGE:

MST M:
    s ─── a ─── b ─── c
          │
          └─── x ─── y ─── v

Current tree T: {s, a, b, c}
Prim's picks: e = (c, v), weight 5
But M has path c→a→x→y→v instead

Edge (x,y) is first edge leaving T on this path
Weight of (x,y) = 8

EXCHANGE:

M' = M - (x,y) + (c,v)

    s ─── a ─── b ─── c
          │           │
          └─── x   y ─┴─ v

Weight change: w(M') = w(M) - 8 + 5 ≤ w(M)
Since M is MST: w(M') = w(M)
Therefore M' is also MST
And T ∪ {(c,v)} ⊆ M' ✓
```

### Concrete Example with Numbers

```
Graph:
         5         8        3
    s ─────── a ─────── b ────── c
    │         │                  │
    │ 10      │ 7                │ 4
    │         │                  │
    d ─────── e                  f
         6

Prim's execution:
1. Start at s: T = ∅

2. Add (s,a) [weight 5]: T = {(s,a)}
   Tree vertices: {s,a}

3. Next lightest: (a,e) [weight 7] vs (s,d) [weight 10]
   Add (a,e): T = {(s,a), (a,e)}
   Tree vertices: {s,a,e}

4. Next lightest: (e,d) [weight 6] vs (s,d) [10] vs (a,b) [8]
   Add (e,d): T = {(s,a), (a,e), (e,d)}
   Tree vertices: {s,a,e,d}

5. Next lightest: (a,b) [weight 8]
   Add (a,b): T = {(s,a), (a,e), (e,d), (a,b)}

6. Next lightest: (b,c) [weight 3]
   Add (b,c): T = {(s,a), (a,e), (e,d), (a,b), (b,c)}

7. Next lightest: (c,f) [weight 4]
   Add (c,f): T = {(s,a), (a,e), (e,d), (a,b), (b,c), (c,f)}

Final MST weight: 5 + 7 + 6 + 8 + 3 + 4 = 33

At each step, the invariant holds:
- T is always a subset of some MST
```

---

## Common Mistakes

### ❌ Mistake 1: Not stating the invariant clearly
**Wrong:** "Prim's always maintains an MST..."
**Right:** "The invariant is: At every iteration, the current set of selected edges T is a subset of some minimum spanning tree M."

### ❌ Mistake 2: Confusing Prim's with Dijkstra's proof structure
**Wrong:** "Use induction and contradiction like Dijkstra..."
**Right:** "Use loop invariant and exchange argument (different from Dijkstra)"

### ❌ Mistake 3: Not explaining why edge (x,y) exists
**Wrong:** "Let (x,y) be an edge in M..."
**Right:** "Since M contains a path from u to v, and this path must cross from T to outside T, let (x,y) be the first edge on this path where x ∈ T and y ∉ T."

### ❌ Mistake 4: Missing the key weight comparison
**Wrong:** "So we replace (x,y) with e..."
**Right:** "Since e is the lightest edge from T to outside T, and (x,y) also connects T to outside T, we have w(e) ≤ w(x,y)."

### ❌ Mistake 5: Not proving M' is a tree
**Wrong:** "Add e to M..."
**Right:** "Removing (x,y) disconnects M into two components. Adding e reconnects them, forming a new spanning tree M'."

### ❌ Mistake 6: Weak conclusion
**Wrong:** "So T is eventually an MST."
**Right:** "When Prim's terminates, T is a spanning tree with |V|-1 edges. By the invariant, T ⊆ some MST M. Since both have |V|-1 edges, T = M, so T is an MST."

### ❌ Mistake 7: Forgetting to prove Prim's creates no cycles
**Wrong:** Just proving the invariant...
**Right:** "First show Prim's produces a spanning tree (adds edges to new vertices → no cycles; graph connected → spans all vertices). Then use invariant to show it's minimum."

---

## Memorization Checklist

### Invariant Statement (Must Know)
- [ ] "At every iteration, T is a subset of some MST"
- [ ] Base case: T = ∅ is subset of all MSTs
- [ ] Inductive hypothesis: T ⊆ M for some MST M
- [ ] Goal: Show T ∪ {e} ⊆ some MST

### Edge Selection (Must Know)
- [ ] Prim's picks e = (u,v) where u ∈ T, v ∉ T
- [ ] e has lightest weight among edges leaving T
- [ ] Two cases: M contains e, or M doesn't

### Exchange Argument (Must Know)
- [ ] M contains path p from u to v (since M is tree)
- [ ] Find first edge (x,y) on p where x ∈ T, y ∉ T
- [ ] Remove (x,y) from M → disconnects into M₁, M₂
- [ ] Add e to reconnect → M' = M ∪ {e} \ {(x,y)}

### Weight Comparison (Must Know)
- [ ] w(e) ≤ w(x,y) because Prim's picks lightest
- [ ] Both e and (x,y) connect T to outside
- [ ] If w(x,y) < w(e), Prim's would've picked (x,y)
- [ ] Therefore w(M') = w(M) - w(x,y) + w(e) ≤ w(M)

### MST Equality (Must Know)
- [ ] M is MST → w(M) ≤ w(M') (definition)
- [ ] We proved w(M') ≤ w(M)
- [ ] Therefore w(M) = w(M')
- [ ] So M' is also an MST

### Final Correctness (Must Know)
- [ ] Prim's produces spanning tree (no cycles, connected)
- [ ] When terminates: T has |V|-1 edges
- [ ] By invariant: T ⊆ some MST M
- [ ] Same edge count → T = M → T is MST

---

## Practice Template

Use this template when practicing the proof:

```
THEOREM: Given connected undirected graph G = (V,E) with edge weights,
Prim's algorithm correctly produces a minimum spanning tree.

PROOF:

[1. INVARIANT STATEMENT]
We prove correctness by showing the following invariant holds:
"At every iteration, the current set of selected edges T is a subset
of some minimum spanning tree of G."

[2. BASE CASE]
Initially T = ∅ (empty set).
The empty set is a subset of every MST of G.
Therefore the invariant holds. ✓

[3. INDUCTIVE HYPOTHESIS]
Suppose at some iteration, T is a subset of some MST M.

[4. ALGORITHM STEP]
Let e = (u,v) be the edge Prim's adds next, where:
- u ∈ T (u is in current tree)
- v ∉ T (v is outside current tree)
- e has the lightest weight among all edges connecting T to vertices outside T

[5. CASE 1: M CONTAINS e]
If M contains e, then T ∪ {e} ⊆ M.
The invariant holds. ✓

[6. CASE 2: M DOES NOT CONTAIN e]
Suppose M does not contain e.
We will construct a new MST M' such that T ∪ {e} ⊆ M'.

[7. FIND PATH IN M]
Since M is a tree, it contains a path p from u to v.

[8. FIND BOUNDARY EDGE]
Since u ∈ T and v ∉ T, at least one edge on path p must leave T.
Let (x,y) be the first edge on path p where x ∈ T and y ∉ T.

[9. CONSTRUCT M']
Remove (x,y) from M → disconnects M into components M₁ (containing x) and M₂ (containing y).
Add e = (u,v) to reconnect → M' = M ∪ {e} \ {(x,y)}.
M' is a spanning tree.

[10. WEIGHT COMPARISON]
Since e is the lightest edge connecting T to outside T,
and (x,y) also connects T (vertex x) to outside T (vertex y),
we have w(e) ≤ w(x,y).

Therefore:
  w(M') = w(M) + w(e) - w(x,y)
        ≤ w(M)

[11. M' IS MST]
Since M is an MST: w(M) ≤ w(M') (by definition of minimum).
We just showed: w(M') ≤ w(M).
Therefore: w(M) = w(M').
So M' is also a minimum spanning tree.

[12. INVARIANT MAINTAINED]
Since T ∪ {e} ⊆ M', the invariant is maintained. ✓

[13. PRIM'S PRODUCES SPANNING TREE]
Prim's adds edges only to new vertices → never creates cycles.
Graph is connected → Prim's visits all vertices → spans all vertices.
Therefore Prim's produces a spanning tree.

[14. CONCLUSION]
When Prim's terminates, T is a spanning tree with |V|-1 edges.
By the invariant, T ⊆ some MST M (which also has |V|-1 edges).
Since both have the same number of edges: T = M.
Therefore T itself is a minimum spanning tree. □
```

---

## Comparison with Dijkstra's Proof

| Aspect | Dijkstra | Prim |
|--------|----------|------|
| **Proof technique** | Induction + Contradiction | Loop Invariant + Exchange |
| **What we prove** | Distance estimates are correct | Edges belong to some MST |
| **Boundary concept** | Vertices x, y on shortest path | Edge (x,y) on path in MST |
| **Key comparison** | dist[y] < dist[u] → contradiction | w(e) ≤ w(x,y) → equal weight MST |
| **Relaxation** | Critical step | Not needed |
| **Weight requirement** | Non-negative | Any weights |
| **Final argument** | By contradiction | By invariant + edge count |

---

## Exam Strategy

### Time Management (7 minutes total)
- **1 min:** Write invariant and base case
- **1 min:** State inductive hypothesis and algorithm step
- **2 min:** Exchange argument (path, find (x,y), construct M')
- **2 min:** Weight comparison and prove M' is MST
- **1 min:** Final correctness argument

### What Examiners Look For
1. **Clear invariant statement**
2. **Both cases** (M contains e vs doesn't)
3. **Finding edge (x,y)** correctly (first edge leaving T on path)
4. **Weight comparison** w(e) ≤ w(x,y) with justification
5. **Proving M' is MST** (weight equality)
6. **Final argument** (spanning tree + invariant → MST)

### Quick Checks Before Submitting
- [ ] Did I state the invariant?
- [ ] Did I prove base case?
- [ ] Did I handle both cases (M contains e or not)?
- [ ] Did I explain how to find edge (x,y)?
- [ ] Did I justify w(e) ≤ w(x,y)?
- [ ] Did I prove M' has same weight as M?
- [ ] Did I conclude with spanning tree argument?

---

## Additional Notes

### Why This Proof Is Important
- Tests understanding of greedy correctness
- Shows exchange argument technique
- Demonstrates MST properties
- Simpler than Dijkstra but still rigorous

### Key Insight
The invariant "T ⊆ some MST" is weaker than "T IS part of THE MST" (since there can be multiple MSTs with same weight). This makes the proof easier because we can construct different MSTs at each step.

### Connection to Other Topics
- **Kruskal's MST:** Similar exchange argument for correctness
- **Dijkstra's:** Same algorithm structure, different proof
- **Greedy algorithms:** Classic example of greedy correctness proof
- **Loop invariants:** General technique for proving iterative algorithms

---

**Last Updated:** Exam Preparation Period
**Difficulty Rating:** ⭐⭐⭐ (3/5)
**Must Know For:** Mid-semester and Final exams
**Practice Recommended:** 2-3 full write-throughs until fluent