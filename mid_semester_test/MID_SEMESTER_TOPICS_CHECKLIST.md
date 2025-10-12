# Mid-Semester Test Topics and Questions Checklist

**Instructions:** Mark each topic/question with your status:
- `[ ]` = Not confident / Need to review
- `[x]` = Confident / Already know

---

## 1. ANALYSIS OF ALGORITHMS

### 1.1 Recurrence Relations & Complexity Analysis
- [ ] **Q1.1:** Deriving recurrence relations from pseudocode (Quiz 1 - power function)
- [ ] **Q1.2:** Solving recurrence relations (T(n) = T(n-2) + c) (Quiz 1)
- [ ] **Q1.3:** Recurrence with quadratic term: T(n) = T(n-2) + c*n^2 + d (Past Mid Q1)
- [ ] **Q1.4:** Telescoping method for solving recurrences (Applied Week 2)
  - T(n) = 2T(n−1) + a
  - T(n) = 2T(n/2) + cn (Merge sort)
  - T(n) = T(n/2) + c (Binary search)
- [ ] **Q1.5:** Master Theorem applications (Applied Week 2, Problem 12)
- [ ] **Q1.6:** Fibonacci recurrences and matrix multiplication (Applied Week 2, Problem 2)
- [ ] **Q1.7:** Time complexity of recursive power function (Applied Week 2, Problem 5)
- [ ] **Q1.8:** Recurrences with different patterns:
  - T(n) = 2T(n/2) + n → O(n log n)
  - T(n) = T(n-1) + an → O(n²)
  - T(n) = 3T(n/2) + n² → O(n²)

### 1.2 Loop Invariants & Correctness Proofs
- [ ] **Q1.9:** Loop invariant for bubble sort (Quiz 2 - fill in the blank)
- [ ] **Q1.10:** Loop invariant for counting algorithm (Applied Week 3, Problem 7)
- [ ] **Q1.11:** Loop invariant for insertion sort (Applied Week 3, Problem 8)
- [ ] **Q1.12:** Proving algorithm correctness using invariants
- [ ] **Q1.13:** Proving algorithm termination

### 1.3 Asymptotic Notation
- [ ] **Q1.14:** Big-O, Big-Θ, Big-Ω definitions and relationships
- [x] **Q1.15:** Comparing growth rates (n, n log n, n², 2^n, n!, etc.)
- [ ] **Q1.16:** Best, average, and worst-case analysis

---

## 2. DIVIDE AND CONQUER

### 2.1 Core Concepts
- [ ] **Q2.1:** Merge Sort implementation and analysis (Applied Week 2)
- [ ] **Q2.2:** Counting inversions using modified merge sort (Applied Week 2, Problem 6)
- [ ] **Q2.3:** Finding local maximum in n×n grid in O(n) (Applied Week 2, Problem 7)
- [ ] **Q2.4:** Karatsuba's multiplication (conceptual understanding)

---

## 3. SORTING ALGORITHMS

### 3.1 Comparison-Based Sorting
- [ ] **Q3.1:** Insertion sort with binary search (Past Mid Q3)
  - Worst-case comparisons vs worst-case time complexity
  - Understanding the difference between comparisons and data movement
- [ ] **Q3.2:** Stabilizing any comparison-based sort (Applied Week 3, Problem 1)
- [ ] **Q3.3:** Insertion sort in non-increasing order (Applied Week 3, Problem 8)
- [ ] **Q3.4:** Hybrid Mergesort + Insertion sort analysis (Applied Week 4, Problem 4)
- [ ] **Q3.5:** Comparison model limitations (Applied Week 3, Problem 11)

### 3.2 Non-Comparison Sorting
- [x] **Q3.6:** Radix sort state after iterations (Quiz 2)
- [ ] **Q3.7:** Radix sort for variable length strings (Applied Week 3, Problem 3)
  - O(ℓk) naive approach
  - O(n) optimal approach with length-based sorting
- [ ] **Q3.8:** Counting sort implementation and stability
- [ ] **Q3.9:** Optimal radix sort base selection (Applied Week 3, Problem 12)

### 3.3 Advanced Sorting Problems
- [ ] **Q3.10:** Merging k sorted lists (Applied Week 3, Problem 2)
  - O(nk) naive approach
  - O(n log k) using divide-and-conquer or priority queue
  - Lower bound proof
- [ ] **Q3.11:** In-place duplicate removal in O(n log n) (Applied Week 3, Problem 3, Problem 4)
- [ ] **Q3.12:** Finding k smallest elements online (Applied Week 3, Problem 5)

---

## 4. ORDER STATISTICS & SELECTION

### 4.1 Quickselect Algorithm
- [ ] **Q4.1:** Quickselect worst-case O(N) with median-of-medians (Past Mid Q2)
- [ ] **Q4.2:** QuickSelect with FIT2004 hybrid Hoare partition (Quiz 3, Question 2)
  - Understanding partition mechanics
  - Tracking array state after multiple rounds
- [ ] **Q4.3:** Average-case analysis of Quickselect = O(n) (Applied Week 4, Problem 1)

### 4.2 Partitioning
- [ ] **Q4.4:** Naive 3-way partitioning vs Hoare partitioning (Quiz 3, Question 1)
- [ ] **Q4.5:** k-way partitioning (Applied Week 4, Problem 5)
  - O(nk) solution
  - O(n log k) divide-and-conquer solution
- [ ] **Q4.6:** Quicksort with average pivot selection - worst case (Applied Week 4, Problem 6)

### 4.3 Selection Variants
- [ ] **Q4.7:** Locks and keys matching problem (Applied Week 4, Problem 2)
- [ ] **Q4.8:** Finding k closest numbers to median in O(n) (Applied Week 4, Problem 3)
- [ ] **Q4.9:** Weighted median using modified Quickselect (Applied Week 4, Problem 7)
- [ ] **Q4.10:** Iterative Quickselect implementation (Applied Week 4, Problem 8)
- [ ] **Q4.11:** kth order statistic of two sorted arrays (Applied Week 4, Problem 9)
  - O(log n log m) solution
  - O(log n + log m) advanced solution

### 4.4 Other Selection Problems
- [ ] **Q4.12:** Two egg drop problem (Applied Week 3, Problem 6)
  - Optimal strategy with n = 17 drops for 150 floors
  - Recurrence relation F₂(k) = k(k+1)/2

---

## 5. GRAPH BASICS

### 5.1 Graph Representation
- [ ] **Q5.1:** Adjacency matrix vs adjacency list trade-offs
- [ ] **Q5.2:** Space complexity: O(V²) vs O(V + E)
- [ ] **Q5.3:** When to use each representation

### 5.2 Graph Traversal - BFS
- [x] **Q5.4:** BFS traversal order with lexicographic tie-breaking (Quiz 4, Question 1)
- [ ] **Q5.5:** Multi-source shortest path using BFS (Applied Week 5, Problem 4)
- [ ] **Q5.6:** BFS for unweighted shortest paths
- [ ] **Q5.7:** BFS time complexity: O(V + E)

### 5.3 Graph Traversal - DFS
- [x] **Q5.8:** DFS traversal order with lexicographic tie-breaking (Quiz 4, Question 2)
- [ ] **Q5.9:** Finding connected components using DFS
- [ ] **Q5.10:** Cycle detection in undirected graphs (Applied Week 5, Problem 3a)
- [ ] **Q5.11:** Cycle detection in directed graphs (Applied Week 5, Problem 3b)
  - Three-state approach: Unvisited, Active, Inactive
- [ ] **Q5.12:** Non-recursive DFS using stack (Applied Week 5, Problem 9)
- [ ] **Q5.13:** DFS time complexity: O(V + E) for cycle detection (Applied Week 5, Problem 10)

### 5.4 Graph Coloring & Bipartite
- [ ] **Q5.14:** Two-coloring algorithm using DFS (Applied Week 5, Problem 1)
- [ ] **Q5.15:** Counting valid two-colorings (Past Mid Q5 & Applied Week 5, Problem 2)
  - Answer = 2^(number of connected components)
- [ ] **Q5.16:** Determining if graph is bipartite (Applied Week 5, Problem 8)
  - Equivalence: bipartite ↔ two-colorable

### 5.5 Topological Sorting
- [ ] **Q5.17:** Kahn's algorithm (queue-based with indegrees)
- [ ] **Q5.18:** DFS-based topological sort (post-order)
- [ ] **Q5.19:** Applications to DAG problems
- [ ] **Q5.20:** Employee raise problem using topological ordering (Applied Week 5, Problem 11)
- [ ] **Q5.21:** Hamiltonian path in DAG (Applied Week 5, Problem 12)

### 5.6 Advanced Graph Problems
- [ ] **Q5.22:** Shortest path with edge type constraints (Applied Week 5, Problem 5)
  - State-graph modeling
  - State = ⟨vertex, was_previous_edge_dotted⟩
- [ ] **Q5.23:** Shortest cycle in directed graph (Applied Week 5, Problem 6)
  - Run BFS from every vertex, O(V(V+E))
- [ ] **Q5.24:** Counting pure cycle components (Applied Week 5, Problem 7)
  - Check degree = 2 for all vertices in component

---

## 6. GREEDY ALGORITHMS

### 6.1 Minimum Spanning Trees - Prim's Algorithm
- [x] **Q6.1:** Prim's algorithm execution (Quiz 5, Question 1)
- [ ] **Q6.2:** Edge addition order starting from source node
- [ ] **Q6.3:** Time complexity: O(E log V) with priority queue
- [ ] **Q6.4:** Implementation using min-heap
- [ ] **Q6.5:** Correctness proof (greedy choice property)

### 6.2 Minimum Spanning Trees - Kruskal's Algorithm
- [x] **Q6.6:** Kruskal's algorithm execution (Quiz 5, Question 2)
- [ ] **Q6.7:** Edge addition order (sorted by weight)
- [ ] **Q6.8:** Time complexity: O(E log E) for sorting + Union-Find
- [ ] **Q6.9:** Implementation with Union-Find
- [ ] **Q6.10:** Correctness proof (greedy choice property)

### 6.3 Union-Find Data Structure
- [ ] **Q6.11:** Union-Find with union by rank
- [ ] **Q6.12:** Union-Find with union by size (negative parent encoding)
- [ ] **Q6.13:** Path compression optimization
- [ ] **Q6.14:** Amortized time complexity (nearly O(1))
- [ ] **Q6.15:** Applications to connectivity queries

### 6.4 Shortest Paths - Dijkstra's Algorithm
- [x] **Q6.16:** Dijkstra's algorithm for non-negative weights
- [ ] **Q6.17:** Time complexity: O((V + E) log V) with priority queue
- [ ] **Q6.18:** Implementation details (relaxation, priority queue updates)
- [x] **Q6.19:** Why it fails with negative weights
- [ ] **Q6.20:** Correctness proof (greedy choice property)

### 6.5 MST Applications
- [ ] **Q6.21:** Clustering by cutting largest MST edges (Past Mid Q4)
  - Maximize minimum inter-cluster distance
  - Algorithm: Build MST, remove k-1 largest edges
  - Time complexity: O(E log E) or O(E log V)

---

## EXAM FORMAT & STRATEGY

### Question Types (from past_mid/syllabus.json)
- [ ] **Essay questions:** Describe algorithms in plain English or pseudocode
- [ ] **Single-answer MCQ:** Select one correct answer
- [ ] **Multiple-answer MCQ:** Select ALL correct choices (partial marking)
- [ ] **Short answer:** Numerical answers only
- [ ] **Matching questions:** Drop-down menu selections

### Key Reminders
- [ ] Total marks: 10 (10% of grade)
- [ ] Coverage: Up to Week 6
- [ ] Closed book format (only blank working sheets)
- [ ] Worst-case complexity unless stated otherwise
- [ ] Avoid guessing on multiple-answer MCQs (negative marking possible)

---

## IMPLEMENTATION SKILLS

### Python Implementations to Review
- [ ] Merge Sort (implementations-algorithms/w1/mergeSort.py)
- [ ] Binary Search (implementations-algorithms/w1/binarySearch.py)
- [ ] Count Inversions (implementations-algorithms/w1/countInversions.py)
- [ ] Selection Sort (implementations-algorithms/w2/selectionSort.py)
- [ ] Counting Sort (implementations-algorithms/w2/countingSort.py)
- [ ] Radix Sort (implementations-algorithms/w2/radixSort.py)
- [ ] Dijkstra's Algorithm (implementations-algorithms/w5/dijkstra.py)
- [ ] Prim's Algorithm (implementations-algorithms/w5/prim.py)
- [ ] Kruskal's Algorithm (implementations-algorithms/w5/kruskal.py)
- [ ] Union-Find (implementations-algorithms/w5/unionFind.py)

---

## STUDY PRIORITY AREAS

Mark the topics below that you need to focus on:

### High Priority (Commonly Tested)
- [ ] Recurrence relation solving
- [ ] Loop invariants and correctness proofs
- [ ] Partitioning algorithms (Hoare vs 3-way)
- [ ] QuickSelect execution and analysis
- [ ] BFS/DFS traversal order
- [ ] MST algorithms (Prim and Kruskal)
- [ ] Union-Find operations
- [ ] Graph coloring and cycle detection

### Medium Priority (Important Concepts)
- [ ] Radix sort mechanics
- [ ] Counting sort stability
- [ ] Binary search variants
- [ ] Topological sorting
- [ ] Dijkstra's algorithm
- [ ] Comparison vs non-comparison sorting

### Advanced (Optional but Good to Know)
- [ ] Weighted median
- [ ] State-graph modeling
- [ ] k-way partitioning
- [ ] Variable-length string radix sort

---

**Next Steps:**
1. Go through this list and mark items you're not confident with
2. Share your markings so we can focus on those specific topics
3. Practice implementations for algorithms you're unsure about
4. Review past mid questions for marked topics
