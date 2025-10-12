# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a FIT2004 (Algorithms and Data Structures) learning repository containing Python implementations of fundamental algorithms, study materials, and exam preparation resources. The focus is on practical algorithm implementations with detailed complexity analysis.

**Important Context**: This repository is being used to prepare for a **deferred mid-semester test**. The mid-semester content is complete, while final exam content is still being populated.

## Repository Structure

```
implementations-algorithms/    # Algorithm implementations organized by week
├── w1/                       # Divide and Conquer (merge sort, binary search, inversions)
├── w2/                       # Sorting algorithms (selection, counting, radix)
├── w5/                       # Graph algorithms (Dijkstra, Prim, Kruskal, Union-Find)
└── w6/                       # Dynamic Programming (coin change)

course_notes/                 # Structured course notes in JSON format
├── chap_one.json through chap_eleven.json

lecture/                      # Lecture materials (l1.json through l9.json)

weekly_quiz/                  # Quiz questions (q1.json through q6.json)

exams/                        # Exam questions and solutions
past_mid/                     # Past mid-semester exam materials
applied_solutions/            # Applied problem solutions (2.txt through 6.txt)
prep_solutions/               # Preparation solutions (prep.json)

examinable_content_mid.txt    # Mid-semester examinable topics (COMPLETE)
examinable_content_exam.txt   # Final exam examinable topics (to be populated)
```

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
