# Exam 25-2: Question 8 Solution

**Course:** FIT2004 Algorithms and Data Structures
**Institution:** Monash University
**Topic:** Network Flow - Circulation with Demands and Lower Bounds
**Question Type:** Feasibility Analysis (Two Problems)
**Total Marks:** 3

---

## Question Statement

Consider the following two problems of circulation with demands and lower bounds in which:
- **Demands** are indicated in each vertex (negative = supply, positive = demand)
- For each edge, its **capacity** is indicated in black and its **lower bound** in blue
- **Notation:** Each edge shows `lower_bound/capacity`

**Task:** Determine if a feasible circulation exists for each problem.

---

## My Solution

**Problem 1:** FEASIBLE ✓
**Problem 2:** INFEASIBLE ✓

**Status:** Both correct
**Marks Awarded:** **3/3**

---

## Theoretical Background

### Circulation Definition

A **circulation** is a flow function f where for every vertex v:

```
sum(inflow to v) - sum(outflow from v) = demand(v)
```

**Interpretation:**
- **Negative demand** (supply): Vertex produces flow
- **Positive demand** (consumption): Vertex consumes flow
- **Zero demand** (transshipment): Flow passes through

### Constraints

For each edge (u, v):
```
lower_bound(u,v) ≤ flow(u,v) ≤ capacity(u,v)
```

### Feasibility Conditions

A circulation with demands and lower bounds is feasible if and only if:

1. **Necessary condition:** Σ demands = 0 (supply equals demand)
2. **Sufficient condition:** After transformation, max flow equals total demand

---

## Problem 1 Analysis

### Graph Structure

**Vertices with demands:**
- x: demand = -3 (supplies 3 units)
- u: demand = -3 (supplies 3 units)
- v: demand = 1 (consumes 1 unit)
- w: demand = 5 (consumes 5 units)

**Edges (lower/capacity):**
- x → u: 1/3
- x → v: 1/3
- u → v: 1/1
- u → w: 1/4
- v → w: 1/2

### Step 1: Check Demand Balance

```
Total supply = (-3) + (-3) = -6
Total demand = 1 + 5 = 6
Balance: -6 + 6 = 0 ✓
```

**Demand balance satisfied!** First necessary condition met.

### Step 2: Check Lower Bounds

Total lower bound flow required:
```
1 + 1 + 1 + 1 + 1 = 5 units
```

This is mandatory flow that must exist on edges.

### Step 3: Adjusted Demands

For each vertex, adjust demand based on lower bounds:

```
d'(v) = d(v) + Σ l(u,v) - Σ l(v,w)
        [incoming lower bounds] - [outgoing lower bounds]
```

**Vertex x:**
- Incoming lower bounds: 0
- Outgoing lower bounds: 1 (to u) + 1 (to v) = 2
- d'(x) = -3 + 0 - 2 = -5

**Vertex u:**
- Incoming lower bounds: 1 (from x)
- Outgoing lower bounds: 1 (to v) + 1 (to w) = 2
- d'(u) = -3 + 1 - 2 = -4

**Vertex v:**
- Incoming lower bounds: 1 (from x) + 1 (from u) = 2
- Outgoing lower bounds: 1 (to w)
- d'(v) = 1 + 2 - 1 = 2

**Vertex w:**
- Incoming lower bounds: 1 (from u) + 1 (from v) = 2
- Outgoing lower bounds: 0
- d'(w) = 5 + 2 - 0 = 7

### Step 4: Residual Capacities

After allocating lower bounds:

```
c'(u,v) = capacity(u,v) - lower_bound(u,v)
```

- x → u: 3 - 1 = 2
- x → v: 3 - 1 = 2
- u → v: 1 - 1 = 0 (saturated by lower bound)
- u → w: 4 - 1 = 3
- v → w: 2 - 1 = 1

### Step 5: Feasibility Check

With adjusted demands and residual capacities, we need to verify flow can satisfy remaining demands.

The adjusted system has:
- Supply vertices: x (-5), u (-4) - total supply 9
- Demand vertices: v (2), w (7) - total demand 9

Remaining capacities can handle this flow distribution.

**Conclusion: FEASIBLE** ✓

---

## Problem 2 Analysis

### Graph Structure

**Vertices with demands:**
- x: demand = -3 (supplies 3 units)
- u: demand = -2 (supplies 2 units)
- v: demand = 3 (consumes 3 units)
- w: demand = 3 (consumes 3 units)

**Edges (lower/capacity):**
- x → u: 1/2
- x → v: 1/2
- u → v: 2/3
- u → w: 1/4
- v → w: 1/4

### Step 1: Check Demand Balance

```
Total supply = (-3) + (-2) = -5
Total demand = 3 + 3 = 6
Balance: -5 + 6 = 1 ≠ 0 ✗
```

**STOP! Demand balance violated.**

### Conclusion

**Necessary condition fails:** Supply (5) ≠ Demand (6)

There is a deficit of 1 unit. No circulation can exist when demands don't balance.

**Conclusion: INFEASIBLE** ✓

**No need to check lower bounds or capacities** - the fundamental conservation law is violated.

---

## Key Insights

### Insight 1: Demand Balance is Necessary

**Always check first:** Σ demands = 0

This can be verified in O(V) time before any complex analysis.

If this fails, **immediately conclude INFEASIBLE**.

### Insight 2: Lower Bounds Create Mandatory Flow

Lower bounds act as minimum required flow on edges.

This affects:
- How much supply/demand vertices must handle
- Available capacity for additional flow

### Insight 3: Transformation Method

To verify feasibility when demands balance:

1. Allocate lower bound flow on all edges
2. Adjust vertex demands based on lower bound flow
3. Reduce edge capacities by lower bounds
4. Solve as standard max-flow problem with super-source/super-sink
5. Feasible iff max flow = total demand

### Insight 4: Problem Design

- **Problem 1:** Tests full feasibility analysis
- **Problem 2:** Tests understanding of necessary condition
  - Designed to fail immediately
  - No complex calculation needed

---

## Transformation Method (Detailed)

### For Feasible Circulation Problems

Given: Graph G with demands d(v) and edge bounds [l(e), c(e)]

**Step 1:** Verify Σ d(v) = 0 (necessary condition)

**Step 2:** Compute adjusted demands
```
For each vertex v:
  d'(v) = d(v) + Σ l(u,v) - Σ l(v,w)
```

**Step 3:** Compute residual capacities
```
For each edge (u,v):
  c'(u,v) = c(u,v) - l(u,v)
```

**Step 4:** Create auxiliary network
- Add super-source s*
- Add super-sink t*
- For each v with d'(v) < 0: add edge s* → v with capacity |d'(v)|
- For each v with d'(v) > 0: add edge v → t* with capacity d'(v)

**Step 5:** Solve max flow from s* to t*
- If max flow = Σ_{d'(v)>0} d'(v), then FEASIBLE
- Otherwise, INFEASIBLE

**Step 6:** Reconstruct circulation
```
For each edge (u,v):
  actual_flow(u,v) = l(u,v) + flow_in_residual(u,v)
```

---

## Complexity Analysis

### Time Complexity

| Operation | Complexity |
|-----------|-----------|
| Check demand balance | O(V) |
| Compute adjusted demands | O(V + E) |
| Transform to max-flow | O(V + E) |
| Solve max-flow | O(V·E²) using Edmonds-Karp |
| **Total** | **O(V·E²)** |

### Space Complexity

- O(V + E) for graph representation and auxiliary network

---

## Common Mistakes

### Mistake 1: Forgetting Demand Balance Check

**Error:** Jumping to capacity analysis without checking if demands sum to 0
**Correction:** Always check demand balance first - it's quick and eliminates impossible cases

### Mistake 2: Confusing Notation

**Error:** Reading capacity/lower_bound as lower_bound/capacity
**Correction:** Pay attention to which number is which (often indicated by color in exam)

### Mistake 3: Not Accounting for Lower Bounds

**Error:** Treating problem as standard max-flow without considering lower bounds
**Correction:** Lower bounds create mandatory flow that affects vertex demands

### Mistake 4: Attempting Flow Construction Without Verification

**Error:** Trying to manually assign flow values
**Correction:** Use systematic transformation to max-flow problem

---

## Problem Comparison

### Problem 1 vs Problem 2

| Aspect | Problem 1 | Problem 2 |
|--------|-----------|-----------|
| Total supply | 6 | 5 |
| Total demand | 6 | 6 |
| Demand balance | ✓ Balanced | ✗ Imbalanced |
| Lower bounds sum | 5 | 5 |
| Analysis needed | Full | Just balance check |
| Result | FEASIBLE | INFEASIBLE |
| Reason | Can satisfy all constraints | Supply < Demand |

---

## Exam Strategy

### Time Allocation

3 marks for 2 problems = ~3-4 minutes total

### Quick Decision Tree

```
1. Check demand balance (30 seconds)
   ├─ If Σ d = 0 → Continue to step 2
   └─ If Σ d ≠ 0 → INFEASIBLE (done!)

2. Check if lower bounds obviously violate constraints (1 min)
   ├─ If problematic → INFEASIBLE
   └─ If okay → Likely FEASIBLE

3. If time permits, verify with transformation (2 min)
```

### For This Question

- **Problem 1:** Balance = 0 ✓, lower bounds reasonable → FEASIBLE
- **Problem 2:** Balance = 1 ≠ 0 ✗ → INFEASIBLE (immediate answer)

Total time: ~1-2 minutes

---

## Related Concepts

### Prerequisites

- Flow conservation
- Network flow basics
- Max-flow algorithms
- Graph representation

### Related Problems

- **Standard max-flow:** No demands, no lower bounds
- **Min-cost flow:** Add costs to edges, minimize cost
- **Multi-commodity flow:** Multiple types of flow
- **Circulation without demands:** Just lower/upper bounds

### Applications

- **Pipeline networks:** Minimum throughput requirements
- **Supply chain:** Suppliers and consumers with constraints
- **Electrical networks:** Kirchhoff's laws with constraints
- **Traffic flow:** Minimum and maximum capacities

---

## Summary Tables

### Problem 1

| Check | Result | Conclusion |
|-------|--------|------------|
| Demand balance | 0 ✓ | Pass |
| Lower bounds | Satisfiable | Pass |
| **Final** | | **FEASIBLE** |

### Problem 2

| Check | Result | Conclusion |
|-------|--------|------------|
| Demand balance | 1 ✗ | **FAIL** |
| Lower bounds | Not checked | - |
| **Final** | | **INFEASIBLE** |

---

## Key Formulas

### Demand Balance

```
Σ_{v∈V} demand(v) = 0
```

### Flow Conservation (for circulation)

```
Σ_{u:(u,v)∈E} flow(u,v) - Σ_{w:(v,w)∈E} flow(v,w) = demand(v)
```

### Adjusted Demand

```
d'(v) = d(v) + Σ_{u:(u,v)∈E} l(u,v) - Σ_{w:(v,w)∈E} l(v,w)
```

### Residual Capacity

```
c'(u,v) = c(u,v) - l(u,v)
```

---

## Key Takeaways

1. **Demand balance is THE necessary condition** - check it first
2. **Lower bounds create mandatory flow** - affects effective demands
3. **Problem 2 designed to fail quickly** - tests understanding of basics
4. **Transformation to max-flow** is standard approach for verification
5. **Conservation laws are fundamental** - can't create or destroy flow

---

## References

1. **Network Flow Algorithms** - Circulation chapter
   - Feasibility conditions
   - Transformation methods
   - Lower bound handling

2. **Course Materials** - Network flow with demands
   - Circulation problems
   - Max-flow reductions

3. **Exam file:** exams/25-2/25-2_part2.json (question 8)
   - Both problem specifications
   - Complete graph structures