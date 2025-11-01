# Algorithm Edge Cases Checklist

This document provides comprehensive edge case checklists for each algorithm type, compiled from past exam problems, mid-semester tests, and applied solutions.

---

## Table of Contents

1. [Graph Algorithms](#graph-algorithms)
2. [Shortest Path Algorithms](#shortest-path-algorithms)
3. [Minimum Spanning Tree (MST)](#minimum-spanning-tree-mst)
4. [Network Flow](#network-flow)
5. [Graph Traversal (DFS/BFS)](#graph-traversal-dfsbfs)
6. [Dynamic Programming](#dynamic-programming)
7. [Sorting & Selection](#sorting--selection)
8. [Trees (AVL, BST)](#trees-avl-bst)
9. [String Algorithms](#string-algorithms)
10. [General Algorithm Edge Cases](#general-algorithm-edge-cases)

---

## Graph Algorithms

### General Graph Edge Cases

- [ ] **Empty graph** (V = 0, E = 0)
- [ ] **Single vertex** (V = 1, E = 0)
- [ ] **Two vertices, no edges** (disconnected)
- [ ] **Two vertices, one edge**
- [ ] **Disconnected graph** (multiple components)
- [ ] **Complete graph** (all vertices connected to all others)
- [ ] **Self-loops** (edge from vertex to itself)
- [ ] **Parallel edges** (multiple edges between same pair of vertices)
- [ ] **Directed vs undirected** considerations
- [ ] **Dense graph** (E ≈ V²)
- [ ] **Sparse graph** (E ≈ V)
- [ ] **Tree structure** (E = V - 1, connected, no cycles)
- [ ] **DAG** (Directed Acyclic Graph)
- [ ] **Graph with cycles**
- [ ] **Bipartite graph**
- [ ] **Non-bipartite graph** (odd-length cycles)

### Edge Weight Edge Cases

- [ ] **All zero weights**
- [ ] **All same positive weight**
- [ ] **Negative weights**
- [ ] **Mixture of positive and negative weights**
- [ ] **Very large weight differences** (e.g., 1 vs 1000)
- [ ] **Integer overflow** potential with large weights

---

## Shortest Path Algorithms

### Dijkstra's Algorithm

- [ ] **Negative edge weights** (algorithm fails/incorrect)
- [ ] **Source equals destination** (distance = 0)
- [ ] **Destination unreachable** from source
- [ ] **Multiple components** (some vertices unreachable)
- [ ] **All edges have same weight** (BFS would suffice)
- [ ] **Very long paths** vs **very short direct paths**
- [ ] **Vertex with no outgoing edges**
- [ ] **Vertex with no incoming edges** (except source)
- [ ] **Paths where first discovery is not optimal** (requires relaxation)
- [ ] **Graph where greedy choice fails** (e.g., path through expensive edge is discovered first)

**Example from exams**: Graph where initial distance estimate must be updated:
```
s --1--> a --1000--> d
 \               ^
  \--2--> b --1-+
```
Distance to `d` via `a` is initially 1001, but should be updated to 4 via `b`.

### Bellman-Ford Algorithm

- [ ] **Negative cycles** (algorithm should detect)
- [ ] **Negative edge weights** (algorithm handles correctly)
- [ ] **Source equals destination**
- [ ] **Destination unreachable**
- [ ] **Edge relaxation order matters** (ensure all edges checked V-1 times)
- [ ] **Graph where distance changes in V-th iteration** (negative cycle)
- [ ] **Very deep paths** (close to V edges long)

**From exams**: After iteration 1, distances may still be suboptimal; full V-1 iterations needed.

### Floyd-Warshall Algorithm

- [ ] **All-pairs shortest paths**
- [ ] **Negative cycles** (check diagonal for negative values)
- [ ] **Disconnected pairs** (distance = ∞)
- [ ] **Path vs direct edge** confusion (result shows path, not edge)
- [ ] **Dense vs sparse graphs** (complexity always O(V³))
- [ ] **Matrix with some ∞ values** (unreachable pairs)
- [ ] **Negative diagonal values** indicate negative cycle

**From exams**: After k iterations, dist[i][j] uses only vertices 1..k as intermediates.

### 0-1 BFS (Binary Edge Weights)

- [ ] **All edges weight 0** (degenerates to standard BFS)
- [ ] **All edges weight 1** (standard BFS)
- [ ] **Mixture of 0 and 1 weights**
- [ ] **Path with multiple 0-weight edges**
- [ ] **First path found is not optimal** (requires deque management)
- [ ] **Multiple paths with same distance**
- [ ] **Source equals destination**

**From past_mid/network_infection_problems.md**: Standard BFS fails when 0-weight edges allow revisiting for better paths.

Example:
```
0 --weak(0)--> 1 --weak(0)--> 2
|                              |
strong(1)                   weak(0)
|                              |
3 --strong(1)--> 4 <--weak(0)- 5
```
Node 4 can be reached in 0 days via path 0→1→2→5→4, not 2 days via 0→3→4.

---

## Minimum Spanning Tree (MST)

### Kruskal's Algorithm

- [ ] **All edges same weight** (multiple valid MSTs)
- [ ] **Negative edge weights** (algorithm still works correctly)
- [ ] **Disconnected graph** (produces minimum spanning forest)
- [ ] **Single vertex**
- [ ] **Tree already** (E = V-1, no cycles)
- [ ] **Complete graph** (many edges to sort)
- [ ] **Edges presented unsorted**
- [ ] **Cycle detection** with Union-Find
- [ ] **Union-by-size vs union-by-rank** implementations
- [ ] **Early termination** when V-1 edges added

**From exams**: Union-Find parent array relationship ≠ graph edges; parent pointers represent set structure, not MST edges.

### Prim's Algorithm

- [ ] **All edges same weight**
- [ ] **Negative edge weights** (works correctly, unlike Dijkstra with negatives)
- [ ] **Starting vertex choice** (any vertex works for connected graph)
- [ ] **Disconnected graph** (only produces MST for one component)
- [ ] **Min-heap vs max-heap** (max-heap produces maximum spanning tree)
- [ ] **Dense vs sparse graphs** (adjacency matrix vs list)
- [ ] **Single vertex**
- [ ] **Already a tree**

**From exams**: Using max-heap instead of min-heap produces maximum spanning tree.

### MST Applications (Clustering)

- [ ] **k clusters from MST** (remove k-1 heaviest edges)
- [ ] **Maximizing minimum inter-cluster distance**
- [ ] **k > number of connected components** (impossible)
- [ ] **k = 1** (entire graph is one cluster)
- [ ] **k = V** (each vertex is its own cluster)
- [ ] **Complete graph with all pairwise distances**

**From exams**: MST clustering works by removing k-1 heaviest edges; complexity O(n² log n) for complete graph.

---

## Network Flow

### Maximum Flow (Ford-Fulkerson)

- [ ] **Source equals sink** (flow = 0 or undefined)
- [ ] **Sink unreachable from source** (max flow = 0)
- [ ] **No edges from source** (max flow = 0)
- [ ] **No edges to sink** (max flow = 0)
- [ ] **All edges saturated**
- [ ] **Bottleneck at source outgoing edges**
- [ ] **Bottleneck at sink incoming edges**
- [ ] **Multiple augmenting paths available**
- [ ] **No augmenting paths** (max flow reached)
- [ ] **Residual graph with backward edges**
- [ ] **Integer vs non-integer capacities**
- [ ] **Very large capacities** (termination issues with non-integer)

**From exams**: Max flow = min cut capacity (theorem).

### Minimum Cut

- [ ] **Vertices reachable from source** in residual graph form set S
- [ ] **Cut capacity equals max flow value**
- [ ] **Multiple minimum cuts** possible
- [ ] **Cut that disconnects source from sink**
- [ ] **Forward vs backward edges** in residual graph

**From exams**: After max flow, run DFS/BFS in residual graph from source to find reachable vertices (set S); cut edges go from S to T.

### Circulation with Demands

- [ ] **Sum of demands ≠ 0** (immediately infeasible)
- [ ] **Sum of demands = 0** (necessary but not sufficient)
- [ ] **Capacity constraints too tight** (infeasible even with balanced demands)
- [ ] **Negative demands** (sinks) vs **positive demands** (sources)
- [ ] **Vertices with zero demand**
- [ ] **Supersource and supersink** construction
- [ ] **All edges from supersource must be saturated** for feasibility
- [ ] **All edges to supersink must be saturated** for feasibility

**From exams**: Problem 2 in s2.json Q14 has sum = 1 ≠ 0, immediately infeasible.

### Bipartite Matching

- [ ] **More left nodes than right nodes** (not all can be matched)
- [ ] **More right nodes than left nodes**
- [ ] **Perfectly matchable** (all left nodes matched)
- [ ] **Some nodes with no preferences/edges**
- [ ] **Nodes with capacity constraints** (e.g., max 5 students per company)
- [ ] **Single preference per node** vs **multiple preferences**
- [ ] **Maximum matching < minimum of left/right sizes**

**From exams**: Student-company assignment with capacities; not all students can be placed.

---

## Graph Traversal (DFS/BFS)

### Depth-First Search (DFS)

- [ ] **Single vertex**
- [ ] **Disconnected graph** (multiple DFS calls needed)
- [ ] **Graph with cycles** (need visited set)
- [ ] **Directed graph cycle detection** (use active/inactive/unvisited states)
- [ ] **Undirected graph cycle detection** (check if neighbor is visited and not parent)
- [ ] **Tree traversal** (no cycles)
- [ ] **Recursive vs iterative** implementation (stack overflow concerns)
- [ ] **Topological sort** (only for DAGs)
- [ ] **Tie-breaking rules** (alphabetical, numerical, etc.)
- [ ] **Visiting order affects result**

**From exams**: Directed cycle detection requires distinguishing between "active" (ancestor in DFS tree) vs "inactive" (different branch) visited nodes.

### Breadth-First Search (BFS)

- [ ] **Single vertex**
- [ ] **Disconnected graph**
- [ ] **Tree structure** (BFS tree height)
- [ ] **Shortest paths in unweighted graphs**
- [ ] **Level-order traversal**
- [ ] **Multi-source BFS** (multiple starting nodes)
- [ ] **Tie-breaking rules**
- [ ] **Queue implementation** (deque in Python)

**From exams**: Multi-source BFS solved by initializing queue with all sources at distance 0.

### Two-Coloring (Bipartite Detection)

- [ ] **Graph with odd-length cycle** (not two-colorable)
- [ ] **Graph with only even-length cycles** (two-colorable)
- [ ] **Tree** (always two-colorable)
- [ ] **Disconnected graph** (check each component)
- [ ] **Number of colorings = 2^(number of components)** if graph is two-colorable
- [ ] **Single vertex** (two-colorable, 2 ways)
- [ ] **Adjacent vertices must have different colors**

**From past_mid**: Graph not two-colorable means answer = 0 for counting two-colorings.

### Topological Sort

- [ ] **Graph with cycle** (topological sort impossible)
- [ ] **DAG** (topological sort exists)
- [ ] **Multiple valid orderings** (many DAGs have multiple topological sorts)
- [ ] **Disconnected DAG** (components can be ordered arbitrarily)
- [ ] **Unique topological ordering** (only if graph is a single path)
- [ ] **Verification of given ordering** (O(E) time to check all edges)

**From exams**: Disconnected DAG allows much freedom in ordering; vertices from different components independent.

---

## Dynamic Programming

### General DP Edge Cases

- [ ] **Base case: n = 0**
- [ ] **Base case: n = 1**
- [ ] **Single element**
- [ ] **Empty input**
- [ ] **All elements same value**
- [ ] **Negative values** (if applicable)
- [ ] **Very large values** (integer overflow)
- [ ] **Optimal substructure** must hold
- [ ] **Overlapping subproblems** must exist
- [ ] **Dependencies between subproblems**
- [ ] **Order of computation** (bottom-up vs top-down)

### House Selling / Non-Adjacent Selection

- [ ] **Single house**
- [ ] **Two houses**
- [ ] **All same profit**
- [ ] **Increasing profits**
- [ ] **Decreasing profits**
- [ ] **Cannot sell to adjacent houses** (i-1, i+1)
- [ ] **Extended constraint**: Cannot sell to i-2, i-1, i+1, i+2
- [ ] **Backtracking to reconstruct solution**
- [ ] **DP[i] = DP[i-1]** means house i not selected
- [ ] **DP[i] > DP[i-1]** means house i potentially selected

**From exams (s1.json Q9)**: DP array [20, 20, 30, 50, 60, 100, 100] → houses 1,4,6 selected via backtracking.

### Grid Path Counting

- [ ] **1x1 grid** (1 way)
- [ ] **Single row** (1 way)
- [ ] **Single column** (1 way)
- [ ] **No blocked cells** (combinatorial formula)
- [ ] **Starting cell blocked** (0 ways)
- [ ] **Ending cell blocked** (0 ways)
- [ ] **All cells blocked** except start/end (0 or 1 ways)
- [ ] **Blocked cells creating impassable barriers**
- [ ] **Movement restrictions** (up, right only vs all directions)

**From exams (s2.json Q20)**: DP[i][j] = DP[i-1][j] + DP[i][j-1] if not blocked; 0 if blocked.

### Knapsack Variants

- [ ] **0/1 Knapsack**: Each item taken 0 or 1 times
- [ ] **Unbounded Knapsack**: Each item taken unlimited times
- [ ] **Capacity = 0** (can't take anything)
- [ ] **Single item**
- [ ] **All items too heavy** (capacity too small)
- [ ] **All items have same value**
- [ ] **Greedy approach fails** (need DP)
- [ ] **Fractional knapsack** (greedy works)

**From exams (25-1.json Q24)**: Greedy fails for 0/1 knapsack; DP ensures optimality.

### Interval Scheduling (Weighted)

- [ ] **Single interval**
- [ ] **Non-overlapping intervals** (take all)
- [ ] **All intervals overlap** (take best one)
- [ ] **Equal weights** (reduces to maximum number of intervals)
- [ ] **Sorted by finish time**
- [ ] **Binary search for compatible previous interval**

**From exams**: Unweighted version uses greedy (earliest finish time); weighted version requires DP.

---

## Sorting & Selection

### Quickselect

- [ ] **k = 1** (find minimum)
- [ ] **k = n** (find maximum)
- [ ] **k = n/2** (find median)
- [ ] **All elements equal**
- [ ] **Already sorted array**
- [ ] **Reverse sorted array**
- [ ] **Duplicate elements**
- [ ] **Pivot selection strategy** (first, last, random, median-of-medians)
- [ ] **Partition into equal halves** vs **unbalanced partitions**
- [ ] **Multiple elements with value equal to k-th**

**From exams**: Median-of-medians guarantees O(n) by ensuring pivot in 30th-70th percentile; eliminates at least 30% per iteration.

### Sorting Algorithms

- [ ] **Empty array**
- [ ] **Single element**
- [ ] **Already sorted**
- [ ] **Reverse sorted**
- [ ] **All elements equal**
- [ ] **Duplicates**
- [ ] **Negative numbers**
- [ ] **Mixed positive and negative**
- [ ] **Stability requirement** (equal elements maintain relative order)

#### Counting Sort / Radix Sort

- [ ] **Negative numbers** (need offset)
- [ ] **Very large range** (k >> n, inefficient)
- [ ] **Non-integer keys**
- [ ] **Base representation choice** in radix sort (higher base = fewer passes, but larger counting sort cost)

**From exams (s2.json Q5)**: Increasing radix base reduces passes but increases per-pass cost; optimal to balance.

---

## Trees (AVL, BST)

### Binary Search Tree (BST)

- [ ] **Empty tree**
- [ ] **Single node**
- [ ] **Degenerate to linked list** (worst-case O(n) height)
- [ ] **Perfectly balanced**
- [ ] **Duplicate values** (left vs right placement convention)
- [ ] **Search for non-existent value**
- [ ] **Insertion causing imbalance**
- [ ] **Deletion of leaf, node with one child, node with two children**
- [ ] **Deletion requiring successor/predecessor**

### AVL Tree

- [ ] **Balance factor = {-1, 0, 1}** (valid range)
- [ ] **Balance factor = -2 or 2** (requires rotation)
- [ ] **Single rotation** (LL, RR cases)
- [ ] **Double rotation** (LR, RL cases)
- [ ] **Insertion causing single vs double rotation**
- [ ] **Deletion maintaining balance**
- [ ] **Height = O(log n)** guarantee
- [ ] **Empty tree**
- [ ] **Single node**

**From exams (s1.json Q15)**: Deleting/inserting may or may not require rotations depending on resulting balance factors.

**Example (s1.json Q15)**:
- Deleting 10 keeps tree balanced (no rotation)
- Inserting 12 causes imbalance at node 10 (requires rotation)

### Hash Tables

- [ ] **Empty table**
- [ ] **All keys hash to same bucket** (worst-case O(n) for all operations)
- [ ] **Uniform distribution** (expected O(1))
- [ ] **Load factor < 1** vs **load factor > 1**
- [ ] **Separate chaining** vs **open addressing**
- [ ] **Collision resolution**: linked list, BST, AVL tree, sorted array
- [ ] **Rehashing/resizing** threshold
- [ ] **Deletion handling** (tombstones in open addressing)

**From exams**: Worst-case complexity depends on chain data structure:
- Linked list: O(n)
- Unbalanced BST: O(n)
- AVL tree: O(log n)
- Sorted array: O(n) due to insertion shifts

---

## String Algorithms

### Suffix Array / Suffix Tree

- [ ] **Empty string**
- [ ] **Single character**
- [ ] **All same character** (e.g., "aaaa$")
- [ ] **No repeated substrings**
- [ ] **Sentinel character** (e.g., "$")
- [ ] **Prefix doubling**: k = 1, 2, 4, 8, ...
- [ ] **Comparing suffixes in O(1)** using rank arrays
- [ ] **Rank ties after k-character sort**

**From exams (s1.json Q12, s2.json Q17)**: Rank array comparison:
- Suffixes i and j have same first k chars if rank[i] = rank[j]
- To sort on first 2k chars, compare (rank[i], rank[i+k]) vs (rank[j], rank[j+k])

### Burrows-Wheeler Transform (BWT)

- [ ] **LF mapping**: LF(i) = rank[BWT[i]] + occ[i]
- [ ] **Reconstructing original string**
- [ ] **Pattern matching** with backward search
- [ ] **Run-length encoding** on BWT (typically better than on original)
- [ ] **occ array**: count of character before position i
- [ ] **rank array**: first occurrence of character in sorted BWT

**From exams (21-1.json Q13-15)**: LF mapping traces character preceding current position in original string.

---

## General Algorithm Edge Cases

### Input Validation

- [ ] **Null input**
- [ ] **Empty input** (n = 0)
- [ ] **Single element** (n = 1)
- [ ] **Two elements** (n = 2)
- [ ] **Negative values** where unexpected
- [ ] **Zero values**
- [ ] **Very large values** (overflow)
- [ ] **Very small values** (underflow)
- [ ] **Integer vs floating-point** precision

### Loop Invariants & Correctness

- [ ] **Initialization**: Invariant holds before loop starts
- [ ] **Maintenance**: If invariant holds at start of iteration i, it holds at start of i+1
- [ ] **Termination**: Invariant holds when loop exits, proving correctness

**From exams (21-1.json Q1-4)**: Loop invariant example: `p = parity of L[1..i-1]` at start of each loop iteration.

### Complexity Edge Cases

- [ ] **Best case**: Already optimal input (e.g., sorted array for insertion sort → O(n))
- [ ] **Worst case**: Adversarial input (e.g., reverse sorted for insertion sort → O(n²))
- [ ] **Average case**: Random input
- [ ] **Amortized complexity** (e.g., dynamic array resizing)
- [ ] **Space complexity**: Auxiliary vs total
- [ ] **Time-space tradeoff** (e.g., memoization)

### Recurrence Relations

- [ ] **Base case: T(0), T(1)**
- [ ] **Master Theorem applicability**
  - Case 1: f(n) = O(n^c), c < log_b(a) → T(n) = Θ(n^log_b(a))
  - Case 2: f(n) = Θ(n^c), c = log_b(a) → T(n) = Θ(n^c log n)
  - Case 3: f(n) = Ω(n^c), c > log_b(a) + regularity → T(n) = Θ(f(n))
- [ ] **Telescoping method** when Master Theorem doesn't apply
- [ ] **Substitution method** for proving bounds

---

## State-Graph / Problem Transformation Edge Cases

### State-Graph Modeling

- [ ] **State = (vertex, additional context)**
- [ ] **Example**: (vertex, fuel_remaining) for refueling problem
- [ ] **Example**: (vertex, last_edge_type) for dotted/solid edge problem
- [ ] **Edges = valid state transitions**
- [ ] **Start state** and **goal state** clearly defined
- [ ] **Multiple goal states** (take minimum distance)

**From applied_solutions**: State-graph allows modeling complex constraints by encoding state in vertices.

### Problem Transformation

- [ ] **Max spanning tree** → negate weights → min spanning tree
- [ ] **Multi-source shortest path** → add supersource → single-source shortest path
- [ ] **Assignment problem** → bipartite matching → max flow
- [ ] **Clustering** → MST + remove k-1 heaviest edges

---

## Common Exam Pitfalls (Meta Edge Cases)

### Conceptual Errors

- [ ] **Confusing path vs direct edge** (e.g., Floyd-Warshall result)
- [ ] **Assuming first discovered path is optimal** (requires relaxation)
- [ ] **Forgetting to check all edges** in Bellman-Ford (need V-1 iterations)
- [ ] **Union-Find parent array ≠ MST edges** (parent array is for set structure)
- [ ] **Ignoring disconnected graphs** (many algorithms assume connectivity)
- [ ] **Stability of sorting** (heap sort, selection sort are NOT stable)
- [ ] **Greedy choice not optimal** (e.g., 0/1 knapsack requires DP, not greedy)

### Implementation Errors

- [ ] **Off-by-one errors** (array indexing)
- [ ] **Loop invariant positioned incorrectly** (must hold at marked location)
- [ ] **Not initializing distances to ∞** (shortest path algorithms)
- [ ] **Not marking vertices as visited** (graph traversal)
- [ ] **Incorrect tie-breaking** (affects traversal order)
- [ ] **Forgetting to handle base cases** (recursion, DP)

### Complexity Errors

- [ ] **Amortized vs worst-case** (e.g., hash table)
- [ ] **Expected vs guaranteed** (e.g., quicksort)
- [ ] **Auxiliary space vs total space**
- [ ] **Graph representation affects complexity** (adjacency matrix vs list)
- [ ] **Alphabet size Θ(1) vs Θ(M)** (affects string algorithm space complexity)

---

## Summary: Top 20 Most Common Edge Cases Across All Algorithms

1. **Empty input** (n = 0, V = 0, E = 0)
2. **Single element** (n = 1, single vertex, single edge)
3. **Disconnected graph** (multiple components)
4. **Source equals destination**
5. **Unreachable destination** (infinite distance)
6. **All same values** (weights, elements, etc.)
7. **Negative values** (weights, array elements)
8. **Zero values** (zero-weight edges, zero capacity)
9. **Already sorted / optimal input** (best-case complexity)
10. **Reverse sorted / adversarial input** (worst-case complexity)
11. **Duplicate values** (ties, equal elements)
12. **Cycles in graph** (directed vs undirected detection)
13. **Self-loops** (edge from vertex to itself)
14. **Multiple valid solutions** (e.g., multiple MSTs with equal weights)
15. **Integer overflow** (very large sums, products)
16. **Base cases in recursion/DP** (T(0), T(1), DP[0])
17. **Off-by-one errors** (array bounds, loop invariants)
18. **First-discovered path not optimal** (requires relaxation)
19. **Tie-breaking rules** (alphabetical, numerical ordering)
20. **Problem transformation** (recognizing when input can be transformed to use standard algorithm)

---

## Checklist Usage Guide

### During Problem Solving

1. **Identify the algorithm type** required
2. **Read the relevant edge case checklist** for that algorithm
3. **Check off each edge case** as you consider it
4. **Write test cases** for unchecked edge cases
5. **Verify your solution handles all checked cases**

### During Exam

1. **Quickly scan the checklist** for the algorithm in the question
2. **Mark edge cases explicitly mentioned** in the problem
3. **Consider 2-3 most likely unlisted edge cases** (empty, single, disconnected)
4. **Verify your solution against these** before finalizing answer

### During Practice

1. **Create failing test cases** from this checklist
2. **Fix your implementation** to handle each edge case
3. **Add your own discovered edge cases** to the list
4. **Review checklist before mid-semester / final exam**

---

## Example: Applying Checklist to a Problem

**Problem**: Given a weighted directed graph and source s, find shortest paths to all vertices using Dijkstra's algorithm.

**Checklist Application**:
- [ ] Source equals destination? → Yes, handle: dist[s] = 0
- [ ] Negative edge weights? → **Dijkstra fails!** Problem invalid or need Bellman-Ford
- [ ] Disconnected graph? → Yes, handle: some vertices will have dist = ∞
- [ ] Single vertex? → Yes, handle: only dist[s] = 0, no edges to process
- [ ] All same weight? → Yes, still works but BFS more efficient
- [ ] Destination unreachable? → Yes, handle: dist[d] = ∞ in final result

**Result**: Solution must handle dist initialization, negative weight check (or problem clarification), and unreachable vertices.

---

## Maintenance

This document should be updated as you:
- Discover new edge cases in practice problems
- Review past exams from other years
- Encounter edge cases in applied class problems
- Find implementation bugs related to edge cases

**Last Updated**: Generated from 2021-2025 exam materials and applied solutions.

---

## Quick Reference: Complexity Cheat Sheet

| Algorithm | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| **Dijkstra** | O((V+E) log V) | O((V+E) log V) | O((V+E) log V) | O(V) |
| **Bellman-Ford** | O(VE) | O(VE) | O(VE) | O(V) |
| **Floyd-Warshall** | O(V³) | O(V³) | O(V³) | O(V²) |
| **BFS/DFS** | O(V+E) | O(V+E) | O(V+E) | O(V) |
| **Kruskal** | O(E log E) | O(E log E) | O(E log E) | O(V) |
| **Prim** | O((V+E) log V) | O((V+E) log V) | O((V+E) log V) | O(V) |
| **Quickselect** | O(n) | O(n) | O(n²) | O(log n) |
| **Quickselect+MoM** | O(n) | O(n) | O(n) | O(log n) |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | O(n) |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) |
| **Counting Sort** | O(n+k) | O(n+k) | O(n+k) | O(n+k) |
| **Radix Sort** | O(d(n+k)) | O(d(n+k)) | O(d(n+k)) | O(n+k) |
| **AVL Insert/Delete/Search** | O(log n) | O(log n) | O(log n) | O(n) |
| **Hash Table** | O(1) | O(1) | O(n) | O(n) |

Where:
- V = vertices, E = edges
- n = array/list size
- k = range of values (counting sort)
- d = number of digits (radix sort)

---

**End of Checklist**
