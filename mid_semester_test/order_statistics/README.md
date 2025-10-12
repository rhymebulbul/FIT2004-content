# Order Statistics - QuickSelect with Hoare's Partition

Study materials for finding the kth order statistic using QuickSelect algorithm with Hoare's partition scheme.

## 📚 Study Guides

### [QUICKSELECT_CHEAT_SHEET.md](guides/QUICKSELECT_CHEAT_SHEET.md) ⚡
**Start here for quick review!**

One-page quick reference with:
- Algorithm in 7 steps
- Critical rules table
- Common traps to avoid
- Quick checklist
- Minimal worked example

**Use for:** Last-minute review, during practice problems, quick lookup

---

### [QUICKSELECT_HOARE_PARTITION_GUIDE.md](guides/QUICKSELECT_HOARE_PARTITION_GUIDE.md) 📖
**Complete reference guide**

Comprehensive guide covering:
- Detailed algorithm explanation
- Step-by-step method for solving problems
- Full worked example (actual quiz question)
- Common mistakes with explanations
- Practice tips and verification checklist
- Quick reference card

**Use for:** Deep understanding, learning the algorithm, exam preparation

---

## 🔧 Python Examples & Tracers

### [quickselect_tracer.py](examples/quickselect_tracer.py) 🎯
**MOST USEFUL - Interactive tracer**

Features:
- Step-by-step tracing with detailed output
- Shows every pointer movement and swap
- Verifies answer options automatically
- Pauses between rounds for review
- **Easy to modify** for your own problems

**Usage:**
```python
# Edit these variables at the top of the file:
ARRAY = [2, 3, 7, 8, 4, 9, 1, 10, 6, 5]
K = 3  # 4th order statistic (0-indexed)
MAX_ROUNDS = 2

OPTIONS = {
    'a': (3, 5),   # Check if A[3]=5
    'b': (8, 6),   # Check if A[8]=6
    # ...
}
```

Then run:
```bash
python3 mid_semester_test/order_statistics/examples/quickselect_tracer.py
```

---

### [quickselect_correct.py](examples/quickselect_correct.py) ✅
**Clean, correct implementation**

Features:
- Properly implemented Hoare's partition
- Excludes pivot from scan (i = lo+1)
- Swaps pivot with j (not i)
- Good for understanding the algorithm flow

**Usage:**
```bash
python3 mid_semester_test/order_statistics/examples/quickselect_correct.py
```

---

### Concept Explainers

These files provide detailed explanations of specific concepts:

#### [hoare_partition_explained.py](examples/hoare_partition_explained.py)
**Why we swap with j, not i**

Explains:
- Partition invariants
- Why j points to element <= pivot
- Why swapping with i would break partition
- Worked examples from the quiz

Run to understand: **Final pivot swap logic**

---

#### [pointer_crossing_explained.py](examples/pointer_crossing_explained.py)
**How pointers cross and pivot selection**

Explains:
- How i moves right, j moves left
- What "crossing" means (i >= j, so j < i)
- Why j is to the left when crossed
- How to choose next pivot (first element of new range)

Run to understand: **Pointer mechanics and next round setup**

---

#### [pivot_exclusion_explained.py](examples/pivot_exclusion_explained.py)
**What gets excluded after partitioning**

Explains:
- We exclude the INDEX where pivot lands, not the VALUE
- New range excludes index j
- Why pivot is in final position
- Visual examples

Run to understand: **Search range updates**

---

#### [partition_unsorted_elements.py](examples/partition_unsorted_elements.py)
**Partition guarantees and limitations**

Explains:
- Partition does NOT sort the array
- Only guarantees relative ordering (left <= pivot <= right)
- Elements within regions are unsorted
- Why this is fine for QuickSelect

Run to understand: **What partition does and doesn't guarantee**

---

### Other Tracers

#### [quickselect_detailed_trace.py](examples/quickselect_detailed_trace.py)
Very detailed trace showing every step of pointer movements

#### [quickselect_trace.py](examples/quickselect_trace.py)
Basic tracer with simplified output

---

## 🎓 Learning Path

### For Complete Beginners
1. Read: `QUICKSELECT_HOARE_PARTITION_GUIDE.md` (sections 1-3)
2. Run: `quickselect_correct.py` to see it work
3. Run: `hoare_partition_explained.py` to understand the swap
4. Practice: Modify `quickselect_tracer.py` with simple examples

### For Quiz/Test Prep
1. Review: `QUICKSELECT_CHEAT_SHEET.md` (5 min)
2. Practice: Use `quickselect_tracer.py` with past quiz questions
3. Reference: Keep cheat sheet open during practice

### For Deep Understanding
1. Read: Full `QUICKSELECT_HOARE_PARTITION_GUIDE.md`
2. Run all explainer files in order:
   - `hoare_partition_explained.py`
   - `pointer_crossing_explained.py`
   - `pivot_exclusion_explained.py`
   - `partition_unsorted_elements.py`
3. Implement your own version from scratch

---

## ⚠️ Common Pitfalls

1. **Starting i at lo instead of lo+1**
   - Fix: Always start i = lo + 1 (exclude pivot from scan)

2. **Swapping pivot with i instead of j**
   - Fix: Always swap A[lo] with A[j] (j points to element <= pivot)

3. **Including pivot index in next range**
   - Fix: Exclude j from next range ([j+1, hi] or [lo, j-1])

4. **Expecting sorted subarrays**
   - Fix: Remember partition only creates relative ordering, not sorting

5. **Wrong comparison operators**
   - Fix: i stops when A[i] >= pivot (not >)
   - Fix: j stops when A[j] <= pivot (not <)

Run the explainer files to understand why each of these is wrong!

---

## 📊 Quick Reference

| Concept | Value | Notes |
|---------|-------|-------|
| Pivot | A[lo] | First element of subarray |
| Start i | lo + 1 | After pivot |
| Start j | hi | End of subarray |
| i stops | A[i] >= pivot | >= not > |
| j stops | A[j] <= pivot | <= not < |
| Final swap | A[lo] ↔ A[j] | Use j, not i |
| Next (j<k) | [j+1, hi] | Exclude j |
| Next (j>k) | [lo, j-1] | Exclude j |

---

## 🔗 Related Topics

- **QuickSort**: Uses same partition repeatedly
- **Randomized QuickSelect**: Uses random pivots for better average case
- **Median Finding**: Finding the middle element (k = n/2)
- **Lomuto Partition**: Alternative partition scheme
- **Master Theorem**: For analyzing complexity

---

## 💡 Tips for Test Day

1. **Draw the array** with indices above each element
2. **Mark the pivot** clearly before starting
3. **Track i and j** with arrows as they move
4. **Write down each swap** - don't do it mentally
5. **Verify the final swap** uses j (most common mistake!)
6. **Check your work** against partition guarantees

**Remember:** "i goes Right, j goes Left, swap with j at the end"

---

**Files in this directory:** 12 (2 guides, 10 examples)
**Time to master:** 2-3 hours with practice
**Exam importance:** HIGH (frequent quiz/test topic)
