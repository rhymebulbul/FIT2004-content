# Focused Study Plan for Mid-Semester Test

**Based on:** Your marked weak areas + likely exam format + applied problem probability

---

## CRITICAL: You Need Deep Understanding, Not Superficial Answers

**Your past mid result (0.5/10)** shows you gave surface-level answers without proper justification. The exam wants:
- **WHY** algorithms work (correctness proofs)
- **HOW** to derive complexity (recurrence solving, counting operations)
- **DETAILED** algorithm descriptions (not just naming techniques)

---

## EXAM FORMAT PREDICTION

- **3 MCQ Questions** (2 marks each) = 6 marks
  - Likely: recurrence solving, algorithm comparison, complexity analysis
  - Could be single-answer OR multiple-answer (watch for negative marking!)

- **2 Long Answer Questions** (2 marks each) = 4 marks
  - Likely from applied problems (2-3 questions total from applied)
  - Require: algorithm design + justification + complexity analysis

---

## PRIORITY 1: HIGH-PROBABILITY APPLIED PROBLEMS (Long Answer)

### These are most likely for 2-mark long answer questions:

#### **MUST KNOW - Applied Week 2:**

1. **Counting Inversions (Problem 6)**
   - **Why important**: Classic divide & conquer application
   - **What to know**:
     - Modify merge sort to count split inversions during merge
     - O(n log n) complexity derivation
     - Pseudocode for MERGE-AND-COUNTSPLITINV
   - **Common mistake**: Not explaining WHY merge step counts split inversions

2. **Recurrence Solving (Problems 1, 3, 4, 9, 10, 11)**
   - **Why important**: Very common MCQ topic
   - **What to know**:
     - Telescoping method step-by-step
     - Master theorem (when to use each case)
     - Recognizing patterns: T(n-1), T(n/2), T(n-2)
   - **Common mistake**: Skipping steps in telescoping, not stating final Θ-bound

#### **MUST KNOW - Applied Week 3:**

3. **Stabilizing Comparison Sorts (Problem 1)**
   - **Why important**: Fundamental sorting property
   - **What to know**:
     - Method: pair each element with original index (aᵢ, i)
     - Compare by value first, then by index
     - Space overhead: Θ(n), no time complexity change
   - **Common mistake**: Not explaining why index breaks ties correctly

4. **Merging k Sorted Lists (Problem 2)**
   - **Why important**: Tests divide-and-conquer + data structure knowledge
   - **What to know**:
     - Naive O(nk): scan all k lists for each of n elements
     - Better O(n log k): divide-and-conquer OR priority queue
     - Lower bound proof: k=n reduces to sorting → Ω(n log n)
   - **Common mistake**: Not explaining BOTH methods or missing lower bound

5. **Radix Sort for Variable Strings (Problem 3)**
   - **Why important**: Non-comparison sorting optimization
   - **What to know**:
     - Naive O(ℓk) pads all strings to max length
     - Optimal O(n): sort by length first, process only relevant strings
     - Key insight: track pointer j for strings of length ≥ i
   - **Common mistake**: Not explaining space/time trade-off clearly

6. **In-Place Duplicate Removal (Problem 4)**
   - **Why important**: Tests in-place algorithm design
   - **What to know**:
     - Sort first (using in-place sort like Heapsort)
     - One pass: copy non-duplicates forward, overwrite duplicates
     - O(n log n) time, O(1) space
   - **Common mistake**: Not specifying which sort to use or why it's in-place

#### **MUST KNOW - Applied Week 4:**

7. **Quickselect Average Case Analysis (Problem 1)**
   - **Why important**: YOU FAILED THIS ON PAST MID (0.5/10)
   - **What to know**:
     - Good pivot = 25th to 75th percentile (middle 50%)
     - Worst good pivot case: recurse on 75% of array
     - Geometric series: T(n) = cn(1 + 0.75 + 0.75² + ...) = cn/(1-0.75) = 4cn = O(n)
     - Expected tries for good pivot = 2 (50% probability)
     - Final: 2 × 4cn = 8cn = O(n)
   - **Common mistake**: Just saying "70-30 split" without geometric series proof ← THIS IS WHAT YOU DID

8. **Locks & Keys Matching (Problem 2)**
   - **Why important**: Clever Quicksort application
   - **What to know**:
     - Pick arbitrary lock, find matching key (n comparisons)
     - Use matching key to partition locks (n-1 comparisons)
     - Recurse on left/right subsets
     - O(n log n) average case (like Quicksort)
   - **Common mistake**: Not explaining why this is similar to Quicksort partitioning

9. **k Closest to Median (Problem 3)**
   - **Why important**: Multiple algorithm composition
   - **What to know**:
     - Step 1: Quickselect to find median in Θ(n)
     - Step 2: Virtual array of |x - median| for each element
     - Step 3: Quickselect for kth smallest absolute difference in Θ(n)
     - Step 4: Take all elements with difference ≤ kth value
     - Total: Θ(n), no extra space
   - **Common mistake**: Copying array instead of using virtual interpretation

#### **MUST KNOW - Applied Week 5:**

10. **Two-Coloring / Bipartite Check (Problem 1)**
    - **Why important**: Graph property detection
    - **What to know**:
      - DFS: color start vertex arbitrarily, neighbors get opposite color
      - If neighbor already has same color → not two-colorable
      - O(V + E) time
      - Pseudocode for DFS with color parameter
    - **Common mistake**: Not handling disconnected components

11. **Counting Valid Two-Colorings (Problem 2)**
    - **Why important**: Builds on Problem 1
    - **What to know**:
      - First check if two-colorable (Problem 1)
      - If yes: answer = 2^(number of connected components)
      - Each component can be colored 2 ways (flip all colors)
    - **Common mistake**: Not explaining why formula is 2^components

12. **Cycle Detection in Directed Graphs (Problem 3)**
    - **Why important**: More complex than undirected case
    - **What to know**:
      - Three states: Unvisited, Active, Inactive
      - Active = currently exploring descendants
      - If edge leads to Active vertex → cycle found
      - If edge leads to Inactive vertex → different branch, no cycle
      - Pseudocode with status array
    - **Common mistake**: Using undirected cycle detection (doesn't work)

13. **Multi-Source Shortest Path (Problem 4)**
    - **Why important**: BFS modification
    - **What to know**:
      - Initialize queue with ALL source vertices at distance 0
      - BFS proceeds normally
      - First vertex to reach any node is closest source
      - Alternative: add super-source connected to all sources, subtract 1 from distances
    - **Common mistake**: Not explaining why first-to-reach is optimal

---

## PRIORITY 2: LIKELY MCQ TOPICS

### These are prime candidates for 3 MCQ questions:

#### **Recurrence Relations** (VERY HIGH PROBABILITY)

- **Q1.3**: T(n) = T(n-2) + c*n² + d → Solve and give Θ-bound
  - **Study**: Applied Week 2, Problems 1, 3, 9, 10, 11
  - **Key skill**: Telescoping step-by-step

- **Q1.5**: Master Theorem application
  - **Study**: Applied Week 2, Problem 12
  - **Three cases**: Compare f(n) with n^(log_b a)

#### **Loop Invariants** (HIGH PROBABILITY)

- **Q1.9**: Fill in blanks for bubble sort invariant
  - **Study**: Quiz 2 solution (already in repo)
  - **Pattern**: A[1...i] contains i smallest elements in sorted order

- **Q1.10**: Counting algorithm invariant
  - **Study**: Applied Week 3, Problem 7
  - **Pattern**: count equals occurrences in A[1..i-1]

- **Q1.11**: Insertion sort invariant
  - **Study**: Applied Week 3, Problem 8
  - **Pattern**: A[1..i] is sorted

#### **Complexity Analysis Comparisons** (HIGH PROBABILITY)

- **Q3.1**: Insertion sort with binary search
  - **Key insight**: O(n log n) comparisons but O(n²) time due to shifts
  - **Lesson**: Comparison model doesn't capture movement cost

- **Q3.4**: Hybrid Mergesort + Insertion sort
  - **Formula**: Θ(nk + n log(n/k))
  - **Reason**: Mergesort down to size k, then Insertion sort on n/k subarrays

#### **Partitioning** (MEDIUM PROBABILITY)

- **Q4.4**: Naive 3-way vs Hoare partitioning
  - **3-way**: Stable, concatenates <, =, > groups
  - **Hoare**: Unstable, in-place swapping

- **Q4.5**: k-way partitioning
  - **Naive O(nk)**: Partition on each pivot sequentially
  - **Better O(n log k)**: Divide-and-conquer on pivots

#### **Graph Properties** (MEDIUM PROBABILITY)

- **Q5.14-Q5.16**: Two-coloring vs Bipartite equivalence
  - **Key**: Graph is bipartite ↔ graph is two-colorable

- **Q5.11**: Directed cycle detection
  - **Key**: Three states (Unvisited, Active, Inactive)

---

## PRIORITY 3: ESSENTIAL THEORY TO MEMORIZE

### Complexity Results (Know by Heart)

```
Comparison-based sorting lower bound: Ω(n log n)
Merge Sort: Θ(n log n) time, Θ(n) space
Counting Sort: Θ(n + k) time, stable
Radix Sort: Θ(d(n + k)) where d = digits
Quickselect average: O(n), worst O(n²)
Quickselect with median-of-medians worst: O(n)
BFS/DFS: Θ(V + E)
Prim/Kruskal: O(E log V)
Dijkstra: O((V + E) log V) with binary heap
Union-Find with both optimizations: O(α(n)) ≈ O(1) amortized
```

### Algorithm Pseudocode Patterns

**For long answer questions, you need clean pseudocode. Practice these templates:**

1. **DFS with state tracking:**
```
function DFS(u, state)
    mark[u] = state
    for each neighbor v of u:
        if mark[v] == ... then
            [handle case]
        else if mark[v] == null then
            DFS(v, new_state)
```

2. **Quickselect pattern:**
```
function QUICKSELECT(A[lo..hi], k)
    if lo >= hi: return A[lo]
    pivot_index = partition(A[lo..hi])
    if k == pivot_index: return A[k]
    else if k < pivot_index: recurse on left
    else: recurse on right
```

3. **Union-Find operations:**
```
function FIND(u):
    if parent[u] != u:
        parent[u] = FIND(parent[u])  // path compression
    return parent[u]

function UNION(u, v):
    root_u, root_v = FIND(u), FIND(v)
    if root_u == root_v: return false
    // union by rank or size
    attach smaller to larger
    return true
```

---

## STUDY PLAN (RECOMMENDED ORDER)

### Day 1-2: Master Recurrence Relations & Quickselect
**Goal**: Never miss a recurrence MCQ again

1. Work through Applied Week 2: Problems 1, 3, 4, 9, 10, 11
   - Write out telescoping steps for each
   - State final Θ-bound with justification

2. **REDO** Quickselect average case analysis (Applied Week 4, Problem 1)
   - Write geometric series from scratch
   - Explain good pivot probability
   - This was your weakest area (0.5/10)

3. Practice: Given random recurrence, solve in <5 minutes

### Day 3-4: Divide & Conquer Applications
**Goal**: Master 2-3 applied problems for long answer

1. **Counting Inversions** (Applied Week 2, Problem 6)
   - Implement in Python
   - Write pseudocode for MERGE-AND-COUNTSPLITINV
   - Explain why merge counts split inversions

2. **k Sorted Lists Merging** (Applied Week 3, Problem 2)
   - Implement both O(nk) and O(n log k) versions
   - Write pseudocode for divide-and-conquer approach
   - Prove lower bound

3. **Variable Length Radix Sort** (Applied Week 3, Problem 3)
   - Understand why naive is O(ℓk)
   - Explain optimal O(n) approach with length sorting

### Day 5-6: Graph Algorithms (Applied Problems)
**Goal**: Strong on graph problem design

1. **Two-Coloring** (Applied Week 5, Problems 1 & 2)
   - Write DFS pseudocode with color parameter
   - Derive 2^components formula

2. **Cycle Detection in Directed Graphs** (Applied Week 5, Problem 3)
   - Understand three-state approach
   - Explain why Active state is necessary

3. **Multi-Source BFS** (Applied Week 5, Problem 4)
   - Explain modification to BFS
   - Justify correctness

### Day 7: Loop Invariants & Sorting Theory
**Goal**: Nail loop invariant MCQs + sorting comparisons

1. **Loop Invariants**:
   - Bubble sort (Quiz 2)
   - Counting algorithm (Applied Week 3, Problem 7)
   - Insertion sort (Applied Week 3, Problem 8)
   - Practice: state invariant, prove base case, prove inductive step

2. **Sorting Comparisons**:
   - Insertion sort with binary search (complexity paradox)
   - Stabilizing sorts (Applied Week 3, Problem 1)
   - Hybrid algorithms (Applied Week 4, Problem 4)

### Day 8: MST Applications & Final Review
**Goal**: Clustering problem + weak areas

1. **Clustering with MST** (Past Mid Q4)
   - Build MST, remove k-1 largest edges
   - Prove why this maximizes minimum inter-cluster distance
   - Complexity: O(E log V)

2. **Review weakness**:
   - Redo any applied problems you struggled with
   - Practice writing clean pseudocode under time pressure

### Day 9-10: Mock Exam & Timed Practice

**Mock Exam Format:**
- Set timer: 2 hours
- 3 MCQ questions (choose from unfamiliar applied problems)
- 2 Long answer (choose complex applied problems)

**Self-Grade Using:**
- Partial credit: algorithm description (1 mark), justification + complexity (1 mark)
- Aim for 8-10/10

---

## HOW TO ANSWER LONG ANSWER QUESTIONS (AVOID 0.5/10)

### Bad Answer Example (Your Past Mid):
**Q: Justify why Quickselect with median-of-medians is O(n)**
❌ "Because the 70-30 split means we recurse on smaller array" (0.5/2 marks)

### Good Answer Example:
**Q: Justify why Quickselect with median-of-medians is O(n)**
✅ Answer should include:

1. **Good pivot definition**: Median-of-medians guarantees pivot in 30th-70th percentile
2. **Worst case recurse size**: At most 70% of array (when pivot at 30th percentile and target is in larger partition)
3. **Recurrence**: T(n) ≤ T(0.7n) + O(n) [finding median-of-medians] + O(n) [partition]
4. **Solving recurrence**:
   - T(n) ≤ T(0.7n) + cn
   - T(n) ≤ T(0.7²n) + 0.7cn + cn
   - T(n) ≤ cn(1 + 0.7 + 0.7² + ...) = cn/(1-0.7) = cn/0.3 ≈ 3.33cn
5. **Conclusion**: T(n) = O(n) ✓

**(This gets full 2 marks)**

### Answer Template for Algorithm Design:

```
1. ALGORITHM DESCRIPTION (0.5 marks)
   - High-level approach in 2-3 sentences
   - Reference known algorithms if applicable

2. PSEUDOCODE OR DETAILED STEPS (0.5 marks)
   - Clear, structured pseudocode OR
   - Step-by-step algorithm execution

3. JUSTIFICATION (0.5 marks)
   - WHY algorithm is correct
   - Key insight that makes it work
   - Handle edge cases if relevant

4. COMPLEXITY ANALYSIS (0.5 marks)
   - Derive time/space complexity
   - Show recurrence if applicable
   - State final Θ-bound
```

---

## FINAL CHECKLIST BEFORE EXAM

### Can you do these in <10 minutes each?

- [ ] Solve T(n) = T(n-2) + cn² + d using telescoping
- [ ] Explain Quickselect average case O(n) with geometric series
- [ ] Write pseudocode for counting inversions (merge sort variant)
- [ ] Describe O(n log k) algorithm for merging k sorted lists
- [ ] Write DFS pseudocode for two-coloring
- [ ] Explain why directed cycle detection needs three states
- [ ] State loop invariant for insertion sort and prove correctness
- [ ] Explain why insertion sort with binary search is still O(n²)
- [ ] Describe clustering algorithm using MST (remove k-1 largest edges)
- [ ] Calculate number of valid two-colorings (2^components formula)

### If you can't do any of the above fluently:
→ That's your focus area for remaining study time

---

## EXAM DAY STRATEGY

1. **Read ALL questions first** (2 minutes)
   - Identify easiest questions
   - Plan time allocation

2. **Do MCQs first** (30 minutes)
   - If stuck, eliminate wrong answers
   - For multiple-answer MCQs: only mark if you're confident (negative marking!)

3. **Long answers** (remaining time)
   - Use template above (description, pseudocode, justification, complexity)
   - If running out of time: write bullet points for partial credit
   - Never skip complexity analysis (often worth 0.5 marks)

4. **Final 10 minutes**:
   - Check you answered all parts
   - Verify complexity bounds have Θ/O/Ω notation
   - Ensure pseudocode has proper structure

---

**Remember**: You got 0.5/10 because you gave surface answers. The exam wants:
- **Detailed justifications** (not just naming techniques)
- **Recurrence solving** (show all steps)
- **Correct terminology** (Θ vs O, stable vs in-place, etc.)

Good luck! 🚀
