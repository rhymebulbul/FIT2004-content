# Floyd-Warshall Visual Cheatsheet for Exams

## The One Thing to Remember

```
┌────────────────────────────────────────────────────────┐
│  After iteration k:                                    │
│  dist[i][j] = shortest path from i to j               │
│               using ONLY {1,2,...,k} as intermediates  │
└────────────────────────────────────────────────────────┘
```

## Visual Matrix Update Pattern

### Iteration k: "Going through vertex k"

```
Look at this pattern:

         j (destination)
         ↓
    ... [k] ...
i → ... [?] ...   ← Can I improve [?] by going i→k→j?

Check: dist[i][j] vs dist[i][k] + dist[k][j]
Update: dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

**Visual guide for k=2:**

```
         1    2    3    4    5
              ↓ Column 2 (paths TO vertex 2)
    1  [ 0   -2    1    ∞    ∞ ]
    2  [ ∞    0    1   -3    3 ] ← Row 2 (paths FROM vertex 2)
    3  [ ∞    ∞    0    ∞    2 ]
    4  [ ∞    ∞    ∞    0   20 ]
    5  [ ∞    ∞    ∞    ∞    0 ]

For each cell [i][j]:
  - Look LEFT to [i][2] (can i reach vertex 2?)
  - Look UP to [2][j] (can vertex 2 reach j?)
  - If both exist (not ∞), try the path i→2→j
```

**Example: Update dist[1][3]**

```
         1    2    3
    1  [ 0   -2    1 ]
                   ↑
                   Currently 1

    Path through vertex 2:
    [1][2] = -2  (go from 1 to 2)
    [2][3] =  1  (go from 2 to 3)
    Sum   = -1   (total path 1→2→3)

    Is -1 < 1? YES!
    Update: dist[1][3] = -1
```

## Hand-Drawn Matrix Template for Speed

**Step 1: Quick Setup (15 seconds)**

```
Draw this template in your exam paper:

     1   2   3   4   5
   ┌───┬───┬───┬───┬───┐
 1 │ 0 │   │   │   │   │
   ├───┼───┼───┼───┼───┤
 2 │   │ 0 │   │   │   │
   ├───┼───┼───┼───┼───┤
 3 │   │   │ 0 │   │   │
   ├───┼───┼───┼───┼───┤
 4 │   │   │   │ 0 │   │
   ├───┼───┼───┼───┼───┤
 5 │   │   │   │   │ 0 │
   └───┴───┴───┴───┴───┘

Leave blank = ∞
```

**Step 2: Fill Edges (30 seconds)**

Graph: 1→2(-2), 1→3(1), 2→3(1), 2→4(-3), 2→5(3), 3→5(2), 4→5(20)

```
     1   2   3   4   5
   ┌───┬───┬───┬───┬───┐
 1 │ 0 │-2 │ 1 │   │   │  ← Fill: 1→2(-2), 1→3(1)
   ├───┼───┼───┼───┼───┤
 2 │   │ 0 │ 1 │-3 │ 3 │  ← Fill: 2→3(1), 2→4(-3), 2→5(3)
   ├───┼───┼───┼───┼───┤
 3 │   │   │ 0 │   │ 2 │  ← Fill: 3→5(2)
   ├───┼───┼───┼───┼───┤
 4 │   │   │   │ 0 │20 │  ← Fill: 4→5(20)
   ├───┼───┼───┼───┼───┤
 5 │   │   │   │   │ 0 │  ← No outgoing edges
   └───┴───┴───┴───┴───┘
```

## Systematic Scan Pattern

### For iteration k=2: Highlight row 2 and column 2

```
     1   2   3   4   5
         ↓ FOCUS COLUMN
   ┌───┬───┬───┬───┬───┐
 1 │ 0 │-2 │ 1 │   │   │  ← Row 1: Has access to vertex 2 ✓
   ├───┼───┼───┼───┼───┤
 2 │   │ 0 │ 1 │-3 │ 3 │  ← FOCUS ROW (skip this row)
   ├───┼───┼───┼───┼───┤
 3 │   │   │ 0 │   │ 2 │  ← Row 3: No access to vertex 2 ✗
   ├───┼───┼───┼───┼───┤
 4 │   │   │   │ 0 │20 │  ← Row 4: No access to vertex 2 ✗
   ├───┼───┼───┼───┼───┤
 5 │   │   │   │   │ 0 │  ← Row 5: No access to vertex 2 ✗
   └───┴───┴───┴───┴───┘

Quick check: Only row 1 can reach vertex 2 (dist[1][2] = -2)
So only cells in row 1 can be updated!
```

### Update cells in row 1 (the only row with access to k=2)

```
Check dist[1][3]: 1 vs (-2 + 1) = -1  → Update to -1 ✓
Check dist[1][4]: ∞ vs (-2 + -3) = -5 → Update to -5 ✓
Check dist[1][5]: ∞ vs (-2 + 3) = 1   → Update to 1 ✓
```

**Final matrix after k=2:**

```
     1   2   3   4   5
   ┌───┬───┬───┬───┬───┐
 1 │ 0 │-2 │-1 │-5 │ 1 │  ← Updated 3 cells
   ├───┼───┼───┼───┼───┤
 2 │   │ 0 │ 1 │-3 │ 3 │
   ├───┼───┼───┼───┼───┤
 3 │   │   │ 0 │   │ 2 │
   ├───┼───┼───┼───┼───┤
 4 │   │   │   │ 0 │20 │
   ├───┼───┼───┼───┼───┤
 5 │   │   │   │   │ 0 │
   └───┴───┴───┴───┴───┘
```

## Smart Filtering: The "Reachability Check"

**Before checking each cell, ask:**

```
For updating dist[i][j] via vertex k:

1. Can i reach k?  → Check dist[i][k] ≠ ∞
2. Can k reach j?  → Check dist[k][j] ≠ ∞

If either is ∞, SKIP this cell (no update possible)
```

**Visual example for k=2:**

```
Column 2 (can reach vertex 2):    Row 2 (can leave vertex 2):
    1 → 2 ✓ (-2)                      2 → 1 ✗ (∞)
    2 → 2 ✓ (0, but skip row k)       2 → 2 ✓ (0)
    3 → 2 ✗ (∞)                       2 → 3 ✓ (1)
    4 → 2 ✗ (∞)                       2 → 4 ✓ (-3)
    5 → 2 ✗ (∞)                       2 → 5 ✓ (3)

Only row 1 has access to vertex 2!
So only check cells: [1][1], [1][3], [1][4], [1][5]
(Skip [1][2] because j=k)
```

## Arithmetic Tips for Negative Numbers

```
Common operations in Floyd-Warshall:

-2 + 1  = -1   ✓
-2 + -3 = -5   ✓ (add magnitudes, keep negative)
-2 + 3  =  1   ✓ (subtract magnitudes, sign of larger)
-5 + 20 = 15   ✓

Comparison with negative numbers:
-1 < 1   → -1 is better (shorter path)
-5 < ∞   → -5 is better
-5 < -3  → -5 is better (more negative = shorter)
```

## Speed Drill: 30-Second Check

**After each iteration, verify:**

1. ✓ Did I check row/column k?
2. ✓ Did I skip cells where dist[i][k] = ∞ or dist[k][j] = ∞?
3. ✓ Did I compare old vs new and only update if new is smaller?
4. ✓ Did I mark updates clearly?

## Common Patterns

### Pattern 1: Vertex 1 as source (typical exam setup)
```
If vertex 1 has NO incoming edges:
→ Column 1 is all ∞ (except dist[1][1] = 0)
→ k=1 iteration makes NO updates
→ Most work happens in k=2, k=3
```

### Pattern 2: Dense vertex (hub)
```
If vertex 2 has many edges (both in and out):
→ k=2 iteration makes MANY updates
→ This is where you spend most time
```

### Pattern 3: Negative weight chains
```
If there's a path 1→2→3→4 with negative weights:
→ Each iteration improves more distant paths
→ dist[1][4] improves in k=2, k=3 iterations
→ Be extra careful with arithmetic!
```

## Exam Strategy Summary

```
┌─────────────────────────────────────────────┐
│ TIME BUDGET for 3-mark question (4.5 min)  │
├─────────────────────────────────────────────┤
│ 0:00 - 0:30  Setup matrix, fill edges       │
│ 0:30 - 1:30  Iteration k=1                  │
│ 1:30 - 3:00  Iteration k=2 (most work)      │
│ 3:00 - 4:00  Calculate answer               │
│ 4:00 - 4:30  Verify arithmetic              │
└─────────────────────────────────────────────┘

SPEED TIPS:
• Use pencil (for corrections)
• Mark updated cells with ↓ or circle
• Only check cells where both [i][k] and [k][j] exist
• Skip row k and column k during iteration k
• Double-check negative arithmetic
```

## Emergency Shortcuts

**If running out of time:**

1. **Skip k=1 if vertex 1 is a source** (usually no updates)
2. **Only update cells you need** for the final answer
3. **Use symmetry** if the graph is undirected
4. **Focus on paths through dense vertices** (many edges)

## One-Liner Memory Aid

```
┌──────────────────────────────────────────────────────────┐
│  "For each k, check if i→k→j beats i→j directly"        │
│                                                           │
│  Look at ROW k (paths FROM k)                            │
│  Look at COLUMN k (paths TO k)                           │
│  Update cells where BOTH exist                           │
└──────────────────────────────────────────────────────────┘
```

## Validation Checklist

Before submitting your answer:

- [ ] Matrix size matches number of vertices
- [ ] Diagonal is all zeros
- [ ] Initial edges match the graph
- [ ] Completed correct number of iterations
- [ ] Arithmetic is correct (especially negatives)
- [ ] Answer format matches question (sum, single value, etc.)
- [ ] Units/vertices are labeled correctly (1-indexed vs 0-indexed)

## Practice Scenarios

### Scenario 1: "After k=2, what is dist[1][5]?"
1. Draw matrix, fill edges (30 sec)
2. Do k=1 iteration (45 sec)
3. Do k=2 iteration (60 sec)
4. Look up dist[1][5] (5 sec)
**Total: ~2.5 minutes**

### Scenario 2: "Sum all non-infinite values after k=2"
1. Draw matrix, fill edges (30 sec)
2. Do k=1 iteration (45 sec)
3. Do k=2 iteration (60 sec)
4. Add all filled cells row by row (45 sec)
**Total: ~3 minutes**

### Scenario 3: "Sum dist[4][3] + dist[5][4] + dist[5][6]"
1. Draw matrix, fill edges (30 sec)
2. Do required iterations (2-3 min)
3. Look up THREE specific cells (15 sec)
4. Add them up (10 sec)
**Total: ~3.5 minutes**

---

**FINAL TIP:** Practice 3-5 Floyd-Warshall problems the night before the exam until you can do them in under 3 minutes. Speed comes from pattern recognition!