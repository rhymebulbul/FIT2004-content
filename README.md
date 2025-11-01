# FIT2004 Algorithms & Data Structures - Study Repository

A comprehensive collection of algorithm implementations, course notes, and exam preparation materials for FIT2004 (Algorithms and Data Structures).

## Repository Purpose

This repository is designed for:
- Exam preparation with organized study materials
- Understanding core algorithms through clean Python implementations
- Quick reference for algorithm complexity and implementation patterns
- Practice with past exam questions and solutions

**Current Focus**: Preparing for deferred mid-semester test. Mid-semester content is complete; final exam content is being populated.

## Repository Structure

```
implementations-algorithms/    # Python implementations with complexity analysis
├── w1/                       # Divide & Conquer (merge sort, binary search, inversions)
├── w2/                       # Sorting (selection, counting, radix)
├── w5/                       # Graphs (Dijkstra, Prim, Kruskal, Union-Find)
└── w6/                       # Dynamic Programming (coin change)

course_notes/                 # Structured notes (chap_one.json - chap_eleven.json)
lecture/                      # Lecture materials (l1.json - l9.json)
weekly_quiz/                  # Quiz questions (q1.json - q6.json)

exams/                        # Exam questions and solutions
past_mid/                     # Past mid-semester exam materials
applied_solutions/            # Applied problem solutions
prep_solutions/               # Preparation solutions (prep.json)

examinable_content_mid.txt    # Mid-semester topics (COMPLETE)
examinable_content_exam.txt   # Final exam topics (in progress)
```

## Quick Start

### Running Algorithm Implementations

All Python files are self-contained and executable:

```bash
# Graph algorithms
python implementations-algorithms/w5/dijkstra.py
python implementations-algorithms/w5/prim.py
python implementations-algorithms/w5/kruskal.py

# Sorting algorithms
python implementations-algorithms/w2/countingSort.py
python implementations-algorithms/w2/radixSort.py
python implementations-algorithms/w1/mergeSort.py
```

Each implementation includes:
- Detailed inline complexity analysis
- Working test cases in `if __name__ == "__main__"` block
- Example data structures for demonstration

## Study Guide

### For Mid-Semester Test

**Start here**: Read `examinable_content_mid.txt` for the authoritative topic list.

**Topics covered**:
1. Analysis of Algorithms (verification, complexity, asymptotic notation)
2. Divide and Conquer
3. Fast Sorting Algorithms
4. Order Statistics and Selection
5. Graph Basics (traversal, connectivity, shortest paths, topological sorting)
6. Greedy Algorithms (Dijkstra, Prim, Kruskal)

**Study materials**:
- `past_mid/` - Past mid-semester exams (most relevant)
- `exams/` - Cross-reference with examinable_content_mid.txt to identify relevant questions
- `implementations-algorithms/w1/, w2/, w5/` - Core implementations
- `course_notes/` and `lecture/` - Theory and concepts

### For Final Exam

Check `examinable_content_exam.txt` for comprehensive topic list (includes mid-semester + additional topics).

Additional topics:
- Dynamic Programming (graphs, knapsack, edit distance)
- Network Flow (Ford-Fulkerson, max-flow min-cut)
- Advanced Trees (AVL, Red-Black, 2-3 trees)
- Tries and Suffix Trees

## Studying with Claude Code

This repository is optimized for use with [Claude Code](https://claude.ai/code), an AI-powered coding assistant that can help you study more effectively. The `CLAUDE.md` file provides context about the repository structure, ensuring Claude understands your exam preparation needs.

### Why Claude Code vs ChatGPT/Generic AI?

**The key difference**: Claude Code has **direct access to ALL your study materials** in this repository. This means:

#### Your Specific Course Context
- **ChatGPT**: Gives generic algorithm explanations based on general knowledge
- **Claude Code**: Explains algorithms using YOUR course's notation, YOUR lecture notes, and YOUR professor's teaching style from `lecture/` and `course_notes/`

#### Personalized to Your Exam
- **ChatGPT**: Doesn't know what's on your exam
- **Claude Code**: Reads `examinable_content_mid.txt` and focuses ONLY on topics you'll be tested on, avoiding wasting time on irrelevant material

#### Past Exam Pattern Recognition
- **ChatGPT**: Creates generic practice problems
- **Claude Code**: Analyzes `past_mid/` and `exams/` to generate practice problems that match your actual exam format, difficulty, and question style

#### Cross-Referencing Your Materials
- **ChatGPT**: Can't connect different resources
- **Claude Code**: "I see this concept was covered in lecture 3 (l3.json), appears in quiz 2 (q2.json), and there's a similar problem in applied_solutions/3.txt - let me show you all three perspectives"

#### Your Implementation Style
- **ChatGPT**: Shows algorithm implementations that might differ from what you learned
- **Claude Code**: Uses YOUR implementations from `implementations-algorithms/` that match your course's conventions (like Union-Find with negative parent encoding)

#### Solution Verification Against Course Solutions
- **ChatGPT**: Can't verify if your approach matches course expectations
- **Claude Code**: Compares your solutions against `applied_solutions/`, `prep_solutions/`, and past exam answers to ensure alignment with course grading criteria

### Real Examples of Claude Code's Advantage

**Example 1: Contextual Explanations**
```
ChatGPT: "Here's how Dijkstra's algorithm works..." [generic explanation]

Claude Code: "Looking at your dijkstra.py implementation and lecture 5 notes (l5.json),
your course emphasizes the greedy choice property. Your implementation uses the
exact priority queue pattern from course_notes/chap_five.json. Let me explain
using the same graph structure from your test case..."
```

**Example 2: Exam-Focused Practice**
```
ChatGPT: "Here's a graph algorithm practice problem..." [random difficulty/style]

Claude Code: "Based on past_mid/ exams, questions typically ask you to:
1) Trace the algorithm step-by-step (like Q2 from 2022)
2) Analyze complexity with justification (like Q4 from 2023)
Here's a practice problem in that exact format, using similar graph sizes..."
```

**Example 3: Connecting Learning Materials**
```
ChatGPT: "Counting sort works by..." [isolated explanation]

Claude Code: "Your lecture notes (l3.json) introduce counting sort, which is then
used in radix sort (w2/radixSort.py). Quiz 2 (q2.json) tested stability, and
applied_solutions/2.txt shows how to apply it. Let me show how all these connect..."
```

**Example 4: Code Tracing with Your Style**
```
ChatGPT: "Here's how Union-Find works..." [generic implementation]

Claude Code: "Your unionFind.py uses negative values to encode tree sizes - this
is the exact optimization mentioned in chap_six.json. Let me trace through your
findParent() function with path compression using your test case..."
```

### How Having All Materials Helps You Study Smarter

#### 1. Comprehensive Topic Coverage Verification
Claude can scan all materials to ensure you haven't missed anything:
- "Check if I've covered all topics from examinable_content_mid.txt across my course_notes/ and lecture/ materials"
- "Which topics appear in past_mid/ but I haven't seen in weekly_quiz/?"

#### 2. Multi-Source Learning
Learn concepts from multiple angles:
- "Explain Prim's algorithm by combining the theory from course_notes/, the lecture explanation from lecture/, and the implementation from w5/prim.py"

#### 3. Gap Analysis
Identify weaknesses in your understanding:
- "Compare my solutions in prep_solutions/ to the official answers in applied_solutions/ - where are my conceptual gaps?"
- "Which quiz questions in weekly_quiz/ did I likely struggle with based on topics I haven't practiced?"

#### 4. Custom Study Paths
Create optimal study sequences:
- "Build a study progression from easiest to hardest sorting algorithms using examples from weekly_quiz/ and exams/"
- "Order graph algorithm review based on dependency relationships shown in lecture/ materials"

#### 5. Exam Simulation
Practice with real exam conditions:
- "Give me a mock mid-semester exam using unused questions from past_mid/ and similar problems from exams/ that match examinable_content_mid.txt"

#### 6. Quick Reference with Context
Fast lookups that understand your course:
- "What's the complexity of radix sort according to my course notes?" (not generic definitions)
- "How does my course define 'stable sorting' in lecture materials?"

#### 7. Solution Pattern Recognition
Learn your course's expected solution format:
- "Show me how to write complexity analysis based on the style used in applied_solutions/"
- "What proof techniques appear most in past_mid/ answers?"

### How Claude Code Can Help

#### 1. Understanding Algorithm Implementations

Ask Claude to explain algorithms in detail:
- "Explain how Dijkstra's algorithm works in implementations-algorithms/w5/dijkstra.py"
- "Walk me through the complexity analysis of merge sort step by step"
- "Why does Union-Find use negative values for parent encoding?"

#### 2. Interactive Learning & Practice

Generate custom examples and variations:
- "Create a new graph example for me to trace through Prim's algorithm manually"
- "Generate practice problems for counting sort with different input ranges"
- "Show me edge cases where Dijkstra's algorithm might be challenging"

#### 3. Exam Preparation

Work through past exams with guided support:
- "Help me solve question 3 from past_mid/ - guide me through the approach without giving away the answer"
- "Check my solution to this problem and identify any mistakes in my complexity analysis"
- "What topics from examinable_content_mid.txt should I focus on based on past exam patterns?"

#### 4. Concept Clarification

Deep dive into theory using your course materials:
- "Explain the difference between Prim and Kruskal using the implementations in w5/"
- "Compare stable vs unstable sorting using examples from w2/"
- "What's the intuition behind the Union-Find optimization with union-by-size?"

#### 5. Study Plan Creation

Get personalized study strategies:
- "Create a 5-day study plan for the mid-semester test based on examinable_content_mid.txt"
- "What order should I review topics for maximum retention?"
- "Suggest practice problems for each topic in the mid-semester content"

#### 6. Code Tracing & Debugging Understanding

Step through algorithms interactively:
- "Trace through dijkstra.py line by line with the test graph"
- "Show me how the priority queue changes at each step of Prim's algorithm"
- "Visualize what the parent array looks like after each union operation"

#### 7. Cross-Reference Materials

Connect different study resources:
- "Find where BFS is covered in course_notes/ and lecture/ materials"
- "Which quiz questions in weekly_quiz/ relate to greedy algorithms?"
- "Compare how Dijkstra is explained in course notes vs the implementation"

### Example Study Sessions

**Concept Review Session**:
```
You: "I'm reviewing greedy algorithms today. Help me understand when to use
     Dijkstra vs Prim vs Kruskal"

Claude: [Compares the three algorithms using your implementations, explains
        use cases, and references relevant sections in course notes]
```

**Practice Problem Session**:
```
You: "Give me a challenging graph problem to practice shortest paths"

Claude: [Generates a custom problem, then helps you work through it step-by-step,
        pointing to relevant code in dijkstra.py when needed]
```

**Past Exam Walkthrough**:
```
You: "Let's go through the past_mid/ exam questions. For each question, tell me
     which topic it covers and guide me to solve it"

Claude: [Reviews questions, categorizes by topic from examinable_content_mid.txt,
        provides hints without spoilers, explains solutions after your attempts]
```

**Implementation Understanding**:
```
You: "I don't understand why Union-Find is O(α(n)). Explain using the code
     in unionFind.py"

Claude: [Walks through the implementation, explains path compression and
        union-by-size optimizations with concrete examples]
```

### Tips for Effective Study with Claude Code

1. **Be Specific**: Reference specific files, topics, or questions for targeted help
2. **Ask for Explanations**: Don't just ask for answers - ask "why" and "how"
3. **Request Variations**: Ask for different examples to test your understanding
4. **Use Course Materials**: Claude has access to all your notes, lectures, and solutions
5. **Practice Active Learning**: Ask Claude to quiz you or create practice problems
6. **Verify Understanding**: Ask Claude to check your explanations and approaches
7. **Connect Concepts**: Ask how different algorithms relate to each other

### Context Awareness

Claude Code automatically understands:
- You're preparing for a mid-semester test (current focus)
- Which topics are examinable (from examinable_content_mid.txt)
- The repository structure and where to find specific materials
- Code conventions used in your implementations
- The relationship between past exams, course notes, and implementations

This means you can ask natural questions like "Help me with graphs" and Claude will know to focus on BFS, DFS, Dijkstra, and MST algorithms from your mid-semester content.

---

## Advanced Study Strategies You Haven't Thought Of

Here are innovative ways to leverage Claude Code with your repository for maximum exam preparation effectiveness:

### 1. Automated Weak Spot Detection

**Strategy**: Have Claude analyze your performance patterns across all materials to identify knowledge gaps.

**How to use it**:
```
"Analyze all my prep_solutions/ (prep.json through prep12.json) and compare them
to applied_solutions/. What patterns of mistakes do I make? Which topics do I
consistently struggle with?"
```

**Why it's powerful**: Claude can cross-reference 12+ prep solutions against official answers, identify recurring errors in your reasoning, and pinpoint specific conceptual weaknesses you might not notice yourself.

### 2. Progressive Difficulty Ladder

**Strategy**: Build a custom learning sequence from easiest to hardest within each topic.

**How to use it**:
```
"Create a progressive difficulty ladder for graph algorithms. Start with the
easiest problems from weekly_quiz/, then move through applied_solutions/,
past_mid/, and finally exams/. Order them by complexity."
```

**Why it's powerful**: You get a confidence-building study path rather than jumping randomly between difficulty levels.

### 3. Concept Dependency Mapping

**Strategy**: Understand prerequisite relationships between topics.

**How to use it**:
```
"Map out the dependency tree for all mid-semester topics. Which concepts must I
understand before tackling others? Show me using course_notes/ and lecture/ to
identify prerequisites."
```

**Why it's powerful**: Study in optimal order - master foundations before building on them. Prevents confusion from learning things out of sequence.

### 4. Exam Question Prediction & Pattern Analysis

**Strategy**: Analyze past exams to predict likely question types.

**How to use it**:
```
"Analyze all questions in past_mid/ and exams/ that cover topics from
examinable_content_mid.txt. What are the most common question formats? What
topics appear most frequently? Generate similar practice questions for
under-represented topics."
```

**Why it's powerful**: Focus study time on high-probability question types and ensure coverage of commonly tested concepts.

### 5. Spaced Repetition Study Plan

**Strategy**: Create a review schedule based on forgetting curves.

**How to use it**:
```
"Create a 2-week spaced repetition schedule for all mid-semester topics.
Schedule review sessions that revisit topics at increasing intervals.
Include specific materials from course_notes/, lecture/, and practice
problems from weekly_quiz/."
```

**Why it's powerful**: Optimize long-term retention using scientifically-proven spacing effects.

### 6. Multi-Modal Learning Synthesis

**Strategy**: Learn each concept through theory, implementation, and application simultaneously.

**How to use it**:
```
"For Union-Find: explain the theory from course_notes/, walk through the
implementation in w5/unionFind.py, then show me how it's applied in practice
problems from applied_solutions/ and past_mid/. Connect all three perspectives."
```

**Why it's powerful**: Deep understanding through multiple angles - theory reinforces code, code clarifies theory, applications show real usage.

### 7. Common Mistakes Database

**Strategy**: Build a personalized error catalog from all solution files.

**How to use it**:
```
"Go through all solutions in applied_solutions/ and prep_solutions/. Create a
'common mistakes' guide showing typical errors students make in complexity
analysis, algorithm correctness proofs, and implementation choices."
```

**Why it's powerful**: Learn from others' mistakes preventatively rather than making them yourself during the exam.

### 8. Time-Boxed Practice Simulations

**Strategy**: Simulate exam conditions with mixed topics.

**How to use it**:
```
"Create a 30-minute mini-exam with 3 questions covering different topics from
examinable_content_mid.txt. Use past_mid/ style. After I attempt them, compare
my answers to similar solutions in applied_solutions/ and grade me."
```

**Why it's powerful**: Practice time management, context switching between topics, and exam pressure.

### 9. Proof Technique Pattern Matching

**Strategy**: Learn standard proof structures from solutions.

**How to use it**:
```
"Extract all correctness proofs from applied_solutions/ and past_mid/. What
proof techniques are most common (induction, contradiction, loop invariants)?
Show me the template structure for each type."
```

**Why it's powerful**: Recognize which proof technique to use and follow proven structural patterns.

### 10. Complexity Analysis Drill Generator

**Strategy**: Practice analyzing complexity until it's automatic.

**How to use it**:
```
"Generate 10 code snippets of varying complexity (loops, recursion, nested
structures). I'll analyze them, then you check my work against the style used
in course_notes/ and applied_solutions/. Focus on topics from
examinable_content_mid.txt section 1.2."
```

**Why it's powerful**: Build muscle memory for the most fundamental exam skill.

### 11. Lecture-to-Implementation Tracing

**Strategy**: Bridge the gap between abstract lecture concepts and concrete code.

**How to use it**:
```
"Take the Dijkstra explanation from lecture/l5.json and course_notes/. Show me
line-by-line how each theoretical concept maps to specific lines in
implementations-algorithms/w5/dijkstra.py."
```

**Why it's powerful**: Understand why code is written a certain way, making it easier to write algorithms from scratch.

### 12. Edge Case Collection

**Strategy**: Build awareness of tricky inputs and boundary conditions.

**How to use it**:
```
"Scan through all problems in past_mid/, exams/, and applied_solutions/. What
edge cases commonly appear? (empty graphs, single nodes, negative weights where
invalid, etc.) Create a checklist for each algorithm type."
```

**Why it's powerful**: Avoid losing easy marks by always checking standard edge cases.

### 13. Topic Interleaving Practice

**Strategy**: Mix topics to improve discrimination and long-term retention.

**How to use it**:
```
"Create a practice session that alternates between sorting (w2/), divide &
conquer (w1/), and graphs (w5/). Use problems from weekly_quiz/ and past_mid/
in shuffled order. This builds my ability to identify which technique to use."
```

**Why it's powerful**: Research shows interleaved practice improves long-term retention better than blocking.

### 14. Verbal Explanation Practice

**Strategy**: Practice explaining concepts as if teaching someone else.

**How to use it**:
```
"I'll explain Kruskal's algorithm to you in my own words. You listen for
misconceptions, unclear explanations, or missing details. Then compare my
explanation to lecture/ and course_notes/ to see what I missed."
```

**Why it's powerful**: Teaching is the best way to identify gaps in your own understanding.

### 15. Algorithmic Intuition Building

**Strategy**: Develop instinct for when to use which algorithm.

**How to use it**:
```
"Give me 10 problem descriptions (don't tell me the algorithm). I'll identify
which algorithm to use and why. Then you reveal the answer from past_mid/ or
applied_solutions/ and we discuss my reasoning."
```

**Why it's powerful**: Exams test algorithm selection skill, not just implementation knowledge.

### 16. Study Guide Auto-Generation

**Strategy**: Let Claude create personalized cheat sheets.

**How to use it**:
```
"Create a 1-page quick reference for graph algorithms using the exact
complexities, pseudocode style, and notation from my course_notes/ and lecture/.
Include only what's in examinable_content_mid.txt sections 5 and 6."
```

**Why it's powerful**: Condensed, course-specific reference in your professor's notation.

### 17. Mistake-Driven Learning Sessions

**Strategy**: Focus study time on your actual weak areas.

**How to use it**:
```
"I got question 3 from past_mid/2023 wrong. Analyze why, find similar problems
in weekly_quiz/ and exams/, then drill me on this specific concept until I
master it."
```

**Why it's powerful**: Targeted remediation rather than reviewing things you already know.

### 18. Cross-Topic Connection Mapping

**Strategy**: Understand how different topics relate to each other.

**How to use it**:
```
"Show me how Union-Find (from section 5.6) is used in Kruskal (section 6.2).
What other topics from examinable_content_mid.txt build on each other? Create
a concept map."
```

**Why it's powerful**: See the bigger picture and understand why topics are taught in a certain order.

### 19. Pre-Exam Confidence Builder

**Strategy**: The day before the exam, do a focused review of your strongest topics.

**How to use it**:
```
"Based on my prep_solutions/ performance, what are my 3 strongest topics?
Create a quick 30-minute review of just those topics using course_notes/ and
implementations-algorithms/ to boost my confidence before the exam."
```

**Why it's powerful**: Enter the exam with momentum from reviewing things you know well.

### 20. Live Debugging Practice

**Strategy**: Find and fix intentional bugs in algorithm implementations.

**How to use it**:
```
"Introduce 3 subtle bugs into implementations-algorithms/w5/dijkstra.py. I'll
find and fix them. This helps me understand the algorithm deeply and practice
debugging under pressure."
```

**Why it's powerful**: Debugging requires deeper understanding than just reading code.

### Bonus: The "All Materials" Meta-Analysis

**The Ultimate Strategy**: Let Claude analyze your entire repository structure to create a personalized study plan.

```
"Analyze EVERYTHING in this repository - all 12 prep_solutions/, all
applied_solutions/, all lecture/ materials, course_notes/, past_mid/, weekly_quiz/,
and exams/. Create a comprehensive 7-day study plan that:

1. Identifies which topics I've practiced least based on prep_solutions/
2. Schedules practice sessions using problems I haven't seen yet
3. Alternates between theory (course_notes/lecture/) and practice
4. Includes daily mock quizzes using unused past_mid/ questions
5. Builds from my current knowledge level to exam readiness
6. Focuses ONLY on examinable_content_mid.txt topics

Track my progress and adjust the plan as I complete each section."
```

**Why it's the ultimate strategy**: Claude can process and synthesize ALL your materials simultaneously to create an optimized, personalized study plan that would take you hours to create manually.

---

## Key Algorithm Implementations

### Graph Algorithms (`w5/`)

| Algorithm | File | Complexity | Use Case |
|-----------|------|------------|----------|
| Dijkstra | `dijkstra.py` | O((V+E) log V) | Single-source shortest paths (non-negative weights) |
| Prim | `prim.py` | O(E log V) | Minimum Spanning Tree (greedy vertex selection) |
| Kruskal | `kruskal.py` | O(E log E) | MST (edge sorting + Union-Find) |
| Union-Find | `unionFind.py` | O(α(n)) amortized | Disjoint set operations |

### Sorting Algorithms (`w1/`, `w2/`)

| Algorithm | File | Complexity | Notes |
|-----------|------|------------|-------|
| Merge Sort | `mergeSort.py` | O(n log n) | Divide-and-conquer, stable |
| Counting Sort | `countingSort.py` | O(n + k) | Integer sorting, stable |
| Radix Sort | `radixSort.py` | O(d(n + k)) | Multi-pass using counting sort |
| Selection Sort | `selectionSort.py` | O(n²) | Basic comparison sort |

### Other Algorithms

- **Binary Search** (`binarySearch.py`): O(log n) search in sorted array
- **Count Inversions** (`countInversions.py`): Modified merge sort for counting inversions

## Code Conventions

### Data Structures
- **Graphs**: Adjacency list as `{node: [(neighbor, weight), ...]}`
- **Union-Find**: Negative parent values indicate root with size = |parent[i]|
- **Priority Queues**: Python's `heapq` for min-heap operations

### Complexity Comments
All implementations document:
- Per-operation time complexity
- Overall algorithm complexity
- Space complexity where relevant

### Testing
- No external test framework
- Tests included in each file's `if __name__ == "__main__"` block
- Simple data structures with stdout output

## Requirements

- Python 3.x
- No external dependencies (uses only standard library: `heapq`, etc.)

## Topics Coverage

This repository covers major algorithm categories:

1. **Analysis & Verification**: Correctness proofs, complexity analysis, Big-O notation
2. **Divide & Conquer**: Merge sort, Karatsuba multiplication
3. **Sorting**: Comparison-based (merge, quick, heap) and non-comparison (counting, radix)
4. **Graph Traversal**: DFS, BFS, topological sorting, connected components
5. **Shortest Paths**: BFS (unweighted), Dijkstra, Bellman-Ford, Floyd-Warshall
6. **Greedy Algorithms**: Activity selection, Dijkstra, MST algorithms
7. **Dynamic Programming**: Knapsack variants, edit distance, matrix chain multiplication
8. **Network Flow**: Ford-Fulkerson, max-flow min-cut theorem, bipartite matching
9. **Trees**: BST, AVL, Red-Black, 2-3 trees
10. **String Algorithms**: Prefix tries, suffix trees, pattern matching

## Contributing

This is a personal study repository. Feel free to fork and adapt for your own learning.

## License

Educational use only.