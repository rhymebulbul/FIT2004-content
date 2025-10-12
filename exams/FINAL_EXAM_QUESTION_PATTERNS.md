# FIT2004 Final Exam Question Patterns by Topic

This document analyzes **final exam only** question patterns based on historical exam data (2021-2025). Mid-semester topics are excluded.

**Last Updated:** 2025-10-12
**Source:** Analysis of 5 past final exams (21-1.json, 25-1.json, s1.json, s2.json, s3.json)

**🚫 OUT OF SYLLABUS:** Hash tables and suffix arrays are completely removed and not documented here.

---

## Table of Contents

1. [Dynamic Programming](#dynamic-programming)
2. [Network Flow](#network-flow)
3. [Advanced Shortest Paths](#advanced-shortest-paths)
4. [AVL Trees](#avl-trees)
5. [2-3 Trees](#2-3-trees)
6. [String Algorithms](#string-algorithms)
7. [Advanced Applications](#advanced-applications)

---

## Dynamic Programming

**Exam Frequency:** **Every final exam** (20-25% of marks)

### Question Type Breakdown

| Question Format | Marks | Frequency | Example |
|----------------|-------|-----------|---------|
| **Algorithm Design** | 3-5 marks | Every exam | "Design DP algorithm for grid path problem with O(mn) complexity" |
| **Recurrence Formulation** | 3-4 marks | Most exams | "Formulate DP recurrence for modified knapsack problem" |
| **Backtracking from DP Table** | 2-3 marks | Most exams | "Given DP table, determine which items were selected" |
| **DP Properties MCQ** | 2 marks | Common | "Which statements about DP are FALSE?" |
| **Grid Path Counting** | 3-4 marks | Common | "Count paths from bottom-left to top-right avoiding obstacles" |

### Specific Question Patterns

#### 1. Grid Path Problems (Most Common)
**Pattern:** Given grid with obstacles/constraints, count paths or find optimal path

**Examples from exams:**
- **Past Exam 2, Q20 (4 marks):** "You're on a grid, can only move up/right, some cells blocked. How many ways to reach top-right corner?"
  - **Format:** Numerical answer
  - **Approach:** DP table with `dp[i][j] = dp[i-1][j] + dp[i][j-1]` (blocked cells = 0)
  - **Complexity:** O(rows × cols)

**Common variants:**
- Counting unique paths
- Finding minimum cost path
- Maximum value collection

**Key skills tested:**
- 2D DP table formulation
- Base case identification
- Handling constraints (obstacles)
- Bottom-up computation order

---

#### 2. Modified Knapsack/House Selling Problems
**Pattern:** Selection with constraints where selecting item i affects neighboring items

**Examples from exams:**
- **Past Exam 1, Q9 (2 marks):** "House selling DP: if sell to house i, cannot sell to i-2, i-1, i+1, i+2"
  - **Format:** Backtracking from DP table
  - **Given:** DP array with maximum profits
  - **Task:** Determine which houses were selected

**Common variants:**
- Standard house robbery (can't select adjacent)
- Extended constraints (can't select within k distance)
- Weighted variants

**Key skills tested:**
- Backtracking from DP table
- Understanding optimal substructure
- Reconstructing solution path

---

#### 3. Recurrence Formulation Questions
**Pattern:** Given problem description, write recurrence relation and justify complexity

**Examples from exams:**
- **2025 Final, Q20-21 (marks split):** "DP variant problem"
  - **Format:** Written response
  - **Required:** Recurrence relation, base cases, computation order, complexity

**Common requirements:**
- Define subproblems clearly
- Write recurrence relation
- Identify base cases
- Justify time/space complexity
- Sometimes: provide pseudocode

**Key skills tested:**
- Identifying optimal substructure
- Formulating recurrences from problem descriptions
- Complexity analysis

---

#### 4. MCQ on DP Properties
**Pattern:** True/False questions about DP characteristics

**Examples from exams:**
- **Past Exam 3, Q11 (2 marks):** "Select WRONG statements about DP"
  - Options include: bottom-up vs top-down speed, time complexity formulas

**Common topics:**
- Bottom-up vs top-down comparison
- Time = (number of subproblems) × (time per subproblem)
- Space optimization techniques
- Optimal substructure requirements

**Key skills tested:**
- Understanding DP theory
- Complexity analysis
- Comparing approaches

---

### Study Strategy for DP

**Must practice:**
1. **Grid path problems** - Most common, always appears
   - Practice with obstacles, costs, value collection
   - Master 2D DP table formulation

2. **Backtracking from DP tables** - High frequency
   - Work backwards from DP[n]
   - Understand how decisions were made

3. **Classical problems** - Build foundations
   - 0/1 Knapsack
   - Coin change
   - Edit distance
   - Matrix chain multiplication

4. **Recurrence formulation** - Core skill
   - Practice translating problem descriptions to recurrences
   - Identify what dp[i][j] represents

**Common mistakes to avoid:**
- Off-by-one errors in indices
- Incorrect base cases
- Wrong computation order (must compute dependencies first)
- Forgetting to handle edge cases

---

## Network Flow

**Exam Frequency:** **Every final exam** (15-20% of marks)

### Question Type Breakdown

| Question Format | Marks | Frequency | Example |
|----------------|-------|-----------|---------|
| **Problem Modeling** | 3-4 marks | Every exam | "Model student-company placement as max-flow problem" |
| **Maximum Flow Calculation** | 1-2 marks | Every exam | "What is the maximum flow from s to t?" |
| **Minimum Cut Identification** | 1-2 marks | Most exams | "Which vertices are in the source side of min-cut?" |
| **Circulation with Demands** | 3-4 marks | Most exams | "Which problems have feasible circulation?" |
| **Bipartite Matching** | 3-4 marks | Common | "Model resource allocation as bipartite matching" |

### Specific Question Patterns

#### 1. Bipartite Matching Modeling (Most Common)
**Pattern:** Model assignment/allocation problem as max-flow with capacities

**Examples from exams:**
- **Past Exam 1, Q26 (3 marks):** "123 students, 25 topics. Each student picks ≤4 topics, gets 1. Each topic has ≤5 students. Model as max-flow."
  - **Format:** Written description of network construction
  - **Required:** Vertices, edges, capacities, interpretation

- **Past Exam 2, Q19 (3 marks):** "240 students, 30 companies. Each student picks 1-3 companies, gets 1. Each company accepts 8 students."
  - **Format:** Written response
  - **Required:** Network construction, Ford-Fulkerson explanation

- **Past Exam 3, Q22 (2 marks):** "300 planets, 200 superheroes. Each planet requests up to 10 heroes, needs exactly 1. Each hero defends up to 2 planets."
  - **Format:** MCQ selecting correct model
  - **Options:** Different capacity configurations

**Common variants:**
- Student-company placement
- Resource allocation
- Task assignment
- Project selection

**Key structure:**
```
Source → [Set L: suppliers] → [Set R: demanders] → Sink

Capacities:
- Source → L: supply constraint per supplier
- L → R: 1 (ensures unique assignment)
- R → Sink: demand constraint per demander

Edge existence: only if valid pairing
```

**Key skills tested:**
- Identifying bipartite structure
- Setting correct capacities
- Understanding flow interpretation (flow = assignment)
- Recognizing when to use max-flow

---

#### 2. Maximum Flow Calculation (Numerical)
**Pattern:** Given flow network diagram, calculate maximum flow

**Examples from exams:**
- **Past Exam 1, Q23 (1.5 marks):** Given network with current flow/capacity notation
  - **Current flow:** 4 units
  - **Find:** Maximum possible flow
  - **Answer:** 7
  - **Method:** Identify augmenting paths in residual network

- **Past Exam 2, Q12 (2 marks):** Given flow network
  - **Current flow:** 6 units
  - **Find:** Maximum flow
  - **Answer:** 8
  - **Method:** Find augmenting paths

**Solution approach:**
1. Identify current flow (sum of flows into sink)
2. Look for augmenting paths in residual network
3. Find bottleneck capacity on each path
4. Augment until no paths remain
5. Verify using min-cut

**Key skills tested:**
- Understanding residual networks
- Finding augmenting paths
- Calculating bottleneck capacities
- Verifying with max-flow min-cut theorem

---

#### 3. Minimum Cut Identification
**Pattern:** Given max-flow network, identify vertices in source side of min-cut

**Examples from exams:**
- **Past Exam 1, Q22 (1.5 marks):** "Which edges comprise the minimum cut?"
  - **Format:** Select edges from list
  - **Answer:** s→a, b→a, d→t, c→d (total capacity = max flow)

- **Past Exam 2, Q13 (1 mark):** "Select vertices in S (source side of min-cut)"
  - **Format:** Multiple-choice multiple-answer
  - **Answer:** s, a, b, c
  - **Method:** Find reachable vertices from s in residual graph

**Solution approach:**
1. Run max-flow algorithm to completion
2. In residual graph, find all vertices reachable from source s via BFS/DFS
3. Reachable vertices = source side (S)
4. Unreachable vertices = sink side (T)
5. Min-cut edges go from S to T

**Key skills tested:**
- Max-flow min-cut theorem application
- Residual graph understanding
- Reachability analysis
- Cut capacity verification

---

#### 4. Circulation with Demands (Feasibility)
**Pattern:** Given circulation problem with demands and capacities, determine feasibility

**Examples from exams:**
- **Past Exam 1, Q14 (3 marks):** Two circulation problems given
  - **Problem 1:** demands sum to 0 → feasible
  - **Problem 2:** demands sum ≠ 0 → infeasible
  - **Format:** Multiple choice selecting which are feasible

- **Past Exam 2, Q14 (4 marks):** Two circulation problems
  - **Problem 1:** demands = {-6, 0, 4, 2}, sum = 0, verify via max-flow → feasible
  - **Problem 2:** demands = {-3, 1, 1, 2}, sum = 1 → infeasible

- **Past Exam 3, Q8 (4 marks):** Two circulation problems
  - Check demand sum first
  - Transform to max-flow if sum = 0

**Solution approach:**
1. **Necessary condition:** Check if sum of all demands = 0
   - If ≠ 0, immediately infeasible
2. **Sufficient check:** Transform to max-flow problem
   - Add super-source connected to all supply nodes (positive demand)
   - Add super-sink connected to all demand nodes (negative demand)
   - Run max-flow
   - Feasible iff max-flow saturates all source/sink edges

**Key skills tested:**
- Demand conservation principle
- Transformation to max-flow
- Feasibility criteria
- Flow conservation understanding

---

### Study Strategy for Network Flow

**Must practice:**
1. **Bipartite matching modeling** - Highest marks (3-4 marks)
   - Identify when problem is bipartite matching
   - Set up correct capacity constraints
   - Understand flow = assignment interpretation

2. **Circulation with demands** - Always appears
   - Check sum of demands first
   - Transform to max-flow for verification
   - Understand feasibility conditions

3. **Max-flow calculation** - Mechanical but important
   - Practice finding augmenting paths
   - Calculate bottleneck capacities
   - Verify with min-cut

4. **Problem recognition** - Key skill
   - Can this problem be modeled as flow?
   - What are the constraints? (become capacities)
   - What are we optimizing? (max-flow value)

**Common mistakes to avoid:**
- Wrong capacity on edges (especially matching edges should be 1)
- Forgetting to check demand sum = 0 for circulation
- Not considering backward edges in residual graph
- Incorrect interpretation of flow values

---

## Advanced Shortest Paths

**Exam Frequency:** Every final exam (20-25% of marks, mostly numerical)

### Question Type Breakdown

| Question Format | Marks | Frequency | Example |
|----------------|-------|-----------|---------|
| **Bellman-Ford Execution** | 1-3 marks | Every exam | "What is dist[A]+dist[B]+dist[C] after iteration 2?" |
| **Floyd-Warshall Execution** | 1-3 marks | Most exams | "After k=2 iterations, what is dist[i][j]?" |
| **Algorithm Properties MCQ** | 2-3 marks | Most exams | "Which statements about Bellman-Ford are TRUE?" |
| **Algorithm Comparison** | 2 marks | Common | "When can Dijkstra work with negative edges?" |
| **Negative Cycle Detection** | 2-3 marks | Common | "Does the graph have a negative cycle?" |

### Specific Question Patterns

#### 1. Bellman-Ford Edge Relaxation (Most Common)
**Pattern:** Trace Bellman-Ford for k iterations with specific edge order

**Examples from exams:**
- **Past Exam 1, Q10 (3 marks):** Run Bellman-Ford from source S for 2 iterations
  - **Given:** Edge relaxation order
  - **Task:** Calculate dist[A]+dist[B]+dist[C]+dist[D] after iteration 2
  - **Answer:** 32
  - **Method:** Manually relax edges in given order

- **Past Exam 2, Q10 (3 marks):** Similar, calculate sum after 2 iterations
  - **Answer:** 32

- **Past Exam 3, Q12 (3 marks):** After 2 iterations, find distances and predecessors
  - **Format:** Numerical + predecessor array

**Solution approach:**
1. Initialize: dist[source] = 0, all others = ∞
2. For each iteration:
   - Process edges in given order
   - For each edge (u,v) with weight w:
     - If dist[u] + w < dist[v]:
       - dist[v] = dist[u] + w
       - pred[v] = u
3. Track changes carefully (edge order matters for intermediate results)

**Key skills tested:**
- Understanding edge relaxation
- Careful arithmetic with negative weights
- Tracking distances across iterations
- Understanding why iteration count matters

---

#### 2. Floyd-Warshall Execution
**Pattern:** Calculate distances after k iterations of outer loop

**Examples from exams:**
- **Past Exam 1, Q20 (2 marks):** After outer loop completed 2 iterations, sum specific distances
  - **Answer:** 11
  - **Method:** Floyd-Warshall considers vertices 1,2 as intermediates

- **Past Exam 2, Q11 (3 marks):** After second iteration, calculate dist[4][3]+dist[5][4]+dist[5][6]
  - **Answer:** 46

**Solution approach:**
1. Initialize: dist[i][j] = edge weight, dist[i][i] = 0, others = ∞
2. For k = 1 to n (outer loop):
   - For each pair (i,j):
     - dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
3. After k iterations, shortest paths using vertices {1,2,...,k} as intermediates

**Key skills tested:**
- Understanding intermediate vertex concept
- 3D iteration structure
- All-pairs shortest paths
- Negative cycle detection (check diagonal)

---

#### 3. Algorithm Properties MCQ
**Pattern:** True/False about algorithm characteristics

**Examples from exams:**
- **Past Exam 3, Q5 (2 marks):** Multiple statements about Dijkstra and graphs
  - "If negative edges only from source, can Dijkstra work?" → TRUE
  - "Is Dijkstra tree same as MST?" → FALSE

- **Past Exam 3, Q7 (2 marks):** "Which statements are TRUE?"
  - "Bellman-Ford can terminate early?" → TRUE
  - "Bellman-Ford requires Θ(V²) space?" → FALSE
  - "Floyd-Warshall can terminate early?" → FALSE
  - "Diagonal in Floyd-Warshall cannot be negative?" → FALSE

**Common topics:**
- Early termination conditions
- Space complexity
- Negative edge handling
- Negative cycle detection
- Algorithm comparison

**Key skills tested:**
- Deep understanding of algorithm mechanics
- Knowing when algorithms can/cannot be used
- Understanding complexity (time and space)
- Recognizing algorithm limitations

---

#### 4. Negative Cycle Applications
**Pattern:** Use shortest path algorithms to detect cycles or solve application problems

**Examples from exams:**
- **Past Exam 3, Q19 (3 marks):** "Arbitrage detection: given currency conversion rates, detect if arbitrage possible in O(N³)"
  - **Solution:** Transform rates using logarithms, use Floyd-Warshall to detect negative cycle
  - **Key insight:** Arbitrage exists iff cycle with product > 1 (sum of logs > 0, or sum of negative logs < 0)

**Solution approach:**
1. Model as graph: currencies = vertices, conversions = edges
2. Transform: weight = -log(rate)
3. Run Floyd-Warshall: O(N³)
4. Check diagonal: if dist[i][i] < 0, negative cycle exists → arbitrage possible

**Key skills tested:**
- Problem transformation
- Negative cycle detection
- Using logarithms for multiplicative problems
- Algorithm application

---

### Study Strategy for Shortest Paths

**Must practice:**
1. **Bellman-Ford execution** - Always appears (2-3 marks)
   - Practice manual edge relaxation
   - Track distances carefully with negative weights
   - Understand iteration-by-iteration changes

2. **Floyd-Warshall** - Common (2-3 marks)
   - Understand intermediate vertex concept (key!)
   - Practice 3-iteration traces
   - Know how to detect negative cycles

3. **Algorithm comparison** - Understanding over memorization
   - When to use each algorithm
   - Space/time tradeoffs
   - Handling negative edges

4. **Properties MCQ** - Quick marks
   - Early termination conditions
   - Complexity results
   - Algorithm limitations

**Common mistakes to avoid:**
- Forgetting edge order matters in Bellman-Ford intermediate results
- Not understanding intermediate vertex in Floyd-Warshall
- Assuming Dijkstra works with any negative edges (only special cases)
- Confusing shortest path tree with MST

---

## AVL Trees

**Exam Frequency:** Most final exams (~5-8% of marks)

### Question Type Breakdown

| Question Format | Marks | Frequency | Example |
|----------------|-------|-----------|---------|
| **Insert/Delete Operations** | 1-2 marks | Most exams | "After deleting X and inserting Y, what is the root?" |
| **Balance Factor MCQ** | 2 marks | Common | "Which operations make tree unbalanced?" |
| **Rotation Identification** | 2 marks | Common | "What rotation is needed?" |

### Specific Question Patterns

#### 1. Multi-Step Operations (Most Common)
**Pattern:** Perform sequence of insert/delete, identify tree structure

**Examples from exams:**
- **Past Exam 2, Q15 (2 marks):** Given AVL tree, perform:
  1. Delete 90
  2. Insert 12
  - **Questions:** What is root? What is left child of 30? What is left child of 23?
  - **Answer:** Root=23, 30's left=27, 23's left=20
  - **Rotations needed:** Right-left rotation during process

- **Past Exam 3, Q14-16 (grouped, marks split):** Delete 25, Insert 27, Delete 40
  - **Questions:** Root value? Left child of 30? Left child of 23?
  - **Rotations:** Multiple rotations needed

**Solution approach:**
1. Perform operation (insert/delete using BST rules)
2. Update heights going up from modified node
3. Check balance factors at each ancestor
4. If |balance| > 1, perform rotation:
   - LL: right rotation
   - RR: left rotation
   - LR: left rotation on child, right rotation on parent
   - RL: right rotation on child, left rotation on parent
5. Continue up the tree

**Key skills tested:**
- BST insert/delete rules
- Height calculation
- Balance factor calculation: height(left) - height(right)
- Rotation type identification
- Multiple rotation sequences

---

#### 2. Balance Factor Analysis MCQ
**Pattern:** Determine if operations make tree balanced/unbalanced

**Examples from exams:**
- **Past Exam 1, Q15 (2 marks):** "Which statements are TRUE about given AVL tree?"
  - Options include: "Deleting X keeps tree balanced", "Inserting Y makes unbalanced"
  - **Requires:** Calculate balance factors after each operation
  - **Answer:** Options A and D

**Common analysis:**
- Current balance factors
- After deletion: predict new heights and balances
- After insertion: predict imbalance location
- Identify if rotation needed

**Key skills tested:**
- Height calculation
- Balance factor prediction
- Understanding when rotations needed
- Deletion vs insertion effects

---

#### 3. Rotation Identification
**Pattern:** Given tree structure, identify rotation type needed

**Examples from exams:**
- Implicit in multi-step operations
- Sometimes explicit: "What rotation is needed at node X?"

**Common scenarios:**
- **LL (Left-Left):** Left child's left subtree too tall → right rotation
- **RR (Right-Right):** Right child's right subtree too tall → left rotation
- **LR (Left-Right):** Left child's right subtree too tall → left-right double rotation
- **RL (Right-Left):** Right child's left subtree too tall → right-left double rotation

**Key skills tested:**
- Identifying imbalance pattern
- Choosing correct rotation
- Understanding rotation mechanics

---

### Study Strategy for AVL Trees

**Must practice:**
1. **Multi-step operations** - Most common format
   - Practice insert/delete sequences
   - Track balance factors carefully
   - Master all 4 rotation types

2. **Balance factor calculation** - Foundation
   - height(left) - height(right)
   - Valid range: {-1, 0, 1}
   - Identify imbalance quickly

3. **Rotation mechanics** - Cannot skip
   - Draw out each rotation type
   - Practice on paper
   - Understand why each rotation works

**Common mistakes to avoid:**
- Wrong balance factor calculation
- Forgetting to update heights after rotation
- Choosing wrong rotation type (LR vs RR, etc.)
- Not propagating balance checks up the tree

**Quick reference:**
```
Balance Factor = height(left) - height(right)

LL: balance = +2, left child balance = +1 or 0 → right rotation
RR: balance = -2, right child balance = -1 or 0 → left rotation
LR: balance = +2, left child balance = -1 → left rotation on child, right on parent
RL: balance = -2, right child balance = +1 → right rotation on child, left on parent
```

---

## 2-3 Trees

**Exam Frequency:** Common in final exams (~3-5% of marks)

### Question Type Breakdown

| Question Format | Marks | Frequency | Example |
|----------------|-------|-----------|---------|
| **Insertion Sequence** | 2 marks | Most exams | "After inserting sequence [5,3,7,2], show tree structure" |
| **Properties MCQ** | 1-2 marks | Common | "Which statements about 2-3 trees are TRUE?" |

### Specific Question Patterns

#### 1. Insertion Execution (Most Common)
**Pattern:** Given insertion sequence, trace tree construction

**Examples from exams:**
- **2025 Final, Q18 (2 marks):** "2-3 tree insertions"
  - **Format:** Numerical/diagram
  - **Method:** Insert values following 2-3 tree rules (splitting, promoting)

**Solution approach:**
1. Start with empty tree
2. For each insertion:
   - Find leaf position (search like BST)
   - Insert into leaf
   - If leaf becomes 4-node:
     - Split into two 2-nodes
     - Promote middle value to parent
     - Recursively handle parent overflow
3. Tree grows from root (unlike AVL)

**Key rules:**
- 2-node: 1 value, 2 children
- 3-node: 2 values, 3 children
- Never have 4-node (immediately split)
- All leaves at same level (perfectly balanced)

**Key skills tested:**
- Understanding node splitting
- Promotion mechanics
- Maintaining balance invariant
- Handling cascading splits

---

#### 2. Properties MCQ
**Pattern:** True/False about 2-3 tree characteristics

**Common topics:**
- Height guarantee: always O(log n)
- Perfect balance: all leaves at same level
- Node fanout: 2 or 3 children
- Splitting mechanics
- Comparison with other trees

**Key skills tested:**
- Understanding balance properties
- Knowing when splits occur
- Height analysis

---

### Study Strategy for 2-3 Trees

**Must practice:**
1. **Insertion sequences** - Primary format
   - Practice splitting and promoting
   - Understand cascading splits
   - Draw out tree after each insertion

2. **Balance properties** - Quick MCQ marks
   - Perfect balance (all leaves same level)
   - Height is Θ(log n)
   - No rotations needed (unlike AVL)

**Common mistakes to avoid:**
- Forgetting to promote middle value during split
- Not handling cascading splits up to root
- Incorrect node structure (must be 2-node or 3-node)

**Quick reference:**
```
2-node: [val] with 2 children
3-node: [val1, val2] with 3 children
4-node (temporary): [val1, val2, val3] → split immediately

Split 4-node:
[a, b, c] → promote b, create [a] and [c] as children
```

---

## String Algorithms

**Exam Frequency:** Occasional (~3-5% of marks when present)

**🚫 Note:** Suffix arrays removed from syllabus. Only suffix trees/tries remain.

### Question Type Breakdown

| Question Format | Marks | Frequency | Example |
|----------------|-------|-----------|---------|
| ~~**Suffix Array Prefix Doubling**~~ 🚫 | ~~2 marks~~ | ~~Most exams~~ | **OUT OF SYLLABUS** |
| **Suffix Tree/Trie Construction** | 2-3 marks | Occasional | "Build suffix tree for string S" |
| **Pattern Matching** | 2 marks | Rare | "How many occurrences of pattern P in text T?" |

### Specific Question Patterns

#### ~~1. Suffix Array Prefix Doubling~~ 🚫 OUT OF SYLLABUS

**This entire section is OUT OF SYLLABUS and should be SKIPPED.**

Previous pattern (now removed):
- ~~Given rank array after sorting by k characters, determine order after 2k~~
- ~~Compare suffixes in O(1) using rank arrays~~
- ~~Multiple choice about relative ordering~~

---

#### 2. Suffix Trees/Tries (May Still Appear)

**Pattern:** Construction or query operations on suffix structures

**Potential formats:**
- **Construction:** Build suffix tree for short string
- **Query:** Count occurrences of pattern
- **Complexity:** State space/time complexity

**Key concepts:**
- Suffix trie: Θ(N²) space in worst case
- Suffix tree: Θ(N) space with path compression
- Pattern matching: O(m) for pattern of length m

**Key skills tested:**
- Understanding suffix structures
- Complexity analysis
- Pattern matching applications

---

### Study Strategy for String Algorithms

**Important:** This section has minimal coverage in finals now that suffix arrays are removed.

**If suffix trees/tries appear:**
1. Know basic construction
2. Understand space complexity differences
3. Pattern matching query complexity

**Time allocation:** Low priority (~3-5% of exam at most)

---

## Advanced Applications

**Exam Frequency:** Every final exam (15-20% of marks)

### Question Type Breakdown

| Question Format | Marks | Frequency | Example |
|----------------|-------|-----------|---------|
| **Selection Algorithm Application** | 3-4 marks | Most exams | "Use Quickselect to find top X% and median" |
| **Algorithm Design** | 3-5 marks | Common | "Design O(N log N) algorithm for problem X" |
| **Optimization Problems** | 3-4 marks | Common | "Minimize/maximize under constraints" |
| **Graph Modeling** | 3-4 marks | Common | "Model real-world problem as graph algorithm" |

### Specific Question Patterns

#### 1. Quickselect Applications (Most Common)
**Pattern:** Use Quickselect to solve percentile/ranking problems in O(N) time

**Examples from exams:**
- **Past Exam 1, Q8 (3 marks):** "Fall Guys lap times: find top 30%, calculate penalties above median of top 30%"
  - **Method:** Quickselect for 70th percentile, then median of top 30%
  - **Complexity:** O(N)

- **Past Exam 2, Q18 (3 marks):** "Superheroes: select top 10% as Team 1, top 10% of remainder as Team 2, calculate training needed to reach Team 1 median"
  - **Method:** Multiple Quickselect calls
  - **Complexity:** O(N)

- **Past Exam 3, Q21 (3 marks):** "Tennis tournament: break into Professional (top 20%) and Amateur (bottom 80%), each split into playoff (top 16) and group stage"
  - **Method:** Quickselect for 80th percentile, then for top 16 in each group
  - **Complexity:** O(N)

**Solution pattern:**
1. Use Quickselect to partition at percentile
2. Use Quickselect again on subgroups if needed
3. Linear scan for final calculations
4. Total: O(N) if all Quickselect calls on linearly smaller inputs

**Key skills tested:**
- Recognizing when to use Quickselect
- Chaining multiple Quickselect calls
- Understanding partitioning
- Complexity analysis (why multiple O(N) calls = O(N) total)

---

#### 2. Interval Scheduling / Greedy Design
**Pattern:** Design greedy algorithm for optimization problem

**Examples from exams:**
- **Past Exam 1, Q20 (3 marks):** "Supercomputer time allocation: N requests with start/finish times, maximize compatible subset"
  - **Solution:** Greedy algorithm (earliest finish time)
  - **Complexity:** O(N log N) for sorting

**Common variants:**
- Interval scheduling (maximize number)
- Weighted interval scheduling (maximize value)
- Resource allocation

**Solution approach:**
1. Sort intervals by finish time
2. Greedily select non-overlapping intervals
3. Prove greedy choice is optimal (exchange argument)

**Key skills tested:**
- Recognizing greedy opportunity
- Sorting as preprocessing
- Greedy choice property
- Correctness justification

---

#### 3. Divide and Conquer Applications
**Pattern:** Design algorithm using divide and conquer paradigm

**Examples from exams:**
- **Past Exam 3, Q20 (3 marks):** "Lock and key matching: N locks, N keys, can only try key in lock. Design O(N log N) average-case algorithm"
  - **Solution:** Modified Quicksort approach
  - **Method:**
    1. Choose random key as pivot
    2. Partition locks using key
    3. Use matching lock to partition keys
    4. Recursively solve subproblems
  - **Complexity:** O(N log N) average, O(N²) worst

**Key skills tested:**
- Recognizing divide and conquer structure
- Using one partition to enable another
- Complexity analysis (recurrence relations)
- Understanding randomization

---

#### 4. Optimization Under Constraints
**Pattern:** Complex optimization with multiple constraints

**Examples from exams:**
- **Past Exam 1, Q22 (4 marks):** "Phone drop testing: 2 prototypes, find threshold in 0-150 meters, minimize worst-case drops"
  - **Solution:** Variable interval sizes (square root decomposition)
  - **Answer:** 17 drops
  - **Method:** Drop at heights: 17, 33, 48, 62, 75, 87, 98, 108, 117, 125, 132, 138, 143, 147, 150
  - **Key insight:** Intervals decrease to balance worst case

**Solution approach:**
1. Analyze constraints (2 prototypes = first can break multiple times)
2. Formulate optimization (minimize maximum drops)
3. Use mathematical insight (triangle numbers: d(d+1)/2 ≥ 151)
4. Design algorithm based on insight

**Key skills tested:**
- Problem analysis
- Mathematical modeling
- Optimization under resource constraints
- Worst-case analysis

---

### Study Strategy for Applications

**Must practice:**
1. **Quickselect applications** - Highest frequency
   - Recognize percentile problems
   - Chain multiple Quickselect calls
   - Analyze why O(N) + O(N) = O(N)

2. **Graph modeling** - Covered in Network Flow section
   - See bipartite matching patterns

3. **Problem recognition** - Key skill
   - Does this need greedy? DP? Divide and conquer?
   - What are the constraints?
   - What's the objective?

4. **Algorithm design framework:**
   - High-level approach
   - Detailed steps
   - Correctness justification
   - Complexity analysis

**Common mistakes to avoid:**
- Not recognizing standard problem types
- Incomplete algorithm descriptions
- Missing complexity analysis
- Not justifying correctness

---

## Summary: High-Value Question Formats

### Questions Worth 3-5 Marks (Focus Here!)

| Topic | Question Type | Marks | Frequency |
|-------|--------------|-------|-----------|
| **Dynamic Programming** | Algorithm design + recurrence | 3-5 | Every exam |
| **Network Flow** | Bipartite matching modeling | 3-4 | Every exam |
| **Network Flow** | Circulation feasibility | 3-4 | Most exams |
| **Quickselect Applications** | Multi-stage selection problems | 3-4 | Most exams |
| **Algorithm Design** | Custom algorithm with justification | 3-5 | Common |
| **Loop Invariants** | Full correctness proof | 3-4 | Common |

### Questions Worth 1-2 Marks (Quick Wins)

| Topic | Question Type | Marks | Frequency |
|-------|--------------|-------|-----------|
| **Bellman-Ford** | Numerical execution | 1-3 | Every exam |
| **Floyd-Warshall** | Numerical execution | 1-3 | Most exams |
| **Max-Flow** | Calculate maximum flow | 1-2 | Every exam |
| **Min-Cut** | Identify vertices in S | 1-2 | Most exams |
| **AVL Trees** | Multi-step operations | 1-2 | Most exams |
| **Algorithm Properties** | MCQ about correctness | 2 | Common |

---

## Exam Day Strategy

### Time Allocation by Question Value

**For 50 marks in 130 minutes:**

1. **1-mark questions** (~5-8 marks): 8-12 minutes total
   - Quick MCQ, numerical answers
   - Do these first for momentum

2. **2-mark questions** (~16-24 marks): 32-48 minutes total
   - MCQ with multiple answers
   - Short execution traces
   - Do second, good balance of time/marks

3. **3-4 mark questions** (~18-24 marks): 54-72 minutes total
   - Algorithm design
   - Problem modeling
   - Requires most careful thought

4. **5-mark questions** (~0-5 marks): 0-15 minutes total
   - Rare, but highest individual value
   - Complex optimization problems
   - Save for end if you have time

### Question Format Speed Guide

**Fast (1-1.5 min/mark):**
- Numerical calculations (Bellman-Ford, Floyd-Warshall)
- Single-answer MCQ
- Max-flow calculations

**Medium (2-2.5 min/mark):**
- Multiple-answer MCQ
- AVL tree operations
- DP backtracking
- Min-cut identification

**Slow (3-4 min/mark):**
- Algorithm design (DP, Network Flow)
- Problem modeling
- Correctness proofs
- Complex applications

### Recommended Order

1. **All 1-mark MCQ** (5-8 minutes) - Build confidence
2. **2-mark numerical** (15-20 minutes) - Bellman-Ford, Floyd-Warshall, AVL
3. **Network Flow modeling** (10-15 minutes) - High value, finite patterns
4. **DP problems** (15-20 minutes) - Highest individual value
5. **Remaining MCQ** (10-15 minutes)
6. **Applications** (20-30 minutes)
7. **Review** (15 minutes) - Check calculations, verify answers

---

**Document created from:** 5 past final exams (2021-2025)
**Coverage:** Final exam only topics (mid-semester topics excluded)
**Out of syllabus:** Hash tables, suffix arrays completely removed

**Last updated:** 2025-10-12
