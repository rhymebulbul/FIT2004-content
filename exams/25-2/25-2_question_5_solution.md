# Exam 25-2: Question 5 Solution

**Course:** FIT2004 Algorithms and Data Structures
**Institution:** Monash University
**Topic:** Greedy Algorithms - Correctness Conditions
**Question Type:** Multiple Select
**Total Marks:** 3

---

## Question Statement

Select all true statements regarding the correctness of greedy graph algorithms.

### Answer Choices

**a)** Dijkstra's algorithm works correctly for directed graphs with negative cycle(s).

**b)** Both Prim's and Kruskal's algorithm work correctly for undirected graphs with negative weights but no negative cycle.

**c)** Dijkstra's algorithm works correctly for directed graphs with negative weights but no negative cycle.

**d)** Both Prim's and Kruskal's algorithm work correctly for undirected graphs with negative cycle(s).

---

## My Solution

**Selected Answers: b only**

**Status:** † **PARTIAL**
**Marks Awarded:** **1.5/3**

**Correct Answers:** b and d
**Missed:** Did not select option d

---

## Detailed Analysis of Each Option

### Option a: Dijkstra + Negative Cycles  FALSE

**Claim:** Dijkstra's algorithm works correctly for directed graphs with negative cycle(s).

**Algorithm:** Dijkstra's algorithm
**Graph type:** Directed
**Edge weights:** General (allowing negative)
**Special condition:** Negative cycles present
**Correctness claim:** FALSE

**Why This is FALSE:**

Dijkstra's algorithm **requires non-negative edge weights** for correctness. With negative cycles, the algorithm fails for two fundamental reasons:

1. **Negative cycles make shortest paths undefined**
   - Can traverse the negative cycle repeatedly
   - Distance can decrease indefinitely
   - No "shortest" path exists (can achieve - distance)

2. **Greedy choice becomes invalid**
   - Dijkstra assumes once a vertex is finalized, its distance is optimal
   - With negative cycles, this assumption breaks
   - A path through a later-discovered negative cycle might be shorter

**Example of Failure:**
```
Graph: A í B (weight 5)
       B í C (weight 3)
       C í A (weight -10)  [creates negative cycle: AíBíCíA = -2]

From A to C:
- First time: A í B í C (cost 8)
- Go through cycle once: A í B í C í A í B í C (cost 6)
- Go through cycle twice: A í ... í C (cost 4)
- Can continue indefinitely, making distance -
```

**Correct Algorithm for Negative Cycles:**
- **Bellman-Ford** can detect negative cycles
- Returns "no solution" if negative cycle exists
- Or identifies which vertices are affected

**Verdict:** L **FALSE**

---

### Option b: Prim/Kruskal + Negative Weights (no cycles)  TRUE

**Claim:** Both Prim's and Kruskal's algorithm work correctly for undirected graphs with negative weights but no negative cycle.

**Algorithms:** Prim's and Kruskal's (MST algorithms)
**Graph type:** Undirected
**Edge weights:** Negative allowed
**Special condition:** No negative cycles
**Correctness claim:** TRUE

**Why This is TRUE:**

MST algorithms work correctly with negative edge weights because:

1. **MST algorithms only compare edge weights**
   - Don't care about absolute values, only relative ordering
   - Negative weights don't break comparison operations
   - Still select minimum weight edges

2. **The cut property still holds**
   - For any cut of the graph, the minimum weight edge crossing the cut is in some MST
   - This property doesn't depend on weights being positive

3. **Negative cycles are irrelevant**
   - MSTs are acyclic by definition (they're trees)
   - Any cycle in the original graph won't appear in the MST
   - The "no negative cycle" condition is actually unnecessary for MST correctness

**Example:**
```
Graph with negative edge:
    A
   /|\
  1 | -5
 /  |  \
B---C---D
    3

MST would include:
- A-D (weight -5)  ê negative edge is fine!
- A-B (weight 1)
- C-D (weight 3) or B-C depending on structure
Total weight: negative, but MST is correct
```

**Why Prim and Kruskal both work:**

**Prim's Algorithm:**
- Grows single tree by adding minimum weight edge connecting tree to non-tree vertex
- Comparison: `if edge.weight < current_min` works with negative weights
- Correctness proof via cut property doesn't require positive weights

**Kruskal's Algorithm:**
- Sorts all edges by weight (works with negative weights)
- Adds minimum weight edge that doesn't create cycle
- Union-find detects cycles independently of edge weights
- Correctness proof doesn't require positive weights

**Verdict:**  **TRUE**

**Note:** I correctly selected this option.

---

### Option c: Dijkstra + Negative Weights (no cycles)  FALSE

**Claim:** Dijkstra's algorithm works correctly for directed graphs with negative weights but no negative cycle.

**Algorithm:** Dijkstra's algorithm
**Graph type:** Directed
**Edge weights:** Negative allowed
**Special condition:** No negative cycles
**Correctness claim:** FALSE

**Why This is FALSE:**

Even without negative cycles, **Dijkstra fails with any negative edge weights**. The greedy choice assumption breaks down.

**Dijkstra's Greedy Choice:**
- Once a vertex is finalized (extracted from priority queue), its shortest distance is known
- Never reconsider finalized vertices
- This works ONLY with non-negative weights

**Counterexample (no negative cycle, but Dijkstra fails):**
```
Graph:
    A --2--> B
    |        |
    1        -4  (negative edge)
    ì        ì
    C --------> D

Finding shortest path from A to D:

Dijkstra's execution:
1. Start: A (dist=0)
2. Finalize A, relax neighbors:
   - B: dist=2
   - C: dist=1
3. Finalize C (smaller dist), relax:
   - D: dist=1 (from AíC, assuming direct edge)
4. Finalize B (dist=2), relax:
   - D: check 2+(-4)=-2 < 1 ê But D already finalized!

Dijkstra's answer: dist(A,D) = 1
Correct answer: dist(A,D) = -2 (via AíBíD)

Dijkstra gives WRONG answer!
```

**Why It Fails:**
- Dijkstra finalized D with distance 1
- Later discovered that path AíBíD has distance -2
- But Dijkstra never revisits finalized vertices
- The greedy choice was wrong

**Correct Algorithm for Negative Weights (no cycles):**
- **Bellman-Ford** algorithm
- Time complexity: O(VE) vs Dijkstra's O((V+E) log V)
- Can handle negative weights (but not negative cycles)

**Verdict:** L **FALSE**

---

### Option d: Prim/Kruskal + Negative Cycles  TRUE

**Claim:** Both Prim's and Kruskal's algorithm work correctly for undirected graphs with negative cycle(s).

**Algorithms:** Prim's and Kruskal's (MST algorithms)
**Graph type:** Undirected
**Edge weights:** General (allowing negative)
**Special condition:** Negative cycles present
**Correctness claim:** TRUE

**Why This is TRUE:**

This is the key insight I missed! MST algorithms work correctly **even with negative cycles** in the original graph.

**Fundamental Reason:**
- **MSTs are trees** - inherently acyclic
- Any cycle in the original graph **cannot be included** in the spanning tree
- The presence of negative cycles in the graph is **irrelevant** to MST construction
- The algorithm correctly identifies and avoids creating cycles while finding minimum weight

**How the Algorithms Handle Negative Cycles:**

**Kruskal's Algorithm:**
```
1. Sort all edges by weight
2. For each edge in sorted order:
   - If adding edge doesn't create cycle: add it to MST
   - Else: skip it

The cycle detection (via Union-Find) prevents ANY cycle, including negative ones!
```

**Prim's Algorithm:**
```
1. Start with arbitrary vertex
2. Repeatedly add minimum weight edge that connects tree to non-tree vertex
3. Stop when all vertices included

By construction, never creates cycles (always grows single tree)
```

**Example:**
```
Graph with negative cycle:
    A
   / \
  1   -2
 /     \
B-------C
    -3

Negative cycle: A-C-B-A has weight: (-2)+(-3)+1 = -4 < 0

MST would include only 2 edges (since 3 vertices need 2 edges):
- A-C (weight -2)
- B-C (weight -3)
Total MST weight: -5

The cycle is NOT in the MST! The algorithm correctly excludes edge A-B.
```

**Why I Missed This:**

I likely confused **shortest path problems** (where negative cycles are problematic) with **MST problems** (where cycles of any kind are excluded by definition).

**Key Distinction:**

| Problem Type | Negative Cycles Impact |
|--------------|----------------------|
| **Shortest Path** | Fundamental problem - paths can use cycles, making distances undefined |
| **MST** | No impact - trees can't contain cycles, so graph cycles are irrelevant |

**Verdict:**  **TRUE**

**My Error:** Did NOT select this option, losing 1.5 marks.

---

## Conceptual Distinctions

### Shortest Path vs MST

#### Shortest Path Problems

**Problem:** Find minimum total weight path between vertices

**Path Characteristics:**
- Can traverse edges multiple times in different paths
- Can revisit vertices
- Can use cycles if beneficial

**Negative Weight Impact:**
- **Negative edges:** Break Dijkstra's greedy assumption
- **Negative cycles:** Make problem ill-defined (can achieve - distance)

**Algorithms:**
- Dijkstra (non-negative weights only)
- Bellman-Ford (allows negative weights, detects negative cycles)
- Floyd-Warshall (all-pairs, detects negative cycles)

#### Minimum Spanning Tree Problems

**Problem:** Find minimum total weight acyclic connected subgraph

**Tree Characteristics:**
- Exactly |V|-1 edges for |V| vertices
- Connected and acyclic
- No cycles by definition

**Negative Weight Impact:**
- **Negative edges:** No problem - just affects total weight value
- **Negative cycles:** Irrelevant - cycles excluded by tree structure

**Algorithms:**
- Prim (vertex-based greedy growth)
- Kruskal (edge-based greedy selection)
- Both work with any edge weights

---

## Algorithm Correctness Requirements

### Dijkstra's Algorithm

**Correctness Conditions:**
-  Graph can be directed or undirected
-  Can have cycles (but not negative cycles)
- L **MUST have non-negative edge weights** (strict requirement)

**Greedy Choice:**
- Always process minimum distance vertex
- Once finalized, distance is optimal
- **This requires non-negative weights to be valid**

**Failure Modes:**
- Negative edges í Breaks greedy choice optimality
- Negative cycles í Shortest paths undefined

**When to Use:**
- Single-source shortest paths
- Non-negative edge weights
- O((V+E) log V) with binary heap

**Alternative for Negative Weights:**
- Bellman-Ford: O(VE), handles negative weights, detects cycles

---

### Prim's Algorithm (MST)

**Correctness Conditions:**
-  Graph should be connected (or find MST for each component)
-  Can have any edge weights (positive, negative, zero)
-  Cycles in graph don't affect correctness

**Greedy Choice:**
- Add minimum weight safe edge
- Cut property ensures correctness
- **Works with any comparable weights**

**Key Insight:**
- MST builds acyclic structure
- Original graph cycles are irrelevant

**Complexity:**
- O((V+E) log V) with binary heap
- O(E + V log V) with Fibonacci heap

---

### Kruskal's Algorithm (MST)

**Correctness Conditions:**
-  Can handle disconnected graphs (produces MST forest)
-  Can have any edge weights
-  Cycles in graph don't affect correctness

**Greedy Choice:**
- Sort edges by weight
- Add minimum weight edge that doesn't create cycle
- **Comparison and cycle detection independent of weight sign**

**Key Insight:**
- Union-find prevents all cycles
- Sorting works with negative weights

**Complexity:**
- O(E log E) or O(E log V) (since log E = O(log V≤) = O(2 log V) = O(log V))
- Dominated by sorting edges

---

## Common Mistakes

### Mistake 1: Confusing shortest path and MST requirements

**Error:** Thinking negative weights break all graph algorithms
**Correction:**
- Negative weights break **Dijkstra** (shortest path)
- Negative weights are fine for **Prim/Kruskal** (MST)

### Mistake 2: Assuming negative cycles affect MST correctness

**Error:** Thinking negative cycles make MST undefined
**Correction:**
- Negative cycles are problematic for **shortest paths**
- Negative cycles are **irrelevant** for MST (trees can't contain cycles)
- **This was my mistake on this question!**

### Mistake 3: Thinking "no negative cycles" helps Dijkstra

**Error:** Believing Dijkstra works if there are no negative cycles
**Correction:**
- Dijkstra requires **no negative edges at all**
- Even one negative edge (without cycles) breaks Dijkstra
- See counterexample in Option c analysis

### Mistake 4: Forgetting spanning trees are acyclic

**Error:** Not recognizing that MST definition excludes all cycles
**Correction:**
- Spanning tree has exactly |V|-1 edges
- By definition acyclic and connected
- Any cycle in original graph is irrelevant

---

## Algorithm Comparison Table

### Requirements Summary

| Algorithm | Neg. Edges OK? | Neg. Cycles OK? | Graph Type | Problem |
|-----------|---------------|-----------------|------------|---------|
| **Dijkstra** | L NO | L NO | Dir/Undir | Shortest Path |
| **Bellman-Ford** |  YES | Detects | Dir/Undir | Shortest Path |
| **Prim** |  YES |  YES | Undirected | MST |
| **Kruskal** |  YES |  YES | Undirected | MST |

### Complexity Comparison

| Algorithm | Time Complexity | Space | Use Case |
|-----------|-----------------|-------|----------|
| Dijkstra | O((V+E) log V) | O(V) | Non-neg weights, single source |
| Bellman-Ford | O(VE) | O(V) | Neg weights, detect cycles |
| Prim | O((V+E) log V) | O(V) | MST, dense graphs |
| Kruskal | O(E log E) | O(V) | MST, sparse graphs |

---

## Graph Properties

### Negative Edges

**Definition:** Edges with weight < 0

**Impact on Dijkstra:** L Breaks correctness
- Algorithm may return incorrect shortest paths
- Greedy assumption violated

**Impact on MST:**  No impact
- Algorithms only compare weights
- Sign doesn't matter for comparisons

**Example Use Cases:**
- Modeling costs vs. profits
- Representing bidirectional preferences
- Optimization problems with penalties

---

### Negative Cycles

**Definition:** Cycle where sum of edge weights < 0

**Impact on Shortest Path:** L Makes problem ill-defined
- Can traverse cycle repeatedly
- Distance can decrease to -
- No finite shortest path

**Impact on MST:**  No impact
- Cycles not included in spanning trees
- MST is acyclic by definition

**Detection:**
- Bellman-Ford can detect in O(VE) time
- Run V-1 iterations, then check if any edge can still improve distances
- If yes, negative cycle exists

---

## Marking Scheme

**Total Marks Available:** 3
**Marks Awarded:** **1.5/3**

**Correct Answers:** b, d
**Student Selected:** b only

**Grading Breakdown:**
- Selected (b):  Correct (+1.5)
- Missed (d):  Should have selected (+0, lost 1.5)
- Correctly rejected (a):  Correct
- Correctly rejected (c):  Correct

**Feedback:** Partial credit. Correctly identified that MST algorithms work with negative weights (no cycles), but missed that they also work with negative cycles present.

---

## Key Insights from Course Materials

### From implementations-algorithms/w5/

**dijkstra.py:**
- Assumes non-negative weights in comments
- Uses priority queue for greedy choice
- Once vertex finalized, never revisited

**prim.py:**
- Only compares edge weights
- Doesn't check for weight signs
- Grows single tree, inherently acyclic

**kruskal.py:**
- Sorts edges (works with any comparable values)
- Union-find prevents cycles
- No assumption about weight signs

---

## Exam Strategy

### Quick Recognition Checklist

**For Shortest Path Algorithms:**
1. Dijkstra REQUIRES non-negative weights
2. Any negative edge í use Bellman-Ford instead
3. Negative cycle í shortest path undefined

**For MST Algorithms:**
1. Prim and Kruskal don't care about weight signs
2. Both work with negative weights
3. **Both work even with negative cycles** (key insight!)
4. Trees are acyclic, so graph cycles are irrelevant

### Key Discriminators

 Separate shortest path algorithms from MST algorithms
 Remember: Dijkstra requires non-negative weights (strict)
 Remember: MST algorithms don't care about edge weight signs
 **Trees are acyclic, so cycles in graph don't affect MST construction**

### Time Management

- 3 marks, should take ~2-3 minutes
- Multiple correct answers possible
- Requires conceptual understanding vs memorization

---

## Summary Table

| Option | Statement | My Answer | Correct | Key Concept |
|--------|-----------|-----------|---------|-------------|
| **a** | Dijkstra + neg cycles |  Rejected |  FALSE | Dijkstra needs non-neg weights |
| **b** | Prim/Kruskal + neg weights (no cycles) |  Selected |  TRUE | MST algorithms weight-sign independent |
| **c** | Dijkstra + neg weights (no cycles) |  Rejected |  FALSE | Even one neg edge breaks Dijkstra |
| **d** | Prim/Kruskal + neg cycles |  Missed |  TRUE | **MSTs are acyclic, graph cycles irrelevant** |

**Final Score:** 1.5/3

---

## References

1. **implementations-algorithms/w5/**
   - `dijkstra.py` - Single-source shortest path implementation
   - `prim.py` - MST algorithm (vertex-based)
   - `kruskal.py` - MST algorithm (edge-based)
   - `unionFind.py` - Cycle detection for Kruskal

2. **topics/GRAPH_COMPLEXITY_EXAM_CHEATSHEET.md**
   - Algorithm correctness conditions
   - Complexity comparisons

3. **course_notes/** (Graph chapters)
   - Shortest path algorithms
   - MST algorithms
   - Negative weight handling

4. **Exam file:** exams/25-2/25-2_part1.json (question 5)
   - Original problem with all options analyzed
