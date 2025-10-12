# Algorithm Analysis

Study materials for algorithm complexity analysis, asymptotic notation, and recurrence relations.

## 📚 Study Guides

### [RECURRENCE_RELATIONS_GUIDE.md](RECURRENCE_RELATIONS_GUIDE.md)
**Complete guide to solving recurrences**

Covers:
- Master Theorem (all cases)
- Recursion tree method
- Substitution method
- Common recurrence patterns
- Practice problems with solutions

**Use for:**
- Analyzing divide-and-conquer algorithms
- Finding time/space complexity
- Proving asymptotic bounds

---

## 🎯 Topics Covered

### Asymptotic Analysis
- Big O, Ω, Θ notation
- Growth rates comparison
- Best/worst/average case analysis

### Recurrence Relations
- Master Theorem application
- Solving divide-and-conquer recurrences
- Common patterns (T(n) = aT(n/b) + f(n))

### Complexity Proofs
- Loop analysis
- Recursive algorithm analysis
- Amortized analysis

---

## 💡 Quick Tips

### Using Master Theorem
```
T(n) = aT(n/b) + f(n)

Compare f(n) with n^(log_b(a)):
- Case 1: f(n) = O(n^(log_b(a) - ε)) → T(n) = Θ(n^(log_b(a)))
- Case 2: f(n) = Θ(n^(log_b(a))) → T(n) = Θ(n^(log_b(a)) log n)
- Case 3: f(n) = Ω(n^(log_b(a) + ε)) → T(n) = Θ(f(n))
```

### Common Recurrences
| Algorithm | Recurrence | Solution |
|-----------|------------|----------|
| Binary Search | T(n) = T(n/2) + O(1) | O(log n) |
| Merge Sort | T(n) = 2T(n/2) + O(n) | O(n log n) |
| QuickSelect (avg) | T(n) = T(n/2) + O(n) | O(n) |
| Naive Multiplication | T(n) = 4T(n/2) + O(n) | O(n²) |
| Karatsuba | T(n) = 3T(n/2) + O(n) | O(n^1.58) |

---

## 📖 Learning Path

1. **Review:** Asymptotic notation basics
2. **Study:** Master Theorem with examples
3. **Practice:** Apply to known algorithms
4. **Test:** Solve practice problems

---

## 🔗 Related Topics

- Divide and Conquer algorithms
- Sorting algorithm analysis
- Graph algorithm complexity
- Dynamic Programming complexity

---

**Files in this directory:** 1 guide
**Time to master:** 2-3 hours
**Exam importance:** HIGH (fundamental to all algorithm analysis)
