# Graph Operations Complexity Cheatsheet

## Quick Reference Table

| Operation | Adjacency Matrix | Adjacency List (Unsorted) | Notes |
|-----------|-----------------|---------------------------|-------|
| **Edge Existence Check** | | | |
| Check if edge (u,v) exists | Θ(1) | Θ(N(u)) | Matrix: direct array access; List: linear search |
| Check if BOTH (u,v) AND (v,u) exist | Θ(1) | Θ(V) | List: worst case when both have many neighbors |
| **Neighbor Operations** | | | |
| Get all outgoing edges from u | Θ(V) | Θ(1) to access, Θ(N(u)) to iterate | Matrix: scan row; List: direct access to list |
| Get all incoming edges to u | Θ(V) | Θ(V+E) | Matrix: scan column; List: scan ALL adjacency lists |
| Print all outgoing edges from u | Θ(V) | Θ(N(u)) | |
| Sum weights of incoming edges to u | Θ(V) | Θ(V+E) | Must examine all potential sources |
| **Degree Calculations** | | | |
| Compute out-degree of u | Θ(V) | Θ(1) | List: just length of u's list |
| Compute in-degree of u | Θ(V) | Θ(V+E) | List: must scan all adjacency lists |
| Compute in-degree of ALL vertices | Θ(V²) | Θ(V+E) | List: one pass through all edges |
| Find max degree in graph | Θ(V²) | Θ(V+E) | Iterate vertices + scan edges |
| **Graph Traversal** | | | |
| BFS from vertex u | Θ(V²) | Θ(V+E) | Matrix: check all V neighbors per vertex |
| DFS from vertex u | Θ(V²) | Θ(V+E) | Same as BFS |
| Complete traversal (all components) | Θ(V²) | Θ(V+E) | Standard graph traversal complexity |

## Key Complexity Patterns

### Pattern 1: Outgoing vs Incoming Edges

**Outgoing Edges (edges FROM vertex u):**
- **Adjacency Matrix**: Θ(V) - scan the entire row for vertex u
- **Adjacency List**: Θ(N(u)) - directly access u's list and iterate

**Incoming Edges (edges TO vertex u):**
- **Adjacency Matrix**: Θ(V) - scan the entire column for vertex u
- **Adjacency List**: Θ(V+E) - must scan ALL vertices' adjacency lists looking for u

**Why the difference?**
- Adjacency lists only store outgoing edges explicitly
- To find incoming edges, must check every other vertex's outgoing edges

### Pattern 2: Edge Existence Checks

**Single Edge Check (u → v):**
- **Adjacency Matrix**: Θ(1) - direct access: `matrix[u][v]`
- **Adjacency List**: Θ(N(u)) - linear search through u's unsorted neighbor list

**Bidirectional Check (u → v AND v → u):**
- **Adjacency Matrix**: Θ(1) - check both `matrix[u][v]` and `matrix[v][u]`
- **Adjacency List**: Θ(N(u) + N(v)) = Θ(V) worst case - search both lists

**Important**: If lists were **sorted**, binary search would give Θ(log N(u))

### Pattern 3: Degree Calculations

**Out-Degree (number of outgoing edges):**
```
Adjacency Matrix: Θ(V)  - count non-zero entries in row
Adjacency List:   Θ(1)  - just the length of the adjacency list
```

**In-Degree (number of incoming edges):**
```
Adjacency Matrix: Θ(V)    - count non-zero entries in column
Adjacency List:   Θ(V+E)  - scan all adjacency lists
```

**All In-Degrees:**
```python
# Adjacency Matrix: Θ(V²)
for each vertex u:
    in_degree[u] = count non-zero in column u  # Θ(V)

# Adjacency List: Θ(V+E)
in_degree = [0] * V                    # Θ(V)
for each vertex u:                     # Θ(V)
    for each neighbor v in adj[u]:     # Total Θ(E) across all iterations
        in_degree[v] += 1
```

**Key Insight**: Computing all in-degrees with adjacency list is Θ(V+E) because each edge is examined exactly once.

### Pattern 4: Graph Traversal (BFS/DFS)

**Why BFS/DFS differ between representations:**

**Adjacency Matrix: Θ(V²)**
```python
visited = [False] * V
queue = [start]
while queue:                        # Θ(V) iterations
    u = queue.pop(0)
    for v in range(V):              # Θ(V) - check ALL possible neighbors
        if matrix[u][v] and not visited[v]:
            queue.append(v)
            visited[v] = True
# Total: V vertices × V checks = Θ(V²)
```

**Adjacency List: Θ(V+E)**
```python
visited = [False] * V
queue = [start]
while queue:                        # Θ(V) iterations
    u = queue.pop(0)
    for v in adj[u]:                # Only actual neighbors
        if not visited[v]:
            queue.append(v)
            visited[v] = True
# Total: V vertices + E edges examined = Θ(V+E)
```

**Key Insight**:
- Matrix: Must check all V positions for each vertex (even if no edge exists)
- List: Only examine actual edges, so work is proportional to E

## Common Question Types

### Type 1: "Determine if edge exists"
**Recognition**: "Check if there is an edge from u to v"

**Solution Template**:
- Adjacency Matrix → Θ(1) [direct array access]
- Adjacency List (unsorted) → Θ(N(u)) [linear search]
- Adjacency List (sorted) → Θ(log N(u)) [binary search]

### Type 2: "Get all incoming/outgoing edges"
**Recognition**: "Obtain all edges pointing to/from vertex u"

**Solution Template**:
```
OUTGOING edges from u:
  - Matrix: Θ(V) [scan row]
  - List:   Θ(N(u)) [access list]

INCOMING edges to u:
  - Matrix: Θ(V) [scan column]
  - List:   Θ(V+E) [scan all lists]
```

### Type 3: "Compute degree of vertices"
**Recognition**: "Find the in-degree/out-degree"

**Solution Template**:
```
OUT-DEGREE of single vertex:
  - Matrix: Θ(V)
  - List:   Θ(1)

IN-DEGREE of single vertex:
  - Matrix: Θ(V)
  - List:   Θ(V+E)

IN-DEGREE of ALL vertices:
  - Matrix: Θ(V²)
  - List:   Θ(V+E) [ONE pass through all edges]
```

### Type 4: "Perform BFS/DFS"
**Recognition**: "Traverse the graph starting from vertex u"

**Solution Template**:
```
BFS/DFS from single source:
  - Matrix: Θ(V²)
  - List:   Θ(V+E)

Complete traversal (all components):
  - Matrix: Θ(V²)
  - List:   Θ(V+E)
```

## Exam Strategy Checklist

When solving graph complexity questions:

1. ✅ **Identify the graph representation** (adjacency matrix vs adjacency list)
2. ✅ **Check if lists are sorted/unsorted** (affects search complexity)
3. ✅ **Determine operation type**:
   - Edge existence check?
   - Getting neighbors?
   - Computing degrees?
   - Graph traversal?
4. ✅ **Consider direction**:
   - Outgoing edges (FROM vertex) → easier in adjacency list
   - Incoming edges (TO vertex) → easier in adjacency matrix
5. ✅ **Watch for "all vertices" operations**:
   - Computing single in-degree: Θ(V+E) for list
   - Computing ALL in-degrees: Still Θ(V+E) for list!
6. ✅ **Use correct notation**:
   - Use Θ (big-Theta) when asked for tight bounds
   - Use O (big-O) when asked for upper bounds

## Common Mistakes to Avoid

❌ **Mistake 1**: Saying adjacency list incoming edges is Θ(V)
- **Correct**: Θ(V+E) - must scan all adjacency lists, which contain E total edges

❌ **Mistake 2**: Saying BFS on adjacency list is Θ(E)
- **Correct**: Θ(V+E) - must visit all V vertices, even if disconnected

❌ **Mistake 3**: Forgetting N(u) notation
- **When given**: Use Θ(N(u)) for operations on vertex u's neighbors
- **When not given**: Use Θ(V) as worst case (complete graph where N(u) = V-1)

❌ **Mistake 4**: Computing all in-degrees is Θ(V) × Θ(V+E) = Θ(V²+VE)
- **Correct**: Θ(V+E) - one pass through all edges suffices

❌ **Mistake 5**: Forgetting that unsorted lists require linear search
- **Check operation**: Θ(N(u)) not Θ(log N(u))

## Space Complexity Quick Reference

| Representation | Total Space | Auxiliary Space (for algorithms) |
|----------------|-------------|----------------------------------|
| Adjacency Matrix | Θ(V²) | Usually Θ(V) for visited array |
| Adjacency List | Θ(V+E) | Usually Θ(V) for visited array |
| Edge List | Θ(E) | Depends on algorithm |

**Total Space**: Space to store the graph representation
**Auxiliary Space**: Extra space needed by algorithm (not counting input)

## Memory Aids

**"Matrix is Fast but Fat"**
- Fast: O(1) edge lookups
- Fat: O(V²) space even for sparse graphs

**"Lists are Lean but Linear"**
- Lean: O(V+E) space, efficient for sparse graphs
- Linear: O(N(u)) to search for specific edge

**"Incoming is Inconvenient for Lists"**
- Incoming edges require scanning ALL lists: Θ(V+E)
- Outgoing edges are direct: Θ(N(u))

**"One Pass for All In-Degrees"**
- Don't multiply: computing all in-degrees is still Θ(V+E)
- Each edge contributes exactly once to exactly one vertex's in-degree

## Practice Patterns

### Pattern Recognition Flow

```
Question asks about graph operation complexity
    ↓
1. Which representation? → Matrix or List
    ↓
2. Which operation type?
    ↓
    ├─ Edge check?
    │   ├─ Matrix → Θ(1)
    │   └─ List (unsorted) → Θ(N(u))
    │
    ├─ Get neighbors?
    │   ├─ Outgoing → Matrix: Θ(V), List: Θ(N(u))
    │   └─ Incoming → Matrix: Θ(V), List: Θ(V+E)
    │
    ├─ Degree calculation?
    │   ├─ Out-degree → Matrix: Θ(V), List: Θ(1)
    │   └─ In-degree → Matrix: Θ(V), List: Θ(V+E)
    │
    └─ Traversal (BFS/DFS)?
        ├─ Matrix → Θ(V²)
        └─ List → Θ(V+E)
```

## Real Exam Examples

### Example 1: Bidirectional Edge Check
**Question**: "Check if edges A→B AND B→A both exist (adjacency list)"

**Analysis**:
- Need to search A's list for B: Θ(N(A))
- Need to search B's list for A: Θ(N(B))
- Total: Θ(N(A) + N(B))
- Worst case: Θ(V) when both vertices have many neighbors

**Answer**: Θ(V)

### Example 2: Sum of Incoming Edge Weights
**Question**: "Sum total weight of incoming edges to vertex A (adjacency matrix)"

**Analysis**:
- Incoming edges = column A in matrix
- Must scan all V rows, checking column A
- For each edge found, add its weight
- Complexity: Θ(V)

**Answer**: Θ(V)

### Example 3: Computing All In-Degrees
**Question**: "Given adjacency-list of directed graph G=(V,E), compute in-degree of every vertex"

**Analysis**:
```python
in_degree = [0] * V              # Θ(V)
for u in range(V):               # Θ(V)
    for v in adj[u]:             # Total Θ(E) across all u
        in_degree[v] += 1
```
- Initialize array: Θ(V)
- Iterate through all edges once: Θ(E)
- Total: Θ(V+E)

**Answer**: Θ(V+E)

**Common Wrong Answer**: Θ(V) × Θ(V+E) = Θ(V²+VE)
**Why Wrong**: Not iterating V times × (V+E) work. Each edge examined exactly once total.

---

## Final Tips

1. **Always clarify assumptions** from the question:
   - Directed vs undirected?
   - Weighted vs unweighted?
   - Sorted vs unsorted adjacency lists?
   - Connected vs potentially disconnected?

2. **Use N(u) when provided** in the question - don't immediately jump to V

3. **For "all vertices" operations**, think about whether work duplicates or amortizes

4. **Draw small examples** (4-5 vertices) to verify your reasoning

5. **Remember the fundamental costs**:
   - Adjacency matrix: Θ(V²) space, Θ(1) lookup, Θ(V) per row/column
   - Adjacency list: Θ(V+E) space, Θ(N(u)) lookup, Θ(V+E) traversal
