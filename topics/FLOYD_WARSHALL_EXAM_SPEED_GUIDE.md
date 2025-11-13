# Floyd-Warshall Exam Speed Guide
**Time Target: 1.5-2 minutes per mark (3-4 minutes for a 2-mark question)**

## The Algorithm (What You're Computing)

```
for k = 1 to n:           # Intermediate vertex
    for i = 1 to n:       # Source
        for j = 1 to n:   # Destination
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

**Key Concept:** After iteration k, `dist[i][j]` = shortest path from i to j using ONLY vertices {1, 2, ..., k} as intermediates.

## Fast 4-Step Method

### Step 1: Draw the Matrix Template (15 seconds)
```
     1    2    3    4    5
1  [ 0                     ]
2  [     0                 ]
3  [          0            ]
4  [               0       ]
5  [                    0  ]
```

**Quick checklist:**
- ✓ Diagonal = 0 (vertices to themselves)
- ✓ Label rows (source) and columns (destination)
- ✓ All other cells start as ∞ (write nothing, fill as you go)

### Step 2: Fill Initial Edges (30 seconds)
**Write ONLY the direct edges from the graph.**

For graph: 1→2(-2), 1→3(1), 2→3(1), 2→4(-3), 2→5(3), 3→5(2), 4→5(20)

```
     1    2    3    4    5
1  [ 0   -2    1    ∞    ∞ ]   ← From vertex 1: edges to 2,3
2  [ ∞    0    1   -3    3 ]   ← From vertex 2: edges to 3,4,5
3  [ ∞    ∞    0    ∞    2 ]   ← From vertex 3: edge to 5
4  [ ∞    ∞    ∞    0   20 ]   ← From vertex 4: edge to 5
5  [ ∞    ∞    ∞    ∞    0 ]   ← From vertex 5: no outgoing edges
```

**Speed tip:** Go row by row, copying edges from the graph diagram.

### Step 3: Iterate Through k (THE CRITICAL STEP)

**For EACH iteration k, scan the matrix systematically.**

#### Iteration 1 (k=1): "Can we improve paths by going through vertex 1?"

**Look at ROW 1 and COLUMN 1:**
- Row 1: Shows how to GET TO other vertices FROM vertex 1
- Column 1: Shows how to GET TO vertex 1 FROM other vertices

**Check each cell dist[i][j]:**
- Can we improve dist[i][j] by going i → 1 → j?
- Calculate: dist[i][1] + dist[1][j]
- If smaller than current dist[i][j], UPDATE IT

```
For each i,j:
  if dist[i][1] ≠ ∞ AND dist[1][j] ≠ ∞:
      new_dist = dist[i][1] + dist[1][j]
      if new_dist < dist[i][j]:
          dist[i][j] = new_dist
```

**Example for k=1:**
- dist[2][2] via vertex 1? dist[2][1] + dist[1][2] = ∞ + (-2) = ∞ (no improvement)
- dist[2][3] via vertex 1? dist[2][1] + dist[1][3] = ∞ + 1 = ∞ (no improvement)
- Most cells don't improve because few edges connect TO vertex 1 (column 1 is mostly ∞)

**After k=1:** Matrix mostly unchanged (typically no improvements if vertex 1 is a source with no incoming edges)

#### Iteration 2 (k=2): "Can we improve paths by going through vertex 2?"

**Look at ROW 2 and COLUMN 2:**
- Row 2: [∞, 0, 1, -3, 3] → paths FROM vertex 2
- Column 2: [-2, 0, ∞, ∞, ∞] → paths TO vertex 2

**Check each cell systematically:**

```
     j=1  j=2  j=3  j=4  j=5
i=1:  —   —    CHK  CHK  CHK   ← Check dist[1][3], dist[1][4], dist[1][5]
i=2:  —   —    —    —    —     ← Skip row 2 (k=2)
i=3:  CHK CHK  —    CHK  CHK   ← Check dist[3][1], dist[3][2], dist[3][4], dist[3][5]
i=4:  CHK CHK  CHK  —    CHK   ← Check dist[4][1], dist[4][2], dist[4][3], dist[4][5]
i=5:  CHK CHK  CHK  CHK  —     ← Check dist[5][1], dist[5][2], dist[5][3], dist[5][4]
```

**Actually compute the important ones (where both components ≠ ∞):**

For row 1 (dist[1][1], dist[1][2] can reach vertex 2):
- dist[1][3]: min(1, dist[1][2] + dist[2][3]) = min(1, -2+1) = min(1, -1) = **-1** ✓ UPDATE
- dist[1][4]: min(∞, dist[1][2] + dist[2][4]) = min(∞, -2+(-3)) = **-5** ✓ UPDATE
- dist[1][5]: min(∞, dist[1][2] + dist[2][5]) = min(∞, -2+3) = **1** ✓ UPDATE

For other rows (dist[i][2] = ∞ for i > 2, so most checks fail):
- Skip rows 3,4,5 because they can't reach vertex 2 (dist[3][2]=∞, dist[4][2]=∞, dist[5][2]=∞)

**After k=2:**
```
     1    2    3    4    5
1  [ 0   -2   -1   -5    1 ]   ← Updated: dist[1][3], dist[1][4], dist[1][5]
2  [ ∞    0    1   -3    3 ]   ← Unchanged
3  [ ∞    ∞    0    ∞    2 ]   ← Unchanged
4  [ ∞    ∞    ∞    0   20 ]   ← Unchanged
5  [ ∞    ∞    ∞    ∞    0 ]   ← Unchanged
```

### Step 4: Calculate the Answer (30 seconds)

**Common question types:**

#### Type 1: Sum of specific values
"What is dist[4][3] + dist[5][4] + dist[5][6]?"

- Look up each value in your final matrix
- Add them up (be careful with negatives!)

#### Type 2: Sum of all non-infinity values
"Sum of all values in dist that are not equal to infinity?"

**Fast method:** Go row by row, add up all filled cells:
```
Row 1: 0 + (-2) + (-1) + (-5) + 1 = -7
Row 2: 0 + 1 + (-3) + 3 = 1
Row 3: 0 + 2 = 2
Row 4: 0 + 20 = 20
Row 5: 0
Total: -7 + 1 + 2 + 20 + 0 = 16
```

**Common mistake:** Don't forget the diagonal zeros!

## Optimization Tricks for Speed

### Trick 1: Only Check Reachable Paths
When processing k, you only need to check cells where:
- dist[i][k] ≠ ∞ (can reach vertex k from i)
- dist[k][j] ≠ ∞ (can reach vertex j from k)

**In the exam:** Look at column k and row k. If both are ∞, skip that cell entirely.

### Trick 2: Skip Row/Column k
When k is the intermediate vertex:
- Skip row k (dist[k][j] won't change via vertex k)
- Skip column k (dist[i][k] won't change via vertex k)

### Trick 3: Smart Matrix Layout
Write your matrix with space between cells for updates:

```
        1      2      3      4      5
1    [  0     -2      1      ∞      ∞  ]
                    ↓-1    ↓-5    ↓1
```

### Trick 4: Focus on Dense Vertices First
If the question asks about iteration k=2 or k=3:
- Look at which vertices have MANY outgoing edges (dense rows)
- Look at which vertices have MANY incoming edges (dense columns)
- These will cause the most updates

## Common Exam Scenarios

### Scenario 1: "After 2 iterations"
- Complete k=1, then k=2
- Usually k=1 makes few changes (if vertex 1 is a source)
- k=2 often makes many changes (if vertex 2 is well-connected)

### Scenario 2: "After vertex k is considered"
- Same as "after k iterations"
- After k=3 means you've done k=1, k=2, k=3

### Scenario 3: Negative weights
- Floyd-Warshall handles negative weights fine
- Be careful with arithmetic: -2 + (-3) = -5
- Negative + Positive can improve paths!

## Practice Example

**Graph:** 1→2(-2), 1→3(1), 2→3(1), 2→4(-3), 2→5(3), 3→5(2), 4→5(20)

**After k=2, what is the sum of dist[1][3] + dist[1][4] + dist[1][5]?**

**Fast solution:**

1. **Initial matrix** (15 sec):
   ```
   dist[1][2] = -2, dist[1][3] = 1, dist[2][3] = 1, dist[2][4] = -3, dist[2][5] = 3, dist[3][5] = 2, dist[4][5] = 20
   ```

2. **k=1 iteration** (30 sec):
   - Column 1 is all ∞ except dist[1][1]=0
   - No improvements possible (can't route THROUGH vertex 1)

3. **k=2 iteration** (60 sec):
   - dist[1][3]: min(1, -2+1) = -1
   - dist[1][4]: min(∞, -2+(-3)) = -5
   - dist[1][5]: min(∞, -2+3) = 1

4. **Calculate answer** (15 sec):
   ```
   dist[1][3] + dist[1][4] + dist[1][5] = -1 + (-5) + 1 = -5
   ```

**Total time: 2 minutes**

## Exam Checklist

Before you start:
- [ ] Drew matrix template with correct size
- [ ] Filled diagonal with 0s
- [ ] Filled initial edges from graph

For each iteration k:
- [ ] Identified row k and column k
- [ ] Checked each cell (i,j) where i≠k and j≠k
- [ ] Updated cells where dist[i][k] + dist[k][j] < dist[i][j]
- [ ] Marked updates clearly (arrows or different color)

For the final answer:
- [ ] Located all required values in final matrix
- [ ] Double-checked arithmetic (especially negatives)
- [ ] Verified answer format (sum, single value, etc.)

## Common Mistakes to Avoid

1. **Confusing iteration count:** "After 2 iterations" means k=1 and k=2 are COMPLETE
2. **Forgetting diagonal:** dist[i][i] = 0 always (counts in sums!)
3. **Arithmetic errors:** -2 + (-3) = -5, not -1
4. **Not updating:** If new path is equal to current (not better), don't update
5. **Wrong intermediate vertex:** For k=2, you check paths through vertex 2, not vertex 1
6. **Including ∞ in sums:** Only sum non-infinite values

## Quick Reference Card

```
┌─────────────────────────────────────────────────────┐
│ FLOYD-WARSHALL ITERATION k                          │
├─────────────────────────────────────────────────────┤
│ Goal: Find shortest paths using vertices {1..k}     │
│                                                      │
│ For each cell dist[i][j]:                           │
│   if i ≠ k AND j ≠ k:                              │
│       new = dist[i][k] + dist[k][j]                │
│       if new < dist[i][j]:                          │
│           dist[i][j] = new                          │
│                                                      │
│ Focus: Look at ROW k and COLUMN k                   │
│                                                      │
│ Time: ~1 minute per iteration for 5-node graphs     │
└─────────────────────────────────────────────────────┘
```

## Time Allocation (for 3-mark question, 4.5 minutes total)

- 0:00-0:30 → Setup matrix and fill initial edges
- 0:30-1:30 → First iteration (k=1)
- 1:30-2:45 → Second iteration (k=2)  ← Most work here
- 2:45-4:00 → Calculate answer
- 4:00-4:30 → Double-check arithmetic

**Speed benchmarks:**
- 5-node graph, 2 iterations: 3-4 minutes
- 6-node graph, 2 iterations: 4-5 minutes
- 4-node graph, 3 iterations: 3-4 minutes

If you're taking longer than 2 minutes per mark, SKIP and come back later!