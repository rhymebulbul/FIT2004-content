# Prep 12 Cheatsheet - Tree Data Structures

## AVL Trees

### Core Definition
- **Self-balancing Binary Search Tree (BST)**
- Heights of left and right subtrees differ by **at most 1**
- Balance maintained through **rotations**

### Balance Factor (BF)
```
Balance Factor = Height(Left Subtree) - Height(Right Subtree)
```
- **Valid range**: BF ∈ {-1, 0, 1}
- **Imbalanced**: |BF| > 1 (requires rebalancing)

### Height Calculation
- **Leaf node**: height = 0
- **Internal node**: height = 1 + max(height(left), height(right))
- **Null node**: height = -1

### Insertion Procedure

#### Step 1: BST Insertion
Insert key using standard BST rules:
- If key < node.value → go left
- If key > node.value → go right
- Insert at empty position

#### Step 2: Update Heights
Travel back up insertion path, updating heights of ancestors

#### Step 3: Check Balance Factors
Calculate BF for each ancestor node on insertion path

#### Step 4: Identify Imbalance
Find the **lowest (deepest) ancestor** with |BF| > 1

#### Step 5: Perform Rotation
Choose rotation based on insertion pattern:

**Case 1: Left-Left (LL) - Single Right Rotation**
- BF(node) = 2 (left-heavy)
- BF(left child) = 1 (left-heavy)
- Action: Right rotate at imbalanced node

```
     z (BF=2)              y
    /                     / \
   y          →          x   z
  /
 x
```

**Case 2: Right-Right (RR) - Single Left Rotation**
- BF(node) = -2 (right-heavy)
- BF(right child) = -1 (right-heavy)
- Action: Left rotate at imbalanced node

```
 x (BF=-2)                y
  \                      / \
   y         →          x   z
    \
     z
```

**Case 3: Left-Right (LR) - Double Rotation**
- BF(node) = 2 (left-heavy)
- BF(left child) = -1 (right-heavy)
- Action: Left rotate at left child, then right rotate at node

```
   z (BF=2)        z           y
  /               /           / \
 x       →       y     →     x   z
  \             /
   y           x
```

**Case 4: Right-Left (RL) - Double Rotation**
- BF(node) = -2 (right-heavy)
- BF(right child) = 1 (left-heavy)
- Action: Right rotate at right child, then left rotate at node

```
 x (BF=-2)      x              y
  \              \            / \
   z      →       y    →     x   z
  /                \
 y                  z
```

### Rotation Mechanics

**Right Rotation at node z:**
```
    z                y
   / \              / \
  y   C    →       A   z
 / \                  / \
A   B                B   C
```

**Left Rotation at node x:**
```
  x                  y
 / \                / \
A   y      →       x   C
   / \            / \
  B   C          A   B
```

### Key Problem-Solving Steps (from prep12.json Problem 1)

1. **Insert 5 into tree** → Standard BST insertion (5 becomes left child of 10)
2. **Calculate heights** → Node 10: height 1, Node 20: height 2 (left), height 0 (right)
3. **Find imbalance** → Node 20 has BF = 2 (left-heavy)
4. **Identify pattern** → LL case (inserted in left subtree of left child)
5. **Execute rotation** → Right rotate at node 20
6. **Result** → Node 10 becomes new root of subtree with children 5 and 20

---

## 2-3 Search Trees

### Core Definition
- **Balanced search tree** where all leaves are at the same level
- Nodes can contain **1 or 2 keys**
- Nodes can have **2 or 3 children**

### Node Types

#### 2-Node
- Contains **1 key**: [k]
- Has **2 children**: left (< k), right (> k)
- Structure: `[k]` with 2 pointers

#### 3-Node
- Contains **2 keys**: [k1, k2] where k1 < k2
- Has **3 children**: left (< k1), middle (k1 < x < k2), right (> k2)
- Structure: `[k1, k2]` with 3 pointers

#### 4-Node (Temporary - INVALID)
- Contains **3 keys**: [k1, k2, k3]
- **Must be split immediately** during insertion
- Never valid in final tree

### Insertion Procedure

#### Step 1: Search for Key
Traverse tree using BST logic to find insertion point
- **If key exists**: No insertion (no duplicates allowed)
- **If key doesn't exist**: Continue to leaf level

#### Step 2: Insert at Leaf Level

**Case A: Leaf is a 2-node [k]**
- Add new key to create 3-node
- Example: [5] + insert 6 → [5, 6]
- **No further action needed**

**Case B: Leaf is a 3-node [k1, k2]**
- Create temporary 4-node [k1, k2, knew]
- **Must split immediately** (proceed to Step 3)

#### Step 3: Split 4-Node

**Split procedure for 4-node [a, b, c]:**
1. **Identify middle key**: b
2. **Create two 2-nodes**: [a] and [c]
3. **Promote middle key**: b moves up to parent
4. **Update pointers**: [a] becomes left child, [c] becomes right child

```
     [a, b, c]           b
     (4-node)           / \
        ↓              a   c
      SPLIT         (2-nodes)
```

#### Step 4: Insert Promoted Key into Parent

**Case 1: Parent is a 2-node**
- Add promoted key to parent → becomes 3-node
- **Done**

**Case 2: Parent is a 3-node**
- Adding promoted key creates another 4-node
- **Recursively split parent**
- Continue until no 4-nodes remain or root is reached

**Case 3: Parent is root and becomes 4-node**
- Split root
- Middle key becomes **new root**
- **Tree height increases by 1**

### Key Problem-Solving Steps (from prep12.json Problem 2)

**Operation a: Insert 6**
- Find insertion point: 2-node [5]
- Result: [5] → [5, 6]
- Valid: Yes

**Operation b: Insert 7**
- Search finds key 7 already exists
- Result: No change (duplicates not allowed)
- Valid: Yes

**Operation c: Insert 50**
1. Find insertion point: 3-node [42, 45]
2. Create 4-node: [42, 45, 50]
3. Split 4-node: [42] and [50], promote 45
4. Insert 45 into parent [40] (2-node)
5. Parent becomes: [40, 45]
6. Valid: Yes

### Critical Rules

1. **No duplicates** - If key exists, do not insert
2. **Insert only at leaf level** - Never insert in internal nodes
3. **All leaves at same depth** - Maintains perfect balance
4. **4-nodes are temporary** - Must be split immediately
5. **Split propagates upward** - May cascade to root

---

## Left-Leaning Red-Black Trees (LLRB)

### Core Definition
- **Binary Search Tree** with colored links/nodes
- Maintains balance through **color constraints**
- Red links represent **horizontal connections** (same logical level)
- Black links represent **vertical connections** (parent-child)

### Color Meanings
- **Red edge/node**: Node is connected to parent with red link (part of 3-node)
- **Black edge/node**: Standard parent-child relationship (separate level)

### Core Properties

1. **Root is always black**
2. **Red nodes can only be LEFT children** (left-leaning property)
3. **No two consecutive red nodes** on any path
4. **All paths from root to leaves have same number of black nodes**
5. **New insertions are always RED**

### Insertion Procedure

#### Step 1: BST Insertion
Insert key using standard BST rules at correct position

#### Step 2: Color New Node RED
**Mandatory**: All new insertions must be red nodes

#### Step 3: Check and Fix Violations
Apply operations in order until all properties satisfied:

### Three Fix-Up Operations

#### Operation 1: Rotate Left
**When to use**: Red node is a **right child** (violates left-leaning)

**Before:**
```
   x (black)
    \
     y (RED)  ← red on right (VIOLATION)
```

**After:**
```
     y (black)
    /
   x (RED)    ← red now on left (FIXED)
```

**Procedure:**
1. Move y up to x's position
2. x becomes left child of y
3. Swap colors: y becomes black, x becomes red

#### Operation 2: Rotate Right
**When to use**: Two consecutive red nodes on **left side**

**Before:**
```
     z (black)
    /
   y (RED)
  /
 x (RED)      ← two consecutive reds (VIOLATION)
```

**After:**
```
   y (black)
  / \
 x   z (both RED)
```

**Procedure:**
1. Move y up to z's position
2. z becomes right child of y
3. Adjust colors appropriately

#### Operation 3: Color Flip
**When to use**: Node has **two red children**

**Before:**
```
      y (black)
     / \
(RED) x   z (RED)  ← two red children
```

**After:**
```
      y (RED)      ← parent becomes red
     / \
(BLACK) x   z (BLACK)  ← children become black
```

**Procedure:**
1. Parent becomes red
2. Both children become black
3. **Check parent's parent** for violations (may cascade upward)

### Cascading Effects

**Important**: After color flip, must check parent node:
- If parent now has two red children → flip again
- If parent's parent has violations → continue fixing
- **Propagate upward until all properties satisfied**

### Key Problem-Solving Steps (from prep12.json Problem 3)

**Operation a: Insert 12**
1. Traverse to find position: left child of 13
2. Insert as RED node
3. Check properties: red node is left child ✓
4. No violations
5. Done

**Operation b: Insert 8**
1. Insert as RED node: right child of 7
2. **Violation**: Red node is right child
3. **Fix**: Rotate left at 7
4. Result: 8 becomes parent, 7 becomes red left child
5. After rotation: 8 is black, 7 is red (left) ✓
6. Done

**Operation c: Insert 15**
1. Insert as RED node: right child of 13
2. **Violation**: 13 now has two red children (12 and 15)
3. **Fix**: Color flip at 13
   - 13 → red
   - 12, 15 → black
4. **New violation**: Parent 9 now has two red children (5 and 13)
5. **Fix**: Color flip at 9
   - 9 → red
   - 5, 13 → black
6. Check further ancestors: all properties satisfied ✓
7. Done

### Decision Tree for Fixing Violations

```
After inserting RED node:

1. Is red node a right child?
   YES → Rotate left
   NO → Continue

2. Are there two consecutive red nodes on left?
   YES → Rotate right
   NO → Continue

3. Does node have two red children?
   YES → Color flip, then check parent
   NO → Continue

4. All properties satisfied?
   YES → Done
   NO → Repeat from step 1 at parent
```

### Critical Rules to Memorize

1. **Always insert as RED** - No exceptions
2. **Red must lean left** - Fix with left rotation
3. **Two red children → flip** - Parent becomes red, children become black
4. **Cascading fixes** - Don't stop until all properties satisfied
5. **Check ancestors** - Violations can propagate upward

---

## Problem-Solving Strategy

### For AVL Trees
1. Draw the tree after BST insertion
2. Calculate heights bottom-up
3. Calculate balance factors for ancestors
4. Identify imbalance type (LL/RR/LR/RL)
5. Apply appropriate rotation(s)
6. Verify balance factors are valid

### For 2-3 Trees
1. Traverse to find insertion point
2. Check if key already exists (duplicates not allowed)
3. If 2-node: simply add key
4. If 3-node: create 4-node, then split
5. Promote middle key and recurse upward
6. Continue until no 4-nodes remain
7. Draw final tree structure

### For Left-Leaning Red-Black Trees
1. Insert as RED using BST rules
2. Apply fixes in sequence:
   - Rotate left (if red on right)
   - Color flip (if two red children)
3. Check parent for new violations
4. Repeat fixes until all properties satisfied
5. Label all node colors in final tree

---

## Common Mistakes to Avoid

### AVL Trees
- Forgetting to update heights after insertion
- Checking balance factors at wrong nodes
- Using wrong rotation for the pattern
- Not identifying the lowest imbalanced ancestor

### 2-3 Trees
- Inserting duplicates (not allowed)
- Inserting at wrong level (must be leaf level)
- Forgetting to split 4-nodes
- Promoting wrong key (must be middle key)
- Not cascading splits upward

### Left-Leaning Red-Black Trees
- Inserting as BLACK instead of RED
- Forgetting to check for cascading violations
- Stopping fixes too early
- Not maintaining left-leaning property
- Incorrect color assignments after rotations

---

## Quick Reference Table

| Tree Type | Balance Mechanism | Max Height | Insertion Complexity |
|-----------|------------------|------------|---------------------|
| AVL | Rotations (BF ≤ 1) | ~1.44 log n | O(log n) |
| 2-3 | Node splits | log n | O(log n) |
| LLRB | Rotations + color flips | ~2 log n | O(log n) |

| Property | AVL | 2-3 | LLRB |
|----------|-----|-----|------|
| Strict balance | Yes (BF ≤ 1) | Yes (all leaves same level) | Relaxed |
| Node keys | 1 | 1-2 | 1 |
| Height growth | Gradual | Only at root split | Gradual |
| Duplicates | Allowed | Not allowed | Allowed |
| Complexity of ops | Rotation logic | Split logic | Color + rotation logic |
