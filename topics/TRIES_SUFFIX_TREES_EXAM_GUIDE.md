# Tries and Suffix Trees - Exam Guide

## Core Trie/Suffix Tree Concepts

### 1. Trie Fundamentals

**Structure**: Tree where each edge represents a character; paths from root represent strings

**Key Properties**:
- **Termination markers**: Use `$` or similar to mark string ends
- **Time complexity**: O(m) for insert/search where m = string length
- **Space complexity**: O(T) where T = total characters across all strings
- **Node properties**: Each node can store metadata (counters, flags, scores)

**Basic Operations**:
- Insert: Follow/create edges for each character, mark end with `$`
- Search: Follow edges for each character, check for `$` at end
- All strings with prefix p: Found in subtree rooted at p's last character

### 2. Prefix Trie vs Suffix Trie vs Suffix Tree

| Structure | Description | Space | Construction Time |
|-----------|-------------|-------|-------------------|
| **Prefix Trie** | Stores strings as-is from root | O(T) | O(T) |
| **Suffix Trie** | Stores all suffixes of a string | O(n²) | O(n²) |
| **Suffix Tree** | Compressed suffix trie | O(n) | O(n) with Ukkonen's |

**Key Differences**:
- **Trie**: One node per character, edges labeled with single characters
- **Tree**: Compresses chains of single-child nodes into edges with string labels
- **Compression**: Each edge in tree represents one or more characters from trie

**When to Use**:
- Prefix trie: Working with complete strings, prefix queries
- Suffix trie: Conceptual understanding, small examples
- Suffix tree: Efficient substring operations, large strings

### 3. Critical Relationships

**The Golden Rule**: Every substring is a *prefix of a suffix*

This means:
- All substrings of string S can be found in a suffix trie/tree of S
- Each substring corresponds to a path from root to some node
- If two substrings are identical, they end at the same node

**Other Key Relationships**:
- **Shared prefixes**: All strings sharing prefix p are in the subtree rooted at p's last character
- **Distinct strings**: Count terminal nodes (`$`) in prefix trie
- **Distinct substrings**:
  - In suffix trie: Count all nodes (excluding `$`)
  - In suffix tree: Sum all edge label lengths (characters stored at edges)
- **Longest repeated substring**: Deepest internal node (has multiple children)

### 4. Augmentation Techniques

**CRITICAL FOR EXAMS**: You'll need to modify standard tries by storing extra information at nodes.

| Augmentation | What to Store | When to Update | Use Case | Example |
|--------------|---------------|----------------|----------|---------|
| **Prefix counters** | Count of strings passing through node | Increment during insertion | Count strings with prefix p | "How many words start with 'pre'?" |
| **Boolean flags** | Properties (e.g., "in s1", "in s2") | Set during insertion/traversal | Longest common substring | "Is this substring in both strings?" |
| **Scores/weights** | Weighted sums | Add weight × depth during insertion | Most powerful prefix | "Prefix with max sum of weights" |
| **Lexicographic tracking** | Last node with smaller sibling | During traversal | Predecessor queries | "Largest string ≤ query" |
| **Depth/length** | Distance from root | Increment on descent | Longest substring problems | "Deepest node with property X" |

**Augmentation Pattern**:
```
During insertion of string S with weight W:
    current_node = root
    depth = 0
    for each character c in S:
        current_node = current_node.get_or_create_child(c)
        depth += 1

        # Update augmented data
        current_node.counter += 1                    # For counting
        current_node.score += W * depth              # For weighted scoring
        current_node.is_from_s1 = True               # For flags
```

### 5. Common Algorithm Patterns

#### Pattern 1: Build + Traverse
```
1. Build trie/suffix tree in O(T) or O(n)
2. Traverse to count/find something in O(T) or O(n)
```

**Used for**: Counting distinct strings/substrings, finding longest repeated substring

**Example - Count Distinct Strings**:
```
1. Build prefix trie, appending "$" to each string: O(T)
2. Traverse tree, count nodes containing "$": O(T)
3. Return count
Total: O(T)
```

**Example - Count Distinct Substrings**:
```
1. Build suffix tree of string S: O(n)
2. Traverse tree, sum edge label lengths: O(n)
3. Return sum (this counts all trie nodes that were compressed)
Total: O(n)
```

#### Pattern 2: Augmented Insertion
```
During insertion:
  - Update counters/flags/scores at each node visited
  - Ensures O(T) preprocessing, O(m) queries
```

**Used for**: Prefix counting, weighted scoring

**Example - Count Strings with Prefix p**:
```
Build phase (modified insertion):
    for each string S:
        for each character c in S:
            node = node.get_or_create_child(c)
            node.counter += 1  # ← Augmentation

Query phase:
    traverse to last character of p: O(m)
    return node.counter: O(1)
Total query: O(m)
```

#### Pattern 3: Multi-String Suffix Trees
```
1. Concatenate strings with unique separators: s1 + "#" + s2 + "$"
2. Build suffix tree
3. Use separators to identify which original string a substring came from
```

**Used for**: Longest common substring, pattern matching across multiple strings

**Key Insight**: Separators `#` and `$` only appear in leaves (never in internal nodes)
- Why? They don't repeat, and internal nodes represent repeating substrings

**Example - Longest Common Substring**:
```
1. Concatenate: s1 + "#" + s2 + "$"
2. Build suffix tree: O(n + m)
3. Traverse tree, at each node set flags:
   - is_in_s1: True if any leaf descendant contains "#"
   - is_in_s2: True if any leaf descendant has no "#"
4. Find deepest node with both flags set: O(n + m)
5. Return substring corresponding to that node
```

#### Pattern 4: Lexicographic Navigation
```
- Track "last node with lexicographically smaller child"
- Backtrack to that node
- Follow lexicographically greatest/smallest path to leaf
```

**Used for**: Predecessor/successor queries

**Example - Predecessor Query**:
```
1. Traverse query string, tracking:
   - Current node
   - Deepest ancestor with child < current path
2. If traversal succeeds completely: return query (it's in trie)
3. If traversal fails:
   - If no tracked ancestor: return null (no predecessor exists)
   - Else: backtrack to ancestor
   - Take the greatest child < original path
   - Follow lexicographically greatest path to leaf
Total: O(m + n) where n = output length
```

## Problem-Solving Checklist

### Step 1: Identify the String Relationship

**Ask yourself**: What am I searching for?

- **Prefixes** → Use prefix trie
  - Examples: "strings starting with...", "words with prefix...", "all extensions of..."

- **Substrings** → Use suffix trie/tree
  - Remember: substring = prefix of suffix
  - Examples: "patterns occurring in...", "repeated substrings", "longest common substring"

- **Multiple strings** → Consider concatenation with separators
  - Examples: "common to s1 and s2", "appears in all strings", "unique to one string"

### Step 2: Determine What to Count/Find

- **Distinct items** → Count nodes (or edge characters in trees)
  - Distinct strings: Count `$` terminal nodes
  - Distinct substrings: Count all nodes (trie) or sum edge lengths (tree)

- **Items with property** → Count nodes with flags/markers
  - Strings with prefix p: Traverse to p, count leaves in subtree
  - Substrings in both s1 and s2: Count nodes with both flags set

- **Optimal item** → Traverse to find max/min score
  - Longest: Find deepest node with property
  - Most powerful: Find node with maximum score
  - Lexicographically greatest/smallest: Navigate using character ordering

### Step 3: Check if Augmentation is Needed

**Ask yourself**: Do I need to store extra information?

- **Counts**: Add counters incremented during insertion
- **Properties**: Add boolean flags set during insertion/traversal
- **Scores**: Add numeric fields updated with formulas during insertion
- **Relationships**: Add parent/depth pointers for navigation

**Complexity check**:
- Augmentation during insertion: No change to O(T) construction if done in O(1) per node
- Augmentation during traversal: Added to traversal cost, usually still O(T) or O(n)

### Step 4: Analyze Complexity

**Construction**:
- Prefix trie: O(T) where T = total characters
- Suffix trie: O(n²) for string of length n
- Suffix tree: O(n) with Ukkonen's algorithm (assumed available)

**Queries**:
- Prefix-based (traverse to specific prefix): O(m) where m = prefix length
- Full traversal (count/find across all nodes): O(T) or O(n)
- Output-sensitive: O(output size) acceptable for some problems

**Common patterns**:
- O(T): Build trie + traverse once
- O(n): Build suffix tree + traverse once
- O(m + n): Query of length m, output of length n
- O(n²): Acceptable only for suffix tries in problems explicitly allowing it

## Problem Analysis Examples

### Problem 1: Count Distinct Strings

**Given**: Sequence of strings over constant-size alphabet
**Find**: Number of distinct strings
**Time**: O(T) where T = total length

**Analysis**:
1. **String relationship**: Complete strings → prefix trie
2. **What to count**: Distinct strings → count terminal markers
3. **Augmentation**: None needed
4. **Algorithm**: Build trie with `$` terminators, count `$` nodes

**Solution**:
```
for each string S:
    insert S + "$" into trie

count = 0
traverse entire trie:
    if node contains "$":
        count += 1
return count
```

### Problem 2: Count Strings with Prefix p

**Given**: Set of strings, query prefix p
**Find**: Number of strings starting with p
**Query time**: O(m) where m = |p|

**Analysis**:
1. **String relationship**: Prefixes → prefix trie
2. **What to count**: Strings in subtree → need efficient counting
3. **Augmentation**: Add counter at each node
4. **Algorithm**: Augmented insertion + traversal to p

**Solution**:
```
Build phase:
    for each string S:
        node = root
        for each character c in S:
            node = node.get_or_create_child(c)
            node.counter += 1  # ← Augmentation

Query phase:
    node = root
    for each character c in p:
        if node has no child c:
            return 0
        node = node.get_child(c)
    return node.counter
```

### Problem 3: Count Distinct Substrings

**Given**: String S of length n
**Find**: Number of distinct substrings
**Time**: O(n)

**Analysis**:
1. **String relationship**: Substrings = prefixes of suffixes → suffix tree
2. **What to count**: Distinct substrings → sum edge lengths
3. **Augmentation**: None needed
4. **Complexity**: Must use suffix tree (not trie) for O(n)

**Key insight**:
- Suffix trie has O(n²) nodes, one per substring
- Suffix tree compresses these: each edge represents multiple trie nodes
- Number of characters on edge = number of trie nodes compressed
- Sum of all edge lengths = total trie nodes = distinct substrings

**Solution**:
```
Build suffix tree of S: O(n)

count = 0
traverse tree:
    for each edge:
        length = edge.end_index - edge.start_index
        count += length
return count
```

### Problem 4: Longest Common Substring

**Given**: Two strings s1, s2
**Find**: Longest string that is substring of both
**Time**: O(n + m)

**Analysis**:
1. **String relationship**: Substrings of multiple strings → multi-string suffix tree
2. **What to find**: Longest substring in both → deepest node with both flags
3. **Augmentation**: Boolean flags (is_in_s1, is_in_s2)
4. **Technique**: Concatenate with separator

**Key insights**:
- Concatenate s1 + "#" + s2 + "$" to avoid false matches
- "#" and "$" only appear in leaves (they don't repeat)
- Node with both flags = substring appears in both originals
- Deepest such node = longest common substring

**Solution**:
```
Build suffix tree of s1 + "#" + s2 + "$": O(n + m)

Traverse tree (post-order):
    for each leaf:
        if leaf contains "#":
            leaf.is_in_s1 = True
        else:
            leaf.is_in_s2 = True

    for each internal node:
        is_in_s1 = any child has is_in_s1 = True
        is_in_s2 = any child has is_in_s2 = True

max_depth = 0
answer_node = null

for each node:
    if node.is_in_s1 AND node.is_in_s2:
        if node.depth > max_depth:
            max_depth = node.depth
            answer_node = node

return substring corresponding to answer_node
```

### Problem 5: Predecessor Query

**Given**: Trie and query string q
**Find**: Lexicographically greatest string in trie ≤ q
**Time**: O(n + m) where n = output length, m = query length

**Analysis**:
1. **String relationship**: Complete strings → prefix trie
2. **What to find**: Optimal (lexicographically greatest ≤ q)
3. **Augmentation**: Track ancestor during traversal
4. **Technique**: Backtrack + navigate

**Key insight**: The answer is either:
- Query itself (if in trie)
- Longest prefix of query that can be extended with a smaller character

**Solution**:
```
Traverse query string:
    ancestor = null
    ancestor_child = null

    for each character c in query:
        if current_node has child < c:
            ancestor = current_node
            ancestor_child = greatest child < c

        if current_node has child c:
            current_node = current_node.get_child(c)
        else:
            break  # Traversal failed

    if reached end (including "$"):
        return query  # Query is in trie

    if ancestor == null:
        return null  # No predecessor exists

    # Backtrack to ancestor
    path = path from root to ancestor

    # Extend with smaller character
    path += ancestor_child.character
    current_node = ancestor_child

    # Follow lexicographically greatest path to leaf
    while current_node is not leaf:
        current_node = greatest child of current_node
        path += current_node.character

    return path (without "$")
```

### Problem 6: Most Powerful Prefix

**Given**: Strings s1...sn with weights w1...wn
**Find**: Prefix p maximizing Σ(wi × |p|) for all i where si has prefix p
**Time**: O(T)

**Analysis**:
1. **String relationship**: Prefixes → prefix trie
2. **What to find**: Optimal (maximum score)
3. **Augmentation**: Score at each node
4. **Formula**: score(node) = Σ(weight × depth) for all strings passing through

**Key insight**: During insertion of string with weight w:
- At depth d, add w × d to node's score
- After all insertions, traverse to find max score

**Solution**:
```
Build phase:
    for each string S with weight W:
        node = root
        depth = 0

        for each character c in S:
            node = node.get_or_create_child(c)
            depth += 1
            node.score += W * depth  # ← Augmentation

Query phase:
    max_score = 0
    answer_node = null

    traverse entire trie:
        if node.score > max_score:
            max_score = node.score
            answer_node = node

    return prefix corresponding to answer_node
```

## Common Pitfalls and Tips

### Pitfall 1: Confusing Trie and Tree Complexities

**Problem**: Using suffix trie when suffix tree is required

**Fix**:
- Suffix trie: O(n²) space and construction
- Suffix tree: O(n) space and construction
- If problem requires O(n) and involves substrings, you MUST use suffix tree

### Pitfall 2: Forgetting Terminators

**Problem**: Not adding `$` to strings, causing incorrect counts

**Example**: Without `$`, "car" and "card" share the same path for "car"
- If "car" has no terminator, you can't tell if it's a complete string

**Fix**: Always append `$` (or similar) to mark string endings

### Pitfall 3: Incorrect Augmentation Timing

**Problem**: Computing counts/scores during query instead of insertion

**Example**: Counting leaves in subtree during each query → O(T) per query
**Fix**: Store count during insertion → O(1) per query

### Pitfall 4: Missing Edge Cases in Concatenation

**Problem**: Not using separators, causing false matches

**Example**: s1="abc", s2="def", looking for common substrings
- Without separator: "abcdef" might find "cd" as repeated (if it appears in both)
- With separator: "abc#def$" correctly separates the strings

**Fix**: Always use unique separator when concatenating strings

### Pitfall 5: Counting Nodes vs Characters

**Problem**: Counting nodes in suffix tree when should count characters

**Example**: Distinct substrings
- Trie: Count nodes directly
- Tree: Count characters on edges (not nodes)

**Fix**: Understand what compression means
- Each edge in tree = multiple nodes in trie
- Edge length = number of nodes compressed

## Practice Strategies

### 1. Draw Small Examples

For any problem, first draw the trie/tree for a tiny example:
- 2-3 short strings (length 3-4 each)
- Manually trace your algorithm
- Verify counts/scores/paths

### 2. Trace Augmented Insertions

Practice these step-by-step:
```
Insert "ab" (weight 10) then "ac" (weight 20)

After "ab":
    root
    └─ a (score: 10×1=10, count: 1)
       └─ b (score: 10×2=20, count: 1)
          └─ $ (score: 10×3=30, count: 1)

After "ac":
    root
    └─ a (score: 10×1+20×1=30, count: 2)
       ├─ b (score: 10×2=20, count: 1)
       │  └─ $ (score: 10×3=30, count: 1)
       └─ c (score: 20×2=40, count: 1)
          └─ $ (score: 20×3=60, count: 1)
```

### 3. Convert Trie Solutions to Tree Solutions

Practice: "I have an O(n²) suffix trie solution, how do I make it O(n)?"
- Identify what you're counting in the trie
- Figure out the equivalent in the tree
- Usually: count characters on edges instead of nodes

### 4. Work with Separators

Practice problems with multiple strings:
- When do you need separators?
- How do separators help identify string origins?
- Why do separators only appear in leaves?

### 5. Analyze Time Complexity

For every solution, write out:
- Construction time
- Traversal time
- Query time (if applicable)
- Space complexity

Make sure you can justify each term.

## Quick Reference

### When to Use What

| Problem Type | Data Structure | Key Technique |
|--------------|----------------|---------------|
| Distinct strings | Prefix trie | Count `$` nodes |
| Distinct substrings | Suffix tree | Sum edge lengths |
| Prefix counting | Augmented prefix trie | Counters at nodes |
| Longest repeated substring | Suffix tree | Deepest internal node |
| Longest common substring | Multi-string suffix tree | Flags + separator |
| Weighted prefix scoring | Augmented prefix trie | Score = Σ(weight × depth) |
| Predecessor/successor | Prefix trie | Lexicographic navigation |

### Complexity Cheat Sheet

| Operation | Prefix Trie | Suffix Trie | Suffix Tree |
|-----------|-------------|-------------|-------------|
| Construction | O(T) | O(n²) | O(n) |
| Space | O(T) | O(n²) | O(n) |
| Search | O(m) | O(m) | O(m) |
| Count with prefix p | O(m) with counters | N/A | N/A |
| Count distinct substrings | N/A | O(n²) traverse | O(n) sum edges |

Where:
- T = total characters in all strings
- n = length of string
- m = length of query/prefix

### Must-Know Formulas

1. **Distinct substrings in suffix tree**: Σ(edge lengths) across all edges
2. **Prefix count**: Store counter at each node, increment during insertion
3. **Weighted prefix score**: score(node) = Σ(wi × depth) for strings i passing through
4. **Longest common substring**: Deepest node with flags from all strings
5. **Number of suffixes**: n (for string of length n)
6. **Number of substrings**: n(n+1)/2 (including empty) or n(n-1)/2 (non-empty)

## Summary

Master these core ideas:
1. **Substring = prefix of suffix** (enables substring problems via suffix trees)
2. **Augmentation** (counters, flags, scores) enables efficient queries
3. **Separators** allow multi-string problems in single tree
4. **Tree compression** (multiple trie nodes → one tree edge) enables O(n) substring algorithms
5. **Lexicographic navigation** enables predecessor/successor queries

Practice by:
- Drawing small examples
- Tracing augmented insertions
- Converting trie solutions to tree solutions
- Analyzing time complexity rigorously
