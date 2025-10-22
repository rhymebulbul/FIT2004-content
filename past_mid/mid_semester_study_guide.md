# Mid-Semester Test - Applied Problems Study Guide

## Overview
This guide identifies which applied problems (from 2.txt through 6.txt) are appropriate for mid-semester test preparation and which can be excluded as too advanced.

---

## ✅ Problems to FOCUS ON

### Week 2 (2.txt) - ALL PROBLEMS
**Topics**: Recurrence relations, Divide & Conquer fundamentals

- ✅ Problem 1: Recurrence relation closed form
- ✅ Problem 2: Fibonacci matrix proof
- ✅ Problem 3: Merge sort recurrence
- ✅ Problem 4: Binary search recurrence
- ✅ Problem 5: Power function analysis
- ✅ Problem 6: Counting inversions
- ✅ Problem 7: Local maximum in grid
- ✅ Problem 8: Fibonacci implementation
- ✅ Problems 9-12: Additional recurrence relations and Master theorem

**Verdict**: All problems are appropriate mid-semester difficulty.

---

### Week 3 (3.txt) - MOSTLY KEEP
**Topics**: Fast sorting algorithms (comparison-based and non-comparison)

#### Keep These:
- ✅ Problem 1: Stabilizing comparison-based sorting
- ✅ Problem 2: Merging k sorted lists (both O(nk) and O(n log k) solutions)
- ✅ Problem 3: Radix sort for variable length strings
- ✅ Problem 4: In-place duplicate removal
- ✅ Problem 5: Finding k smallest elements online (using heap)
- ✅ Problem 7: Loop invariant for counting algorithm
- ✅ **Problem 8 (Supplementary): Insertion sort in non-increasing order**
  - Understanding loop invariants for sorting
- ✅ **Problem 9 (Supplementary): Binary search variants**
  - Finding first/last occurrence (critical for understanding binary search invariants)
- ✅ **Problem 10 (Supplementary): Fixed point search**
  - O(log n) binary search on transformed sequences
- ✅ **Problem 11 (Supplementary): Fast insertion sort analysis** ⚠️ **APPEARED ON PAST MID-SEMESTER TEST**
  - Uses binary search to find insertion position: O(n log n) comparisons
  - Still requires shifting elements: O(n²) time complexity
  - **Key insight**: Comparison model vs. actual time complexity
  - Demonstrates that optimal comparisons ≠ optimal runtime

#### Exclude These:
- ❌ **Problem 6: Two Egg Drop Problem** - Too advanced for mid-semester
  - Requires sophisticated mathematical reasoning (triangular numbers)
  - DP-style state analysis beyond typical mid-semester scope

---

### Week 4 (4.txt) - MOSTLY KEEP
**Topics**: Order statistics, Selection algorithms, Quickselect

#### Keep These:
- ✅ Problem 1: Quickselect average-case analysis
- ✅ Problem 2: Locks and keys matching
- ✅ Problem 3: k closest numbers to median
- ✅ Problem 4: Merge sort + insertion sort hybrid
- ✅ Problem 5: k-partitioning (O(nk) and O(n log k))
- ✅ Problem 6: Quicksort with average pivot (worst-case analysis)
- ✅ Problem 8 (Supplementary): Iterative Quickselect

#### Exclude These:
- ❌ **Problem 7: Weighted Median** - Too advanced
  - Complex modification of Quickselect
  - Beyond typical mid-semester difficulty

- ❌ **Problem 9 (Supplementary): k-th order statistic in two sorted arrays**
  - Requires nested binary search
  - O(log n × log m) complexity too complex

---

### Week 5 (5.txt) - MOSTLY KEEP
**Topics**: Graph basics, DFS, BFS, Traversal, Topological sorting, Connectivity

#### Keep These (ALL MAIN PROBLEMS):
- ✅ Problem 1: Two-colourable graphs (bipartite detection)
- ✅ Problem 2: Counting valid two-colourings
- ✅ Problem 3: Cycle detection in directed graphs
- ✅ Problem 4: Multi-source shortest path
- ✅ Problem 5: State-graph with edge type constraints
- ✅ Problem 6: Shortest cycle in directed graph
- ✅ Problem 7: Counting pure cycle components

#### Keep These (SOME SUPPLEMENTARY):
- ✅ Problem 8: Bipartite graph detection
- ✅ Problem 9: Non-recursive DFS with stack
- ✅ Problem 10: Cycle detection complexity analysis

#### Exclude These:
- ❌ **Problem 11 (Supplementary): Company raises with topological ordering**
  - Requires O(V² + VE) complexity
  - Sophisticated graph reasoning beyond mid-semester

- ❌ **Problem 12 (Supplementary): Hamiltonian paths in DAGs**
  - NP-hard concepts
  - Too theoretical for mid-semester

---

### Week 6 (6.txt) - PARTIAL COVERAGE
**Topics**: Greedy algorithms (Dijkstra, Prim, Kruskal, MST)

#### Keep These:
- ✅ Problem 1: Buggy Dijkstra implementation
- ✅ Problem 2: MST algorithms with negative weights
- ✅ **Problem 4: Bottleneck paths** ⚠️ **FOUNDATIONAL FOR PAST MID-SEMESTER TEST QUESTION 5**
  - Part (a): Example where shortest path ≠ bottleneck path
  - Part (b): **Prove all MST paths are bottleneck paths** (KEY INSIGHT for clustering)
  - Part (c): Prove not all bottleneck paths are in MST
  - **Critical for understanding why MST-based clustering works**
- ✅ Problem 5: Reverse Kruskal's algorithm (removing edges)
- ✅ Problem 7: Request scheduling greedy algorithm

#### Exclude These:
- ❌ **Problem 3: Cross-country road trip with petrol stations**
  - Requires complex state-graph modeling
  - State = ⟨town, fuel_level⟩ is too advanced

- ❌ **Problem 6: Zero-one shortest path (0-1 BFS)**
  - Very advanced BFS modification using deques
  - Too complex for mid-semester

- ❌ **All Supplementary Problems (8-11)**
  - Problem 8: Union-find complexity proofs (induction on tree height)
  - Problem 9: Dijkstra with bounded integer weights
  - Problem 10: Kruskal's invariant analysis
  - Problem 11: Union-find visualization with path compression

---

## 📊 Summary Statistics

### Total Problems to Study:
- **Week 2**: 12/12 problems ✅ (100%)
- **Week 3**: 9/11 problems ✅ (82%) - Skip Problem 6 only (added supplementary 8-11)
- **Week 4**: 7/9 problems ✅ (78%) - Skip Problems 7 and 9
- **Week 5**: 10/12 problems ✅ (83%) - Skip supplementary Problems 11-12
- **Week 6**: 5/11 problems ✅ (45%) - Skip Problems 3, 6, and all supplementary (added Problem 4)

### Key Exclusion Reasons:
1. **Advanced state-graph modeling** (Week 6 Problem 3)
2. **Sophisticated mathematical reasoning** (Week 3 Problem 6: Two Egg Drop with triangular numbers)
3. **Complex algorithm modifications** (Week 6 Problem 6: 0-1 BFS, Week 4 Problem 7: Weighted median)
4. **NP-hard/theoretical concepts** (Week 5 Problem 12: Hamiltonian paths)
5. **Union-find advanced proofs** (Week 6 supplementary 8-11)

---

## 🎯 Study Priority Order

### High Priority (Core Mid-Semester Topics):
1. **Recurrence relations** (Week 2: all problems) ⚠️ **Q1 on past mid - students struggled**
2. **Graph traversal & Two-colorability** (Week 5: Problems 1-10 including supplementary 8-10) ⚠️ **Q2 on past mid - "very poor" performance**
3. **Selection algorithms & Quickselect** (Week 4: Problems 1-6, 8) ⚠️ **Q3 on past mid - students couldn't explain MoM**
4. **Sorting & Binary Search** (Week 3: Problems 1-5, 7-11 including supplementary) ⚠️ **Q4 on past mid (Problem 11)**
5. **MST, Greedy & Clustering** (Week 6: Problems 1-2, 4, 5, 7) ⚠️ **Q5 on past mid - MST clustering**

### Critical Exam-Relevant Problems:
- ⚠️ **Week 3 Problem 11**: Fast insertion sort (APPEARED AS Q4 ON PAST MID)
- ⚠️ **Week 6 Problem 4**: Bottleneck paths (FOUNDATIONAL FOR Q5 ON PAST MID)
- ⚠️ **Week 5 Problems 1-2 + Supp 8**: Two-colorability/bipartite (Q2 ON PAST MID - students performed poorly)
- ⚠️ **Week 4 Quickselect problems**: Understanding MoM justification (Q3 ON PAST MID)

### Medium Priority:
- Week 5 supplementary Problems 9-10 (Non-recursive DFS, cycle detection analysis)

### Skip Entirely for Mid-Semester:
- Week 3: Problem 6 (Two Egg Drop - requires triangular numbers/DP)
- Week 4: Problems 7, 9 (Weighted median, nested binary search)
- Week 5: Problems 11-12 (Advanced graph theory, Hamiltonian paths)
- Week 6: Problems 3, 6, 8-11 (State graphs, 0-1 BFS, Union-find proofs)

---

## 📝 Notes

- The excluded problems are **NOT** irrelevant—they're just too advanced for the mid-semester test based on:
  - Examinable content scope (examinable_content_mid.txt)
  - Past mid-semester exam difficulty patterns
  - Typical mid-semester time constraints

- These excluded problems **MAY BE RELEVANT** for the final exam, so don't delete them—just deprioritize for mid-semester study.

- Focus your limited study time on mastering the **43 included problems** (12+9+7+10+5) rather than struggling with the 13 excluded ones.

### CORRECTIONS MADE:
- ✅ **Added Week 3 Supplementary Problems 8-11** (previously incorrectly marked as "too advanced")
  - Problem 11 explicitly appeared on past mid-semester test as Q4
- ✅ **Added Week 6 Problem 4 (Bottleneck paths)** (previously incorrectly excluded)
  - Foundational theory for understanding MST clustering (Question 5 on past mid)
- ✅ **Elevated Week 5 Supplementary Problem 8 to HIGH PRIORITY** (previously medium priority)
  - Bipartite detection is directly tested as two-colorability (Q2 on past mid)
  - Students performed "very poorly" - needs more emphasis

---

**Last Updated**: Based on analysis of examinable_content_mid.txt and past_mid exam patterns