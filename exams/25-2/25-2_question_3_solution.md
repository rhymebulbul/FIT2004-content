# Exam 25-2: Question 3 Solution

**Course:** FIT2004 Algorithms and Data Structures
**Institution:** Monash University
**Topic:** Graph Algorithms - Time Complexity Analysis
**Question Type:** Multiple Select
**Total Marks:** 3

---

## Question Statement

Consider a graph G = (V, E). **Select all true statements.**

**Graph Notation:**
- V: Set of vertices
- E: Set of edges
- Standard graph notation G = (V, E)

### Answer Choices

**a)** In the case the graph is represented using adjacency matrix, the worst-case time complexity to check if there is an edge between vertices u and v is ˜(1).

**b)** In the case the graph is sparse and represented using adjacency matrix, the worst-case time complexity of Dijkstra's algorithm is ˜(|V| log |V|).

**c)** In the case the graph is sparse and represented using adjacency list, the worst-case time complexity of Prim's algorithm is ˜(|V| log |V|).

**d)** In the case the graph is represented using adjacency matrix, the worst-case time complexity of DFS is ˜(|V|+|E|).

---

## My Solution

**Selected Answer: a only**

**Status:**  **CORRECT**
**Marks Awarded:** **1.5/3** (Partial credit)

**Note:** Option (a) is correct, but option (c) is also correct in certain interpretations. Marks deducted for not selecting (c).

---

## Detailed Analysis of Each Option

### Option a: Adjacency Matrix Edge Check - ˜(1)  CORRECT

**Claim:** Edge check between u and v is ˜(1) with adjacency matrix.

**Mathematical Formulation:**
- **Operation:** Edge existence check
- **Representation:** Adjacency Matrix
- **Complexity:** ˜(1)

**Explanation:**
In an adjacency matrix, checking if edge (u,v) exists is a direct array access: `matrix[u][v]`, which is constant time regardless of graph size.

**Implementation:**
```python
# Adjacency matrix representation
adj_matrix = [[0, 1, 0],
              [1, 0, 1],
              [0, 1, 0]]

# Check if edge exists between vertex u and v
def has_edge(u, v):
    return adj_matrix[u][v] == 1  # O(1) array access
```

**Verdict:**  **TRUE** - This is a fundamental property of adjacency matrices.

---

### Option b: Sparse Graph + Adjacency Matrix + Dijkstra = ˜(|V| log |V|)  FALSE

**Claim:** Dijkstra with adjacency matrix on sparse graph is ˜(|V| log |V|).

**Why This is FALSE:**

**Key Insight:** Adjacency matrix representation requires ˜(|V|) time to find all neighbors of each vertex, **regardless of whether the graph is sparse or dense**.

**Analysis:**
```
With adjacency matrix representation:
- To find neighbors of vertex u: scan entire row matrix[u][0...V-1]
- This takes ˜(|V|) time PER VERTEX
- Must do this for all |V| vertices
- Total: ˜(|V|²) regardless of |E|
```

**Dijkstra's Algorithm Complexity by Representation:**

| Implementation | Time Complexity | Notes |
|---------------|-----------------|-------|
| Adjacency matrix + simple array | ˜(|V|²) | Extract-min: O(V), for V vertices |
| Adjacency matrix + binary heap | ˜(|V|² log |V|) | Neighbor scan dominates: O(V²) |
| **Adjacency list + binary heap** | **˜((|V| + |E|) log |V|)** | Efficient for sparse graphs |
| Adjacency list + Fibonacci heap | ˜(|E| + |V| log |V|) | Theoretical optimum |

**Why sparsity doesn't help with adjacency matrix:**
- Sparse graph: |E| << |V|²
- But with adjacency matrix, you still scan all |V| entries per vertex
- You can't "skip" empty entries without checking them
- Result: ˜(|V|²) time regardless of sparsity

**Correct Answer:** ˜(|V|²) or ˜(|V|² log |V|) depending on priority queue implementation

**Verdict:** L **FALSE**

---

### Option c: Sparse Graph + Adjacency List + Prim = ˜(|V| log |V|) ~ CONTEXTUAL

**Claim:** Prim with adjacency list on sparse graph is ˜(|V| log |V|).

**Analysis:**

**Prim's Algorithm with Binary Heap and Adjacency List:**
```
Time Complexity: ˜((|V| + |E|) log |V|)

Breakdown:
- |V| vertex extractions from heap: ˜(|V| log |V|)
- |E| edge relaxations with decrease-key: ˜(|E| log |V|)
- Total: ˜((|V| + |E|) log |V|)
```

**Sparse Graph Definition:**
- **Formal:** |E| = o(|V|²) (little-o notation)
- **Typical:** |E| = ˜(|V|) or |E| = ˜(|V| log |V|)
- **Informal:** |E| is much less than |V|²

**When is the statement TRUE?**

If "sparse" specifically means |E| = ˜(|V|):
```
˜((|V| + |E|) log |V|)
= ˜((|V| + ˜(|V|)) log |V|)
= ˜(|V| log |V|) 
```

**When is the statement FALSE?**

The statement says "worst-case time complexity" - the worst case over ALL sparse graphs could still have |E| approaching |V|², giving:
```
˜((|V| + |E|) log |V|)
= ˜(|V|² log |V|) [if |E| approaches |V|²]
```

**Exam Context:**
- The question likely expects "sparse" to mean |E| = ˜(|V|)
- In that specific case, the statement is TRUE
- The marking scheme awarded partial credit for not selecting this

**Verdict:**  **TRUE** (in the context of |E| = ˜(|V|))

**My Error:** Did not select this option, assuming "worst-case" meant worst over all graph densities.

---

### Option d: Adjacency Matrix + DFS = ˜(|V|+|E|)  FALSE

**Claim:** DFS with adjacency matrix is ˜(|V| + |E|).

**Why This is FALSE:**

**DFS Algorithm Structure:**
```python
def DFS(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)  # Visit vertex: ˜(1)

            # Find all neighbors - REPRESENTATION DEPENDENT!
            for neighbor in graph.neighbors(vertex):
                if neighbor not in visited:
                    stack.append(neighbor)
```

**With Adjacency Matrix:**
```python
# Finding neighbors requires scanning entire row
for v in range(|V|):  # ˜(|V|) iterations
    if adj_matrix[u][v] == 1:  # ˜(1) check
        # Process neighbor
```

**Complexity Analysis:**

| Component | Adjacency Matrix | Adjacency List |
|-----------|-----------------|----------------|
| Visit each vertex | ˜(|V|) | ˜(|V|) |
| Find neighbors per vertex | ˜(|V|) | ˜(degree(v)) |
| **Total** | **˜(|V|²)** | **˜(|V| + |E|)** |

**Detailed Breakdown for Adjacency Matrix:**
```
For each of |V| vertices:
    - Visit vertex: ˜(1)
    - Scan matrix row to find neighbors: ˜(|V|)
    - Total per vertex: ˜(|V|)

Total: |V| × ˜(|V|) = ˜(|V|²)
```

**Why NOT ˜(|V| + |E|)?**
- Must check all |V| potential neighbors for each vertex
- Can't skip non-edges without checking them
- Even if graph has only |E| = |V|-1 edges (a tree), still scan |V|² entries

**Correct Answer:** ˜(|V|²) with adjacency matrix

**Verdict:** L **FALSE**

---

## Key Concepts

### Adjacency Matrix vs Adjacency List

| Aspect | Adjacency Matrix | Adjacency List |
|--------|------------------|----------------|
| **Space** | ˜(|V|²) | ˜(|V| + |E|) |
| **Edge check** | ˜(1) | ˜(degree(v)) |
| **Find all neighbors** | ˜(|V|) | ˜(degree(v)) |
| **Best for** | Dense graphs (|E| H |V|²) | Sparse graphs (|E| << |V|²) |
| **Add edge** | ˜(1) | ˜(1) |
| **Remove edge** | ˜(1) | ˜(degree(v)) |

### Graph Algorithm Complexities

#### Dijkstra's Algorithm

| Representation | Implementation | Time Complexity |
|----------------|----------------|-----------------|
| Adjacency Matrix | Simple array | ˜(|V|²) |
| Adjacency Matrix | Binary heap | ˜(|V|² log |V|) |
| **Adjacency List** | **Binary heap** | **˜((|V| + |E|) log |V|)** |
| Adjacency List | Fibonacci heap | ˜(|E| + |V| log |V|) |

**For sparse graphs (|E| = ˜(|V|)):**
- Adjacency list + binary heap: ˜(|V| log |V|)

#### Prim's Algorithm (MST)

Same complexity structure as Dijkstra:

| Representation | Implementation | Time Complexity |
|----------------|----------------|-----------------|
| Adjacency Matrix | Simple | ˜(|V|²) |
| **Adjacency List** | **Binary heap** | **˜((|V| + |E|) log |V|)** |
| Adjacency List | Fibonacci heap | ˜(|E| + |V| log |V|) |

**For sparse graphs (|E| = ˜(|V|)):**
- Adjacency list + binary heap: ˜(|V| log |V|)

#### DFS and BFS

| Representation | Time Complexity |
|----------------|-----------------|
| Adjacency Matrix | ˜(|V|²) |
| **Adjacency List** | **˜(|V| + |E|)** |

---

## Common Mistakes

### Mistake 1: Confusing adjacency list and matrix complexities
**Error:** Assuming ˜(|V| + |E|) works for both representations
**Correction:** This only applies to adjacency list. Adjacency matrix neighbor finding is always ˜(|V|).

### Mistake 2: Thinking sparsity helps with adjacency matrix
**Error:** Believing sparse graphs with adjacency matrix give better complexity
**Correction:** Adjacency matrix always requires ˜(|V|) to find neighbors, regardless of actual edge count.

### Mistake 3: Not considering "worst-case" carefully
**Error:** Assuming "sparse" means a specific density
**Correction:** "Worst-case" could mean worst over all input graphs, or worst for a given graph structure. Context matters.

### Mistake 4: Forgetting representation affects algorithm choice
**Error:** Using adjacency matrix for all algorithms
**Correction:** Choose representation based on graph density and operations needed.

---

## Edge Cases and Special Conditions

### Complete Graph (Dense)
- **Properties:** |E| = ˜(|V|²)
- **Implications:** Adjacency matrix may be more efficient due to cache locality
- **DFS/BFS:** ˜(|V|²) complexity same for both representations

### Tree or Forest (Sparse)
- **Properties:** |E| = ˜(|V|) or |E| < |V|
- **Implications:** Adjacency list dramatically outperforms matrix for traversal
- **Example:** |V| = 1000, |E| = 999
  - Matrix: scan 1,000,000 entries
  - List: examine only 1,998 edges (each edge appears twice in undirected)

### Disconnected Graph
- **Properties:** May have |E| << |V|
- **Implications:** DFS/BFS must handle multiple components
- **Complexity:** Still depends on representation used

---

## Learning Objectives

1. Understand how graph representation affects algorithm performance
2. Analyze worst-case time complexity for different graph representations
3. Recognize when sparsity affects algorithm complexity
4. Apply complexity analysis to classic graph algorithms (Dijkstra, Prim, DFS)
5. Distinguish between ˜(|V| + |E|) and ˜(|V|²) complexities

---

## Marking Scheme

**Total Marks Available:** 3
**Marks Awarded:** **1.5/3**

**Correct Answers:** a, c
**Student Selected:** a only

**Grading Breakdown:**
- Selected (a):  Correct (+1.5)
- Missed (c):  Should have selected (+0, lost 1.5)
- Correctly rejected (b):  Correct
- Correctly rejected (d):  Correct

**Feedback:** Partially correct. Correctly identified that adjacency matrix allows ˜(1) edge checks, but missed that Prim's with adjacency list on sparse graphs is ˜(|V| log |V|).

---

## Summary Table

| Option | Statement | My Answer | Correct | Explanation |
|--------|-----------|-----------|---------|-------------|
| **a** | Adjacency matrix edge check is ˜(1) |  Selected |  TRUE | Direct array access |
| **b** | Dijkstra + matrix + sparse = ˜(\|V\| log \|V\|) |  Not selected |  FALSE | Still ˜(\|V\|²), matrix always scans all V |
| **c** | Prim + list + sparse = ˜(\|V\| log \|V\|) |  Not selected |  TRUE | When \|E\| = ˜(\|V\|) |
| **d** | DFS + matrix = ˜(\|V\|+\|E\|) |  Not selected |  FALSE | Actually ˜(\|V\|²) |

**Final Score:** 1.5/3

---

## References

1. **topics/GRAPH_COMPLEXITY_EXAM_CHEATSHEET.md**
   - Graph representation complexity comparisons
   - Algorithm complexity by representation

2. **course_notes/** (Graph chapters)
   - Adjacency matrix vs adjacency list properties
   - Graph algorithm implementations

3. **implementations-algorithms/w5/**
   - `dijkstra.py` - Dijkstra implementation with adjacency list
   - `prim.py` - Prim's MST algorithm

4. **Exam file:** exams/25-2/25-2_part1.json (question 3)
   - Original problem with all options analyzed