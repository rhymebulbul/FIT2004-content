# Question 10 - 2-3 Search Tree Insertions

**Course:** FIT2004 Algorithms and Data Structures
**Institution:** Monash University
**Exam:** 25-2
**Marks:** 3
**Topic:** 2-3 Search Trees - Insertion Operations

---

## Question Statement

Consider the following 2-3 Search Tree and perform, in order, the following insertion operations. **How many 3-Nodes are there in the resulting 2-3 Search Tree?**

### Initial Tree Structure

```
                              [12, 23]
                          /       |       \
                         /        |        \
                        /         |         \
                   [3, 7]       [20]        [32]
                  /  |  \       /  \        /  \
                 /   |   \     /    \      /    \
               [2] [5] [8,9] [17]  [22]  [28] [33,37]
```

**Initial tree breakdown (corrected for valid 2-3 tree):**
- Root: [12, 23] (3-node) - has 3 children ✓
- Left subtree root: [3, 7] (3-node) - has 3 children ✓
  - Leaves: [2], [5], [8, 9] (where [8, 9] is a 3-node)
- Middle subtree root: [20] (2-node) - has 2 children ✓
  - Leaves: [17], [22] (both 2-nodes)
- Right subtree root: [32] (2-node) - has 2 children ✓
  - Leaves: [28], [33, 37] (where [33, 37] is a 3-node)

**Initial 3-node count: 4**
1. [12, 23] - root
2. [3, 7] - left subtree root
3. [8, 9] - leaf
4. [33, 37] - leaf

### Operations to Perform (In Order)
1. Insert 26
2. Insert 11
3. Insert 50
4. Insert 29

---

## Background: 2-3 Tree Properties

### Node Types
- **2-node:** Contains 1 key, has 2 children (or 0 if leaf)
- **3-node:** Contains 2 keys, has 3 children (or 0 if leaf)

### Insertion Rules
1. Always insert at the leaf level
2. Search down the tree to find the appropriate leaf
3. If leaf is a 2-node, convert it to a 3-node
4. If leaf is a 3-node (becomes 4-node with new key), **split** it:
   - Promote the middle key to parent
   - Left and right keys become separate 2-nodes
5. If parent overflows, continue splitting upward
6. If root splits, create new root (tree height increases)

### Split Mechanics for 4-node [a, b, c]:
- Promote: **b** (middle key)
- Left child: [a] (2-node)
- Right child: [c] (2-node)

---

## Step-by-Step Solution

### Overview of Changes

| Operation | 3-Nodes Before | Action | Splits? | 3-Nodes After | Change |
|-----------|----------------|--------|---------|---------------|--------|
| Initial | — | — | — | 4 | — |
| Insert 26 | 4 | [28] → [26,28] | No | 5 | +1 |
| Insert 11 | 5 | [8,9] → cascade | **3 splits!** | 2 | -3 |
| Insert 50 | 2 | [33,37] → [32,37] | 1 split | 2 | 0 |
| Insert 29 | 2 | [26,28] → cascade | **2 splits!** | 1 | -1 |
| **Final** | — | — | — | **1** | — |

---

### Operation 1: Insert 26

**Search path:** Root → Take right branch (26 > 23) → [32] → Take left branch (26 < 32) → [28]

**Action:** Insert 26 into leaf [28]

**Result:** [28] becomes [26, 28] (3-node)

**Split required?** No (leaf was a 2-node)

**3-node count change:** +1 (new 3-node created)

**Current 3-node count: 5**

```
Current 3-nodes: [12, 23], [3, 7], [8, 9], [33, 37], [26, 28]
```

**Tree after Insert 26:**

```
                              [12, 23]
                          /       |       \
                         /        |        \
                        /         |         \
                   [3, 7]       [20]        [32]
                  /  |  \       /  \        /  \
                 /   |   \     /    \      /    \
               [2] [5] [8,9] [17]  [22] [26,28] [33,37]
```

---

### Operation 2: Insert 11

**Search path:** Root → Take left branch (11 < 12) → [3, 7] → Take rightmost branch (11 > 7) → [8, 9]

**Action:** Insert 11 into leaf [8, 9] (already a 3-node!)

**Result:** [8, 9] becomes [8, 9, 11] (4-node - **OVERFLOW**)

**Split required?** **YES**

#### Split Operation Details:

**4-node to split:** [8, 9, 11]

**Middle key (promote):** 9

**Left 2-node:** [8]

**Right 2-node:** [11]

**Parent node before:** [3, 7] (3-node)

**Parent node after:** Insert 9 → [3, 7, 9] (4-node - **OVERFLOW AGAIN!**)

**Parent split required?** **YES**

#### Parent Split:

**4-node to split:** [3, 7, 9]

**Middle key (promote):** 7

**Left 2-node:** [3]

**Right 2-node:** [9]

**Grandparent (root) before:** [12, 23] (3-node)

**Grandparent (root) after:** Insert 7 → [7, 12, 23] (4-node - **OVERFLOW!**)

**Root split required?** **YES - This creates a new root!**

#### Root Split:

**4-node to split:** [7, 12, 23]

**Middle key (promote):** 12

**Left 2-node:** [7]

**Right 2-node:** [23]

**New root:** [12]

**3-node count change:**
- Original [8, 9] 3-node destroyed → becomes [8] and [11]
- Original [3, 7] 3-node destroyed → becomes [3] and [9]
- Original [12, 23] root 3-node destroyed → becomes [7] and [23]
- Net change: -3 three-nodes

**Current 3-node count: 2**

**Tree height increased from 2 to 3!**

```
Current 3-nodes: [26, 28], [33, 37]
```

**Tree after Insert 11 (with cascading splits):**

```
Step 1: [8,9] + 11 → [8,9,11] splits to [8] and [11], promotes 9

Step 2: [3,7] + 9 → [3,7,9] splits to [3] and [9], promotes 7

Step 3: [12,23] + 7 → [7,12,23] splits to [7] and [23], promotes 12
        Creates NEW ROOT [12]

Final tree after Insert 11:
                         [12]
                        /    \
                       /      \
                     [7]      [23]
                    /  \      /  \
                   /    \    /    \
                 [3]    [9] [20]  [32]
                 / \    / \  / \   / \
               [2][5] [8][11][17][22][26,28][33,37]
```

---

### Operation 3: Insert 50

**Search path:** New root [12] → Take right branch (50 > 12) → [23] → Take right branch (50 > 23) → [32] → Take right branch (50 > 32) → [33, 37]

**Action:** Insert 50 into leaf [33, 37] (already a 3-node!)

**Result:** [33, 37] becomes [33, 37, 50] (4-node - **OVERFLOW**)

**Split required?** **YES**

#### Split Operation Details:

**4-node to split:** [33, 37, 50]

**Middle key (promote):** 37

**Left 2-node:** [33]

**Right 2-node:** [50]

**Parent node before:** [32] (2-node)

**Parent node after:** Insert 37 → [32, 37] (3-node)

**Parent overflow?** No

**3-node count change:**
- Original [33, 37] 3-node destroyed
- New [32, 37] 3-node created
- Net change: 0

**Current 3-node count: 2**

```
Current 3-nodes: [26, 28], [32, 37]
```

**Tree after Insert 50:**

```
Step 1: [33,37] + 50 → [33,37,50] splits to [33] and [50], promotes 37

Step 2: [32] + 37 → [32,37] (no further split needed)

Final tree after Insert 50:
                         [12]
                        /    \
                       /      \
                     [7]      [23]
                    /  \      /  \
                   /    \    /    \
                 [3]    [9] [20]  [32,37]
                 / \    / \  / \   / | \
               [2][5] [8][11][17][22][26,28][33][50]
```

---

### Operation 4: Insert 29

**Search path:** New root [12] → Take right branch (29 > 12) → [23] → Take right branch (29 > 23) → [32, 37] → Take left branch (29 < 32) → [26, 28]

**Action:** Insert 29 into leaf [26, 28] (already a 3-node)

**Result:** Leaf becomes [26, 28, 29] (4-node - **OVERFLOW**)

**Split required?** **YES** (4-node must split)

#### Split Operation Details:

**4-node to split:** [26, 28, 29]

**Middle key (promote):** 28

**Left 2-node:** [26]

**Right 2-node:** [29]

**Parent node before:** [32, 37] (3-node)

**Parent node after:** Insert 28 → [28, 32, 37] (4-node - **OVERFLOW!**)

**Parent split required?** **YES**

#### Parent Split:

**4-node to split:** [28, 32, 37]

**Middle key (promote):** 32

**Left 2-node:** [28]

**Right 2-node:** [37]

**Grandparent before:** [23] (2-node)

**Grandparent after:** Insert 32 → [23, 32] (3-node)

**Grandparent overflow?** No

**3-node count change:**
- Original [26, 28] 3-node destroyed
- Original [32, 37] 3-node destroyed
- New [23, 32] 3-node created
- Net change: -1

**Current 3-node count: 1**

```
Current 3-nodes: [23, 32]
```

**Tree after Insert 29:**

```
Step 1: [26,28] + 29 → [26,28,29] splits to [26] and [29], promotes 28

Step 2: [32,37] + 28 → [28,32,37] splits to [28] and [37], promotes 32

Step 3: [23] + 32 → [23,32] (no further split needed)

Final tree after Insert 29:
                         [12]
                        /    \
                       /      \
                     [7]      [23, 32]
                    /  \      /   |   \
                   /    \    /    |    \
                 [3]    [9] [20] [28] [37]
                 / \    / \  / \  / \  / \
               [2][5] [8][11][17][22][26][29][33][50]
```

---

## Final Tree Structure

After all four insertions (26, 11, 50, 29), the tree has grown taller and undergone significant restructuring:

```
                         [12]
                        /    \
                       /      \
                     [7]      [23, 32]
                    /  \      /   |   \
                   /    \    /    |    \
                 [3]    [9] [20] [28] [37]
                 / \    / \  / \  / \  / \
               [2][5][8][11][17][22][26][29][33][50]
```

**Final tree breakdown:**
- New root: [12] (2-node) - height increased to 3
- Level 1: [7] (2-node), [23, 32] (3-node)
- Level 2: [3], [9], [20], [28], [37] (all 2-nodes)
- Level 3: Leaves [2], [5], [8], [11], [17], [22], [26], [29], [33], [50]

### All 3-nodes in Final Tree:

1. **[23, 32]** - Only 3-node in the entire tree!

---

## Final Answer

**Number of 3-nodes in the resulting tree: 1**

### Is This the Only Possible Answer?

**YES - The solution is unique and deterministic.**

**Why there's only one possible answer:**

1. **Search paths are deterministic:** The BST ordering property means each key has exactly one valid insertion location based on comparisons with existing keys.

2. **No algorithmic choices:** Unlike Red-Black trees (which have rotation choices), 2-3 trees have a single, deterministic insertion algorithm:
   - Insert always occurs at leaf level
   - 4-nodes always split the same way (promote middle key)
   - No variation in split mechanics

3. **Order matters:** The operations must be performed sequentially (Insert 26, then 11, then 50, then 29), so each operation operates on a well-defined tree state.

4. **Split mechanics are fixed:** When [26, 28, 29] forms, there's only one valid split:
   - Middle key (28) must be promoted
   - Not the left (26) or right (29) key
   - This is part of the 2-3 tree definition

**Therefore, any correct execution of the insertion algorithm will result in exactly 1 three-node.**

---

## Student Answer Analysis

**Student's answer:** 4
**Correct answer:** 1
**Result:** Incorrect (0/3 marks)

### Where the Error Occurred

The student got 4, but the correct answer is 1. With the corrected initial tree structure:

**Initial 3-nodes: 4** ([12, 23], [3, 7], [8, 9], [33, 37])

**Major cascading splits occurred:**

1. **Insert 11** caused a cascade of 3 splits all the way to the root:
   - [8, 9, 11] split → triggered [3, 7, 9] split → triggered [7, 12, 23] split
   - All three original 3-nodes destroyed, tree height increased
   - Result: Only 2 three-nodes remaining ([26, 28] and [33, 37])

2. **Insert 50** into [33, 37]:
   - One split, destroyed [33, 37], created [32, 37]
   - Result: Still 2 three-nodes

3. **Insert 29** into [26, 28]:
   - Cascade of 2 splits
   - Destroyed both [26, 28] and [32, 37]
   - Created [23, 32]
   - Result: Only 1 three-node remaining

**Student's mistake:** Likely didn't trace through the cascading splits properly, especially the dramatic restructuring from Insert 11 which split all the way to the root.

---

## Key Insights

### Pattern Recognition
- **Insert 26:** Into 2-node [28] → creates 3-node [26, 28]
- **Insert 11:** Into 3-node [8, 9] → **MASSIVE CASCADE** - splits propagate all the way to root, destroying all 3 original 3-nodes, tree grows taller
- **Insert 50:** Into 3-node [33, 37] → one split
- **Insert 29:** Into 3-node [26, 28] → cascade of 2 splits

### Counting Strategy
After all operations, systematically count by level:
- **Level 0 (root):** [12] ✗
- **Level 1:** [7] ✗, [23, 32] ✓
- **Level 2:** [3], [9], [20], [28], [37] - all 2-nodes ✗
- **Level 3:** All leaves are 2-nodes ✗
- **Total:** 1 three-node

### Split Impact on 3-node Count
When a 3-node splits:
- The 3-node is destroyed (becomes two 2-nodes)
- The middle key promotes to parent
- If parent was a 2-node → becomes 3-node (net change: 0)
- If parent was a 3-node → triggers another split (cascade, can reduce 3-node count significantly)

### Critical Observation
The initial tree had [8, 9] and [33, 37] as 3-node **leaves** - inserting into these caused immediate splits and cascades, dramatically restructuring the tree.

---

## Complexity Analysis

### Time Complexity
- Each insertion: **O(log n)** (tree height)
- 4 insertions: **O(4 log n) = O(log n)**

### Space Complexity
- Tree storage: **O(n)** where n is number of keys

### Height Analysis
- Initial height: 2
- Final height: 2 (no root split occurred)
- Height range for 2-3 tree: floor(log₃(n)) ≤ h ≤ floor(log₂(n+1))

---

## Verification Checklist

✅ All leaves remain at the same depth (perfect balance maintained)
✅ All internal nodes are either 2-nodes or 3-nodes
✅ Binary search tree property maintained
✅ Split operations performed correctly
✅ Parent node updates handled properly

---

## Common Mistakes to Avoid

1. **Forgetting splits:** Not recognizing when a 4-node forms
2. **Incorrect split mechanics:** Not promoting the middle key
3. **Not updating parent:** Forgetting to insert promoted key into parent
4. **Miscounting nodes:** Confusing 2-nodes with 3-nodes
5. **Ignoring tree invariants:** Not maintaining perfect balance

---

## Related Concepts

- **B-Trees:** 2-3 trees are B-trees of order 3
- **Red-Black Trees:** Can be viewed as binary representation of 2-3 trees
- **AVL Trees:** Different balancing approach using rotations instead of splits
- **Self-balancing trees:** All maintain O(log n) operations

---

## Practice Exercise

Try these variations:
1. What would happen if we inserted 27 instead of 29?
2. How many splits would occur if we inserted 1 through 10 in order?
3. What is the maximum height of a 2-3 tree with 15 keys?

