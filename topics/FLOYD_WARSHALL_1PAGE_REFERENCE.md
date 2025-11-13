# Floyd-Warshall 1-Page Quick Reference

## Algorithm Core (3 nested loops)
```python
for k in 1..n:           # Intermediate vertex
    for i in 1..n:       # Source
        for j in 1..n:   # Destination
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

## 4-Step Exam Method (Target: 3-4 minutes)

### 1. SETUP (30 sec)
```
     1    2    3    4    5
1  [ 0                    ]  ← Fill diagonal = 0
2  [      0               ]
3  [           0          ]
4  [                0     ]
5  [                   0  ]
```
Fill edges from graph → blank cells = ∞

### 2. ITERATION k (90 sec per iteration)
**For k=2 example:**
- Look at **ROW 2** (paths FROM vertex 2)
- Look at **COLUMN 2** (paths TO vertex 2)
- For each cell [i][j] where i≠2 and j≠2:
  - **Check:** Is [i][2] ≠ ∞ AND [2][j] ≠ ∞?
  - **Calculate:** new = dist[i][2] + dist[2][j]
  - **Update:** If new < dist[i][j], set dist[i][j] = new

### 3. CALCULATE (30 sec)
**Type A:** Sum specific cells → Look up each value, add
**Type B:** Sum all non-∞ → Add row by row (don't forget diagonal!)

### 4. VERIFY (30 sec)
- Check arithmetic (especially negatives)
- Confirm iteration count
- Match answer format

## Speed Tricks

| Trick | How | Saves |
|-------|-----|-------|
| **Skip impossible paths** | If dist[i][k]=∞ OR dist[k][j]=∞ → skip cell [i][j] | 50% time |
| **Skip row/column k** | During iteration k, row k and column k don't change | 30% time |
| **Start with dense vertices** | If k has many edges, expect many updates | Better focus |
| **Use arrow notation** | Mark updates with ↓ instead of erasing | Cleaner work |

## Common Mistakes ❌→✓

| Wrong ❌ | Right ✓ |
|---------|---------|
| After 2 iterations = after k=2 only | After k=1 AND k=2 complete |
| -2 + -3 = -1 | -2 + -3 = -5 |
| Forget diagonal in sum | Include all zeros from diagonal |
| Check all n² cells | Only check cells where path exists |
| Update equal values | Only update if NEW < OLD |

## Visual Memory Aid

```
    i → [?] → j
         ↓
    Currently: dist[i][j]

    Via k:     dist[i][k] + dist[k][j]
                  ↓              ↓
           Look LEFT        Look UP

    Update if: i→k→j < i→j
```

## Negative Numbers Cheat Sheet
```
-2 + 1  = -1     -5 < -3 ✓ (more negative = shorter)
-2 +-3  = -5     -1 < 1  ✓ (negative < positive)
-2 + 3  = +1     -5 < ∞  ✓ (anything < infinity)
```

## Iteration k Checklist
- [ ] Highlight row k and column k
- [ ] Scan each cell [i][j] (skip i=k or j=k)
- [ ] Check if dist[i][k] ≠ ∞ and dist[k][j] ≠ ∞
- [ ] Calculate new = dist[i][k] + dist[k][j]
- [ ] Update only if new < old
- [ ] Mark updates clearly

## Time Benchmarks (Target pace)
| Task | 5 vertices | 6 vertices |
|------|------------|------------|
| Setup matrix | 30 sec | 40 sec |
| k=1 iteration | 30 sec | 45 sec |
| k=2 iteration | 90 sec | 120 sec |
| Calculate sum | 30 sec | 45 sec |
| **Total (2 iter)** | **3 min** | **4 min** |

## Example Walkthrough (k=2)

**Given:** 1→2(-2), 2→3(1), 2→4(-3)

**Initial:**
```
     1    2    3    4
1  [ 0   -2    ∞    ∞ ]
2  [ ∞    0    1   -3 ]
3  [ ∞    ∞    0    ∞ ]
4  [ ∞    ∞    ∞    0 ]
```

**Check k=2 (can we improve by going through vertex 2?):**
- Row 1 has dist[1][2]=-2 ✓ (can reach vertex 2)
- Row 2 skip (k=2)
- Rows 3,4 have dist[3][2]=∞, dist[4][2]=∞ ✗ (cannot reach vertex 2)

**Updates in Row 1:**
- dist[1][3]: ∞ vs (-2+1)=-1 → Update to **-1**
- dist[1][4]: ∞ vs (-2+-3)=-5 → Update to **-5**

**After k=2:**
```
     1    2    3    4
1  [ 0   -2   -1   -5 ]  ← Updated
2  [ ∞    0    1   -3 ]
3  [ ∞    ∞    0    ∞ ]
4  [ ∞    ∞    ∞    0 ]
```

## Emergency Mode (Running out of time)

1. **Calculate only what's asked** - If question wants dist[1][5], don't compute full matrix
2. **Skip k=1 if safe** - If vertex 1 is source (no incoming edges), k=1 rarely updates anything
3. **Guess strategically** - If unsure, compute paths through most-connected vertex

## One-Minute Pre-Exam Drill

Close your eyes and recite:
1. "For each k, I check if paths through k are shorter"
2. "I look at row k and column k"
3. "I update [i][j] if [i][k] + [k][j] < [i][j]"
4. "After k iterations, I can use vertices 1 through k"

---

**REMEMBER:** Floyd-Warshall is algorithmic and systematic. Follow the pattern, check your arithmetic, and you'll get full marks! Practice until you can do 2 iterations in under 3 minutes.