# FIT2004 Proof Checklist

**Last Updated:** 2025-11-08

---

## Proofs to Know

### 1. Quicksort Average-Case Runtime ⚠️ **MID-SEMESTER**
**Theorem:** The average-case run time for Quicksort is O(n log n).

**Proof Methods:**
- Intuitive proof based on coin flips and probability
- Rigorous proof using recurrence relations

---

### 2. Median of Medians - Worst Case ⚠️ **ASKED ON MID-SEMESTER TEST**
**Theorem:** Quickselect using the median of medians strategy has worst-case O(n) performance.

---

### 3. Dijkstra's Algorithm Correctness ✅ **MID-SEMESTER**
**Theorem:** Given a graph G = (V, E) with non-negative weights and a source vertex s, Dijkstra's algorithm correctly finds shortest paths to each vertex v ∈ V.

---

### 4. Prim's Algorithm Invariant ✅ **MID-SEMESTER**
**Theorem:** In every iteration of Prim's algorithm, the current set of selected edges in T is a subset of some minimum spanning tree of G.

**Corollary:** Correctness of Prim's algorithm - Prim's algorithm correctly produces a minimum spanning tree.

---

### 5. Kruskal's Algorithm Invariant ⚠️ **ASKED ON MID-SEMESTER TEST**
**Theorem:** In every iteration of Kruskal's algorithm, the current set of selected edges T is a subset of some minimum spanning tree of G.

**Corollary:** Correctness of Kruskal's algorithm - Kruskal's algorithm correctly produces a minimum spanning tree.

---

### 6. Floyd-Warshall Correctness ⚠️ **FINAL EXAM ONLY**
**Theorem:** Floyd-Warshall produces the correct distances for all pairs of vertices (u, v) such that there exists a shortest path between u and v.

---

### 7. Min-Cut Max-Flow Theorem ⚠️ **FINAL EXAM ONLY**
**Theorem:** Given a flow network G = (V, E) with a source vertex s and sink vertex t, the value of a maximum s-t flow in G is equal to the minimum capacity s-t cut in G. Mathematically:
```
max |f| = min c(S, T)
 f      (S,T)
```

---

### 8. Ford-Fulkerson Correctness ⚠️ **FINAL EXAM ONLY**
**Corollary:** Correctness of Ford-Fulkerson - The Ford-Fulkerson algorithm correctly computes the maximum flow in a flow network.
