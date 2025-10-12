# QuickSelect + Hoare Partition - Quick Reference Cheat Sheet

## Algorithm in 7 Steps

### For Each Round:

**1. Identify Pivot**
```
pivot = A[lo]  (first element of search range)
```

**2. Initialize Pointers**
```
i = lo + 1  (AFTER pivot, not at pivot!)
j = hi
```

**3. Scan and Swap Loop**
```
while i <= j:
    Move i right while A[i] < pivot
    Move j left while A[j] > pivot

    if i < j:
        swap A[i] and A[j]
        i++, j--
    else:
        break  (pointers crossed)
```

**4. Final Pivot Swap**
```
swap A[lo] and A[j]  (ALWAYS use j, NEVER i!)
```

**5. Pivot is at index j**

**6. Decision**
```
if j == k: FOUND!
if j < k:  search [j+1, hi]
if j > k:  search [lo, j-1]
```

**7. Next pivot = first element of new range**

---

## Critical Rules ⚠️

| Rule | Correct | Wrong |
|------|---------|-------|
| Start i | `i = lo + 1` | ~~`i = lo`~~ |
| i stops when | `A[i] >= pivot` | ~~`A[i] > pivot`~~ |
| j stops when | `A[j] <= pivot` | ~~`A[j] < pivot`~~ |
| Final swap | `swap A[lo], A[j]` | ~~`swap A[lo], A[i]`~~ |
| Next range (j<k) | `[j+1, hi]` | ~~`[j, hi]`~~ |
| Next range (j>k) | `[lo, j-1]` | ~~`[lo, j]`~~ |

---

## Quick Checklist ✓

Before answering:
- [ ] Used first element as pivot
- [ ] Started i at lo+1
- [ ] Stopped i when A[i] >= pivot
- [ ] Stopped j when A[j] <= pivot
- [ ] Swapped with j (not i)
- [ ] Excluded pivot index from next range
- [ ] Tracked all array changes

---

## Common Traps 🚨

1. **Pivot location**: First element of SUBARRAY, not always A[0]
2. **i starting point**: lo+1 (exclude pivot!)
3. **Final swap**: Use j (element <= pivot), not i
4. **Partition result**: NOT sorted, only relatively ordered
5. **Next range**: Exclude index j (pivot's final position)

---

## One-Round Trace Template

```
Array: [___________________]
Index:  0  1  2  3  4  ...
Range: [lo, hi] = [__, __]
Pivot: A[lo] = __

i = lo+1 = __
j = hi = __

Scan:
  i stops at __: A[__] = __ (>= pivot)
  j stops at __: A[__] = __ (<= pivot)
  Swap? [Yes/No]
  (repeat until i >= j)

Final swap: A[lo] ↔ A[j]
Result: j = __

Decision:
  j __ k, so search [____]
  Next pivot: A[__] = __
```

---

## Memory Aid 🧠

**"i goes Right, j goes Left, swap with j at the end"**

**i**ncreases → Right →
**j** ??? (no memory aid, just remember it goes left)
**j**ust use **j** for final swap

---

## Example (Minimal)

```
A = [2,3,7,8,4,9,1,10,6,5], k=3

Round 1: pivot=2, i=1, j=9
  Swap A[1]↔A[6]: [2,1,7,8,4,9,3,10,6,5]
  Pointers cross at i=2, j=1
  Swap pivot: [1,2,7,8,4,9,3,10,6,5]
  j=1 < k=3 → search [2,9]

Round 2: pivot=7, i=3, j=9
  Swap A[3]↔A[9]: [1,2,7,5,4,9,3,10,6,8]
  Swap A[5]↔A[8]: [1,2,7,5,4,6,3,10,9,8]
  Pointers cross at i=7, j=6
  Swap pivot: [1,2,3,5,4,6,7,10,9,8]
  j=6 > k=3 → would search [2,5]

Final: [1,2,3,5,4,6,7,10,9,8]
A[3]=5 ✓, A[9]=8 ✓, A[4]=4 ✓
```

---

## Time Saver Tips ⏱️

1. **Draw the array** with indices above
2. **Mark the pivot** clearly
3. **Track i and j** with arrows
4. **Write each swap** - don't do mentally
5. **Verify <= and >=** for left/right sides
6. **Double-check j** in final swap

---

## Partition Guarantees

After partition at j:
```
[... < pivot ...] [pivot] [... > pivot ...]
    lo ... j-1       j       j+1 ... hi
```

**NOT sorted within regions!**

---

*Use with QUICKSELECT_HOARE_PARTITION_GUIDE.md for detailed explanations*
