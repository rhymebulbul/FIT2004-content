# Disconnected Graphs: Complete Algorithm Checklist

## Quick Reference

**Connected Graph**: A graph where there is a path between every pair of vertices.

**Disconnected Graph**: A graph with 2+ separate connected components (no paths between components).

**Key Insight**: Most graph algorithms are designed assuming connected graphs. Understanding their behavior on disconnected graphs is CRITICAL for exams.

---

## Complete Algorithm Compatibility Matrix

**IMPORTANT NOTE**: This checklist focuses on **GRAPH ALGORITHMS ONLY**. Non-graph algorithms (sorting, selection, dynamic programming on arrays/strings, etc.) do NOT operate on graphs and therefore the concept of "disconnected graphs" does NOT apply to them.

### ✅ Algorithms That Operate on Graphs (Covered in This Document)

**Graph Traversal & Connectivity:**
- DFS, BFS, Connected Components, Strongly Connected Components

**Shortest Paths:**
- BFS (unweighted), Dijkstra, Bellman-Ford, Floyd-Warshall, Johnson's, SPFA

**Minimum Spanning Tree:**
- Prim's Algorithm, Kruskal's Algorithm

**DAG Algorithms:**
- Topological Sort (Kahn's & DFS), Critical Path, Transitive Closure (Warshall), Path Counting, Transitive Reduction, DAG String Matching

**Network Flow:**
- Ford-Fulkerson, Bipartite Matching, Circulation with Demands

**Data Structures for Graphs:**
- Union-Find (Disjoint Set)

**Cycle Detection:**
- Undirected graphs, Directed graphs, Negative cycles

---

### ❌ Algorithms That Do NOT Operate on Graphs (Not Covered Here)

**Sorting Algorithms** - Operate on arrays/lists, not graphs:
- Merge Sort, Quick Sort, Heap Sort, Selection Sort, Insertion Sort, Counting Sort, Radix Sort, Timsort

**Selection Algorithms** - Operate on arrays, not graphs:
- QuickSelect, Median of Medians

**Partition Algorithms** - Operate on arrays, not graphs:
- Hoare's Partition, Dutch National Flag

**String/Array Dynamic Programming** - Not graph-based:
- Edit Distance, Longest Common Subsequence, Coin Change, Knapsack (0/1 & Unbounded), Matrix Chain Multiplication

**Number Theory/Mathematical Algorithms** - Not graph-based:
- Karatsuba Multiplication, Binary Search, Euclid's Algorithm, Strassen's Matrix Multiplication, FFT

**Note**: These algorithms don't operate on graphs, so asking "does this work on disconnected graphs?" is meaningless for them.

---

## GRAPH ALGORITHMS: Compatibility Matrix

### Traversal & Basic Algorithms

| Algorithm | Works on Disconnected? | Modifications | Output Behavior |
|-----------|------------------------|---------------|-----------------|
| **DFS** | ✅ YES | Add outer loop | Explores one component per call |
| **BFS** | ✅ YES | Add outer loop | Explores one component per call |
| **Finding Connected Components** | ✅ YES | Designed for this! | Returns all components |
| **Strongly Connected Components** | ✅ YES | Add outer loop | Finds SCCs in each component |

### Shortest Path Algorithms

| Algorithm | Works on Disconnected? | Modifications | Output Behavior |
|-----------|------------------------|---------------|-----------------|
| **BFS (unweighted shortest paths)** | ⚠️ PARTIAL | Run from each component | Unreachable vertices = ∞ |
| **Dijkstra** | ⚠️ PARTIAL | Run from each component | Unreachable vertices = ∞ |
| **Bellman-Ford** | ⚠️ PARTIAL | Run from each component | Unreachable vertices = ∞ |
| **Floyd-Warshall** | ✅ YES | None needed | dist[u][v] = ∞ for different components |
| **Johnson's Algorithm** | ✅ YES | None needed | Handles all components automatically |
| **SPFA** | ⚠️ PARTIAL | Run from each component | Unreachable vertices = ∞ |

### MST Algorithms

| Algorithm | Works on Disconnected? | Modifications | Output Behavior |
|-----------|------------------------|---------------|-----------------|
| **Prim's MST** | ❌ NO | Run on each component | Creates MST for ONE component only |
| **Kruskal's MST** | ✅ YES | None needed | Creates MSF (Minimum Spanning Forest) |

### DAG Algorithms

| Algorithm | Works on Disconnected? | Modifications | Output Behavior |
|-----------|------------------------|---------------|-----------------|
| **Topological Sort (Kahn's)** | ✅ YES | None needed | Orders all vertices across components |
| **Topological Sort (DFS)** | ✅ YES | Add outer loop | Orders all vertices across components |
| **Critical Path (Longest Path in DAG)** | ✅ YES | Add outer loop | Finds longest path in each component |
| **Transitive Closure (Warshall)** | ✅ YES | None needed | Shows reachability within components |
| **Transitive Reduction** | ✅ YES | None needed | Reduces edges within each component |
| **Path Counting in DAG** | ⚠️ PARTIAL | Must specify endpoints | Counts paths within same component |
| **DAG String Matching** | ⚠️ PARTIAL | Must specify endpoints | Matches within same component |

### Network Flow Algorithms

| Algorithm | Works on Disconnected? | Modifications | Output Behavior |
|-----------|------------------------|---------------|-----------------|
| **Ford-Fulkerson (Max Flow)** | ⚠️ DEPENDS | Requires s-t path | No flow if s and t in different components |
| **Bipartite Matching** | ✅ YES | None needed | Finds matching within each bipartite component |
| **Circulation with Demands** | ⚠️ DEPENDS | Components must be self-sufficient | Each component must satisfy ΣD=0 independently |

### Data Structures & Other

| Algorithm | Works on Disconnected? | Modifications | Output Behavior |
|-----------|------------------------|---------------|-----------------|
| **Union-Find** | ✅ YES | None needed | Naturally handles multiple components |
| **Cycle Detection (Undirected)** | ✅ YES | Add outer loop | Checks all components for cycles |
| **Cycle Detection (Directed)** | ✅ YES | Add outer loop | Checks all components for cycles |
| **Negative Cycle Detection** | ⚠️ PARTIAL | Run from all vertices | Detects cycles in each component |

---

## Detailed Analysis by Algorithm Category

## 1. GRAPH TRAVERSAL ALGORITHMS

### 1.1 Depth-First Search (DFS)

```
Works on Disconnected: ✅ YES
Modifications: Add outer loop through all unvisited vertices
Time Complexity: O(V + E) - SAME for connected and disconnected
```

**Standard Connected Version:**
```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited
```

**Disconnected Version (explores ALL components):**
```python
def dfs_all_components(graph):
    visited = set()
    for vertex in graph:
        if vertex not in visited:
            dfs(graph, vertex, visited)  # Explores one component
    return visited
```

**Key Points:**
- Single DFS call explores exactly ONE connected component
- To traverse entire disconnected graph: outer loop through all vertices
- Number of DFS calls initiated = number of connected components
- Complexity remains O(V + E) even with outer loop

**Applications:**
- Connected components
- Cycle detection
- Topological sorting
- Path finding within a component

---

### 1.2 Breadth-First Search (BFS)

```
Works on Disconnected: ✅ YES
Modifications: Add outer loop through all unvisited vertices
Time Complexity: O(V + E) - SAME for connected and disconnected
```

**Standard Connected Version:**
```python
def bfs(graph, start):
    visited = set([start])
    queue = [start]
    while queue:
        u = queue.pop(0)
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                queue.append(v)
    return visited
```

**Disconnected Version:**
```python
def bfs_all_components(graph):
    visited = set()
    for vertex in graph:
        if vertex not in visited:
            queue = [vertex]
            while queue:
                u = queue.pop(0)
                if u not in visited:
                    visited.add(u)
                    for v in graph[u]:
                        if v not in visited:
                            queue.append(v)
    return visited
```

**Key Points:**
- Same behavior as DFS for disconnected graphs
- Each BFS call explores one component
- Need outer loop to process all components

---

### 1.3 Finding Connected Components

```
Works on Disconnected: ✅ YES
Modifications: NONE - this is the PRIMARY use case!
Time Complexity: O(V + E)
```

**Implementation:**
```python
def find_connected_components(graph):
    visited = set()
    components = []
    component_id = {}

    for vertex in graph:
        if vertex not in visited:
            component = set()
            dfs(graph, vertex, component)  # Discovers one component
            visited.update(component)
            components.append(component)

            # Assign component ID to all vertices
            comp_num = len(components) - 1
            for v in component:
                component_id[v] = comp_num

    return components, component_id
```

**Output:**
- List of sets, each containing vertices in one component
- Component ID mapping for quick lookup
- Number of components = len(components)

**Key Points:**
- Designed specifically for disconnected graphs
- Each DFS/BFS call discovers exactly one component
- Fundamental algorithm for detecting disconnection

---

### 1.4 Strongly Connected Components (Directed Graphs)

```
Works on Disconnected: ✅ YES
Modifications: Add outer loop (algorithms handle this naturally)
Time Complexity: O(V + E)
```

**Kosaraju's Algorithm:**
```python
def kosaraju_scc(graph):
    # Step 1: DFS on original graph to get finish times
    visited = set()
    stack = []

    def dfs1(v):
        visited.add(v)
        for u in graph[v]:
            if u not in visited:
                dfs1(u)
        stack.append(v)  # Post-order

    # Run DFS on all unvisited vertices
    for v in graph:
        if v not in visited:
            dfs1(v)

    # Step 2: DFS on transpose graph in reverse finish order
    transpose = {v: [] for v in graph}
    for v in graph:
        for u in graph[v]:
            transpose[u].append(v)

    visited.clear()
    sccs = []

    while stack:
        v = stack.pop()
        if v not in visited:
            scc = set()
            dfs(transpose, v, scc)
            sccs.append(scc)
            visited.update(scc)

    return sccs
```

**Key Points:**
- Finds strongly connected components in directed graphs
- Works on disconnected graphs via outer loops
- SCC condensation creates DAG of components

---

## 2. SHORTEST PATH ALGORITHMS

### 2.1 BFS for Unweighted Shortest Paths

```
Works on Disconnected: ⚠️ PARTIAL
Modifications: Accept that unreachable vertices have distance ∞
Time Complexity: O(V + E) - only explores source's component
```

**Implementation:**
```python
def bfs_shortest_paths(graph, source):
    dist = {v: float('inf') for v in graph}
    pred = {v: None for v in graph}
    dist[source] = 0

    queue = [source]

    while queue:
        u = queue.pop(0)
        for v in graph[u]:
            if dist[v] == float('inf'):  # Unvisited
                dist[v] = dist[u] + 1
                pred[v] = u
                queue.append(v)

    return dist, pred
```

**Behavior on Disconnected Graphs:**
- Only computes distances to vertices in source's component
- Vertices in other components: `dist[v] = ∞`, `pred[v] = None`
- This is CORRECT behavior, not an error!

**Detection of Unreachable Vertices:**
```python
dist, pred = bfs_shortest_paths(graph, 'A')
unreachable = [v for v in dist if dist[v] == float('inf')]
# unreachable contains all vertices in different components from A
```

**To Get Shortest Paths Between All Pairs:**
```python
# Option 1: Run BFS from each vertex
all_pairs = {}
for v in graph:
    all_pairs[v] = bfs_shortest_paths(graph, v)

# Option 2: Find components first, run within each
components = find_connected_components(graph)
for comp in components:
    # Run BFS within this component only
    pass
```

**Key Points:**
- Single BFS only explores source's component
- Unreachable vertices correctly reported as distance ∞
- Time complexity O(V + E) but only visits reachable vertices

---

### 2.2 Dijkstra's Algorithm

```
Works on Disconnected: ⚠️ PARTIAL
Modifications: Accept unreachable vertices at distance ∞
Time Complexity: O((V + E) log V) - but only processes source's component
Weight Requirement: Non-negative weights only
```

**Implementation from w5/dijkstra.py:**
```python
def dijkstra(graph, source):
    dist = {v: float('inf') for v in graph}
    pred = {v: None for v in graph}
    dist[source] = 0

    pq = [(0, source)]
    visited = set()

    while pq:
        d, u = heapq.heappop(pq)

        if u in visited:
            continue
        visited.add(u)

        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                pred[v] = u
                heapq.heappush(pq, (dist[v], v))

    return dist, pred
```

**Behavior on Disconnected Graphs:**
- Priority queue only processes vertices reachable from source
- Vertices in other components never added to visited set
- Final distances: source component = computed, other components = ∞

**Example:**
```python
graph = {
    'A': [('B', 5), ('C', 3)],
    'B': [('C', 1)],
    'C': [],
    'D': [('E', 2)],  # Different component
    'E': []
}

dist, pred = dijkstra(graph, 'A')
# dist['A'] = 0
# dist['B'] = 5
# dist['C'] = 3
# dist['D'] = ∞  (different component)
# dist['E'] = ∞  (different component)
```

**Detecting Disconnection:**
```python
dist, pred = dijkstra(graph, source)
num_reachable = sum(1 for d in dist.values() if d != float('inf'))
is_disconnected = num_reachable < len(graph)
```

**Key Points:**
- Algorithm completes successfully with incomplete results
- Check `dist[v] == ∞` to identify unreachable vertices
- Vertices in different components correctly remain at ∞
- Total work done: O((|reachable V| + |reachable E|) log V)

---

### 2.3 Bellman-Ford Algorithm

```
Works on Disconnected: ⚠️ PARTIAL
Modifications: Accept unreachable vertices at distance ∞
Time Complexity: O(V × E) - processes ALL edges but only updates reachable vertices
Weight Requirement: Any weights, detects negative cycles
```

**Implementation:**
```python
def bellman_ford(graph, source):
    dist = {v: float('inf') for v in graph}
    pred = {v: None for v in graph}
    dist[source] = 0

    # Relax all edges V-1 times
    for i in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u]:
                if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    pred[v] = u

    # Check for negative cycles reachable from source
    for u in graph:
        for v, weight in graph[u]:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                return None  # Negative cycle detected

    return dist, pred
```

**Behavior on Disconnected Graphs:**
- Processes ALL edges in the graph (even unreachable ones)
- Only updates distances for vertices reachable from source
- Relaxation condition `dist[u] != ∞` prevents updates to unreachable vertices

**Negative Cycle Detection:**
- Only detects negative cycles **reachable from source**
- Negative cycles in other components are NOT detected

**To Detect All Negative Cycles:**
```python
def detect_all_negative_cycles(graph):
    # Add artificial source connected to all vertices
    augmented = {v: graph[v].copy() for v in graph}
    augmented['__source__'] = [(v, 0) for v in graph]

    result = bellman_ford(augmented, '__source__')
    return result is None  # True if any negative cycle exists
```

**Key Points:**
- Algorithm runs in O(V × E) time even for disconnected graphs
- Only finds negative cycles reachable from source
- Unreachable vertices remain at ∞ (correct behavior)
- Less efficient than Dijkstra when no negative weights exist

---

### 2.4 Floyd-Warshall Algorithm

```
Works on Disconnected: ✅ YES
Modifications: NONE - handles disconnected graphs perfectly
Time Complexity: O(V³) - SAME for connected and disconnected
Weight Requirement: Any weights, detects all negative cycles
```

**Implementation:**
```python
def floyd_warshall(graph):
    vertices = list(graph.keys())
    dist = {u: {v: float('inf') for v in vertices} for u in vertices}

    # Initialize distances
    for v in vertices:
        dist[v][v] = 0
    for u in graph:
        for v, weight in graph[u]:
            dist[u][v] = weight

    # Dynamic programming: try each vertex as intermediate
    for k in vertices:
        for u in vertices:
            for v in vertices:
                if dist[u][k] + dist[k][v] < dist[u][v]:
                    dist[u][v] = dist[u][k] + dist[k][v]

    return dist
```

**Behavior on Disconnected Graphs:**
- Computes shortest paths between ALL pairs of vertices
- Pairs in different components: `dist[u][v] = ∞` (no path exists)
- Pairs in same component: `dist[u][v] = shortest path weight`

**Example:**
```python
# Graph with two components: {A,B} and {C,D}
graph = {
    'A': [('B', 3)],
    'B': [],
    'C': [('D', 5)],
    'D': []
}

dist = floyd_warshall(graph)
# dist['A']['B'] = 3  (same component)
# dist['A']['C'] = ∞  (different components)
# dist['A']['D'] = ∞  (different components)
# dist['C']['D'] = 5  (same component)
```

**Negative Cycle Detection:**
```python
def has_negative_cycle(dist):
    for v in dist:
        if dist[v][v] < 0:
            return True
    return False

# Detects ALL negative cycles, not just from one source
```

**Key Points:**
- BEST algorithm for all-pairs shortest paths on disconnected graphs
- No modifications needed - handles naturally
- dist[u][v] = ∞ correctly indicates different components
- Detects ALL negative cycles (any vertex v with dist[v][v] < 0)

---

### 2.5 Johnson's Algorithm

```
Works on Disconnected: ✅ YES
Modifications: NONE - artificial source handles all components
Time Complexity: O(V² log V + VE) - better than Floyd-Warshall for sparse graphs
Weight Requirement: Any weights (reweights to make non-negative)
```

**Algorithm Steps:**
1. Add artificial source s' with 0-weight edges to all vertices
2. Run Bellman-Ford from s' to compute potentials h[v] for all v
3. Reweight edges: w'(u,v) = w(u,v) + h[u] - h[v]
4. Run Dijkstra from each vertex on reweighted graph
5. Recover true distances by adjusting for potentials

**Why It Works on Disconnected Graphs:**
- Artificial source connects to ALL vertices (even in different components)
- Potentials computed for ALL vertices via Bellman-Ford
- Each Dijkstra run operates on its component
- Final distances correctly show ∞ for different components

**Implementation Sketch:**
```python
def johnsons(graph):
    # Add artificial source
    vertices = list(graph.keys())
    augmented = {v: graph[v].copy() for v in vertices}
    augmented['__s__'] = [(v, 0) for v in vertices]

    # Compute potentials with Bellman-Ford
    h = bellman_ford(augmented, '__s__')
    if h is None:
        return None  # Negative cycle exists

    # Reweight edges
    reweighted = {}
    for u in graph:
        reweighted[u] = []
        for v, w in graph[u]:
            w_new = w + h[u] - h[v]
            reweighted[u].append((v, w_new))

    # Run Dijkstra from each vertex
    all_pairs = {}
    for u in vertices:
        dist_u = dijkstra(reweighted, u)
        # Recover true distances
        for v in vertices:
            dist_u[v] = dist_u[v] - h[u] + h[v]
        all_pairs[u] = dist_u

    return all_pairs
```

**Key Points:**
- Artificial source connects all components
- More efficient than Floyd-Warshall for sparse graphs: O(V² log V) vs O(V³)
- Handles disconnected graphs without special cases
- Detects negative cycles via Bellman-Ford step

---

### 2.6 SPFA (Shortest Paths Faster Algorithm)

```
Works on Disconnected: ⚠️ PARTIAL
Modifications: Same as Bellman-Ford - accept unreachable = ∞
Time Complexity: O(VE) worst case, better average case
Weight Requirement: Any weights
```

**Implementation:**
```python
def spfa(graph, source):
    dist = {v: float('inf') for v in graph}
    pred = {v: None for v in graph}
    in_queue = {v: False for v in graph}
    count = {v: 0 for v in graph}  # For negative cycle detection

    dist[source] = 0
    queue = [source]
    in_queue[source] = True

    while queue:
        u = queue.pop(0)
        in_queue[u] = False
        count[u] += 1

        # Negative cycle detection
        if count[u] >= len(graph):
            return None  # Negative cycle reachable from source

        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                pred[v] = u
                if not in_queue[v]:
                    queue.append(v)
                    in_queue[v] = True

    return dist, pred
```

**Behavior on Disconnected Graphs:**
- Queue only contains vertices in source's component
- Vertices in other components never enqueued
- Unreachable vertices remain at ∞

**Key Points:**
- Optimization of Bellman-Ford for average case
- Same behavior as Bellman-Ford on disconnected graphs
- Only explores source's component

---

## 3. MINIMUM SPANNING TREE ALGORITHMS

### 3.1 Prim's Algorithm

```
Works on Disconnected: ❌ NO (creates MST for one component only)
Modifications: Must run separately on each component to create MSF
Time Complexity: O(E log V) per component
Weight Requirement: Non-negative weights
```

**Implementation from w5/prim.py:**
```python
def prim(graph, start):
    visited = set()
    mst_edges = []
    total_weight = 0
    pq = []

    visited.add(start)
    for v, w in graph[start]:
        heapq.heappush(pq, (w, start, v))

    while pq and len(visited) < len(graph):
        w, u, v = heapq.heappop(pq)
        if v in visited:
            continue

        visited.add(v)
        mst_edges.append((u, v, w))
        total_weight += w

        for to, wt in graph[v]:
            if to not in visited:
                heapq.heappush(pq, (wt, v, to))

    return mst_edges, total_weight
```

**Behavior on Disconnected Graphs:**
- Algorithm only spans vertices in start vertex's component
- Priority queue exhausts when no more edges reach unvisited vertices IN THAT COMPONENT
- Result: MST for ONE component, NOT entire graph

**Example:**
```python
graph = {
    'A': [('B', 5), ('C', 3)],
    'B': [('A', 5), ('C', 1)],
    'C': [('A', 3), ('B', 1)],
    'D': [('E', 2)],  # Different component
    'E': [('D', 2)]
}

mst, weight = prim(graph, 'A')
# mst = [('A', 'C', 3), ('C', 'B', 1)]  - only spanning A, B, C
# len(mst) = 2, but connected graph with 5 vertices would have 4 edges
```

**Detection of Disconnection:**
```python
mst_edges, weight = prim(graph, start)
is_disconnected = len(mst_edges) < len(graph) - 1

# Connected graph: |MST edges| = |V| - 1
# Disconnected graph: |MST edges| < |V| - 1
```

**Creating Minimum Spanning Forest:**
```python
def prim_msf(graph):
    """Create MSF for disconnected graph"""
    visited = set()
    all_mst_edges = []
    total_weight = 0
    num_components = 0

    for vertex in graph:
        if vertex not in visited:
            # Run Prim on this component
            mst_edges, weight = prim(graph, vertex)
            all_mst_edges.extend(mst_edges)
            total_weight += weight
            num_components += 1

            # Mark all vertices in this component as visited
            for u, v, w in mst_edges:
                visited.add(u)
                visited.add(v)

    return all_mst_edges, total_weight, num_components
```

**Key Points:**
- Single Prim call creates MST for ONE component only
- Must run on each component separately for full MSF
- Check `len(mst_edges) == |V| - 1` to verify connectivity
- Number of edges in MST for k-vertex component = k - 1

---

### 3.2 Kruskal's Algorithm

```
Works on Disconnected: ✅ YES
Modifications: NONE - naturally creates Minimum Spanning Forest
Time Complexity: O(E log E) = O(E log V) - SAME for connected and disconnected
Weight Requirement: Non-negative weights
```

**Implementation from w5/kruskal.py:**
```python
def kruskal(graph):
    # Extract all edges
    edges = []
    for u in graph:
        for v, w in graph[u]:
            if (v, u, w) not in edges:  # Avoid duplicates
                edges.append((u, v, w))

    # Sort edges by weight
    edges.sort(key=lambda x: x[2])

    # Initialize Union-Find
    uf = UnionFind(graph.keys())

    mst_edges = []
    total_weight = 0

    # Process edges in increasing weight order
    for u, v, w in edges:
        if uf.union(u, v):  # If u and v in different components
            mst_edges.append((u, v, w))
            total_weight += w
        if len(mst_edges) == len(graph) - 1:  # Early termination
            break

    return mst_edges, total_weight
```

**Why It Works on Disconnected Graphs:**
- Edge-centric approach processes ALL edges regardless of connectivity
- Union-Find tracks which vertices are in which component
- Naturally stops when no more edges can connect components
- Result is Minimum Spanning Forest automatically

**Example:**
```python
graph = {
    'A': [('B', 5), ('C', 3)],
    'B': [('A', 5), ('C', 1)],
    'C': [('A', 3), ('B', 1)],
    'D': [('E', 2)],  # Different component
    'E': [('D', 2)]
}

mst, weight = kruskal(graph)
# mst = [('B', 'C', 1), ('D', 'E', 2), ('A', 'C', 3)]
# Spans all vertices: A-B-C in one tree, D-E in another tree
# len(mst) = 3 = |V| - |components| = 5 - 2
```

**Detecting Number of Components:**
```python
mst_edges, weight = kruskal(graph)
num_components = len(graph) - len(mst_edges)

# Connected graph (k=1): |MST| = |V| - 1
# Disconnected graph (k components): |MSF| = |V| - k
```

**Key Properties:**
- No modifications needed for disconnected graphs
- Creates one spanning tree per component (Minimum Spanning Forest)
- Number of edges in MSF = |V| - (number of components)
- Union-Find naturally prevents cycles within and across components

**Why Kruskal > Prim for Disconnected Graphs:**
- Kruskal: Works out of box, single pass through sorted edges
- Prim: Needs component detection + separate run on each component

---

## 4. TOPOLOGICAL SORTING ALGORITHMS

### 4.1 Kahn's Algorithm (Queue-based)

```
Works on Disconnected: ✅ YES
Modifications: NONE - processes all sources across all components
Time Complexity: O(V + E) - SAME for connected and disconnected
Graph Requirement: DAG (Directed Acyclic Graph)
```

**Implementation:**
```python
def kahns_topological_sort(graph):
    # Compute in-degrees
    indegree = {v: 0 for v in graph}
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1

    # Initialize queue with ALL sources (indegree 0)
    queue = [v for v in graph if indegree[v] == 0]
    result = []

    while queue:
        u = queue.pop(0)
        result.append(u)

        # Remove edges from u
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    # Cycle detection
    if len(result) != len(graph):
        return None  # Cycle detected

    return result
```

**Behavior on Disconnected DAGs:**
- Initial queue contains sources from ALL components
- Algorithm processes vertices from all components
- Relative order between components is arbitrary but valid
- Each component's internal ordering is correct

**Example:**
```python
# Two separate components
graph = {
    'A': ['B'],
    'B': ['C'],
    'C': [],
    'D': ['E'],  # Different component
    'E': []
}

result = kahns_topological_sort(graph)
# Possible: ['A', 'D', 'B', 'E', 'C']
# Possible: ['D', 'A', 'E', 'B', 'C']
# Both valid! A before B before C, and D before E, but inter-component order arbitrary
```

**Key Points:**
- Works perfectly on disconnected DAGs
- Produces valid total ordering across all components
- Multiple valid orderings possible
- Inter-component ordering is arbitrary

---

### 4.2 DFS-based Topological Sort

```
Works on Disconnected: ✅ YES
Modifications: Add outer loop through all unvisited vertices
Time Complexity: O(V + E) - SAME for connected and disconnected
Graph Requirement: DAG
```

**Implementation:**
```python
def dfs_topological_sort(graph):
    visited = set()
    stack = []

    def dfs(u):
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                dfs(v)
        stack.append(u)  # Post-order: add AFTER processing all descendants

    # Process all unvisited vertices (handles all components)
    for v in graph:
        if v not in visited:
            dfs(v)

    return stack[::-1]  # Reverse post-order
```

**Why Outer Loop Is Critical:**
- Without outer loop: only processes one component
- With outer loop: processes all components
- Each DFS call adds one component's vertices to stack

**Example with Two Components:**
```python
graph = {
    'A': ['B'],
    'B': [],
    'C': ['D'],  # Different component
    'D': []
}

# Without outer loop (starting from 'A'):
# Result: ['A', 'B'] - missing C and D!

# With outer loop:
# Result: ['A', 'B', 'C', 'D'] or ['C', 'D', 'A', 'B']
# Both valid!
```

**Key Points:**
- MUST have outer loop for disconnected graphs
- Reverse post-order gives valid topological ordering
- Each component processed in correct internal order
- Inter-component order depends on vertex iteration order

---

## 5. DAG-SPECIFIC ALGORITHMS

### 5.1 Critical Path / Longest Path in DAG

```
Works on Disconnected: ✅ YES
Modifications: Add outer loop for all unvisited vertices
Time Complexity: O(V + E)
Graph Requirement: DAG only (longest path undefined for cyclic graphs)
```

**DP Formulation:**
- State: longest[u] = length of longest path starting at u
- Base case: longest[v] = 0 for vertices with no outgoing edges
- Recurrence: longest[u] = max over v∈adj[u] of (w(u,v) + longest[v])

**Implementation (Reverse Topological Order):**
```python
def longest_path_dag(graph):
    # Step 1: Get topological sort
    topo_order = dfs_topological_sort(graph)

    # Step 2: DP in reverse topological order
    longest = {v: 0 for v in graph}
    pred = {v: None for v in graph}

    for u in reversed(topo_order):
        for v, weight in graph[u]:
            if weight + longest[v] > longest[u]:
                longest[u] = weight + longest[v]
                pred[u] = v

    return longest, pred
```

**Behavior on Disconnected DAGs:**
- Topological sort handles all components (with outer loop)
- DP processes all vertices across all components
- Longest path computed for each component separately
- Global longest path = max(longest[v] for v in graph)

**Key Points:**
- Only works on DAGs (longest path NP-hard for general graphs)
- Disconnected: compute longest path in each component
- Negative weights allowed (unlike Dijkstra)

---

### 5.2 Transitive Closure (Warshall's Algorithm)

```
Works on Disconnected: ✅ YES
Modifications: NONE
Time Complexity: O(V³) - SAME for connected and disconnected
```

**DP Formulation:**
- State: reachable[u][v] after k iterations = true iff path u→v exists using intermediates {1...k}
- Base case: reachable[u][v] = true for edges, reachable[v][v] = true
- Recurrence: reachable[u][v] = reachable[u][v] OR (reachable[u][k] AND reachable[k][v])

**Implementation:**
```python
def warshalls_algorithm(graph):
    vertices = list(graph.keys())
    reachable = {u: {v: False for v in vertices} for u in vertices}

    # Initialize: direct edges and self-loops
    for v in vertices:
        reachable[v][v] = True
    for u in graph:
        for v in graph[u]:
            reachable[u][v] = True

    # Dynamic programming
    for k in vertices:
        for u in vertices:
            for v in vertices:
                reachable[u][v] = reachable[u][v] or \
                                   (reachable[u][k] and reachable[k][v])

    return reachable
```

**Behavior on Disconnected Graphs:**
- Computes reachability within each component
- Pairs in different components: reachable[u][v] = False
- Pairs in same component: reachable[u][v] = True if path exists

**Key Points:**
- No modifications needed for disconnected graphs
- Output correctly shows component structure
- Can identify components by checking reachable[u][v] for all pairs

---

### 5.3 Path Counting in DAGs

```
Works on Disconnected: ⚠️ PARTIAL
Modifications: Must specify source and destination
Time Complexity: O(V + E)
```

**DP Formulation:**
- State: count[u] = number of paths from u to destination t
- Base case: count[t] = 1
- Recurrence: count[u] = sum of count[v] for all neighbors v

**Implementation:**
```python
def count_paths_dag(graph, source, dest):
    # Topological sort
    topo_order = dfs_topological_sort(graph)

    # DP in reverse topological order
    count = {v: 0 for v in graph}
    count[dest] = 1

    for u in reversed(topo_order):
        if u == dest:
            continue
        for v in graph[u]:
            count[u] += count[v]

    return count[source]
```

**Behavior on Disconnected Graphs:**
- If source and dest in same component: returns path count
- If source and dest in different components: returns 0 (no paths)

**Key Points:**
- Must specify endpoints
- Works correctly for disconnected graphs (returns 0 if no path)

---

### 5.4 Transitive Reduction

```
Works on Disconnected: ✅ YES
Modifications: NONE
Time Complexity: O(V² + V·E)
```

**Definition:** Find the minimal edge set that preserves reachability (remove redundant edges).

**DP Formulation:**
- First compute transitive closure (reachability)
- Remove edge (u,v) if path u→v exists through intermediate vertices

**Implementation:**
```python
def transitive_reduction(graph):
    # Step 1: Compute transitive closure
    reachable = warshalls_algorithm(graph)

    # Step 2: Remove redundant edges
    reduced = {v: [] for v in graph}

    for u in graph:
        for v in graph[u]:
            # Check if u can reach v through another path
            is_redundant = False
            for w in graph:
                if w != u and w != v:
                    if reachable[u][w] and reachable[w][v]:
                        is_redundant = True
                        break

            if not is_redundant:
                reduced[u].append(v)

    return reduced
```

**Behavior on Disconnected Graphs:**
- Operates independently on each component
- Edges within a component are reduced to minimal set
- No edges between components (as in original graph)

**Example:**
```python
# Graph with transitive edge
graph = {
    'A': ['B', 'C'],  # A→C is redundant if A→B→C exists
    'B': ['C'],
    'C': [],
    'D': ['E'],  # Different component
    'E': []
}

reduced = transitive_reduction(graph)
# Result: A→B, B→C (removed A→C), D→E
# Each component reduced independently
```

**Key Points:**
- Works on disconnected DAGs without modification
- Each component reduced to minimal edge set
- Preserves reachability within components

---

### 5.5 DAG String Matching

```
Works on Disconnected: ⚠️ PARTIAL
Modifications: Must specify source and target
Time Complexity: O((V+E)·n) where n = string length
```

**Problem:** Count paths in DAG that spell a specific string.

**DP Formulation:**
- State: DP[u, i] = number of paths from u that spell S[i..n]
- Base case: DP[v, n] = 1 if we've spelled entire string
- Recurrence: DP[u, i] = sum of DP[v, i+1] for all edges (u,v) where edge label = S[i]

**Implementation Sketch:**
```python
def dag_string_matching(graph, source, target_string):
    n = len(target_string)
    topo_order = dfs_topological_sort(graph)

    # DP[u][i] = paths from u spelling target_string[i:]
    DP = {u: [0] * (n + 1) for u in graph}

    # Base case: empty string always matched
    for u in graph:
        DP[u][n] = 1

    # Fill in reverse topological order
    for u in reversed(topo_order):
        for i in range(n - 1, -1, -1):
            for v, edge_label in graph[u]:  # Assume edges have labels
                if edge_label == target_string[i]:
                    DP[u][i] += DP[v][i + 1]

    return DP[source][0]
```

**Behavior on Disconnected Graphs:**
- If source and target in same component: counts matching paths
- If source and target in different components: returns 0

**Key Points:**
- Requires labeled edges (each edge has a character)
- Source and target must be in same component for non-zero result
- Returns 0 if no path exists (disconnected components)

---

## 6. NETWORK FLOW ALGORITHMS

### 6.1 Ford-Fulkerson / Max Flow

```
Works on Disconnected: ⚠️ DEPENDS
Modifications: Requires path from source to sink
Time Complexity: O(E·|f*|) where f* is max flow
```

**Problem:** Find maximum flow from source s to sink t.

**Algorithm:**
1. Initialize flow = 0
2. While augmenting path exists from s to t:
   - Find augmenting path using BFS (Edmonds-Karp) or DFS
   - Compute bottleneck capacity
   - Update flow along path
3. Return total flow

**Behavior on Disconnected Graphs:**
- If s and t in **same component**: algorithm works normally
- If s and t in **different components**: NO augmenting path exists, max flow = 0

**Example:**
```python
# Flow network with disconnected components
graph = {
    's': [('a', 10), ('b', 5)],
    'a': [('t', 10)],
    'b': [('t', 5)],
    't': [],
    'x': [('y', 100)],  # Different component
    'y': []
}

max_flow = ford_fulkerson(graph, 's', 't')  # Works: returns 15
max_flow = ford_fulkerson(graph, 's', 'y')  # No path: returns 0
```

**Key Points:**
- Requires s-t connectivity for non-zero flow
- Check if s and t in same component before running
- Use BFS to detect if path exists: O(V + E)

---

### 6.2 Bipartite Matching

```
Works on Disconnected: ✅ YES
Modifications: NONE - finds matching in each component
Time Complexity: O(V·E) using Ford-Fulkerson
```

**Problem:** Maximum matching in bipartite graph G = (L ∪ R, E).

**Reduction to Max Flow:**
1. Direct all edges from L to R
2. Add source s with edges to all L vertices (capacity 1)
3. Add sink t with edges from all R vertices (capacity 1)
4. Run Ford-Fulkerson
5. Matching size = max flow value

**Behavior on Disconnected Bipartite Graphs:**
- Each component's bipartite matching computed independently
- Total matching = sum of matchings in each component
- Algorithm naturally handles multiple components

**Example:**
```python
# Bipartite graph with two components
L = ['L1', 'L2', 'L3']
R = ['R1', 'R2', 'R3']

edges = [
    ('L1', 'R1'), ('L1', 'R2'),  # Component 1
    ('L2', 'R1'),
    ('L3', 'R3')  # Component 2 (separate)
]

matching = bipartite_matching(L, R, edges)
# Finds: L1→R1, L2→R2 (or L1→R2, L2→R1), L3→R3
# Total matching size = 3
```

**Key Points:**
- Works perfectly on disconnected bipartite graphs
- Source s connects to ALL L vertices (even in different components)
- Each component contributes to total matching independently

---

### 6.3 Circulation with Demands

```
Works on Disconnected: ⚠️ DEPENDS
Modifications: Each component must satisfy ΣD = 0
Time Complexity: O(Max-Flow complexity)
```

**Problem:** Determine if flow can satisfy all node demands.

**Constraints:**
- Capacity: 0 ≤ f(e) ≤ c(e)
- Demand: Σf(e_in) - Σf(e_out) = d(u) for each vertex u
- **Necessary condition:** Σ(all demands) = 0

**Behavior on Disconnected Graphs:**
- **Each component must independently satisfy ΣD = 0**
- Cannot transfer flow between components

**Example:**
```python
# Two components
graph = {
    'A': [('B', 10)],  # Component 1
    'B': [],
    'C': [('D', 5)],   # Component 2
    'D': []
}

demands = {
    'A': -5,   # Supply
    'B': +5,   # Demand (Component 1: Σ = 0 ✓)
    'C': -3,   # Supply
    'D': +3    # Demand (Component 2: Σ = 0 ✓)
}

# Feasible: each component balances independently

demands_bad = {
    'A': -10,  # Supply
    'B': +5,   # Demand (Component 1: Σ = -5 ✗)
    'C': -3,   # Supply
    'D': +8    # Demand (Component 2: Σ = +5 ✗)
}

# NOT feasible: components don't balance
```

**Reduction to Max Flow:**
1. Add super-source s and super-sink t
2. For each vertex u with d(u) < 0 (supply): add edge s→u with capacity |d(u)|
3. For each vertex u with d(u) > 0 (demand): add edge u→t with capacity d(u)
4. Check if all s→u and u→t edges are saturated in max flow

**Key Points:**
- Each disconnected component must satisfy ΣD = 0 independently
- Pre-check: verify balance in each component before running
- Use connected components algorithm to identify components first

---

## 7. CYCLE DETECTION ALGORITHMS

### 7.1 Cycle Detection in Undirected Graphs (DFS)

```
Works on Disconnected: ✅ YES
Modifications: Add outer loop to check all components
Time Complexity: O(V + E)
```

**Implementation:**
```python
def has_cycle_undirected(graph):
    visited = set()

    def dfs(u, parent):
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                if dfs(v, u):
                    return True
            elif v != parent:  # Back edge (not reverse edge)
                return True
        return False

    # Check all components
    for v in graph:
        if v not in visited:
            if dfs(v, None):
                return True

    return False
```

**Why Outer Loop Is Needed:**
- Graph could have cycle in any component
- Must check ALL components to ensure no cycles exist
- Early termination when cycle found in any component

**Key Points:**
- Must check all components
- A graph is acyclic only if ALL components are acyclic

---

### 7.2 Cycle Detection in Directed Graphs (DFS with Colors)

```
Works on Disconnected: ✅ YES
Modifications: Add outer loop to check all components
Time Complexity: O(V + E)
```

**Implementation:**
```python
def has_cycle_directed(graph):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {v: WHITE for v in graph}

    def dfs(u):
        color[u] = GRAY  # Currently being processed
        for v in graph[u]:
            if color[v] == GRAY:  # Back edge = cycle
                return True
            if color[v] == WHITE:
                if dfs(v):
                    return True
        color[u] = BLACK  # Finished processing
        return False

    # Check all components
    for v in graph:
        if color[v] == WHITE:
            if dfs(v):
                return True

    return False
```

**Color Meanings:**
- WHITE: Unvisited
- GRAY: In current DFS path (visiting)
- BLACK: Completely processed (visited)

**Key Points:**
- GRAY vertex encountered = back edge = cycle
- Must check all components via outer loop

---

### 7.3 Negative Cycle Detection (Bellman-Ford)

```
Works on Disconnected: ⚠️ PARTIAL
Modifications: Run from artificial source to detect ALL negative cycles
Time Complexity: O(V × E)
```

**Standard Bellman-Ford:**
- Only detects negative cycles reachable from specified source
- Cycles in other components NOT detected

**Detecting All Negative Cycles:**
```python
def has_any_negative_cycle(graph):
    # Add artificial source connected to all vertices
    augmented = {v: graph[v].copy() for v in graph}
    augmented['__source__'] = [(v, 0) for v in graph]

    # Run Bellman-Ford from artificial source
    result = bellman_ford(augmented, '__source__')

    return result is None  # None indicates negative cycle
```

**Key Points:**
- Single-source Bellman-Ford: only checks source's component
- Artificial source: connects all components, detects all cycles
- Floyd-Warshall better for detecting all negative cycles

---

### 7.4 Negative Cycle Detection (Floyd-Warshall)

```
Works on Disconnected: ✅ YES
Modifications: NONE
Time Complexity: O(V³)
```

**Detection Method:**
```python
dist = floyd_warshall(graph)

# Check diagonal for negative values
for v in dist:
    if dist[v][v] < 0:
        print(f"Negative cycle involving vertex {v}")
```

**Key Points:**
- Detects ALL negative cycles in ALL components
- No artificial source needed (unlike Bellman-Ford)
- dist[v][v] < 0 indicates v is in a negative cycle

---

## 8. UNION-FIND DATA STRUCTURE

```
Works on Disconnected: ✅ YES
Modifications: NONE - specifically designed for tracking components!
Time Complexity: O(α(n)) ≈ O(1) per operation with optimizations
```

**Purpose:** Maintain disjoint sets and support:
- FIND(u): Get component representative
- UNION(u, v): Merge components

**Implementation from w5/unionFind.py:**
```python
class UnionFind:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])  # Path compression
        return self.parent[v]

    def union(self, u, v):
        root_u, root_v = self.find(u), self.find(v)
        if root_u == root_v:
            return False  # Already in same set

        # Union by rank
        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1
        return True
```

**Applications with Disconnected Graphs:**

**1. Check if vertices in same component:**
```python
uf = UnionFind(graph.keys())

if uf.find(u) == uf.find(v):
    print("u and v are connected")
else:
    print("u and v are in different components")
```

**2. Count number of components:**
```python
num_components = len(set(uf.find(v) for v in graph))
```

**3. Kruskal's algorithm cycle detection:**
```python
for u, v, w in edges:
    if uf.union(u, v):  # Different components - no cycle
        mst_edges.append((u, v, w))
    # else: same component - would create cycle
```

**Key Points:**
- Designed SPECIFICALLY for disconnected graphs
- Each component has unique root representative
- Nearly O(1) operations with path compression + union by rank
- Essential for Kruskal's algorithm

---

## SUMMARY: COMPREHENSIVE COMPATIBILITY TABLE

### Single-Source Algorithms (Process One Component)

| Algorithm | Status | Unreachable Vertices | What To Do |
|-----------|--------|---------------------|------------|
| DFS | ✅ YES (with loop) | Not visited | Loop through all vertices |
| BFS | ✅ YES (with loop) | Not visited | Loop through all vertices |
| BFS Shortest Paths | ⚠️ PARTIAL | dist = ∞ | Accept ∞ or run on each component |
| Dijkstra | ⚠️ PARTIAL | dist = ∞ | Accept ∞ or run on each component |
| Bellman-Ford | ⚠️ PARTIAL | dist = ∞ | Accept ∞ or run on each component |
| SPFA | ⚠️ PARTIAL | dist = ∞ | Accept ∞ or run on each component |
| Prim's MST | ❌ NO | Not spanned | Run on each component separately |

### All-Pairs Algorithms (Process All Components)

| Algorithm | Status | Different Components | Notes |
|-----------|--------|---------------------|-------|
| Floyd-Warshall | ✅ YES | dist[u][v] = ∞ | Perfect for disconnected graphs |
| Johnson's | ✅ YES | dist[u][v] = ∞ | Artificial source handles all |
| Warshall (Transitive Closure) | ✅ YES | reachable = false | Shows connectivity |

### Edge-Based Algorithms

| Algorithm | Status | Behavior | Notes |
|-----------|--------|----------|-------|
| Kruskal's MST | ✅ YES | Creates MSF | Best MST algorithm for disconnected graphs |

### DAG Algorithms

| Algorithm | Status | Modification | Notes |
|-----------|--------|--------------|-------|
| Kahn's Topological Sort | ✅ YES | None | Processes all sources |
| DFS Topological Sort | ✅ YES | Outer loop | Must loop through all vertices |
| Critical Path | ✅ YES | Outer loop | Finds longest in each component |
| Transitive Reduction | ✅ YES | None | Reduces each component independently |
| Path Counting | ⚠️ PARTIAL | None | Returns 0 if endpoints in different components |
| DAG String Matching | ⚠️ PARTIAL | None | Returns 0 if endpoints in different components |

### Network Flow Algorithms

| Algorithm | Status | Modification | Notes |
|-----------|--------|--------------|-------|
| Ford-Fulkerson (Max Flow) | ⚠️ DEPENDS | Requires s-t path | Returns 0 if s and t in different components |
| Bipartite Matching | ✅ YES | None | Finds matching in each component independently |
| Circulation with Demands | ⚠️ DEPENDS | Each component must balance | Each component must satisfy ΣD = 0 |

### Cycle Detection

| Algorithm | Status | Modification | Notes |
|-----------|--------|--------------|-------|
| DFS (Undirected) | ✅ YES | Outer loop | Check all components |
| DFS (Directed) | ✅ YES | Outer loop | Check all components |
| Bellman-Ford | ⚠️ PARTIAL | Artificial source | Only checks reachable from source |
| Floyd-Warshall | ✅ YES | None | Checks all components |

### Data Structures

| Structure | Status | Purpose | Notes |
|-----------|--------|---------|-------|
| Union-Find | ✅ YES | Track components | DESIGNED for disconnected graphs |

---

## KEY FORMULAS FOR DISCONNECTED GRAPHS

**Number of Components:**
```
k = number of connected components
|V| = total vertices
|E| = total edges
```

**For Minimum Spanning Forest:**
```
|MSF edges| = |V| - k
```

**Example:**
- 10 vertices, 3 components
- MSF will have 10 - 3 = 7 edges

**For Each Component:**
- Component i has |Vi| vertices
- MST of component i has |Vi| - 1 edges

**Detecting Disconnection via MST:**
```python
mst_edges = kruskal(graph) or prim(graph, start)
num_components = len(graph) - len(mst_edges)
is_connected = (num_components == 1)
```

---

## EXAM STRATEGY CHECKLIST

### Before Running Any Algorithm:

**1. Check if graph is connected**
- [ ] Does problem statement say "connected graph"?
- [ ] If not mentioned, assume potentially disconnected

**2. Identify algorithm type**
- [ ] Single-source (DFS, BFS, Dijkstra, Bellman-Ford, Prim)
- [ ] All-pairs (Floyd-Warshall, Johnson's)
- [ ] Edge-based (Kruskal)
- [ ] DAG-specific (Topological sort, critical path)

**3. Determine modifications needed**
- [ ] Single-source traversal: Add outer loop
- [ ] Single-source shortest path: Accept dist = ∞ or run per component
- [ ] Prim: Run on each component OR use Kruskal
- [ ] Kruskal: No modification needed
- [ ] Floyd-Warshall: No modification needed

**4. Understand output behavior**
- [ ] Shortest paths: Unreachable = ∞
- [ ] MST: Expect MSF with |V| - k edges
- [ ] Traversal: Only visits one component without outer loop
- [ ] All-pairs: ∞ or false for different components

---

## COMMON EXAM MISTAKES TO AVOID

**1. Assuming connectivity without verification**
- Always check if problem states "connected"
- If not stated, consider disconnected case

**2. Running Dijkstra and expecting complete results**
- dist[v] = ∞ means unreachable, NOT error
- Check which vertices are reachable

**3. Running Prim once and calling it MST**
- Verify: len(mst_edges) == |V| - 1?
- If less: graph is disconnected

**4. Forgetting outer loop in DFS/BFS**
- Single call explores ONE component only
- Need: `for v in graph: if v not in visited: dfs(v)`

**5. Miscounting components**
- After Kruskal: k = |V| - |MSF edges|
- After DFS: k = number of DFS calls initiated

**6. Using wrong algorithm for disconnected graphs**
- DON'T use Prim without component detection
- DO use Kruskal for MST on disconnected graphs
- DO use Floyd-Warshall for all-pairs on disconnected graphs

---

## QUICK DECISION TREE

**Need to traverse entire disconnected graph?**
- → DFS or BFS with outer loop

**Need shortest paths?**
- Single-source → Dijkstra/Bellman-Ford, accept ∞ for unreachable
- All-pairs → Floyd-Warshall (perfect for disconnected)

**Need MST?**
- → Use Kruskal (automatic MSF)
- → OR find components first, then Prim on each

**Need topological sort?**
- → Kahn's (automatic) or DFS-based (with outer loop)

**Need to count components?**
- → Run DFS with outer loop, count initiations
- → OR run Kruskal, compute |V| - |MSF edges|
- → OR use Union-Find

**Need to detect cycles?**
- → DFS with outer loop (check all components)

**Need connectivity queries?**
- → Use Union-Find data structure

---

## COMPLEXITY ANALYSIS ON DISCONNECTED GRAPHS

**Key Insight:** Most algorithms have SAME complexity on disconnected graphs!

| Algorithm | Connected | Disconnected | Difference |
|-----------|-----------|--------------|------------|
| DFS | O(V + E) | O(V + E) | None |
| BFS | O(V + E) | O(V + E) | None |
| Dijkstra | O((V+E) log V) | O((V+E) log V)* | *Only processes one component |
| Bellman-Ford | O(VE) | O(VE) | None |
| Floyd-Warshall | O(V³) | O(V³) | None |
| Prim | O(E log V) | O(E log V) per component | ×k for k components |
| Kruskal | O(E log E) | O(E log E) | None |
| Topological | O(V + E) | O(V + E) | None |

**Note:** Dijkstra technically runs in same time but only processes reachable portion.

---

## FINAL RECOMMENDATIONS

**For Exam Success:**

1. **Always check connectivity**
   - Not mentioned = assume potentially disconnected

2. **Know which algorithms need modification**
   - Traversal: outer loop
   - MST: use Kruskal OR run Prim per component
   - Single-source shortest path: accept ∞

3. **Recognize disconnection in output**
   - dist[v] = ∞ (shortest paths)
   - |MST edges| < |V| - 1 (spanning tree)
   - Vertices not visited (traversal)

4. **Use right algorithm for the job**
   - MST on disconnected → Kruskal
   - All-pairs on disconnected → Floyd-Warshall
   - Component tracking → Union-Find

5. **Master these detection methods**
   - Run DFS, count visited
   - Run Kruskal, check edge count
   - After Dijkstra, check for ∞ distances

---

## PRACTICE QUESTIONS

**Q1:** You run Prim's from vertex A and get 7 edges. Graph has 10 vertices. How many components?

<details>
<summary>Answer</summary>

**3 components**

Reasoning:
- Prim's created MST for one component with 8 vertices (7 edges = 8 - 1)
- Remaining 2 vertices must be in other component(s)
- Minimum: 1 additional component with 2 vertices
- More likely: 2 additional components with 1 vertex each
- Total: 1 (size 8) + 2 (size 1 each) = 3 components

To find exact number: need to run Prim on other components or use Kruskal.
</details>

**Q2:** Can Kruskal detect disconnection? How?

<details>
<summary>Answer</summary>

**YES**

Method:
```python
mst_edges = kruskal(graph)
num_components = len(graph) - len(mst_edges)
is_connected = (num_components == 1)
```

Connected graph: |MSF| = |V| - 1
Disconnected with k components: |MSF| = |V| - k
</details>

**Q3:** Dijkstra from A gives dist['Z'] = ∞. Is Z unreachable?

<details>
<summary>Answer</summary>

**YES** (assuming non-negative weights)

dist[v] = ∞ means no path from A to v exists.
Z is in a different connected component from A.
This is CORRECT behavior, not an error!
</details>

**Q4:** When do you need outer loop for DFS?

<details>
<summary>Answer</summary>

**Depends on goal:**

- **Explore one component:** No outer loop needed
  - `dfs(graph, start, visited)`

- **Explore ALL components:** Outer loop required
  ```python
  for v in graph:
      if v not in visited:
          dfs(graph, v, visited)
  ```

- **Count components:** Outer loop required
  - Count = number of times DFS initiated
</details>

**Q5:** Which MST algorithm is better for disconnected graphs?

<details>
<summary>Answer</summary>

**KRUSKAL**

Reasons:
1. **No modification needed** - creates MSF automatically
2. **Single pass** - processes all edges once
3. **Natural detection** - |MSF edges| reveals component count

Prim requires:
1. Detecting components first
2. Running separately on each component
3. More complex implementation

Exception: If components already known and you need MST for specific component, Prim is fine.
</details>

**Q6:** Floyd-Warshall on disconnected graph: what is dist[u][v] for u, v in different components?

<details>
<summary>Answer</summary>

**dist[u][v] = ∞**

This correctly indicates no path exists between u and v.
Floyd-Warshall handles disconnected graphs perfectly without modification.
</details>

**Q7:** Topological sort on disconnected DAG: does it work?

<details>
<summary>Answer</summary>

**YES**

Both algorithms work:

1. **Kahn's:** No modification needed
   - Initial queue has sources from ALL components

2. **DFS-based:** Needs outer loop
   ```python
   for v in graph:
       if v not in visited:
           dfs(v)
   ```

Result: Valid total ordering across all components.
Inter-component order is arbitrary but valid.
</details>

**Q8:** How to count components using Union-Find?

<details>
<summary>Answer</summary>

```python
uf = UnionFind(graph.keys())

# Union all edges
for u in graph:
    for v in graph[u]:
        uf.union(u, v)

# Count unique roots
num_components = len(set(uf.find(v) for v in graph))
```

Each unique root = one component.
</details>

---

## CONDENSED REFERENCE CARD

### ✅ WORKS WITHOUT MODIFICATION:
**MST & Spanning:**
- Kruskal (creates MSF automatically)

**All-Pairs Algorithms:**
- Floyd-Warshall (∞ for different components)
- Johnson's (artificial source handles all)
- Warshall's transitive closure (false for different components)

**DAG Algorithms:**
- Kahn's topological sort (processes all sources)
- Transitive Reduction (reduces each component)

**Data Structures:**
- Union-Find (designed for components)

**Matching:**
- Bipartite Matching (matches within components)

---

### ⚠️ NEEDS OUTER LOOP:
**Traversal:**
- DFS (for full traversal)
- BFS (for full traversal)

**DAG Algorithms:**
- DFS topological sort
- Critical path in DAG

**Cycle Detection:**
- Undirected graphs (DFS)
- Directed graphs (DFS with colors)

**Component Finding:**
- Connected components (by design)
- Strongly connected components

---

### ❌ NEEDS PER-COMPONENT EXECUTION:
- Prim's MST (OR just use Kruskal instead)

---

### 📊 WORKS BUT INCOMPLETE RESULTS:
**Single-Source Shortest Paths:**
- Dijkstra (unreachable = ∞)
- Bellman-Ford (unreachable = ∞)
- BFS shortest paths (unreachable = ∞)
- SPFA (unreachable = ∞)

**DAG Path Problems:**
- Path Counting (returns 0 if endpoints in different components)
- DAG String Matching (returns 0 if endpoints in different components)

---

### 🔀 DEPENDS ON PROBLEM:
**Network Flow:**
- Ford-Fulkerson / Max Flow (requires s-t path; returns 0 if different components)
- Circulation with Demands (each component must satisfy ΣD = 0 independently)

**Cycle Detection:**
- Negative Cycle Detection with Bellman-Ford (only detects in reachable component; use artificial source for all)

---

### 📐 DETECTION FORMULAS:
```
Number of components k:

After Kruskal:     k = |V| - |MSF edges|
After DFS:         k = number of DFS initiations
After Prim:        k ≥ 2 if |MST edges| < |V| - 1
After Union-Find:  k = number of unique roots

Disconnection indicators:
- Dijkstra: vertices with dist = ∞
- BFS: unvisited vertices after traversal
- Floyd-Warshall: pairs with dist[u][v] = ∞
```

---

### 🎯 GOLDEN RULES:

1. **Check connectivity assumption**
   - If problem doesn't say "connected", assume potentially disconnected

2. **Choose right algorithm for disconnected graphs**
   - MST → Use Kruskal (not Prim)
   - All-pairs shortest paths → Use Floyd-Warshall
   - Component tracking → Use Union-Find

3. **Understand output meanings**
   - dist = ∞ is CORRECT for unreachable vertices (not an error!)
   - |MST edges| < |V| - 1 indicates disconnection
   - Unvisited vertices = different component

4. **Modify traversal algorithms**
   - Always add outer loop for DFS/BFS to process all components
   - Count loop initiations to get component count

5. **Verify preconditions for flow problems**
   - Max Flow: check if s and t in same component
   - Circulation: verify each component satisfies ΣD = 0

---

### 🚫 ALGORITHMS NOT IN THIS GUIDE:
These operate on arrays/strings, NOT graphs:
- Sorting (Merge, Quick, Heap, Counting, Radix, Selection, Insertion)
- Selection (QuickSelect, Median of Medians)
- Partition algorithms
- Array/String DP (Edit Distance, LCS, Knapsack, Coin Change)
- Number Theory (Karatsuba, Binary Search, Euclid's GCD)
