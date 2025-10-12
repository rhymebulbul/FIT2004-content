# FIT2004 Exam Marks Distribution Analysis

This document provides a comprehensive analysis of marks distribution, question types, and topic coverage across FIT2004 exams.

**Last Updated:** 2025-10-12
**Repository:** FIT2004-content/exams/

**🚫 IMPORTANT - Topics OUT OF SYLLABUS This Semester:**
- **Hash Tables** (collision resolution, probing, separate chaining)
- **Suffix Arrays** (prefix doubling, rank arrays)

These topics are marked with 🚫 throughout the document and should be **completely skipped**.

---

## Table of Contents

1. [Exam Format Overview](#exam-format-overview)
2. [Mid-Semester Test Analysis](#mid-semester-test-analysis)
3. [Final Exam Analysis](#final-exam-analysis)
4. [Marks Distribution by Question Type](#marks-distribution-by-question-type)
5. [Topic Coverage by Question Type](#topic-coverage-by-question-type)
6. [Study Recommendations](#study-recommendations)

---

## Exam Format Overview

### Duration
- **Mid-Semester Test:** Variable (not specified in materials)
- **Final Exam:** 2 hours 10 minutes (130 minutes)

### Total Marks
- **Mid-Semester Test:** 10 marks (based on past_mid/question.json)
- **Final Exam:** 50 marks (standard across all past exams)

### Authorized Materials
- **No calculators**
- **No dictionaries**
- **No notes**
- **Working sheets provided**
- **No other permitted items**

---

## Mid-Semester Test Analysis

### Overall Structure

| Metric | Value |
|--------|-------|
| **Total Questions** | 5 |
| **Total Marks** | 10 |
| **Marks per Question** | 2 marks (uniform) |
| **Duration** | Not specified |

### Question Type Breakdown

| Question Type | Count | Marks per Question | Total Marks | Percentage |
|--------------|-------|-------------------|-------------|------------|
| **Single-Choice MCQ** | 1 | 2 | 2 | 20% |
| **Multiple-Choice MCQ** | 1 | 2 | 2 | 20% |
| **Open Response** | 2 | 2 | 4 | 40% |
| **Numerical** | 1 | 2 | 2 | 20% |

### Topic Distribution (Mid-Semester)

Based on `examinable_content_mid.txt` and past mid-semester questions:

| Topic | Question Type | Marks | Mid-Sem Relevant? |
|-------|---------------|-------|-------------------|
| **Recurrence Relations** | Single-Choice MCQ | 2 | ✓ (Analysis of Algorithms) |
| **Quickselect Algorithm** | Open Response | 2 | ✓ (Order Statistics) |
| **Insertion Sort Variant** | Multiple-Choice MCQ | 2 | ✓ (Sorting) |
| **Clustering (MST-based)** | Open Response | 2 | ✓ (Greedy - MST) |
| **Graph Coloring** | Numerical | 2 | ✓ (Graph Basics) |

### Mid-Semester Examinable Topics

**✓ Topics covered in mid-semester:**
1. **Analysis of Algorithms** (Program Verification, Complexity, Recurrences, Asymptotic Notation)
2. **Divide and Conquer** (Karatsuba, Merge Sort, Inversions)
3. **Fast Sorting** (Heapsort, Quicksort, Counting Sort, Radix Sort)
4. **Order Statistics** (Quickselect, Median of Medians)
5. **Graph Basics** (Traversal, Connectivity, Shortest Paths - BFS, Topological Sort)
6. **Greedy Algorithms** (Dijkstra, Prim, Kruskal, Union-Find)

**✗ Topics NOT covered in mid-semester (Final exam only):**
- **Dynamic Programming** (all topics)
- **Network Flow** (max-flow, min-cut, bipartite matching, circulation with demands)
- **Advanced Shortest Paths** (Bellman-Ford, Floyd-Warshall)
- **AVL Trees** (rotations, balance factors)
- **Advanced String Algorithms** (suffix trees, tries)
- **2-3 Trees, Red-Black Trees**

**🚫 Topics OUT OF SYLLABUS this semester (not examinable at all):**
- **Hash Tables** (collision resolution, probing techniques, separate chaining)
- **Suffix Arrays** (prefix doubling, rank arrays)

---

## Final Exam Analysis

### Overall Structure (Multiple Past Exams)

| Exam | Questions | Total Marks | Duration |
|------|-----------|-------------|----------|
| **2025 S1 Final** | 26 (some grouped) | ~50 | 2h 10m |
| **2021 S1 Practice** | 26 | ~45 | 2h 10m |
| **Past Exam 1** | 22 | 50 | 2h 10m |
| **Past Exam 2** | 20 | 50 | 2h 10m |
| **Past Exam 3** | 22 | 50 | 2h 10m |

### Typical Question Count Distribution

| Marks per Question | Typical Count | Total Marks | Percentage of Exam |
|-------------------|---------------|-------------|-------------------|
| **0.5 marks** | 1-2 | 0.5-1 | 1-2% |
| **1 mark** | 5-8 | 5-8 | 10-16% |
| **2 marks** | 8-12 | 16-24 | 32-48% |
| **3 marks** | 5-7 | 15-21 | 30-42% |
| **4 marks** | 2-3 | 8-12 | 16-24% |
| **5 marks** | 0-1 | 0-5 | 0-10% |

### Section Breakdown (Typical Final Exam)

Based on Past Exam 1 and 2 structure:

| Section | Questions | Approximate Marks | Percentage |
|---------|-----------|-------------------|------------|
| **Analysis of Algorithms** | 3-5 | 8-12 | 16-24% |
| **Graphs** | 8-10 | 18-25 | 36-50% |
| **Data Structures** | 2-3 | 4-8 | 8-16% (reduced) |
| **Applications** | 3-5 | 10-15 | 20-30% |

**Note:** Data Structures section reduced due to hash tables and suffix arrays being out of syllabus.

---

## Marks Distribution by Question Type

### Multiple Choice Questions (MCQ)

#### Single-Answer MCQ
- **Typical Marks:** 1-3 marks
- **Common Topics:**
  - Recurrence relations (complexity analysis)
  - Sorting algorithm properties (stability, complexity)
  - Graph algorithm properties (correctness)
  - Data structure complexity (worst-case operations)

**Examples:**
- "Which recurrence relation is TRUE?" (2-3 marks)
- "Which sorting algorithm is stable?" (1-2 marks)
- "What is the height of the BFS tree?" (1 mark)

#### Multiple-Answer MCQ
- **Typical Marks:** 2-3 marks
- **Common Topics:**
  - Algorithm properties (multiple true statements)
  - Graph algorithm correctness
  - Data structure operations
  - Complexity analysis

**Examples:**
- "Select all correct statements about insertion sort" (2 marks)
- "Which data structures cause Θ(N) insert complexity?" (2 marks)
- "Which statements about MST algorithms are TRUE?" (2 marks)

### Written/Open Response Questions

- **Typical Marks:** 2-5 marks
- **Common Topics:**
  - Algorithm design and justification
  - Proof of correctness (loop invariants)
  - Complexity analysis with explanation
  - Problem modeling (graphs, flow networks)
  - Algorithm modification

**Examples:**
- "Justify why Quickselect with median-of-medians achieves O(N)" (2 marks)
- "Describe algorithm to sort N integers in O(N) time" (2 marks)
- "Model as max-flow problem and solve with Ford-Fulkerson" (3-4 marks)
- "Design O(N log N) algorithm for interval scheduling" (3 marks)
- "Prove correctness using loop invariant" (4 marks)

### Numerical/Calculation Questions

- **Typical Marks:** 1-2 marks
- **Common Topics:**
  - Algorithm execution tracing
  - Graph algorithm results (Bellman-Ford, Floyd-Warshall)
  - Tree operations (AVL rotations)
  - Counting problems (topological orderings, path counting)

**Examples:**
- "What is dist[A]+dist[B]+dist[C] after iteration 2?" (2 marks)
- "How many distinct topological orderings?" (3 marks)
- "What is the root after these AVL operations?" (1 mark)
- "What is the maximum flow?" (1-2 marks)

### Algorithm Tracing/Execution Questions

- **Typical Marks:** 2-3 marks
- **Common Topics:**
  - BFS/DFS traversal order
  - Bellman-Ford edge relaxation
  - Floyd-Warshall iteration
  - AVL tree rotations
  - 2-3 tree insertions
  - ~~Suffix array prefix doubling~~ 🚫 **OUT OF SYLLABUS**

**Examples:**
- "Perform BFS starting from A with alphabetical tie-breaking" (1-2 marks)
- "What is dist[E] after first Bellman-Ford iteration?" (1 mark)
- "Show AVL tree after delete and insert operations" (2-3 marks)
- "Show 2-3 tree after inserting sequence of values" (2 marks)

---

## Topic Coverage by Question Type

### Analysis of Algorithms

**Topics:**
- Program verification (correctness, termination)
- Complexity analysis (time, space, asymptotic)
- Recurrence relations
- Loop invariants

**Question Types:**
| Type | Typical Marks | Example Topics |
|------|---------------|----------------|
| **MCQ** | 2-3 | Recurrence relation solutions, complexity comparisons |
| **Written** | 3-4 | Loop invariant proofs, complexity justification |
| **Numerical** | 1-2 | Algorithm runtime counting |

**Mid-Semester:** ✓ Heavily tested
**Final Exam:** ✓ Continues to appear (15-20% of marks)

---

### Sorting and Selection

**Topics:**
- Comparison sorts (insertion, selection, merge, quick, heap)
- Non-comparison sorts (counting, radix)
- Selection algorithms (quickselect, median-of-medians)
- Properties (stability, in-place, adaptivity)

**Question Types:**
| Type | Typical Marks | Example Topics |
|------|---------------|----------------|
| **MCQ** | 1-2 | Stability, best/worst-case complexity |
| **Written** | 2-3 | Algorithm design (e.g., radix sort with base conversion) |
| **Applications** | 3-4 | Using quickselect for percentile problems |

**Mid-Semester:** ✓ Core topic
**Final Exam:** ✓ Tested as applications (10-15% of marks)

---

### Divide and Conquer

**Topics:**
- Karatsuba multiplication
- Merge sort and variants
- Counting inversions

**Question Types:**
| Type | Typical Marks | Example Topics |
|------|---------------|----------------|
| **MCQ** | 2 | Recurrence relation analysis |
| **Written** | 2-3 | Algorithm design and analysis |

**Mid-Semester:** ✓ Core topic
**Final Exam:** ✓ Less emphasized, mostly in recurrence questions

---

### Graph Basics and Traversal

**Topics:**
- Graph representations (adjacency matrix vs list)
- DFS and BFS
- Connected components
- Cycle detection
- Topological sorting

**Question Types:**
| Type | Typical Marks | Example Topics |
|------|---------------|----------------|
| **MCQ** | 2 | Complexity of graph operations by representation |
| **Execution** | 1-2 | BFS/DFS traversal order |
| **Written** | 2-3 | Algorithm modification (e.g., DFS to topological sort) |
| **Numerical** | 1-3 | Tree height, component count, topological orderings |

**Mid-Semester:** ✓ Core topic (20-30% of marks)
**Final Exam:** ✓ Foundation for advanced topics (15-20% of marks)

---

### Shortest Path Algorithms

**Topics:**
- BFS (unweighted)
- Dijkstra (non-negative weights)
- Bellman-Ford (negative edges)
- Floyd-Warshall (all-pairs)

**Question Types:**
| Type | Typical Marks | Example Topics |
|------|---------------|----------------|
| **MCQ** | 2-3 | Algorithm properties, correctness conditions |
| **Numerical** | 1-3 | Distance calculations after k iterations |
| **Written** | 3 | Algorithm design using shortest paths |

**Mid-Semester:** ✓ Dijkstra and BFS (greedy section)
**Final Exam:** ✓ All variants heavily tested (20-25% of marks)

---

### Greedy Algorithms (MST)

**Topics:**
- Prim's algorithm
- Kruskal's algorithm
- Union-Find data structure
- Maximum spanning tree

**Question Types:**
| Type | Typical Marks | Example Topics |
|------|---------------|----------------|
| **MCQ** | 2 | Algorithm properties, negative edges, uniqueness |
| **Written** | 3-4 | Problem modeling (clustering, network design) |
| **Numerical** | 2-3 | MST construction, edge selection |

**Mid-Semester:** ✓ Core topic (15-20% of marks)
**Final Exam:** ✓ Continues to appear (10-15% of marks)

---

### Dynamic Programming

**Topics:**
- Optimal substructure
- Overlapping subproblems
- Bottom-up vs top-down
- Backtracking solutions
- Classical problems (knapsack, edit distance, matrix chain, grid paths)

**Question Types:**
| Type | Typical Marks | Example Topics |
|------|---------------|----------------|
| **MCQ** | 2 | DP properties, complexity analysis |
| **Written** | 3-5 | Algorithm design, recurrence formulation |
| **Numerical** | 2-3 | Backtracking from DP table |

**Mid-Semester:** ✗ NOT covered
**Final Exam:** ✓ Major topic (20-25% of marks)

---

### Network Flow

**Topics:**
- Maximum flow (Ford-Fulkerson, Edmonds-Karp)
- Min-cut max-flow theorem
- Residual networks
- Circulation with demands
- Bipartite matching
- Applications (assignment problems)

**Question Types:**
| Type | Typical Marks | Example Topics |
|------|---------------|----------------|
| **MCQ** | 1-2 | Minimum cut vertex sets |
| **Numerical** | 1-2 | Maximum flow value |
| **Written** | 3-4 | Problem modeling, feasibility analysis |

**Mid-Semester:** ✗ NOT covered
**Final Exam:** ✓ Significant topic (15-20% of marks)

---

### Data Structures (Advanced)

**Topics:**
- AVL trees (rotations, balance factors)
- ~~Hash tables (probing, collision resolution)~~ 🚫 **OUT OF SYLLABUS**
- ~~Suffix arrays (prefix doubling)~~ 🚫 **OUT OF SYLLABUS**
- Suffix trees/tries
- 2-3 trees, Red-Black trees

**Question Types:**
| Type | Typical Marks | Example Topics |
|------|---------------|----------------|
| **MCQ** | 2 | Complexity analysis, properties |
| **Numerical** | 1-2 | Tree operations results (AVL, 2-3 trees) |
| **Written** | 2-3 | String algorithms (suffix trees/tries) |

**Mid-Semester:** ✗ NOT covered
**Final Exam:** ✓ Moderate coverage (~8-12% of marks, reduced due to hash tables/suffix arrays removal)

**🚫 Important Note:** Hash tables and suffix arrays are **OUT OF SYLLABUS this semester**. Not examinable in mid-semester OR final exam.

---

## Question Format Patterns by Topic

This section identifies which topics consistently appear as **long answer/application problems** (3-5 marks) versus topics that remain **MCQ/numerical only**.

### Topics ALWAYS Asked as Long Answer/Application Problems

These topics consistently appear as written response questions requiring algorithm design, problem modeling, or detailed explanations (worth 3-5 marks):

| Topic | Typical Question Format | Marks Range | Exam Frequency |
|-------|------------------------|-------------|----------------|
| **Dynamic Programming** | Design DP solution with recurrence formulation | 3-5 marks | **Every final exam** |
| **Network Flow Applications** | Model problem as max-flow/bipartite matching | 3-4 marks | **Every final exam** |
| **Bipartite Matching** | Student-company, resource allocation problems | 3-4 marks | **Every final exam** |
| **Order Statistics Applications** | Quickselect for percentile/ranking problems | 3-4 marks | Most exams |
| **MST Applications** | Clustering, network design problems | 3-4 marks | Mid-sem + final |
| **Algorithm Modification** | Modify DFS/BFS for specific tasks | 2-3 marks | Most exams |
| **Loop Invariant Proofs** | Full correctness proof (initialization, maintenance, termination) | 3-4 marks | Most exams |
| **Interval Scheduling** | Greedy algorithm design | 3 marks | Common |
| **Circulation with Demands** | Feasibility analysis and justification | 3-4 marks | Final exams |

**Study Strategy:** These require deep understanding and practice. Cannot be memorized. Must practice:
- Formulating recurrence relations (DP)
- Modeling real-world problems as graphs/flow networks
- Writing clear algorithm descriptions with complexity analysis

---

### Topics ONLY Asked as MCQ/Numerical (Never Long Application)

These topics **never** appear as long answer/application problems. They are tested only through:
- Multiple choice questions (properties, complexity)
- Numerical execution (tracing algorithm steps)
- Short calculations

| Topic | Question Types | Marks Range | Why No Long Answer? |
|-------|---------------|-------------|---------------------|
| ~~**Hash Tables**~~ 🚫 | ~~MCQ about complexity, probing types~~ | ~~2 marks~~ | **OUT OF SYLLABUS** |
| ~~**Suffix Arrays**~~ 🚫 | ~~MCQ/numerical about prefix doubling~~ | ~~2 marks~~ | **OUT OF SYLLABUS** |
| **AVL Trees** | Numerical about rotations after insert/delete | 1-2 marks | Mechanical execution only |
| **Recurrence Relations** | MCQ about solving recurrences | 2-3 marks | Direct application of Master's theorem |
| **Sorting Properties** | MCQ about stability, in-place, complexity | 1-2 marks | Recall of properties |
| **Graph Representation Complexity** | MCQ matching operations to complexity | 2-3 marks | Theoretical comparison |
| **BFS/DFS Traversal Order** | Numerical execution | 1-2 marks | Mechanical tracing |
| **2-3 Trees** | Numerical about insertions | 2 marks | Execution only |

**Study Strategy:** Focus on:
- Memorizing properties and complexity results
- Practicing mechanical execution (AVL rotations, 2-3 tree insertions, traversals)
- Quick recall for MCQs
- **Note:** Hash tables and suffix arrays removed from syllabus

---

### Topics Asked in BOTH Formats

These topics can appear as either MCQ/numerical OR as written application problems:

| Topic | MCQ Format | Long Answer Format |
|-------|-----------|-------------------|
| **Shortest Paths** | Properties MCQ (2 marks) | Rarely: problem design using shortest paths |
| **MST Algorithms** | Properties MCQ (2 marks) | Applications: clustering, network design (3-4 marks) |
| **Loop Invariants** | Select correct invariant MCQ (1 mark) | Full proof (3-4 marks) |
| **Complexity Analysis** | Compare complexity MCQ (2 marks) | Justify algorithm complexity (2-3 marks) |
| **Sorting Algorithms** | Properties MCQ (2 marks) | Design custom sort (e.g., radix with base conversion) |

---

## Study Recommendations

### For Mid-Semester Test

**High Priority (60-70% of marks):**
1. **Recurrence Relations** (MCQ, 2 marks)
   - Master's theorem application
   - Telescoping method
   - Recursion tree method

2. **Order Statistics / Selection** (Open Response, 2 marks)
   - Quickselect algorithm and complexity
   - Median-of-medians intuition
   - Application problems

3. **Graph Basics** (Numerical, 2 marks)
   - Traversal algorithms
   - Graph properties
   - Problem modeling

**Medium Priority (20-30% of marks):**
4. **Sorting Algorithms** (MCQ, 2 marks)
   - Properties: stability, complexity, in-place
   - Variants and modifications

5. **Greedy Algorithms** (Open Response, 2 marks)
   - MST algorithms (Prim, Kruskal)
   - Problem applications

**Practice Focus:**
- **MCQ:** 40% of marks (2 questions) - Know definitions and properties cold
- **Open Response:** 40% of marks (2 questions) - Practice explaining algorithms clearly
- **Numerical:** 20% of marks (1 question) - Trace algorithms carefully

---

### For Final Exam

**High Priority Topics (50-60% of marks):**
1. **Dynamic Programming** (20-25% of marks)
   - DP table formulation
   - Recurrence relations
   - Backtracking solutions
   - Grid path problems

2. **Shortest Path Algorithms** (20-25% of marks)
   - Bellman-Ford execution
   - Floyd-Warshall all-pairs
   - Algorithm comparison

3. **Network Flow** (15-20% of marks)
   - Maximum flow calculation
   - Minimum cut identification
   - Bipartite matching modeling
   - Circulation with demands

**Medium Priority (30-35% of marks):**
4. **Graph Algorithms** (15-20% of marks)
   - Traversal (BFS, DFS)
   - Topological sorting
   - MST algorithms

5. **Data Structures** (~8-12% of marks, reduced)
   - AVL tree operations
   - 2-3 trees
   - ~~Hash table analysis~~ 🚫 **OUT OF SYLLABUS**
   - ~~Suffix arrays~~ 🚫 **OUT OF SYLLABUS**
   - **Note:** These are MCQ/numerical only, never long answer

**Lower Priority (15-20% of marks):**
6. **Analysis & Complexity** (15-20% of marks)
   - Still important but less emphasized
   - Recurrence relations
   - Loop invariants

**Practice Focus by Question Type:**
- **MCQ (Single):** 15-20% of marks - Quick recall
- **MCQ (Multiple):** 10-15% of marks - Deep understanding
- **Written:** 35-45% of marks - Algorithm design and justification
- **Numerical:** 15-20% of marks - Careful tracing
- **Applications:** 20-25% of marks - Problem modeling

---

### Question Type Strategy

#### For Multiple Choice (25-35% of total marks)

**Strategy:**
1. Read all options before answering
2. Eliminate obviously wrong answers first
3. For "select all that apply," treat each option independently
4. Watch for edge cases and special conditions
5. Time allocation: ~1-2 minutes per mark

**Common MCQ Topics:**
- Algorithm complexity comparisons
- Correctness conditions
- Data structure operation costs
- Graph algorithm properties

#### For Written Response (35-45% of total marks)

**Strategy:**
1. Structure your answer clearly (algorithm steps, justification, complexity)
2. For correctness proofs: State invariant → prove initialization → prove maintenance → prove termination
3. For algorithm design: High-level idea → detailed steps → complexity analysis
4. Show your work for partial credit
5. Time allocation: ~2-3 minutes per mark

**Common Written Topics:**
- Algorithm design and justification
- Loop invariant proofs
- Problem modeling (graphs, flow networks)
- Complexity analysis with explanation

#### For Numerical/Execution (15-25% of total marks)

**Strategy:**
1. Read the question carefully for exact requirements
2. Show intermediate steps when possible
3. Double-check calculations
4. For graph algorithms: Draw diagrams
5. Time allocation: ~1.5-2 minutes per mark

**Common Numerical Topics:**
- Algorithm execution (Bellman-Ford, Floyd-Warshall)
- Tree operations (AVL rotations)
- Counting problems (paths, orderings)
- Flow/cut calculations

---

## Exam Time Management

### Mid-Semester Test (10 marks, ~30-45 minutes estimated)

- **5 minutes:** Read all questions, identify easy wins
- **25-35 minutes:** Solve questions (2 marks × 5 = 10 marks)
  - MCQ: ~3-4 minutes each (4 marks total)
  - Open response: ~8-10 minutes each (4 marks total)
  - Numerical: ~3-5 minutes (2 marks)
- **5 minutes:** Review and check answers

**Rate:** ~3-4.5 minutes per mark

### Final Exam (50 marks, 130 minutes)

- **10 minutes:** Read all questions, identify easy wins
- **105 minutes:** Solve questions
  - MCQ (1-2 marks): ~1.5-2 minutes per mark
  - Written (2-5 marks): ~2.5-3 minutes per mark
  - Numerical (1-3 marks): ~2 minutes per mark
- **15 minutes:** Review and check answers

**Rate:** ~2.6 minutes per mark (50 marks / 130 minutes = 2.1 min/mark solving time)

**Recommended Order:**
1. **Quick wins:** All 1-mark MCQs (5-8 minutes)
2. **Medium MCQs:** 2-3 mark questions (15-20 minutes)
3. **Numerical:** Algorithm execution (10-15 minutes)
4. **Written:** Shorter responses 2-3 marks (20-30 minutes)
5. **Applications:** Longer 4-5 mark questions (30-40 minutes)
6. **Review:** Check all answers (15 minutes)

---

## Summary Statistics

### Mid-Semester Test

| Metric | Value |
|--------|-------|
| **Total Marks** | 10 |
| **Total Questions** | 5 |
| **Average Marks per Question** | 2 |
| **MCQ Percentage** | 40% (4 marks) |
| **Written Percentage** | 40% (4 marks) |
| **Numerical Percentage** | 20% (2 marks) |

### Final Exam

| Metric | Value |
|--------|-------|
| **Total Marks** | 50 |
| **Total Questions** | 20-26 (typical: 22) |
| **Average Marks per Question** | 2-2.5 |
| **MCQ Percentage** | 25-35% (12-18 marks) |
| **Written Percentage** | 35-45% (18-22 marks) |
| **Numerical Percentage** | 15-25% (8-12 marks) |

---

## Topic Weight Comparison

### Mid-Semester vs Final Exam

| Topic | Mid-Sem Weight | Final Exam Weight | Change |
|-------|----------------|-------------------|--------|
| **Analysis of Algorithms** | 20% (2 marks) | 15-20% (8-10 marks) | Maintained |
| **Sorting & Selection** | 40% (4 marks) | 10-15% (5-8 marks) | Decreased |
| **Divide & Conquer** | Implicit | 5% (2-3 marks) | Decreased |
| **Graph Basics** | 20% (2 marks) | 15-20% (8-10 marks) | Maintained |
| **Greedy (MST)** | 20% (2 marks) | 10-15% (5-8 marks) | Decreased |
| **Shortest Paths** | Implicit in Greedy | 20-25% (10-12 marks) | **Increased** |
| **Dynamic Programming** | ✗ Not covered | 20-25% (10-12 marks) | **New & Major** |
| **Network Flow** | ✗ Not covered | 15-20% (8-10 marks) | **New & Major** |
| **Advanced Data Structures** | ✗ Not covered | ~8-12% (4-6 marks) | **New** (reduced: hash tables/suffix arrays removed) |

---

## Key Takeaways

### For Mid-Semester Test Preparation

1. **Focus on fundamentals:** Analysis, sorting, basic graphs
2. **Practice explaining:** 40% of marks are open-response
3. **Know algorithm properties:** Stability, complexity, correctness
4. **Master core algorithms:** Quickselect, Dijkstra, MST algorithms
5. **Understand, don't memorize:** Can justify why algorithms work

**✗ Topics to SKIP for mid-semester:**
- AVL trees (rotations, balancing) - Final exam only
- Dynamic Programming (all topics) - Final exam only
- Network Flow (all topics) - Final exam only
- Bellman-Ford / Floyd-Warshall - Final exam only

**🚫 Topics OUT OF SYLLABUS (skip completely):**
- Hash tables (collision resolution, probing)
- Suffix arrays (prefix doubling)

### For Final Exam Preparation

1. **DP is crucial:** 20-25% of marks, **ALWAYS long answer** (3-5 marks per question)
2. **Network flow applications:** Must know how to model problems, **ALWAYS long answer** (3-4 marks)
3. **Shortest paths:** Bellman-Ford and Floyd-Warshall heavily tested (mostly numerical)
4. **Build on mid-semester:** Those topics still appear (~35-40% of final)
5. **Practice problem modeling:** Many "application" questions worth 3-5 marks
6. **Know your data structures:** AVL trees, 2-3 trees appear regularly (**MCQ/numerical only**)
   - ~~Hash tables and suffix arrays~~ removed from syllabus
7. **Time management:** With 50 marks in 130 minutes, efficiency is key

**Focus allocation:**
- **High-value long answer topics (35-40% of exam):** DP, Network Flow, Applications
  - Cannot be memorized, require problem-solving practice
  - Worth 3-5 marks each, build these skills first
- **MCQ/numerical topics (~15-20% of exam, reduced):** AVL trees, 2-3 trees, recurrence relations
  - Quick recall and mechanical execution
  - Worth 1-2 marks each, easier to prepare
  - **Note:** Hash tables and suffix arrays removed from syllabus
- **Mixed format topics (30-35% of exam):** Shortest paths, graphs, MST
  - Some MCQ, some applications

---

**Document maintained by:** FIT2004 Study Group
**Source files:** past_mid/, exams/, examinable_content_mid.txt
**For questions or corrections:** Create an issue in the repository