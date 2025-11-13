# 8-Day Spaced Repetition Schedule for FIT2004 Final Exam

## Overview
This schedule uses spaced repetition principles to optimize retention. Topics are introduced, then revisited at increasing intervals (1 day, 2 days, 4 days) to strengthen long-term memory.

**Legend:**
- **INTRO**: First exposure to topic (in-depth study)
- **REVIEW-1**: First review (1 day later - practice problems)
- **REVIEW-2**: Second review (2-3 days later - harder problems)
- **REVIEW-3**: Third review (4+ days later - exam-level problems)

---

## Day 1: Foundations - Analysis & Verification

### Morning Session (2-3 hours)
**INTRO: Analysis of Algorithms**

**Theory Study:**
- **course_notes/chap_one.json** - Program verification, complexity analysis
- **lecture/l1.json** - Introduction to algorithm analysis
- **lecture/l2.json** - Asymptotic notation

**Key Concepts to Master:**
- Big-O, Big-Θ, Big-Ω definitions and relationships
- Loop invariants (initialization, maintenance, termination)
- Arguing correctness and termination
- Best/average/worst-case analysis

**Practice Problems:**
- **prep_solutions/prep.json** - Problems prereq_p7, prereq_p8 (asymptotic notation)
- **weekly_quiz/q1.json** - Week 1 quiz questions
- **prep_solutions/prep.json** - Problem week3_p1 (loop invariants for minimum element)

**Coding Exercise:**
- Review **implementations-algorithms/w1/binarySearch.py**
- Write loop invariants for binary search
- Prove correctness using loop invariant method

---

### Afternoon Session (2-3 hours)
**INTRO: Recurrence Relations**

**Theory Study:**
- **course_notes/chap_two.json** - Recurrence relations
- **lecture/l2.json** - Solving recurrences

**Key Concepts to Master:**
- Deriving recurrences from recursive algorithms
- Telescoping method for solving recurrences
- Master theorem patterns:
  - T(n) = T(n-1) + O(1) → O(n)
  - T(n) = T(n/2) + O(1) → O(log n)
  - T(n) = 2T(n/2) + O(n) → O(n log n)

**Practice Problems:**
- **prep_solutions/prep.json** - Problems week2_p1 through week2_p5 (deriving and solving recurrences)
- **applied_solutions/2.txt** - Applied recurrence problems

**Coding Exercise:**
- Review **implementations-algorithms/w1/mergeSort.py**
- Derive T(n) = 2T(n/2) + O(n) from the code
- Solve using recursion tree method

---

## Day 2: Divide & Conquer + Fast Sorting

### Morning Session (2-3 hours)
**INTRO: Divide and Conquer**

**Theory Study:**
- **course_notes/chap_two.json** - Divide and conquer paradigm
- **lecture/l3.json** - Merge sort and applications

**Key Concepts to Master:**
- Merge sort: O(n log n) all cases, stable, O(n) space
- Counting inversions using modified merge sort
- Karatsuba multiplication: O(n^1.585)

**Practice Problems:**
- **weekly_quiz/q2.json** - Week 2 quiz on divide & conquer
- **prep_solutions/prep.json** - Problem week3_p1 (prove merge sort correct)
- **applied_solutions/2.txt** - Inversion counting problems

**Coding Exercise:**
- **implementations-algorithms/w1/mergeSort.py** - Trace execution
- **implementations-algorithms/w1/countInversions.py** - Understand modification

---

### Afternoon Session (2-3 hours)
**INTRO: Fast Sorting (Quicksort, Heapsort, Radix)**

**Theory Study:**
- **course_notes/chap_three.json** - Fast sorting algorithms
- **lecture/l3.json**, **lecture/l4.json** - Quicksort and integer sorting

**Key Concepts to Master:**
- Quicksort: avg O(n log n), worst O(n²), pivot strategies
- Heapsort: O(n log n) all cases, O(1) space, not stable
- Counting sort: O(n+k), requires integer range
- Radix sort: O(d(n+k)), stable, digit-by-digit
- Decision tree lower bound: Ω(n log n) for comparison sorts

**Practice Problems:**
- **prep_solutions/prep.json** - Problems week4_p1, week4_p3 (quicksort analysis, partitioning)
- **prep_solutions/prep.json** - Problem week3_p3 (radix sort trace)
- **weekly_quiz/q3.json** - Week 3 quiz

**Coding Exercise:**
- **implementations-algorithms/w2/countingSort.py** - Trace with example
- **implementations-algorithms/w2/radixSort.py** - Understand multi-pass process
- Implement Hoare partitioning and trace on sample array

---

### Evening Session (1 hour)
**REVIEW-1: Day 1 Material (Analysis & Recurrences)**

**Quick Review:**
- Redo 2-3 asymptotic notation problems without looking at solutions
- Solve 1-2 new recurrence relations
- **exams/s1.json** - Select 1-2 relevant problems on complexity analysis

---

## Day 3: Order Statistics + Graph Basics

### Morning Session (2-3 hours)
**INTRO: Order Statistics and Selection**

**Theory Study:**
- **course_notes/chap_four.json** - Order statistics
- **lecture/l4.json** - Selection algorithms

**Key Concepts to Master:**
- Quickselect: avg O(n), worst O(n²)
- Median of medians: deterministic O(n)
- Randomized pivot selection
- Comparison with Quicksort

**Practice Problems:**
- **prep_solutions/prep.json** - Problem week4_p2 (Quicksort vs Quickselect)
- **weekly_quiz/q4.json** - Week 4 quiz
- **applied_solutions/4.txt** - Selection algorithm applications

**Coding Exercise:**
- Implement Quickselect algorithm
- Compare recursion depth with Quicksort on same input

---

### Afternoon Session (2-3 hours)
**INTRO: Graph Basics & Traversal**

**Theory Study:**
- **course_notes/chap_five.json** - Graph basics, DFS, BFS
- **lecture/l5.json** - Graph representation and traversal

**Key Concepts to Master:**
- Adjacency matrix: O(V²) vs adjacency list: O(V+E)
- DFS: O(V+E), uses stack/recursion, applications: cycle detection, connectivity
- BFS: O(V+E), uses queue, applications: shortest path (unweighted), level-order
- Connected components using DFS/BFS
- Topological sorting: Kahn's algorithm, DFS-based

**Practice Problems:**
- **prep_solutions/prep.json** - Problems week5_p1, week5_p2 (DFS/BFS tracing)
- **weekly_quiz/q5.json** - Week 5 quiz
- **applied_solutions/5.txt** - Graph traversal applications

**Coding Exercise:**
- Trace DFS and BFS on paper for a given graph
- **implementations-algorithms/w5/** - Review graph implementations
- Write algorithm to find all vertices reachable from source s

---

### Evening Session (1 hour)
**REVIEW-1: Day 2 Material (Divide & Conquer, Fast Sorting)**

**Quick Review:**
- Trace quicksort with different pivot strategies
- Trace radix sort on new dataset
- Compare time complexities of all sorting algorithms learned

---

## Day 4 (Saturday): Greedy Algorithms (Shortest Paths + MST)

### Morning Session (2-3 hours)
**INTRO: Dijkstra's Algorithm**

**Theory Study:**
- **course_notes/chap_six.json** - Greedy algorithms: shortest paths
- **lecture/l6.json** - Dijkstra's algorithm

**Key Concepts to Master:**
- Dijkstra's: O((V+E) log V) with priority queue
- Requirement: non-negative edge weights
- Greedy choice: always visit unvisited vertex with min distance
- Produces shortest path tree from source
- Triangle inequality and optimal substructure

**Practice Problems:**
- **prep_solutions/prep.json** - Problem week6_p1 (Dijkstra trace)
- **weekly_quiz/q6.json** - Week 6 quiz
- **applied_solutions/6.txt** - Shortest path applications

**Coding Exercise:**
- **implementations-algorithms/w5/dijkstra.py** - Trace execution
- Practice on paper: run Dijkstra from different source vertices
- Reconstruct shortest path tree

---

### Afternoon Session (2-3 hours)
**INTRO: Minimum Spanning Trees**

**Theory Study:**
- **course_notes/chap_six.json** - MST algorithms
- **lecture/l6.json** - Prim's and Kruskal's algorithms

**Key Concepts to Master:**
- Prim's: O(E log V), grows tree from root, greedy choice: min edge from tree to non-tree
- Kruskal's: O(E log E), sorts edges, greedy choice: global min edge without cycle
- Union-Find data structure: union-by-size, path compression
- Both produce same total weight MST

**Practice Problems:**
- **prep_solutions/prep.json** - Problems week6_p2, week6_p3 (Prim, Kruskal, Union-Find)
- **applied_solutions/6.txt** - MST applications

**Coding Exercise:**
- **implementations-algorithms/w5/prim.py** - Trace execution
- **implementations-algorithms/w5/kruskal.py** - Trace execution
- **implementations-algorithms/w5/unionFind.py** - Trace union-by-size operations
- Verify both algorithms produce same MST weight on sample graph

---

### Evening Session (1.5 hours)
**REVIEW-2: Day 1 Material (Analysis & Recurrences)**

**Deeper Review:**
- **exams/s1.json** - Complete 2-3 exam-level problems on complexity
- Prove correctness of an algorithm using loop invariants
- Solve harder recurrence relations

---

## Day 5 (Sunday): Dynamic Programming Fundamentals

### Morning Session (3 hours)
**INTRO: Dynamic Programming Basics**

**Theory Study:**
- **course_notes/chap_seven.json** - DP fundamentals
- **lecture/l7.json** - Introduction to DP

**Key Concepts to Master:**
- Optimal substructure and overlapping subproblems
- Top-down (memoization) vs bottom-up (tabulation)
- Subproblem table design and recurrence formulation
- Reconstructing optimal solutions

**Practice Problems:**
- **weekly_quiz/q7.json** - Week 7 quiz on DP basics
- **applied_solutions/7.txt** - Basic DP problems

**Coding Exercise:**
- **implementations-algorithms/w6/** - Review DP implementations
- Implement Fibonacci: recursive, memoized, iterative
- Compare time/space complexity

---

### Afternoon Session (3 hours)
**INTRO: Classical DP Problems**

**Theory Study:**
- **course_notes/chap_seven.json** - Knapsack, edit distance, matrix chain
- **lecture/l7.json**, **lecture/l8.json** - DP applications

**Key Concepts to Master:**
- 0-1 Knapsack: O(nW), choose each item once
- Unbounded Knapsack: O(nW), items can repeat
- Edit Distance: O(mn), insertions/deletions/substitutions
- Matrix Chain Multiplication: O(n³), optimal parenthesization
- Space-saving trick: reduce to O(W) or O(min(m,n))

**Practice Problems:**
- **applied_solutions/7.txt** - Knapsack and edit distance
- **exams/s2.json** - DP exam problems

**Coding Exercise:**
- Implement 0-1 knapsack with solution reconstruction
- Implement edit distance and trace back operations
- Apply space-saving optimization

---

### Evening Session (1 hour)
**REVIEW-1: Day 4 Material (Greedy - Dijkstra, MST)**

**Quick Review:**
- Trace Dijkstra on new graph
- Trace Prim and Kruskal on same graph
- Verify MST properties

---

## Day 6 (Monday): DP Graph Algorithms + Network Flow

### Morning Session (2-3 hours)
**INTRO: DP on Graphs**

**Theory Study:**
- **course_notes/chap_eight.json** - DP graph algorithms
- **lecture/l8.json** - Bellman-Ford, Floyd-Warshall

**Key Concepts to Master:**
- Bellman-Ford: O(VE), handles negative weights, detects negative cycles
- Floyd-Warshall: O(V³), all-pairs shortest paths
- Transitive closure: Boolean reachability
- Critical path in DAG: longest path using topological order

**Practice Problems:**
- **weekly_quiz/q8.json** - Week 8 quiz
- **applied_solutions/8.txt** - DP graph problems
- **exams/s2.json** - Bellman-Ford and Floyd-Warshall problems

**Coding Exercise:**
- Trace Bellman-Ford with negative edges
- Trace Floyd-Warshall on small graph
- Detect negative cycle using Bellman-Ford

---

### Afternoon Session (2-3 hours)
**INTRO: Network Flow**

**Theory Study:**
- **course_notes/chap_nine.json** - Network flow
- **lecture/l9.json** - Ford-Fulkerson, max-flow min-cut

**Key Concepts to Master:**
- Ford-Fulkerson: O(E × max_flow), augmenting paths
- Residual network: represents remaining capacities
- Min-cut max-flow theorem: flow value = cut capacity
- Bipartite matching: reduce to max flow
- Circulations with demands and lower bounds

**Practice Problems:**
- **weekly_quiz/q9.json** - Week 9 quiz
- **applied_solutions/9.txt** - Network flow applications
- **exams/s3.json** - Max flow problems

**Coding Exercise:**
- Trace Ford-Fulkerson on small network
- Identify augmenting paths and residual capacities
- Find minimum cut from final residual graph

---

### Evening Session (1.5 hours)
**REVIEW-2: Day 2 Material (Divide & Conquer, Fast Sorting)**

**Deeper Review:**
- **exams/s1.json** - Exam-level sorting problems
- Implement and analyze a variation of quicksort
- Prove lower bound for comparison-based sorting

---

## Day 7 (Tuesday): Advanced Trees + String Algorithms

### Morning Session (2-3 hours)
**INTRO: Self-Balancing Search Trees**

**Theory Study:**
- **course_notes/chap_ten.json** - BST, AVL, Red-Black, 2-3 Trees
- **lecture/l10.json** - Balanced trees

**Key Concepts to Master:**
- BST: avg O(log n), worst O(n)
- AVL: height difference ≤ 1, rotations for rebalancing
- Red-Black: height ≤ 2log(n+1), color properties
- 2-3 Trees: nodes with 2-3 children, perfectly balanced
- Comparison: AVL (faster lookups) vs RBT (faster inserts)

**Practice Problems:**
- **weekly_quiz/q10.json** - Week 10 quiz
- **applied_solutions/10.txt** - Tree problems
- **exams/25-1.json**, **exams/21-1.json** - Tree exam problems

**Coding Exercise:**
- Trace AVL insertions with rotations (LL, LR, RR, RL)
- Compare BST vs AVL height for same insertions
- Trace 2-3 tree insertions

---

### Afternoon Session (2-3 hours)
**INTRO: Tries and Suffix Trees**

**Theory Study:**
- **course_notes/chap_eleven.json** - Prefix tries, suffix trees
- **lecture/l11.json**, **lecture/l12.json** - String algorithms

**Key Concepts to Master:**
- Prefix Trie: O(L) search/insert/delete (L = word length)
- Applications: autocomplete, spell-check, dictionary compression
- Suffix Tree: O(n) space with Ukkonen's algorithm
- Applications: substring search, pattern matching, longest repeated substring

**Practice Problems:**
- **weekly_quiz/q11.json** - Week 11 quiz
- **applied_solutions/11.txt** - Trie and suffix tree problems

**Coding Exercise:**
- Build prefix trie from list of words
- Trace suffix tree construction
- Use suffix tree for pattern matching

---

### Evening Sessions (2 hours)
**REVIEW-1: Day 6 Material (DP Graphs + Network Flow)**

**Quick Review:**
- Trace Bellman-Ford on new graph
- Trace Floyd-Warshall and compare with repeated Dijkstra
- Find max flow in new network

**REVIEW-2: Day 3 Material (Order Statistics + Graph Basics)**

**Deeper Review:**
- **exams/s1.json** - Graph traversal exam problems
- Implement topological sort using both methods (Kahn's, DFS)
- Compare DFS vs BFS for different applications

---

## Day 8 (Wednesday): Comprehensive Review & Mock Exam

### Morning Session (3 hours)
**REVIEW-3: All Major Topics (Days 1-4)**

**Systematic Review:**

1. **Analysis & Verification (30 min)**
   - Review Big-O/Θ/Ω quick reference
   - Practice 2 loop invariant proofs
   - Solve 2 asymptotic notation problems

2. **Sorting Algorithms (45 min)**
   - Create comparison table: time, space, stability
   - Trace quicksort with median-of-three pivot
   - Trace radix sort on new dataset
   - **exams/s2.json** - Sorting exam questions

3. **Graph Algorithms (45 min)**
   - Trace DFS and BFS on same graph, compare results
   - Run Dijkstra from different sources
   - Compare Prim vs Kruskal on same graph
   - **exams/s3.json** - Graph exam questions

4. **Recurrences (30 min)**
   - Solve 3 different recurrence patterns
   - Derive recurrences from new recursive algorithms

---

### Afternoon Session (3 hours)
**REVIEW-3: Advanced Topics (Days 5-7)**

1. **Dynamic Programming (60 min)**
   - Review all DP problem patterns
   - Solve 1 knapsack variant
   - Solve 1 string DP problem (edit distance variant)
   - **exams/25-1.json** - DP exam questions

2. **DP Graph Algorithms (30 min)**
   - Trace Bellman-Ford with negative cycle detection
   - Compare Floyd-Warshall vs V runs of Dijkstra
   - Critical path problem on new DAG

3. **Network Flow (30 min)**
   - Find max flow in new network
   - Identify minimum cut
   - Solve bipartite matching problem

4. **Trees & Strings (30 min)**
   - AVL rotation practice
   - Trie operations
   - Compare tree structures for different use cases

---

### Evening Session (2-3 hours)
**Mock Exam Simulation**

**Comprehensive Practice:**
- **exams/25-1.json** - Complete past exam under timed conditions
- **exams/21-1.json** - Additional exam questions
- **exams/s1.json, s2.json, s3.json** - Mixed problem sets

**Post-Exam Review:**
- Identify weak areas
- Revisit course notes for any gaps
- Review **exams/EXAM_MARKS_DISTRIBUTION.md** and **exams/FINAL_EXAM_QUESTION_PATTERNS.md**

---

## Spaced Repetition Summary

### Topic Review Schedule

| Topic | Day Introduced | Review-1 | Review-2 | Review-3 |
|-------|---------------|----------|----------|----------|
| Analysis & Recurrences | Day 1 | Day 2 (eve) | Day 4 (eve) | Day 8 (am) |
| Divide & Conquer, Sorting | Day 2 | Day 3 (eve) | Day 6 (eve) | Day 8 (am) |
| Order Statistics, Graph Basics | Day 3 | Day 4 (eve) | Day 7 (eve) | Day 8 (am) |
| Greedy (Dijkstra, MST) | Day 4 | Day 5 (eve) | Day 7 (eve) | Day 8 (am) |
| DP Fundamentals | Day 5 | Day 6 (eve) | Day 8 (pm) | - |
| DP Graphs, Network Flow | Day 6 | Day 7 (eve) | Day 8 (pm) | - |
| Trees & Strings | Day 7 | Day 8 (pm) | - | - |

---

## Daily Study Protocol

### For Each Study Session:

1. **Active Learning (not passive reading)**
   - Take notes by hand
   - Draw diagrams and trace algorithms
   - Explain concepts out loud

2. **Practice-Focused**
   - Solve problems without looking at solutions first
   - Time yourself on harder problems
   - Implement algorithms from scratch

3. **Review Protocol**
   - Don't just re-read notes
   - Test yourself with new problems
   - If you struggle, go back to INTRO materials

4. **Mistake Log**
   - Keep a document of all mistakes
   - Review this before Day 8 mock exam
   - Identify patterns in your errors

---

## Resource Priority Guide

### Must-Know for Exam:

**Tier 1 (Critical):**
- All course_notes/ chapters (chap_one through chap_eleven)
- prep_solutions/prep.json (foundation problems)
- implementations-algorithms/w1, w2, w5, w6 (core algorithms)
- exams/25-1.json, 21-1.json (actual past exams)

**Tier 2 (Important):**
- All lecture/ JSON files (l1 through l12)
- All weekly_quiz/ files (q1 through q11)
- exams/s1.json, s2.json, s3.json (exam-style problems)

**Tier 3 (Supplementary):**
- applied_solutions/ (2 through 11) - additional practice
- exams/EXAM_MARKS_DISTRIBUTION.md - understand point allocation
- exams/FINAL_EXAM_QUESTION_PATTERNS.md - question types

---

## Exam Day Preparation

### Day Before Exam:
- Light review only (no new material)
- Review your mistake log
- Review formula sheets from prep.json
- Get 8 hours of sleep

### Exam Day Morning:
- Quick review of complexity cheat sheets
- Review Big-O/Θ/Ω definitions
- Review algorithm complexities table
- Don't cram - trust your preparation

---

## Key Formulas & Complexities Quick Reference

### Sorting Algorithms:
- Merge Sort: Θ(n log n), O(n) space, stable
- Quicksort: avg Θ(n log n), worst Θ(n²), O(log n) space
- Radix Sort: Θ(d·n), O(n+k) space, stable
- Counting Sort: Θ(n+k), O(k) space, stable

### Graph Algorithms:
- DFS/BFS: O(V+E)
- Dijkstra: O((V+E) log V)
- Bellman-Ford: O(VE)
- Floyd-Warshall: O(V³)
- Prim/Kruskal: O(E log V)
- Ford-Fulkerson: O(E × max_flow)

### DP Classics:
- 0-1 Knapsack: O(nW)
- Edit Distance: O(mn)
- Matrix Chain: O(n³)

### Trees:
- BST operations: avg O(log n), worst O(n)
- AVL/RBT operations: O(log n) guaranteed
- Trie operations: O(L) where L = word length

---

## Good Luck!

Remember: **Spaced repetition works if you stick to the schedule.** Don't skip review sessions - they're scientifically proven to improve retention!

Focus on understanding over memorization. If you understand WHY algorithms work, you can derive complexities and prove correctness under exam pressure.
