# Network Infection Problems - Mid-Semester Practice

## Problem 1: Dual-Weight Network Infection

### Problem Statement

Given a network where:
- **Nodes**: Computers (some initially infected with a virus)
- **Edges**: Two types of connections
  - **Weak edges**: Infection spreads instantly (0 days)
  - **Strong edges**: Infection takes 1 day to spread
- **Goal**: Find the minimum number of days required to infect the entire network

Design an algorithm that runs in **O(V + E)** time.

### Example

```
Graph:
         weak      weak
    0 -------- 1 -------- 2
    |                      |
  strong                 weak
    |                      |
    3 -------- 4 -------- 5
        strong     weak

Initially infected: [0]
```

**Answer: 1 day**

**Explanation:**
- Day 0: Nodes {0, 1, 2, 5, 4} infected
  - 0: initially infected
  - 1: via weak edge from 0
  - 2: via weak edge from 1
  - 5: via weak edge from 2
  - 4: via weak edge from 5
- Day 1: Node {3} infected via strong edge from 0

### Solution: 0-1 BFS

This is a **shortest path problem** with edge weights of only 0 or 1. Use **0-1 BFS** (deque-based BFS) for O(V+E) complexity.

#### Algorithm

```python
from collections import deque

def days_to_infect_network(graph, initially_infected):
    """
    Calculate days needed to infect entire network.

    Args:
        graph: dict of {node: [(neighbor, edge_type), ...]}
               edge_type: 'weak' (0 days) or 'strong' (1 day)
        initially_infected: list of initially infected nodes

    Returns:
        Maximum days to infect all nodes, or -1 if impossible

    Time: O(V + E)
    Space: O(V)
    """
    # Initialize distances to infinity
    dist = {node: float('inf') for node in graph}

    # Use deque for 0-1 BFS
    dq = deque()

    # All initially infected nodes start at day 0
    for node in initially_infected:
        dist[node] = 0
        dq.append(node)

    # 0-1 BFS
    while dq:
        u = dq.popleft()

        for neighbor, edge_type in graph[u]:
            # Calculate infection time for this edge
            if edge_type == 'weak':
                weight = 0  # Instant infection
            else:  # edge_type == 'strong'
                weight = 1  # Takes 1 day

            new_dist = dist[u] + weight

            # Relaxation step
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist

                # 0-1 BFS optimization:
                # - Add to front if weight = 0 (weak edge)
                # - Add to back if weight = 1 (strong edge)
                if weight == 0:
                    dq.appendleft(neighbor)
                else:
                    dq.append(neighbor)

    # Find maximum days needed
    max_days = max(dist.values())

    # Check if all nodes are reachable
    if max_days == float('inf'):
        return -1  # Not all computers can be infected

    return max_days
```

#### Complexity Analysis

- **Time Complexity**: O(V + E)
  - Each node is processed at most once
  - Each edge is examined at most once
  - Deque operations (append/appendleft/popleft) are O(1)

- **Space Complexity**: O(V)
  - Distance dictionary: O(V)
  - Deque: O(V) in worst case

#### Key Concepts

1. **0-1 BFS**: Optimized BFS for graphs with edge weights of only 0 or 1
2. **Deque invariant**: Maintains distances in order [d, d, ..., d, d+1, d+1, ..., d+1]
3. **Relaxation**: Update distance if a better path is found
4. **Multi-source shortest path**: Handle multiple starting nodes

#### Why 0-1 BFS Works

When edges have weights only 0 or 1:
- **Weak edge (weight 0)**: Add neighbor to **front** of deque (process immediately)
- **Strong edge (weight 1)**: Add neighbor to **back** of deque (process later)

This maintains the property that the deque is always sorted by distance, ensuring we process nodes in non-decreasing order of their optimal distance.

---

## Common Mistake: Using Standard BFS

### Incorrect Approach

A common mistake is to use standard BFS with a "mark visited once" strategy:

```python
def incorrect_approach(graph, initially_infected):
    """
    INCORRECT: Standard BFS doesn't handle different edge weights correctly
    """
    infected = set(initially_infected)
    queue = deque()

    for node in initially_infected:
        queue.append((node, 0))

    max_days = 0

    while queue:
        u, days = queue.popleft()

        for neighbor, edge_type in graph[u]:
            if neighbor not in infected:
                infected.add(neighbor)

                if edge_type == 'strong':
                    new_days = days + 1
                else:
                    new_days = days

                max_days = max(max_days, new_days)
                queue.append((neighbor, new_days))

    return max_days
```

### Why This Fails

**Issue**: The first path to reach a node may not be the fastest path when edges have different weights.

**Counterexample**:
```
         weak      weak
    0 -------- 1 -------- 2
    |                      |
  strong                 weak
    |                      |
    3 -------- 4 -------- 5
        strong     weak

Initially infected: [0]
```

**Standard BFS result**: 2 days
- Discovers node 4 via path 0→3→4 (days: 0→1→2)

**Correct answer**: 1 day
- Node 4 reached via path 0→1→2→5→4 on day 0
- Node 3 reached on day 1

### Key Differences

| Standard BFS | 0-1 BFS |
|-------------|---------|
| Mark visited once, never revisit | Allow updates via relaxation |
| First path found = final answer | Multiple paths considered |
| Works only for unweighted graphs | Works for weights {0, 1} |
| No distance updates | Updates distance if better path found |

---

## Related Problems

### Variation 1: Multiple Virus Sources
If multiple computers are initially infected, the algorithm handles this naturally by initializing all source nodes to day 0.

### Variation 2: Finding Unreachable Computers
If `dist[node] = ∞` after the algorithm completes, that node cannot be infected (disconnected from all infected sources).

### Variation 3: K Different Edge Weights
If edges can have weights {0, 1, 2, ..., k}, use:
- **Dijkstra's algorithm** with priority queue: O((V+E) log V)
- **Modified multi-deque approach**: O(V + E) with k deques (advanced)

---

## Problem 2: Kruskal's Algorithm Correctness Proof

### Algorithm Overview

**Kruskal's Algorithm** finds a Minimum Spanning Tree (MST) for a connected, weighted graph by:
1. Sorting all edges by weight (ascending)
2. Iterating through edges in sorted order
3. Adding an edge to the MST if it doesn't create a cycle
4. Using Union-Find to detect cycles efficiently

### Implementation

```python
class UnionFind:
    def __init__(self, n):
        # parent[i] < 0 means i is root with size |parent[i]|
        # parent[i] >= 0 means parent of i is parent[i]
        self.parent = [-1] * n

    def find(self, x):
        """Find root with path compression. O(α(n)) amortized"""
        if self.parent[x] < 0:
            return x
        self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        """Union by size. Returns True if union performed, False if already connected"""
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Already in same set, would create cycle

        # Union by size: attach smaller tree to larger
        if self.parent[root_x] > self.parent[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_x] += self.parent[root_y]  # Update size
        self.parent[root_y] = root_x  # Attach root_y to root_x
        return True

def kruskal(vertices, edges):
    """
    Find MST using Kruskal's algorithm.

    Args:
        vertices: number of vertices (0 to vertices-1)
        edges: list of (u, v, weight)

    Returns:
        List of edges in MST, total MST weight

    Time: O(E log E)
    Space: O(V)
    """
    # Sort edges by weight: O(E log E)
    edges.sort(key=lambda e: e[2])

    uf = UnionFind(vertices)
    mst = []
    total_weight = 0

    # Process edges in order: O(E * α(V))
    for u, v, weight in edges:
        if uf.union(u, v):  # If doesn't create cycle
            mst.append((u, v, weight))
            total_weight += weight

            if len(mst) == vertices - 1:  # MST complete
                break

    return mst, total_weight
```

### Correctness Proof

We prove Kruskal's algorithm produces an MST using the **Cut Property** and **Exchange Argument**.

#### Theorem: Kruskal's Algorithm Produces an MST

**Proof by Induction**

**Claim**: At each step, the set of edges chosen so far can be extended to form an MST.

**Base Case**:
- Initially, we have no edges
- The empty set can trivially be extended to an MST
- ✓ Base case holds

**Inductive Hypothesis**:
- Assume after adding k edges, we have a set A of edges that can be extended to some MST T

**Inductive Step**:
- Let e = (u, v) be the next edge Kruskal's algorithm adds
- We need to show A ∪ {e} can be extended to an MST

**Two cases:**

**Case 1: e is already in T**
- Then A ∪ {e} ⊆ T
- So A ∪ {e} can be extended to T (an MST)
- ✓ Inductive step holds

**Case 2: e is not in T**
- Since T is a spanning tree, adding e to T creates exactly one cycle C
- All edges in C were considered by Kruskal before or when processing e
- Since Kruskal didn't add some edge e' in C before e, either:
  - e' has weight ≥ weight(e), OR
  - e' would have created a cycle at the time (already connected)

**Key observation**: When Kruskal adds e = (u, v):
- u and v are in different components in A
- Since T is spanning, there exists a path P from u to v in T
- This path P must contain some edge f = (x, y) where x and y are in different components of A
- f was available when we processed e, but we chose e instead
- Therefore: weight(e) ≤ weight(f)

**Exchange argument**:
- Remove f from T and add e: T' = T - {f} + {e}
- T' is still a spanning tree (connects the two components that f connected)
- weight(T') = weight(T) - weight(f) + weight(e) ≤ weight(T)
- Since T is an MST, weight(T') = weight(T) (can't be less)
- Therefore weight(e) = weight(f)
- So T' is also an MST
- A ∪ {e} ⊆ T'
- ✓ Inductive step holds

**Conclusion**: By induction, Kruskal's algorithm produces an MST. ∎

#### Alternative Proof: Cut Property

**Cut Property**: For any cut (S, V-S) of the graph, the minimum weight edge crossing the cut is in some MST.

**Proof using Cut Property**:

For each edge e = (u, v) that Kruskal adds:
1. When e is considered, u and v are in different components A and B
2. Define cut S = A, V-S = rest of graph
3. e is the minimum weight edge crossing this cut (because edges are sorted and we process in order)
4. By the Cut Property, e is in some MST
5. Therefore, Kruskal's greedy choice is safe

Since Kruskal builds a spanning tree (adds V-1 edges without cycles) containing only MST edges, the result is an MST. ∎

### Complexity Analysis

- **Sorting edges**: O(E log E)
- **Union-Find operations**: O(E · α(V)) where α is inverse Ackermann (practically constant)
- **Total**: O(E log E) dominated by sorting

### Key Properties

1. **Greedy**: Always chooses minimum weight available edge
2. **Correctness**: Guaranteed to find an MST (not just any spanning tree)
3. **Cycle detection**: Union-Find efficiently checks if edge creates cycle
4. **Edge-focused**: Better than Prim's for sparse graphs

---

## Problem 3: Verifying Topological Ordering for Disconnected Graphs

### Problem Statement

Given a directed graph G (possibly disconnected) and an ordering of vertices, verify whether the ordering is a valid topological ordering.

**Requirements**:
- A topological ordering is valid if for every directed edge (u, v), u appears before v in the ordering
- The graph must be a DAG (Directed Acyclic Graph) - no cycles
- For disconnected graphs, we can order vertices from different components arbitrarily

### Solution Algorithm

```python
def verify_topological_order(graph, ordering):
    """
    Verify if given ordering is a valid topological ordering.

    Args:
        graph: dict of {node: [list of neighbors]}
               Directed edges: node → neighbor
        ordering: list of vertices in proposed topological order

    Returns:
        True if valid topological ordering, False otherwise

    Time: O(V + E)
    Space: O(V)
    """
    # Create position map: O(V)
    position = {node: i for i, node in enumerate(ordering)}

    # Check all vertices are included
    if set(position.keys()) != set(graph.keys()):
        return False  # Missing vertices or extra vertices

    # Check all edges respect the ordering: O(E)
    for u in graph:
        for v in graph[u]:  # For each edge u → v
            if position[u] >= position[v]:
                # u appears after or at same position as v: INVALID
                return False

    return True


def is_valid_topological_order_with_details(graph, ordering):
    """
    Verify topological ordering with detailed feedback.

    Returns:
        (is_valid, violated_edges)
    """
    position = {node: i for i, node in enumerate(ordering)}

    if set(position.keys()) != set(graph.keys()):
        missing = set(graph.keys()) - set(position.keys())
        extra = set(position.keys()) - set(graph.keys())
        return False, f"Missing: {missing}, Extra: {extra}"

    violated = []
    for u in graph:
        for v in graph[u]:
            if position[u] >= position[v]:
                violated.append((u, v, position[u], position[v]))

    if violated:
        return False, violated

    return True, []
```

### Example: Disconnected Graph

```
Graph (two components):

Component 1:        Component 2:
    0 → 1               3 → 4
    ↓   ↓               ↓
    2 → 5               6

Adjacency list:
{
    0: [1, 2],
    1: [5],
    2: [5],
    3: [4, 6],
    4: [],
    5: [],
    6: []
}
```

**Valid orderings**:
- `[0, 1, 2, 5, 3, 4, 6]` ✓
- `[3, 0, 4, 1, 6, 2, 5]` ✓
- `[0, 2, 1, 5, 3, 6, 4]` ✓
- `[3, 4, 6, 0, 1, 2, 5]` ✓ (entire component 2 before component 1)

**Invalid orderings**:
- `[1, 0, 2, 5, 3, 4, 6]` ✗ (1 before 0, but 0→1 exists)
- `[0, 5, 1, 2, 3, 4, 6]` ✗ (5 before 1, but 1→5 exists)
- `[0, 1, 2, 3, 6, 4, 5]` ✗ (6 before 4, but 3→4 exists)

### Testing Implementation

```python
def test_topological_verification():
    # Disconnected graph example
    graph = {
        0: [1, 2],
        1: [5],
        2: [5],
        3: [4, 6],
        4: [],
        5: [],
        6: []
    }

    # Test valid orderings
    valid_orders = [
        [0, 1, 2, 5, 3, 4, 6],
        [3, 0, 4, 1, 6, 2, 5],
        [0, 2, 1, 5, 3, 6, 4],
        [3, 4, 6, 0, 1, 2, 5]
    ]

    for order in valid_orders:
        result = verify_topological_order(graph, order)
        print(f"Order {order}: {result}")
        assert result == True, f"Should be valid: {order}"

    # Test invalid orderings
    invalid_orders = [
        [1, 0, 2, 5, 3, 4, 6],      # 1 before 0
        [0, 5, 1, 2, 3, 4, 6],      # 5 before 1
        [0, 1, 2, 3, 6, 4, 5],      # 6 before 4
        [0, 1, 2, 5, 6, 3, 4]       # 6 before 3
    ]

    for order in invalid_orders:
        result, details = is_valid_topological_order_with_details(graph, order)
        print(f"Order {order}: {result}")
        if not result:
            print(f"  Violated edges: {details}")
        assert result == False, f"Should be invalid: {order}"


def generate_topological_order(graph):
    """
    Generate a valid topological ordering using DFS.
    Works for disconnected graphs.

    Time: O(V + E)
    """
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)  # Add to stack after visiting all descendants

    # Process all components
    for node in graph:
        if node not in visited:
            dfs(node)

    return stack[::-1]  # Reverse to get topological order
```

### Key Insights for Disconnected Graphs

1. **Components are independent**: Vertices from different strongly connected components can be ordered arbitrarily relative to each other

2. **Within-component ordering matters**: Within each component, the topological constraints must be respected

3. **Verification is O(V + E)**:
   - Build position map: O(V)
   - Check all edges: O(E)
   - No need to identify components separately

4. **Multiple valid orderings**: A DAG typically has many valid topological orderings, especially if disconnected

### Common Mistakes

**Mistake 1**: Assuming a unique topological ordering
- Reality: Most DAGs have multiple valid orderings
- Disconnected graphs have even more freedom

**Mistake 2**: Trying to verify by generating a topological order and comparing
- Problem: Graph might have different valid orderings
- Solution: Check edge constraints directly

**Mistake 3**: Forgetting to check all vertices are included
- Must verify ordering contains exactly the vertices in the graph

**Mistake 4**: Assuming graph is connected
- Disconnected graphs are valid DAGs
- Need to handle all components

### Practice Questions

1. **Counting**: How many valid topological orderings exist for the example disconnected graph above?

2. **Generation**: Write an algorithm to generate all possible topological orderings for a given DAG.

3. **Unique ordering**: Under what conditions does a DAG have exactly one topological ordering?

4. **Cycle detection**: Modify the verification algorithm to detect if the graph contains a cycle.

5. **Partial order**: Given a partial topological ordering (only some vertices), determine which vertices can legally come next.

---

## Practice Questions

1. **Modified Problem**: What if weak edges take 0 days but strong edges take 2 days? How does the algorithm change?

2. **Proof Question**: Prove that 0-1 BFS correctly finds shortest paths for graphs with edge weights {0, 1}.

3. **Implementation**: Modify the algorithm to return the infection path (sequence of nodes) that takes the longest time.

4. **Analysis**: Why can't we use standard BFS for this problem? Provide a counterexample.

5. **Extension**: If some computers have antivirus (cannot be infected), how would you modify the algorithm?

---

## Key Takeaways

- **Graph representation**: Crucial for algorithm selection
- **Edge weights matter**: Different weights require different algorithms
- **0-1 BFS**: Efficient O(V+E) solution for binary edge weights
- **Relaxation**: Essential for finding optimal paths with varying weights
- **Multi-source shortest path**: Natural extension of single-source algorithms
- **Deque operations**: Enable optimal complexity for {0, 1} weights

This problem tests understanding of:
- Graph traversal algorithms
- Shortest path algorithms
- Algorithm optimization for special cases
- Complexity analysis