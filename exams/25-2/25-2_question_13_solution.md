# Question 13 Solution: Evacuation Route Planning

## Problem Statement
Given a directed graph G = (V, E) with two disjoint vertex sets:
- **P**: Set of populated vertices (starting points)
- **S**: Set of safe vertices (ending points)

Find |P| **edge-disjoint paths** from P to S, where:
- Each vertex in P is the starting point of exactly one path
- Each path ends at a vertex in S
- Paths do not share any edges

## Correct Solution

This is a **maximum flow problem with edge-disjoint paths**.

### Algorithm

**Step 1: Graph Transformation**
1. Create a super source `s` connected to all vertices in P
2. Create a super sink `t` connected from all vertices in S
3. Set all edge capacities to 1 (to enforce edge-disjoint property)

**Graph Construction:**
- V' = V ∪ {s, t}
- Add edge (s, v) with capacity 1 for all v ∈ P
- Add edge (v, t) with capacity 1 for all v ∈ S
- All original edges in E get capacity 1

**Step 2: Run Maximum Flow Algorithm**
- Apply Ford-Fulkerson with BFS (Edmonds-Karp), or
- Apply Dinic's algorithm, or
- Apply any max flow algorithm

**Step 3: Check Feasibility and Extract Paths**
- If max_flow_value == |P|: Valid evacuation paths exist
- If max_flow_value < |P|: No valid set exists, return None
- Use flow decomposition to extract the |P| edge-disjoint paths
- Remove super source and sink edges to get paths from P to S

### Correctness

**Why this works:**
- Each edge has capacity 1, so each edge can be used in at most one path (edge-disjoint)
- Each vertex in P has exactly one outgoing edge from super source with capacity 1
- Maximum flow of |P| means we can route exactly one unit from each P vertex to some S vertex
- Flow decomposition guarantees we can extract |P| edge-disjoint paths

**Proof:**
- **Necessity**: If valid paths exist, max flow ≥ |P| (each P vertex sends 1 unit)
- **Sufficiency**: If max flow = |P|, by integer flow property and unit capacities, we can decompose into exactly |P| edge-disjoint paths

### Complexity Analysis

**Graph Transformation:** O(|V| + |E|)
- Adding super source and super sink with edges

**Maximum Flow Computation:**

1. **Edmonds-Karp (BFS):** O(|V| × |E|²)
   - Standard complexity

2. **Dinic's Algorithm:** O(|V|² × |E|)
   - Better for general graphs

3. **Unit Capacity Optimization:** O(|E| × min(|P|, |S|))
   - For unit capacity networks, flow value bounded by min(|P|, |S|)
   - Each augmenting path takes O(|E|) time with BFS/DFS
   - This is the **tightest bound** for this specific problem

**Path Extraction:** O(|V| + |E|)
- Flow decomposition via DFS/BFS traversal

**Overall Best Complexity:** **O(|E| × min(|P|, |S|))**

### Alternative: DFS-Based Approach

Instead of traditional max flow, use modified DFS:
1. Construct super source and super sink as above
2. For each vertex in P, run DFS to find path to S
3. Mark edges as used to ensure edge-disjoint property
4. Keep count of successful paths
5. If count == |P|, return paths; otherwise return None

**Complexity:** O(|P| × (|V| + |E|)) = O(|P| × |E|) for connected graphs
- Each DFS takes O(|V| + |E|)
- Run at most |P| times

**Note:** This is essentially Ford-Fulkerson with DFS for finding augmenting paths.

## Related Applied Problems

This solution is based on **Week 9 Applied Problem 6: Edge-Disjoint Paths**

### Key Insight from Applied Problem 6
"Given a directed graph, determine the maximum number of edge-disjoint paths from vertex s to vertex t by:
- Creating a flow network with all edges having capacity 1
- Running maximum flow algorithm
- The resulting flow value equals the number of edge-disjoint paths"

### Adaptation for Question 13
- Instead of single source/sink, we have sets P and S
- Solution: Add super source and super sink to reduce to single source/sink problem
- Same unit capacity principle applies

## Common Mistakes

1. **Not using super source/sink**: Trying to find paths individually from each P vertex
2. **Forgetting unit capacities**: Capacities ensure edge-disjoint property
3. **Incomplete complexity analysis**: Not recognizing unit capacity optimization
4. **Confusing edge-disjoint with vertex-disjoint**: This problem allows shared vertices, just not shared edges

## Grading Rubric (5 marks)

**Algorithm Description (2 marks):**
- Super source/sink construction (0.5)
- Unit capacity assignment (0.5)
- Max flow algorithm specification (0.5)
- Path extraction method (0.5)

**Correctness (1.5 marks):**
- Correct identification of edge-disjoint paths problem (0.5)
- Proper use of unit capacities (0.5)
- Correct feasibility check (flow == |P|) (0.5)

**Complexity Analysis (1.5 marks):**
- Time complexity with justification (0.75)
- Best possible asymptotic bound (0.5)
- Recognition of unit capacity optimization (0.25)
