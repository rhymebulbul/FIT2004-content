# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a FIT2004 (Algorithms and Data Structures) learning repository containing Python implementations of fundamental algorithms, study materials, and exam preparation resources. The focus is on practical algorithm implementations with detailed complexity analysis.

**Important Context**: This repository is being used to prepare for a **deferred mid-semester test**. The mid-semester content is complete, while final exam content is still being populated.

## Repository Structure

```
implementations-algorithms/    # Algorithm implementations organized by week (15 files)
├── w1/                       # Divide and Conquer (binarySearch, mergeSort, countInversions)
├── w2/                       # Sorting algorithms (selectionSort, countingSort, radixSort, findingMin)
├── w3/                       # Order Statistics (quickselect)
├── w5/                       # Graph algorithms (dijkstra, prim, kruskal, unionFind, main)
└── w6/                       # Dynamic Programming (coinChangeTopDown, coinChangeBottomUp)

course_notes/                 # Structured course notes in JSON format (12 files)
├── chap_one.json through chap_eleven.json, plus notes.txt

lecture/                      # Lecture materials (12 files: l1.json through l12.json)

weekly_quiz/                  # Quiz questions (11 files: q1.json through q11.json)

exams/                        # Exam questions and solutions (7 files)
├── 21-1.json, 25-1.json     # Past exams from 2021, 2025
├── s1.json, s2.json, s3.json # Practice exam sets
├── EXAM_MARKS_DISTRIBUTION.md
└── FINAL_EXAM_QUESTION_PATTERNS.md

mid_semester_test/            # Dedicated mid-semester prep materials (13 files)
├── FOCUSED_STUDY_PLAN.md
├── MID_SEMESTER_TOPICS_CHECKLIST.md
├── README.md
├── analysis/                 # Recurrence relations guides
└── order_statistics/         # Quickselect guides + 8 Python tracer examples

past_mid/                     # Past mid-semester exam materials (5 files)
├── question.json, solution.json
├── mid_semester_study_guide.md
├── network_infection_problems.md
└── syllabus.json

prep_solutions/               # Preparation solutions (13 files)
├── prep.json, prep1.json through prep12.json

applied_solutions/            # Applied problem solutions (11 files)
├── 2.txt through 6.txt      # Text-format solutions
└── 12.json                  # JSON-format solution

topics/                       # Topic-specific study guides (13 markdown files, ~230KB)
├── LOOP_INVARIANT_QUESTIONS_GUIDE.md (32KB)
├── PROVE_CORRECTNESS_QUESTIONS_GUIDE.md (21KB)
├── PROOF_CHECKLIST.md
├── DAG_TOPOLOGICAL_SORT_EXAM_GUIDE.md (19KB)
├── GRAPH_COMPLEXITY_EXAM_CHEATSHEET.md (11KB)
├── DISCONNECTED_GRAPHS_CHECKLIST.md (60KB)
├── ALGORITHM_EDGE_CASES_CHECKLIST.md (25KB)
├── quick/                   # Quickselect & Order Statistics
│   ├── QUICKSELECT_MEDIANS_EXAM_CHEATSHEET.md (21KB)
│   ├── quickselect_partition_guide.md (11KB)
│   └── k_partitioning_guide.md (21KB)
├── trees/                   # Advanced tree topics
│   ├── prep12_cheatsheet.md
│   └── tree_rebalancing_properties.md
└── recurrence/              # Recurrence relations
    └── recurrence_quick_reference.md

8_DAY_SPACED_REPETITION_SCHEDULE.md  # Strategic spaced repetition study plan (20KB)
examinable_content_mid.txt           # Mid-semester examinable topics (COMPLETE, 160 lines)
examinable_content_exam.txt          # Final exam examinable topics (308 lines, being populated)
README.md                            # Comprehensive repository overview (27KB)
```

## Materials Quick Reference Guide

### Where to Find Specific Content

**Algorithm Implementations:**
- **Divide & Conquer:** `implementations-algorithms/w1/` (binarySearch, mergeSort, countInversions)
- **Sorting:** `implementations-algorithms/w2/` (selectionSort, countingSort, radixSort)
- **Order Statistics:** `implementations-algorithms/w3/quickselect.py`
- **Graph Algorithms:** `implementations-algorithms/w5/` (dijkstra, prim, kruskal, unionFind)
- **Dynamic Programming:** `implementations-algorithms/w6/` (coinChange variants)

**Study Guides by Topic:**
- **Loop Invariants:** `topics/LOOP_INVARIANT_QUESTIONS_GUIDE.md`
- **Correctness Proofs:** `topics/PROVE_CORRECTNESS_QUESTIONS_GUIDE.md` + `topics/PROOF_CHECKLIST.md`
- **Quickselect/Order Statistics:** `topics/quick/` (3 comprehensive guides)
- **Graph Algorithms:** `topics/GRAPH_COMPLEXITY_EXAM_CHEATSHEET.md`, `topics/DAG_TOPOLOGICAL_SORT_EXAM_GUIDE.md`
- **Disconnected Graphs:** `topics/DISCONNECTED_GRAPHS_CHECKLIST.md`
- **Algorithm Edge Cases:** `topics/ALGORITHM_EDGE_CASES_CHECKLIST.md`
- **Recurrence Relations:** `topics/recurrence/recurrence_quick_reference.md`
- **Advanced Trees:** `topics/trees/` (prep12_cheatsheet, tree_rebalancing_properties)

**Exam Preparation:**
- **Mid-Semester Focus:** `mid_semester_test/` (13 files with focused study plan)
- **Past Mid-Semester Exams:** `past_mid/` (questions, solutions, study guide)
- **Final Exam Materials:** `exams/` (past exams 2021, 2025 + practice sets s1-s3)
- **Practice Problems:** `weekly_quiz/` (q1-q11), `prep_solutions/` (prep + prep1-prep12)
- **Applied Problems:** `applied_solutions/` (2.txt through 6.txt, 12.json)

**Conceptual Learning:**
- **Course Notes:** `course_notes/` (chap_one through chap_eleven JSON files)
- **Lecture Materials:** `lecture/` (l1 through l12 JSON files)
- **Study Schedule:** `8_DAY_SPACED_REPETITION_SCHEDULE.md`

**Scope Verification:**
- **Mid-Semester Topics:** `examinable_content_mid.txt` (COMPLETE - authoritative source)
- **Final Exam Topics:** `examinable_content_exam.txt` (being populated)

### Total Materials Count
- **~107 files** covering algorithm implementations, study guides, exam prep, and practice problems
- **All mid-semester content COMPLETE** and ready for deferred test preparation

## Exam Scope and Study Materials

### Mid-Semester Test Content
The **examinable_content_mid.txt** file contains the complete and authoritative list of topics for the mid-semester test. This covers:
- Analysis of Algorithms (verification, complexity, asymptotic notation)
- Divide and Conquer
- Fast Sorting Algorithms
- Order Statistics and Selection
- Graph Basics (traversal, connectivity, shortest paths, topological sorting)
- Greedy Algorithms (Dijkstra, Prim, Kruskal)

### Materials Organization
- **past_mid/**: Past mid-semester exam materials (directly relevant for mid-semester study)
- **exams/**: Contains questions and solutions, some of which are relevant for mid-semester preparation
  - When working with files in exams/, cross-reference with **examinable_content_mid.txt** to determine if the topic is mid-semester relevant
  - Content beyond topics in examinable_content_mid.txt is for the final exam
- **implementations-algorithms/**: w1, w2, w5 are mid-semester relevant; w6+ may be final exam content

### Final Exam Content
**examinable_content_exam.txt** will eventually contain all topics including mid-semester + additional topics (Dynamic Programming graphs, Network Flow, Advanced Trees, Tries/Suffix Trees). This is still being populated.

## Running Code

All Python files in `implementations-algorithms/` are self-contained and can be executed directly:

```bash
python implementations-algorithms/w5/dijkstra.py
python implementations-algorithms/w5/prim.py
python implementations-algorithms/w2/countingSort.py
```

Each implementation file contains:
- The core algorithm implementation with detailed complexity comments
- Test cases in the `if __name__ == "__main__":` block
- Example graph/data structures for demonstration

## Key Algorithm Implementations

### Graph Algorithms (w5/)
- **dijkstra.py**: Single-source shortest paths with non-negative weights using priority queue; O((V+E) log V)
- **prim.py**: Minimum Spanning Tree using greedy vertex selection; O(E log V)
- **kruskal.py**: MST using edge sorting and Union-Find; O(E log E)
- **unionFind.py**: Two implementations:
  - `UnionFindNaive`: Basic implementation
  - `UnionFind`: Optimized with union-by-size (stores negative sizes in parent array)

### Sorting Algorithms (w1/, w2/)
- **mergeSort.py**: Divide-and-conquer sorting; O(n log n)
- **countingSort.py**: Integer sorting with stable implementation; O(n + k)
- **radixSort.py**: Multi-pass sorting using counting sort on digits
- **selectionSort.py**: Basic comparison sort; O(n²)

### Other Algorithms
- **binarySearch.py**: Binary search implementation
- **countInversions.py**: Count inversions using modified merge sort

## Codebase Conventions

### Data Structures
- **Graph Representation**: Adjacency list format as dict: `{node: [(neighbor, weight), ...]}`
- **Union-Find Parent Encoding**: Negative values indicate root with size = |parent[i]|, non-negative values point to parent
- **Priority Queues**: Use Python's `heapq` module for efficient min-heap operations

### Complexity Analysis
All implementations include inline comments documenting:
- Time complexity for each operation
- Overall algorithm complexity
- Space complexity where relevant

### Testing
Each implementation includes test cases demonstrating typical usage. Tests use simple data structures and print results to stdout.

## Course Topics (from examinable_content_exam.txt)

The repository covers these major algorithm categories:
1. **Analysis**: Correctness proofs, complexity analysis, asymptotic notation
2. **Sorting**: Comparison-based (merge, quick, heap) and non-comparison (counting, radix)
3. **Divide and Conquer**: Karatsuba multiplication, merge sort variants
4. **Graph Traversal**: DFS, BFS, topological sorting, connected components
5. **Shortest Paths**: BFS (unweighted), Dijkstra, Bellman-Ford, Floyd-Warshall
6. **Greedy**: Dijkstra, Prim, Kruskal with Union-Find
7. **Dynamic Programming**: Knapsack variants, edit distance, matrix chain
8. **Network Flow**: Ford-Fulkerson, max-flow min-cut, bipartite matching
9. **Trees**: BST, AVL, Red-Black, 2-3 trees
10. **Strings**: Prefix tries, suffix trees

## Development Notes

- Python 3 is used throughout (no specific version requirements found)
- No external dependencies beyond Python standard library (heapq, etc.)
- No test framework; all tests are inline using `if __name__ == "__main__"`
- No build process required
