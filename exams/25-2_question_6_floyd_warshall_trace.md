# Floyd-Warshall Algorithm Trace - Question 6

## Graph Structure

**Vertices:** 1, 2, 3, 4

**Edges (6 edges total):**
- 1 → 2: weight 2
- 2 → 4: weight 3
- 3 → 1: weight 1
- 3 → 2: weight 4
- 4 → 3: weight 2
- 4 → 1: weight 4

## Initial Distance Matrix (k=0)

Direct edges and self-loops only:

```
     1    2    3    4
1    0    2    ∞    ∞
2    ∞    0    ∞    3
3    1    4    0    ∞
4    4    ∞    2    0
```

**Non-infinity values: 10 total (4 diagonal zeros + 6 edges)**

---

## Iteration k=1 (Intermediate vertex = 1)

**Check all pairs (i,j) to see if path i→1→j improves distance[i][j]**

### Improvements during k=1:

1. **d[3][2]**:
   - Current: 4
   - Via vertex 1: d[3][1] + d[1][2] = 1 + 2 = 3
   - **3 < 4 → IMPROVED** ✓

2. **d[4][2]**:
   - Current: ∞
   - Via vertex 1: d[4][1] + d[1][2] = 4 + 2 = 6
   - **6 < ∞ → IMPROVED** ✓

**Total improvements in k=1: 2**

### Distance Matrix after k=1:

```
     1    2    3    4
1    0    2    ∞    ∞
2    ∞    0    ∞    3
3    1    3    0    ∞
4    4    6    2    0
```

**Changes from initial:**
- d[3][2]: 4 → 3
- d[4][2]: ∞ → 6

---

## Iteration k=2 (Intermediate vertex = 2)

**Check all pairs (i,j) to see if path i→2→j improves distance[i][j]**

### Improvements during k=2:

1. **d[1][4]**:
   - Current: ∞
   - Via vertex 2: d[1][2] + d[2][4] = 2 + 3 = 5
   - **5 < ∞ → IMPROVED** ✓

2. **d[3][4]**:
   - Current: ∞
   - Via vertex 2: d[3][2] + d[2][4] = 3 + 3 = 6
   - **6 < ∞ → IMPROVED** ✓

3. **d[4][4]**:
   - Current: 0
   - Via vertex 2: d[4][2] + d[2][4] = 6 + 3 = 9
   - 9 ≥ 0 → No improvement

**Total improvements in k=2: 2**

### Distance Matrix after k=2:

```
     1    2    3    4
1    0    2    ∞    5
2    ∞    0    ∞    3
3    1    3    0    6
4    4    6    2    0
```

**Changes from k=1:**
- d[1][4]: ∞ → 5
- d[3][4]: ∞ → 6

---

## Answers to Question 6

### 6a) How many distance estimates are improved during the first iteration (k=1)?
**Answer: 2**
- d[3][2] improved from 4 to 3
- d[4][2] improved from ∞ to 6

### 6b) What is the distance estimate from vertex 1 to vertex 3 after k=1 and k=2?
**Answer: infinity**
- d[1][3] = ∞ (no edge 1→3 exists, never changed)

### 6c) What is the distance estimate from vertex 3 to vertex 4 after k=1 and k=2?
**Answer: 6**
- d[3][4] starts at ∞ (no direct edge)
- After k=2: path 3→2→4 = 3 + 3 = 6

---

## Student's Answers vs Correct Answers

| Sub-Q | Student Answer | Correct Answer | Mark |
|-------|----------------|----------------|------|
| 6a    | 2              | 2              | 1/1 ✓ |
| 6b    | infinity       | infinity       | 1/1 ✓ |
| 6c    | 6              | 6              | 1/1 ✓ |

**Total: 3/3 marks** ✓✓✓
