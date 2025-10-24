# Tree Rebalancing Properties - Quick Reference

## Purpose
This document lists the exact properties that MUST be maintained during rebalancing operations for AVL Trees, 2-3 Search Trees, and Left-Leaning Red-Black Trees. Use this as a checklist when solving rebalancing problems.

---

## AVL Trees

### Properties to ALWAYS Maintain

#### 1. Binary Search Tree Property
- **Rule**: For every node N with key k:
  - All keys in left subtree < k
  - All keys in right subtree > k
- **Check after**: Every rotation
- **If violated**: Rotation was performed incorrectly

#### 2. Balance Factor Property (CRITICAL)
- **Rule**: For every node: `-1 ≤ Balance Factor ≤ 1`
- **Formula**: `BF(node) = Height(left) - Height(right)`
- **Check after**: Every insertion, every rotation
- **Valid values**: {-1, 0, 1}
- **Violation triggers**: |BF| > 1 → Must rebalance

#### 3. Height Property
- **Rule**: Height must be correctly calculated for all nodes
- **Formula**: `Height(node) = 1 + max(Height(left), Height(right))`
- **Leaf height**: 0
- **Null child height**: -1
- **Check after**: Every insertion, every rotation

#### 4. Structural Integrity
- **Rule**: Parent-child pointers must be correctly updated
- **Check after**: Every rotation
- **Verify**:
  - Children point to correct parent
  - Parent points to correct children
  - Subtrees maintain BST ordering

### Rebalancing Checklist for AVL

When performing insertion:
- [ ] Insert using standard BST rules
- [ ] Update heights of all ancestors (bottom-up)
- [ ] Calculate balance factors for all ancestors
- [ ] Find lowest ancestor with |BF| > 1
- [ ] Identify rotation case (LL/RR/LR/RL)
- [ ] Perform rotation(s)
- [ ] Verify BST property maintained
- [ ] Verify all balance factors in {-1, 0, 1}
- [ ] Verify heights are correct

### Common Violations and Fixes

| Violation | Cause | Fix |
|-----------|-------|-----|
| BF = 2 (left-heavy) | Insertion in left subtree | LL or LR rotation |
| BF = -2 (right-heavy) | Insertion in right subtree | RR or RL rotation |
| BST property broken | Incorrect rotation | Redo rotation with correct pointers |
| Height incorrect | Forgot to update | Recalculate bottom-up |

---

## 2-3 Search Trees

### Properties to ALWAYS Maintain

#### 1. Search Tree Ordering
- **2-node [k]**: left < k < right
- **3-node [k1, k2]**: left < k1 < middle < k2 < right
- **Check after**: Every split, every insertion
- **If violated**: Keys inserted in wrong order

#### 2. Node Validity (CRITICAL)
- **Rule**: Only 2-nodes and 3-nodes allowed in final tree
- **2-node structure**: [k] with 2 children
- **3-node structure**: [k1, k2] with 3 children (k1 < k2)
- **4-node status**: Temporary only - MUST be split immediately
- **Check after**: Every insertion
- **If 4-node remains**: Incomplete split operation

#### 3. Perfect Balance Property (CRITICAL)
- **Rule**: ALL leaf nodes must be at the SAME depth
- **Check after**: Every insertion, every split
- **Violation**: Tree becomes unbalanced (should never happen if splits done correctly)
- **This is the defining property**: Automatically maintained by insertion algorithm

#### 4. Unique Keys Property
- **Rule**: No duplicate keys allowed
- **Check before**: Every insertion
- **Action**: If key exists, do NOT insert

#### 5. Insertion Location Property
- **Rule**: New keys can ONLY be inserted at leaf level
- **Check before**: Every insertion
- **Never**: Insert at internal nodes

### Rebalancing Checklist for 2-3 Trees

When performing insertion:
- [ ] Search for key (check if duplicate)
- [ ] If key exists → Do NOT insert, return
- [ ] Traverse to appropriate leaf node
- [ ] If leaf is 2-node → Add key (becomes 3-node), DONE
- [ ] If leaf is 3-node → Create 4-node, proceed to split
- [ ] Split 4-node: create two 2-nodes, promote middle key
- [ ] Insert promoted key into parent
- [ ] If parent becomes 4-node → Recursively split parent
- [ ] Continue until no 4-nodes remain
- [ ] Verify all leaves at same depth
- [ ] Verify no 4-nodes in final tree

### Split Operation Properties

**When splitting 4-node [a, b, c]:**
- [ ] Middle key (b) is promoted
- [ ] Left 2-node contains [a]
- [ ] Right 2-node contains [c]
- [ ] Original 4-node's children redistributed correctly:
  - [a] gets leftmost 2 children
  - [c] gets rightmost 2 children
- [ ] Parent receives promoted key in sorted order
- [ ] All subtree relationships maintain search property

### Common Violations and Fixes

| Violation | Cause | Fix |
|-----------|-------|-----|
| 4-node in final tree | Incomplete split | Complete the split operation |
| Leaves at different depths | Incorrect split | Redo splits from root |
| Duplicate key | Didn't check before insert | Remove duplicate |
| Wrong key promoted | Promoted wrong key from 4-node | Promote middle key only |
| Keys out of order in node | Inserted without sorting | Sort keys in node |

---

## Left-Leaning Red-Black Trees

### Properties to ALWAYS Maintain

#### 1. Binary Search Tree Property
- **Rule**: Standard BST ordering must hold
- **Check after**: Every rotation, every insertion
- **If violated**: Rotation performed incorrectly

#### 2. Root Property
- **Rule**: Root must ALWAYS be BLACK
- **Check after**: Every insertion, every color flip
- **Fix**: If root becomes red after color flip, change to black

#### 3. Red Node Placement Property (CRITICAL - "Left-Leaning")
- **Rule**: Red nodes can ONLY be LEFT children
- **Check after**: Every insertion
- **Violation trigger**: Red node is right child
- **Fix**: Rotate left to move red to left side

#### 4. New Insertion Color Property
- **Rule**: ALL new insertions must be RED
- **No exceptions**: This is mandatory
- **Check**: Every insertion
- **Reason**: Maintains black-height property

#### 5. No Consecutive Red Property
- **Rule**: A red node cannot have a red child
- **Check after**: Every insertion, every color flip
- **Violation trigger**: Red node has red parent
- **Fix**: Rotate right (if left-left reds), then potentially color flip

#### 6. Two Red Children Property (CRITICAL)
- **Rule**: A node cannot have two red children simultaneously
- **Check after**: Every insertion, especially after color flips
- **Violation trigger**: Both children are red
- **Fix**: Color flip (parent becomes red, children become black)

#### 7. Black-Height Property
- **Rule**: All paths from root to leaves must contain same number of black nodes
- **Check after**: Complete insertion and fix-up operations
- **Maintained by**: Correct rotations and color flips
- **If violated**: Incorrect color assignments during fix-up

### Rebalancing Checklist for LLRB

When performing insertion:
- [ ] Insert using standard BST rules
- [ ] Color new node RED (mandatory)
- [ ] Check for violations starting at inserted node
- [ ] Apply fixes in bottom-up order:

**Fix sequence at each node (bottom-up):**
1. [ ] **Check**: Is right child red AND left child black?
   - If YES → Rotate left
2. [ ] **Check**: Are left child AND left-left grandchild both red?
   - If YES → Rotate right
3. [ ] **Check**: Are both children red?
   - If YES → Color flip (parent red, children black)
4. [ ] **Check parent**: If violations exist, continue fix-up at parent
5. [ ] **Repeat** until no violations remain
6. [ ] **Final check**: Ensure root is black

### Color Flip Cascading Rules

**When performing color flip:**
- [ ] Parent becomes RED
- [ ] Both children become BLACK
- [ ] Check parent's parent for new violations
- [ ] If parent now violates properties → apply fixes at parent
- [ ] Continue propagating until root or no violations

### Rotation Color Rules

**Left Rotation:**
- [ ] Right child moves up (becomes parent)
- [ ] Original parent becomes left child
- [ ] Colors: typically swap colors of rotated nodes
- [ ] Verify left-leaning property after rotation

**Right Rotation:**
- [ ] Left child moves up (becomes parent)
- [ ] Original parent becomes right child
- [ ] Colors: maintain or adjust to fix consecutive reds
- [ ] Verify no consecutive reds after rotation

### Common Violations and Fixes

| Violation | Trigger | Fix |
|-----------|---------|-----|
| Red node is right child | Insertion on right | Rotate left |
| Two consecutive red (left-left) | Insertion in left-left | Rotate right |
| Two red children | After insertion or color flip | Color flip |
| Red root | After color flip at root's child | Change root to black |
| Red node with red parent (not left-left) | Complex insertion | Rotate + color flip combination |

### Decision Flow for Fixing LLRB

```
After inserting RED node (or after any operation):

START → Check current node

1. Right child red AND left child black?
   YES → Rotate left, continue to step 2
   NO → Continue to step 2

2. Left child red AND left-left grandchild red?
   YES → Rotate right, continue to step 3
   NO → Continue to step 3

3. Both children red?
   YES → Color flip, move to parent, go to step 1
   NO → Continue to step 4

4. At root?
   YES → Ensure root is black, DONE
   NO → Move to parent, go to step 1
```

---

## Comparison Matrix: What to Check After Each Operation

| Operation | AVL | 2-3 | LLRB |
|-----------|-----|-----|------|
| **After Insertion** | Heights, BFs | Node types, leaf depth | Colors, left-leaning |
| **After Rotation** | BFs, BST order | N/A | Colors, BST order |
| **After Split** | N/A | Node types, leaf depth | N/A |
| **After Color Flip** | N/A | N/A | Consecutive reds, parent violations |
| **Final Verification** | All BFs ∈ {-1,0,1} | No 4-nodes, equal depth | Root black, no violations |

---

## Problem-Solving Workflow

### For AVL Trees
1. **Insert** → Use BST rules
2. **Update** → Heights bottom-up
3. **Check** → Balance factors of ancestors
4. **Identify** → Lowest imbalanced node
5. **Classify** → LL/RR/LR/RL case
6. **Rotate** → Apply appropriate rotation
7. **Verify** → All BFs valid, BST property holds

### For 2-3 Trees
1. **Search** → Check for duplicate
2. **Insert** → At leaf level only
3. **Check node type** → 2-node or 3-node
4. **If 3-node** → Split into 2-nodes, promote middle
5. **Insert promoted** → Into parent
6. **Recurse** → If parent becomes 4-node
7. **Verify** → No 4-nodes, all leaves same depth

### For LLRB Trees
1. **Insert** → Use BST rules, color RED
2. **Check** → Red on right? → Rotate left
3. **Check** → Left-left reds? → Rotate right
4. **Check** → Two red children? → Color flip
5. **Move up** → Apply checks at parent
6. **Repeat** → Until root reached
7. **Verify** → Root black, no violations

---

## Critical "Must Not Forget" Rules

### AVL Trees
- **MUST** update heights after every rotation
- **MUST** check balance factors at ALL ancestors, not just inserted node
- **MUST** identify LOWEST imbalanced ancestor (deepest in tree)
- **MUST** verify BST property after rotation

### 2-3 Trees
- **MUST** split 4-nodes immediately (never remain in final tree)
- **MUST** promote MIDDLE key when splitting, not left or right
- **MUST** insert ONLY at leaf level
- **MUST** reject duplicate keys
- **MUST** maintain all leaves at same depth

### LLRB Trees
- **MUST** insert new nodes as RED (no exceptions)
- **MUST** fix violations bottom-up (not just at insertion point)
- **MUST** continue fixing until ALL violations resolved (cascading)
- **MUST** maintain left-leaning property (red nodes only on left)
- **MUST** ensure root is black at end

---

## Quick Verification Checklist

### Before Submitting Answer - AVL
- [ ] Every node has |BF| ≤ 1?
- [ ] Heights correctly calculated?
- [ ] BST property maintained?
- [ ] All rotations correctly executed?

### Before Submitting Answer - 2-3
- [ ] No 4-nodes in final tree?
- [ ] All leaves at same depth?
- [ ] All nodes are 2-nodes or 3-nodes?
- [ ] Keys in sorted order within nodes?
- [ ] No duplicate keys?

### Before Submitting Answer - LLRB
- [ ] Root is black?
- [ ] All red nodes are left children?
- [ ] No node has two red children?
- [ ] No consecutive red nodes?
- [ ] BST property maintained?
- [ ] All new insertions were red?
