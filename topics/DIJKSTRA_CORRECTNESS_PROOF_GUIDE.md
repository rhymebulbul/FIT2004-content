# Dijkstra's Algorithm Correctness Proof - Exam Guide

**Topic:** Greedy Algorithms - Dijkstra's Algorithm
**Proof Type:** Induction + Proof by Contradiction
**Difficulty:** Medium-Hard
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

**Theorem:** Correctness of Dijkstra's Algorithm

Given a graph G = (V, E) with **non-negative edge weights** and a source vertex s, Dijkstra's algorithm correctly finds shortest paths to each vertex v ∈ V.

**Key requirement:** Non-negative weights (proof fails without this)

---

## Proof Structure Overview

### Type of Proof
- **Primary method:** Mathematical induction
- **Secondary method:** Proof by contradiction (within inductive step)

### What We Induct On
**Set S = V \ Q** (vertices removed from priority queue = visited vertices)

### Inductive Claim
For any vertex v ∈ S, dist[v] = δ(s,v) (distance estimate equals true shortest distance)

### Proof Flow Diagram
```
[Base Case]
    ↓
[Inductive Hypothesis]
    ↓
[Inductive Step: Assume contradiction]
    ↓
[Define boundary vertices x, y]
    ↓
[Build inequality chain]
    ↓
[Use relaxation to show dist[y] < dist[u]]
    ↓
[Contradiction: PQ would choose y not u]
    ↓
[Conclusion: dist[u] must be correct]
```

---

## Detailed Proof Steps

### Step 1: Base Case

**What to prove:** When S = {s} (only source visited), dist[s] is correct.

**Proof:**
- Initially, dist[s] = 0
- The source s is the first vertex removed from Q
- True shortest distance δ(s,s) = 0 (no negative weights)
- Therefore dist[s] = δ(s,s) ✓

**Key phrase for exam:**
> "For the base case, the source vertex s is removed first with dist[s] = 0, which is correct since the graph contains no negative weights."

---

### Step 2: Inductive Hypothesis

**Assume:** At some point during execution, for all vertices v ∈ S (already visited), dist[v] = δ(s,v) (correct).

**Key phrase for exam:**
> "Suppose for induction that at some point, for all v ∈ S, dist[v] is correct."

---

### Step 3: Inductive Step Setup

**Goal:** Prove that when we remove the next vertex u from Q, dist[u] is also correct.

**Proof by contradiction setup:**

Assume for contradiction that dist[u] is **incorrect**, meaning:
- ∃ a shorter path from s to u
- True shortest distance δ(s,u) < dist[u]

**Key phrase for exam:**
> "Let u be the next vertex removed from the priority queue. Suppose for contradiction that there exists a shorter path for s⇝u with distance δ(s,u) < dist[u]."

---

### Step 4: Define Boundary Vertices x and y

This is the **most important conceptual step**.

#### Define x (last visited vertex on true path)
**x** = the furthest vertex along the true shortest s⇝u path that is **in S** (already visited)

Properties of x:
- x ∈ S (visited, removed from Q)
- x is on the true shortest path from s to u
- By inductive hypothesis: **dist[x] = δ(s,x)** (correct)

#### Define y (first unvisited vertex on true path)
**y** = the next vertex on the shortest path after x

Properties of y:
- y ∉ S (not yet visited, still in Q)
- Edge (x,y) exists on the true shortest path
- y is the "boundary" between visited and unvisited regions

**Visual representation:**
```
TRUE SHORTEST PATH s ⇝ u:

s → ... → x → y → ... → u
      ↑VISITED↑ ↑UNVISITED→↑
       (in S)    (not in S)

Edge (x,y) is the BOUNDARY
```

**Key phrase for exam:**
> "Let x be the furthest vertex along the true shortest s⇝u path that is in S. Let y be the next vertex on this shortest path after x. Since x ∈ S, by the inductive hypothesis, dist[x] = δ(s,x)."

---

### Step 5: Build the Key Inequality Chain

**Goal:** Show that δ(s,y) < dist[u]

#### Part A: Why δ(s,y) ≤ δ(s,u)

Since y is on the shortest path from s to u:
```
Path: s ⇝ y ⇝ u
      └─────┘ └──┘
      δ(s,y)  extra

Total: δ(s,u) = δ(s,y) + (y to u distance)

Since all weights ≥ 0:
δ(s,y) ≤ δ(s,u)
```

**This step requires non-negative weights!**

#### Part B: Combine with contradiction assumption

We assumed: δ(s,u) < dist[u]

Chain them together:
```
δ(s,y) ≤ δ(s,u) < dist[u]

Therefore: δ(s,y) < dist[u]
```

**Key phrase for exam:**
> "Since δ(s,u) < dist[u] and all edge weights are non-negative, it must be true that δ(s,y) ≤ δ(s,u) < dist[u]."

---

### Step 6: The Relaxation Argument

**Key insight:** When we visited x, we relaxed all edges leaving x, including (x,y).

#### What happened when x was removed from Q:
```python
# Dijkstra's algorithm when popping x:
for each neighbor v of x:
    if dist[x] + weight(x,v) < dist[v]:
        dist[v] = dist[x] + weight(x,v)
```

#### Applying this to edge (x,y):

Since (x,y) is on the shortest path:
```
After relaxation:
dist[y] = dist[x] + weight(x,y)
        = δ(s,x) + weight(x,y)    [dist[x] correct by IH]
        = δ(s,y)                  [x→y is on shortest path]
```

**Therefore: dist[y] = δ(s,y)**

#### Final inequality:
```
dist[y] = δ(s,y) < dist[u]

So: dist[y] < dist[u]
```

**Key phrase for exam:**
> "But y is adjacent to x on a shortest path, which means edge (x,y) was relaxed when x was removed from Q. This means dist[y] = δ(s,y) < dist[u]."

---

### Step 7: The Contradiction

We now have:
- Both u and y are in the priority queue Q
- dist[y] < dist[u]

**Case 1: If y ≠ u**

Dijkstra's uses a min-priority queue that always removes the vertex with **minimum distance estimate**.

If dist[y] < dist[u], then the algorithm would have removed **y** from Q, not **u**.

But we stated that **u** was just removed from Q.

**Contradiction!**

**Case 2: If y = u**

Then dist[y] < dist[u] becomes dist[u] < dist[u], which is impossible.

**Contradiction!**

**Key phrase for exam:**
> "If dist[y] < dist[u] and y ≠ u, then Dijkstra's algorithm would have popped y from the priority queue instead of u, a contradiction. Alternatively if y = u and dist[y] < dist[u], this is also a contradiction."

---

### Step 8: Conclusion

Since our assumption (that dist[u] is incorrect) leads to a contradiction, the assumption must be false.

Therefore: **dist[u] must be correct**

By induction on the set S, when Dijkstra's algorithm terminates (S = V), dist[v] is correct for all v ∈ V.

**Key phrase for exam:**
> "By contradiction, we conclude that dist[u] must be correct, and hence by induction on the set S, when Dijkstra's algorithm terminates, dist[v] is correct for all v ∈ V."

---

## Visual Understanding

### The Big Picture

```
GRAPH DURING EXECUTION:

┌─────────────────────┐         ┌─────────────────────┐
│   VISITED (S)       │         │   UNVISITED (Q)     │
│                     │         │                     │
│   s ──→ a ──→ x     │────────→│ y ──→ ... ──→ u    │
│                     │ (x,y)   │                     │
│   dist[x] correct   │  edge   │  dist[y] = δ(s,y)  │
│   (by IH)           │         │  dist[u] = ?        │
└─────────────────────┘         └─────────────────────┘

When we removed x, we relaxed (x,y), making dist[y] correct.

If dist[y] < dist[u], we'd visit y next, not u.
Since we visited u, dist[u] must be ≤ dist[y], and therefore correct.
```

### Concrete Example with Numbers

```
Graph:
    2        3        5
s ──→ a ──→ x ──→ y ──→ u
      |              ↗
      └────────12────┘

Dijkstra's current state:
- S = {s, a, x}  (visited)
- Just popped u from Q
- dist[u] = 12   (via direct edge s→a→u)
- dist[y] = 10   (via s→a→x→y)

TRUE shortest path to u: s→a→x→y→u (total: 15)

Apply proof:
1. Assume true shortest is 15 < 12? NO! Our assumption fails.
   Actually dist[u] = 12 IS correct (no shorter path exists).

Better example where proof applies:

Graph:
    2        3        5        1
s ──→ a ──→ x ──→ y ──→ z ──→ u
      |                        ↗
      └──────────20────────────┘

If Dijkstra somehow had dist[u] = 20 (wrong),
but true path is s→a→x→y→z→u = 11,

Then:
- x ∈ S (visited), dist[x] = 5 (correct)
- y is next on true path
- After relaxing (x,y): dist[y] = 5+5 = 10
- dist[y] = 10 < dist[u] = 20
- So y would be popped next, not u!
- Contradiction: u can't be popped if dist[y] < dist[u]
```

---

## Common Mistakes

### ❌ Mistake 1: Not clearly defining S
**Wrong:** "Use induction on vertices..."
**Right:** "Use induction on set S = V \ Q, the set of vertices removed from the priority queue."

### ❌ Mistake 2: Forgetting to state what we're proving
**Wrong:** "Assume dist[u] is wrong..."
**Right:** "We will show dist[u] = δ(s,u). Assume for contradiction that δ(s,u) < dist[u]..."

### ❌ Mistake 3: Not defining x and y clearly
**Wrong:** "Let x be a vertex on the path..."
**Right:** "Let x be the **furthest** vertex on the true shortest s⇝u path that is **in S**."

### ❌ Mistake 4: Missing the relaxation step
**Wrong:** "Since x is visited, dist[y] is correct..."
**Right:** "Since x ∈ S, when x was removed from Q, edge (x,y) was relaxed, so dist[y] = dist[x] + weight(x,y) = δ(s,y)."

### ❌ Mistake 5: Weak contradiction statement
**Wrong:** "This is a contradiction."
**Right:** "If dist[y] < dist[u], Dijkstra's would have removed y from the priority queue instead of u, contradicting the fact that u was just removed."

### ❌ Mistake 6: Not mentioning non-negative weights
**Wrong:** Just proving the inequality...
**Right:** "Since all edge weights are non-negative, δ(s,y) ≤ δ(s,u)."

### ❌ Mistake 7: Circular reasoning
**Wrong:** "Dijkstra is correct because it always picks the shortest path..."
**Right:** Use the formal induction structure to build the proof step-by-step.

---

## Memorization Checklist

### Core Structure (Must Know)
- [ ] Induction on set S = V \ Q
- [ ] Base case: dist[s] = 0
- [ ] IH: dist[v] correct for all v ∈ S
- [ ] Goal: Show dist[u] correct for next removed vertex u

### Contradiction Setup (Must Know)
- [ ] Assume δ(s,u) < dist[u] (shorter path exists)
- [ ] Define x = furthest visited vertex on true path
- [ ] Define y = next vertex after x on true path
- [ ] x ∈ S, y ∉ S, edge (x,y) on shortest path

### Key Inequality (Must Know)
- [ ] δ(s,y) ≤ δ(s,u) < dist[u]
- [ ] Why first inequality: y before u on path, non-negative weights
- [ ] Why second inequality: contradiction assumption

### Relaxation (Must Know)
- [ ] When x removed, edge (x,y) was relaxed
- [ ] dist[x] = δ(s,x) by IH
- [ ] After relaxation: dist[y] = δ(s,y)
- [ ] Therefore: dist[y] < dist[u]

### Contradiction (Must Know)
- [ ] Priority queue removes minimum distance
- [ ] If dist[y] < dist[u], would remove y not u
- [ ] But u was removed → contradiction
- [ ] Case y = u: dist[u] < dist[u] is impossible

### Non-Negative Weights (Must Know)
- [ ] Used in δ(s,y) ≤ δ(s,u) step
- [ ] Subpaths of shortest paths are shortest
- [ ] Without this, proof fails (negative edges could make later path cheaper)

---

## Practice Template

Use this template when practicing the proof:

```
THEOREM: Given graph G = (V,E) with non-negative weights and source s,
Dijkstra's algorithm correctly finds shortest paths to all vertices.

PROOF:

[1. STRUCTURE]
Use induction on S = V \ Q (vertices removed from priority queue).
Claim: For all v ∈ S, dist[v] = δ(s,v).

[2. BASE CASE]
First vertex removed is s with dist[s] = 0.
True distance δ(s,s) = 0 (no negative weights).
Therefore dist[s] correct. ✓

[3. INDUCTIVE HYPOTHESIS]
Assume: For all v ∈ S, dist[v] = δ(s,v) (correct).

[4. INDUCTIVE STEP]
Let u = next vertex removed from Q.
Show: dist[u] = δ(s,u).

[5. CONTRADICTION ASSUMPTION]
Suppose for contradiction: ∃ shorter path with δ(s,u) < dist[u].

[6. DEFINE BOUNDARY]
Let x = furthest vertex on true shortest s⇝u path with x ∈ S.
Let y = next vertex after x on this path.
Properties: x ∈ S (so dist[x] = δ(s,x) by IH), y ∉ S, edge (x,y) exists.

[7. INEQUALITY CHAIN]
Since y is before u on shortest path and weights ≥ 0:
  δ(s,y) ≤ δ(s,u) < dist[u]

[8. RELAXATION]
When x was removed from Q, edge (x,y) was relaxed.
  dist[y] = dist[x] + weight(x,y)
          = δ(s,x) + weight(x,y)    [by IH]
          = δ(s,y)                  [x→y on shortest path]

Therefore: dist[y] = δ(s,y) < dist[u]

[9. CONTRADICTION]
If dist[y] < dist[u] and y ≠ u:
  Priority queue would remove y (smaller) instead of u.
  But u was just removed. Contradiction!

If y = u:
  Then dist[u] < dist[u], which is impossible. Contradiction!

[10. CONCLUSION]
By contradiction, dist[u] must be correct.
By induction on S, when algorithm terminates (S = V),
dist[v] is correct for all v ∈ V. □

[11. ROLE OF NON-NEGATIVE WEIGHTS]
Crucial for δ(s,y) ≤ δ(s,u) step.
Without this, negative edges could make δ(s,u) < δ(s,y)
even when y precedes u, breaking the proof.
```

---

## Exam Strategy

### Time Management (7 minutes total)
- **1 min:** Write structure outline
- **1 min:** Base case
- **2 min:** Define x, y and build inequality
- **2 min:** Relaxation and contradiction
- **1 min:** Conclusion and non-negative weights note

### What Examiners Look For
1. **Clear structure** (induction framework)
2. **Precise definitions** (x and y)
3. **Logical flow** (inequality chain)
4. **Correct reasoning** (relaxation → dist[y] exact)
5. **Clear contradiction** (PQ would choose differently)
6. **Mention non-negative weights** (where it's used)

### Quick Checks Before Submitting
- [ ] Did I state what S represents?
- [ ] Did I prove base case?
- [ ] Did I define x and y clearly?
- [ ] Did I explain the relaxation step?
- [ ] Did I state the contradiction explicitly?
- [ ] Did I mention non-negative weights?

---

## Additional Notes

### Why This Proof Is Hard
- Requires understanding both induction AND contradiction
- The x, y construction is non-obvious
- Need to track what's true at what point in the algorithm
- Easy to handwave the relaxation step

### Why This Proof Is Important
- Tests understanding of greedy algorithms
- Shows how to prove algorithmic correctness formally
- Demonstrates limitations (non-negative weights required)
- Reinforces understanding of Dijkstra's mechanics

### Connection to Other Topics
- **Bellman-Ford:** Similar induction structure, but works with negative weights
- **Prim's MST:** Similar greedy correctness argument
- **Loop Invariants:** Related concept for iterative algorithms

---

**Last Updated:** Exam Preparation Period
**Difficulty Rating:** ⭐⭐⭐⭐ (4/5)
**Must Know For:** Mid-semester and Final exams
**Practice Recommended:** 3-5 full write-throughs until fluent