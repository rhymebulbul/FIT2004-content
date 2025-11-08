# DAG and Topological Sort - Complete Exam Guide

## Table of Contents
1. [Core Definitions](#core-definitions)
2. [Topological Sort Algorithms](#topological-sort-algorithms)
3. [Key Properties and Theorems](#key-properties-and-theorems)
4. [Common Exam Question Types](#common-exam-question-types)
5. [Implementation Details](#implementation-details)
6. [Tricky Concepts and Edge Cases](#tricky-concepts-and-edge-cases)
7. [Problem-Solving Patterns](#problem-solving-patterns)

---

## Core Definitions

### Directed Acyclic Graph (DAG)
**Definition:** A directed graph that contains no cycles.

**Properties:**
- Must be both directed AND acyclic
- If there's a cycle, it's NOT a DAG
- Edges have direction (u→v) where u ≠ v typically

**Real-World Applications:**
- Course prerequisites (subject A must complete before subject B)
- Project task dependencies (task X must finish before task Y)
- Build systems (compile file A before linking B)
- Genealogy with "is ancestor of" relationships
- Power sets with "is subset of" relationships

**How to Identify a DAG:**
1. Check if graph is directed (edges have direction)
2. Check if graph is acyclic (no paths that loop back)
3. Both conditions must hold

---

## Topological Sort Algorithms

### What is Topological Ordering?

**Definition:** A permutation (ordering) of vertices such that for every directed edge (u→v), vertex u appears before vertex v in the ordering.

**Interpretation:** A valid order to complete tasks satisfying all prerequisites.

**Key Facts:**
- Only applicable to DAGs (if graph has cycle, no topological ordering exists)
- DAG can have **multiple** valid topological orderings
- Not unique unless there's a unique path structure

### Algorithm 1: Kahn's Algorithm (Queue-Based)

**Core Idea:** Process vertices with no incoming edges (no prerequisites) first.

**Algorithm Steps:**
```
1. Initialize queue with all vertices having in-degree = 0
2. While queue is not empty:
   a. Remove vertex u from queue
   b. Add u to topological ordering
   c. For each outgoing edge u→v:
      - Decrement in-degree[v] by 1
      - If in-degree[v] becomes 0, add v to queue
3. If ordering contains all vertices, return it
   Otherwise, graph has a cycle (not a DAG)
```

**Implementation Details:**
- Don't actually delete edges; maintain an in-degree array and decrement it
- In-degree[v] = number of incoming edges to v
- Time Complexity: **O(V + E)**
- Space Complexity: **O(V)** for in-degree array and queue

**Example Trace:**
```
Graph: A→B→E, C→D→E, F→E

Initial in-degrees: A=0, B=1, C=0, D=1, E=3, F=0
Queue: [A, C, F]

Step 1: Remove A, add to order
  - Decrement in-degree[B]: 1→0
  - Queue: [C, F, B]
  - Order: [A]

Step 2: Remove C, add to order
  - Decrement in-degree[D]: 1→0
  - Queue: [F, B, D]
  - Order: [A, C]

Step 3: Remove F, add to order
  - Decrement in-degree[E]: 3→2
  - Queue: [B, D]
  - Order: [A, C, F]

... continue until all vertices processed
```

### Algorithm 2: DFS-Based Topological Sort

**Core Idea:** Add each vertex to the ordering AFTER visiting all its descendants (post-order).

**Algorithm Steps:**
```
1. Initialize: visited array (all False), order array (empty)
2. For each vertex u in graph:
   a. If u not visited, call DFS(u)
3. Return REVERSED order array

DFS(u):
1. Mark u as visited
2. For each neighbor v of u:
   a. If v not visited, call DFS(v)
3. Add u to order array  # Post-order: after all descendants
```

**Why Reverse?**
- DFS adds vertices in **reverse topological order**
- Vertices are added AFTER their descendants
- So descendants appear later in the array
- Reversing gives correct topological order

**Time Complexity:** **O(V + E)** (same as DFS)
**Space Complexity:** **O(V)** for recursion stack and visited array

**Key Advantage:** No need to compute in-degrees; works directly with DFS framework

**Example Trace:**
```
Graph: A→B, A→C, B→D, C→D

DFS from A:
  DFS from B:
    DFS from D:
      Add D to order → order = [D]
    Add B to order → order = [D, B]
  DFS from C:
    D already visited
    Add C to order → order = [D, B, C]
  Add A to order → order = [D, B, C, A]

Reversed order: [A, C, B, D] ✓ (valid topological order)
```

---

## Key Properties and Theorems

### 1. Existence of Topological Ordering
**Theorem:** A directed graph has a topological ordering if and only if it is a DAG.

**Proof (⇐):**
- If graph has cycle u₁→u₂→...→uₖ→u₁
- Then u₁ must come before u₂, u₂ before u₃, ..., uₖ before u₁
- This means u₁ must come before itself → impossible
- Therefore, cycle implies no topological ordering exists

**Proof (⇒):**
- If graph is DAG, both Kahn's and DFS algorithms produce valid ordering
- Existence proven by construction

### 2. Multiple Valid Orderings
**Property:** A DAG can have multiple topological orderings if vertices are incomparable.

**Incomparable Vertices:** Vertices u and v are incomparable if:
- No path from u to v
- No path from v to u
- They can appear in either order in a topological sort

**Example:**
```
Graph: A→B, A→C (B and C are incomparable)

Valid orderings:
- A, B, C ✓
- A, C, B ✓

Both are valid because no edge between B and C
```

### 3. Counting Topological Orderings
**Key Insight:** This is a complex combinatorial problem.

**Approach:**
1. Identify vertices with in-degree 0 (can be placed first)
2. For each choice, recursively count orderings of remaining graph
3. Sum across all choices

**Example (from exams):**
```
Graph: A→B→E, C→D→E, F→E, E→H, E→I, G→I

Initial choices: A, C, F, G (in-degree 0)
Answer: 18 distinct orderings (requires systematic enumeration)
```

### 4. Relationship to Tree Properties
**Important:** Every tree has exactly 2 valid topological orderings (for any root choice) when treated as directed DAG from root to leaves.

---

## Common Exam Question Types

### Type 1: Identify Valid Topological Orderings

**Question:** Which of the following is a valid topological ordering?

**Strategy:**
1. For each proposed ordering, check every edge (u→v)
2. Ensure u appears before v in the ordering
3. If any edge violates this, ordering is invalid

**Example:**
```
Graph: A→B, B→C, A→C

Test ordering [A, B, C]:
- A→B: A before B ✓
- B→C: B before C ✓
- A→C: A before C ✓
Valid! ✓

Test ordering [B, A, C]:
- A→B: A before B? No! A appears after B ✗
Invalid! ✗
```

### Type 2: Modify DFS to Perform Topological Sort

**Question:** Add 3 lines to convert DFS into topological sort.

**Answer:**
```python
# Line 1: At beginning of TRAVERSE function
order = []  # Create empty order array

# Line 2: At end of DFS function (after visiting all neighbors)
order.append(u)  # Add vertex after descendants processed

# Line 3: At end of TRAVERSE function
return reversed(order)  # Return reversed array
```

### Type 3: Count Distinct Topological Orderings

**Question:** How many distinct topological orderings exist?

**Strategy:**
1. Identify all vertices with in-degree 0
2. For each, recursively count orderings after removing it
3. Use dynamic programming or systematic enumeration

**Common Patterns:**
- Linear chain (A→B→C→D): **1** ordering
- Two independent chains: **Multiple** orderings (combinatorial)
- Complete DAG (edges everywhere possible): **1** ordering

### Type 4: Algorithm Trace/Execution

**Question:** Trace Kahn's algorithm step-by-step.

**Strategy:**
1. Compute initial in-degrees
2. Initialize queue with in-degree 0 vertices
3. Process queue step by step
4. Show state after each dequeue operation

**Example:**
```
Step 1: Queue = [A, C], Order = []
Step 2: Remove A, Queue = [C, B], Order = [A]
Step 3: Remove C, Queue = [B, D], Order = [A, C]
...
```

### Type 5: Detect Cycles Using Topological Sort

**Question:** Does the graph have a cycle?

**Strategy:**
1. Attempt topological sort (Kahn's or DFS)
2. If Kahn's: check if all vertices added to ordering
3. If DFS: detect back edges (edge to visited vertex in current path)

**Kahn's Cycle Detection:**
```python
if len(topological_order) != V:
    return "Graph has cycle"
else:
    return "Graph is DAG"
```

---

## Implementation Details

### Kahn's Algorithm - Complete Implementation

```python
def kahns_topological_sort(graph, V):
    """
    graph: adjacency list {u: [v1, v2, ...]}
    V: number of vertices
    Returns: topological ordering or None if cycle exists
    """
    # Step 1: Compute in-degrees
    in_degree = [0] * V
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    # Step 2: Initialize queue with in-degree 0 vertices
    queue = []
    for u in range(V):
        if in_degree[u] == 0:
            queue.append(u)

    # Step 3: Process vertices
    topological_order = []
    while queue:
        u = queue.pop(0)  # Dequeue
        topological_order.append(u)

        # Reduce in-degree of neighbors
        if u in graph:
            for v in graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

    # Step 4: Check for cycle
    if len(topological_order) != V:
        return None  # Cycle detected

    return topological_order

# Time Complexity: O(V + E)
# Space Complexity: O(V)
```

### DFS-Based Topological Sort - Complete Implementation

```python
def dfs_topological_sort(graph, V):
    """
    graph: adjacency list {u: [v1, v2, ...]}
    V: number of vertices
    Returns: topological ordering
    """
    visited = [False] * V
    order = []

    def dfs(u):
        visited[u] = True
        if u in graph:
            for v in graph[u]:
                if not visited[v]:
                    dfs(v)
        order.append(u)  # Post-order: add after descendants

    # Visit all vertices
    for u in range(V):
        if not visited[u]:
            dfs(u)

    return list(reversed(order))  # Reverse for correct order

# Time Complexity: O(V + E)
# Space Complexity: O(V) for recursion stack
```

### Cycle Detection in Directed Graphs (3-State DFS)

```python
def has_cycle(graph, V):
    """
    Uses 3 states: Unvisited, Active, Inactive
    Active = currently exploring descendants (in recursion stack)
    Inactive = finished exploring
    """
    UNVISITED, ACTIVE, INACTIVE = 0, 1, 2
    state = [UNVISITED] * V

    def dfs(u):
        state[u] = ACTIVE
        if u in graph:
            for v in graph[u]:
                if state[v] == ACTIVE:
                    return True  # Back edge found → cycle
                if state[v] == UNVISITED:
                    if dfs(v):
                        return True
        state[u] = INACTIVE
        return False

    for u in range(V):
        if state[u] == UNVISITED:
            if dfs(u):
                return True
    return False

# Time Complexity: O(V + E)
```

**Why 3 States?**
- **Unvisited:** Never seen before
- **Active:** Currently in recursion stack (ancestors of current vertex)
- **Inactive:** Finished processing (all descendants explored)

**Back Edge:** Edge to ACTIVE vertex means cycle (path from ancestor back to itself)

---

## Tricky Concepts and Edge Cases

### 1. Why DFS Gives Reverse Order

**Intuition:** When DFS finishes with a vertex u, all vertices reachable from u are already added to the order.

**Example:**
```
Graph: A→B→C

DFS(A):
  DFS(B):
    DFS(C):
      C has no neighbors
      Add C → order = [C]
    Add B → order = [C, B]
  Add A → order = [C, B, A]

Reversed: [A, B, C] ✓
```

**Why Post-Order Works:**
- In topological sort, u must appear before all vertices it reaches
- Post-order ensures descendants are added first
- Reversing puts u before its descendants

### 2. Difference Between Undirected and Directed Cycle Detection

**Undirected Graph:**
- Cycle exists if edge to visited vertex (excluding parent)
- Simple: just track parent

**Directed Graph:**
- Need to distinguish back edges from cross edges
- Back edge: edge to ancestor in DFS tree → cycle
- Cross edge: edge to vertex in different branch → not cycle
- Solution: Use 3 states (Unvisited, Active, Inactive)

**Common Mistake:** Using 2-state approach for directed graphs gives false positives

**Example (False Positive):**
```
    a → b → d
    ↓       ↑
    c ------+

2-state DFS would incorrectly identify cycle
3-state DFS correctly identifies no cycle (c→d is cross edge, not back edge)
```

### 3. Non-Uniqueness of Topological Orderings

**When Unique?**
- Linear chain: A→B→C→D has exactly 1 ordering
- Complete ordering: Every pair has an edge → unique

**When Multiple?**
- Incomparable vertices exist
- Example: A→B, A→C (B||C incomparable)
  - Valid: A,B,C or A,C,B

**Hamiltonian Path Connection:**
- DAG has unique topological ordering ⟺ DAG has Hamiltonian path
- Hamiltonian path visits every vertex exactly once
- If unique ordering exists, consecutive vertices in ordering form Hamiltonian path

### 4. In-Degree vs Out-Degree

**In-Degree:** Number of incoming edges
- Relevant for Kahn's algorithm
- Vertices with in-degree 0 can be processed first

**Out-Degree:** Number of outgoing edges
- Not directly used in topological sort
- Can be used in other graph algorithms

**Common Exam Trap:** Don't confuse the two!

### 5. Topological Sort in Disconnected Graphs

**Key Point:** Both algorithms handle disconnected components correctly.

**Kahn's:**
- Queue initially contains ALL vertices with in-degree 0 from all components

**DFS:**
- Outer loop visits all unvisited vertices
- Each component processed independently

**Result:** Topological ordering covers all vertices across all components

---

## Problem-Solving Patterns

### Pattern 1: Detecting DAG vs Non-DAG

**Problem:** Is this graph a DAG?

**Solution:**
1. Attempt topological sort using Kahn's algorithm
2. If all vertices added to ordering → DAG
3. Otherwise → contains cycle (not DAG)

**Alternative:** Use cycle detection with 3-state DFS

### Pattern 2: Counting Valid Orderings

**Problem:** How many distinct topological orderings?

**Recursive Approach:**
```python
def count_orderings(graph, in_degree, remaining):
    if not remaining:
        return 1

    # Find vertices with in-degree 0
    candidates = [v for v in remaining if in_degree[v] == 0]

    total = 0
    for v in candidates:
        # Choose v as next in ordering
        # Update in-degrees by removing v's edges
        # Recursively count remaining
        total += count_orderings(graph, updated_in_degree, remaining - {v})

    return total
```

**Complexity:** Exponential (can be optimized with memoization)

### Pattern 3: Longest/Shortest Path in DAG

**Problem:** Find longest path in DAG (common in project scheduling).

**Solution:**
1. Compute topological ordering
2. Process vertices in topological order
3. For each vertex u, update distances to neighbors:
   - `dist[v] = max(dist[v], dist[u] + weight(u,v))`

**Why Topological Order?**
- Ensures we process u before all vertices reachable from u
- Guarantees optimal substructure property

**Time Complexity:** O(V + E) (linear!)

**Note:** This only works for DAGs; general graphs require different algorithms

### Pattern 4: Critical Path Problem

**Problem:** Find critical path in project network (longest path determining minimum project duration).

**Solution:**
1. Represent tasks as vertices, dependencies as edges
2. Edge weights = task durations
3. Find longest path from start to end using topological sort + dynamic programming

**Application:** Project management, scheduling, PERT charts

### Pattern 5: Checking Valid Topological Ordering

**Problem:** Is this ordering valid?

**Algorithm:**
```python
def is_valid_topological_order(graph, ordering):
    # Create position map: position[u] = index of u in ordering
    position = {v: i for i, v in enumerate(ordering)}

    # Check all edges
    for u in graph:
        for v in graph[u]:
            if position[u] >= position[v]:
                return False  # u should come before v

    return True
```

**Time Complexity:** O(V + E)

### Pattern 6: Multi-Source Shortest Path in DAG

**Problem:** Find shortest distance from ANY source vertex.

**Modified Approach:**
1. Add super-source connected to all actual sources (weight 0)
2. Perform topological sort
3. Run DP for shortest paths
4. Subtract 1 from final distances (or don't add super-source initially)

**Alternative:** Initialize all source distances to 0 simultaneously

### Pattern 7: State-Graph Transformation

**Problem:** Complex constraints on valid paths (e.g., can't use consecutive dotted edges).

**Solution:**
1. Define state = (vertex, additional_info)
   - Example: (vertex, was_previous_edge_dotted)
2. Create state-graph with vertices = states
3. Add directed edges between valid state transitions
4. Run standard algorithm on state-graph

**Example:**
```
Original: Cannot traverse consecutive dotted edges
State: ⟨vertex, used_dotted⟩
States: ⟨A, False⟩, ⟨A, True⟩, ⟨B, False⟩, ⟨B, True⟩, ...
Edges:
  - ⟨A, False⟩ → ⟨B, False⟩ if A→B solid
  - ⟨A, False⟩ → ⟨B, True⟩ if A→B dotted
  - ⟨A, True⟩ → ⟨B, False⟩ if A→B solid
  - ⟨A, True⟩ → (nothing) if A→B dotted (invalid!)
```

**Benefit:** Transforms complex problem into standard graph problem

---

## Summary: What You MUST Know for Exams

### Definitions (Memorize)
1. **DAG:** Directed Acyclic Graph (no cycles)
2. **Topological Ordering:** Permutation where u→v implies u before v
3. **In-Degree:** Number of incoming edges
4. **Incomparable Vertices:** No path in either direction

### Algorithms (Trace on Demand)
1. **Kahn's Algorithm:** Queue-based, uses in-degrees, O(V+E)
2. **DFS Topological Sort:** Post-order traversal, reverse result, O(V+E)
3. **3-State Cycle Detection:** Track Unvisited/Active/Inactive

### Key Facts
1. Topological ordering exists ⟺ Graph is DAG
2. DAGs can have multiple valid orderings
3. DFS gives reverse topological order (must reverse!)
4. Both algorithms handle disconnected graphs correctly
5. Cycle detection requires 3 states for directed graphs

### Common Exam Traps
1. Forgetting to reverse DFS result
2. Using 2-state cycle detection for directed graphs (gives false positives)
3. Confusing in-degree with out-degree
4. Assuming topological ordering is unique
5. Not checking if all vertices processed (cycle check)

### Complexity Analysis
- **Kahn's:** O(V + E) time, O(V) space
- **DFS Topological Sort:** O(V + E) time, O(V) space (recursion)
- **Cycle Detection:** O(V + E) time, O(V) space

### When to Use Which Algorithm
- **Kahn's:** When you need to detect cycles AND get ordering
- **DFS:** When integrating with other DFS-based algorithms
- **Either:** Both produce valid results; choose based on context

---

## Final Exam Tips

1. **Practice Tracing:** Be able to trace both algorithms step-by-step with diagrams
2. **Understand Why:** Don't just memorize; understand why DFS needs reversal, why 3 states needed
3. **Draw Pictures:** Visualize graphs and orderings
4. **Check Edge Cases:** Empty graph, single vertex, disconnected components
5. **Time Yourself:** Practice identifying valid orderings quickly
6. **Count Systematically:** For counting problems, enumerate methodically
7. **Verify Answers:** After finding ordering, verify all edges satisfy property
