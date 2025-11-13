#!/usr/bin/env python3
"""
Floyd-Warshall Calculator for Exam Practice

Quick tool to verify your Floyd-Warshall calculations during practice.
Shows step-by-step iterations to help you understand the algorithm.

Usage:
    python floyd_warshall_calculator.py

Time: Should complete in <5 seconds for typical exam graphs
"""

def floyd_warshall_step_by_step(edges, n, iterations=None):
    """
    Compute Floyd-Warshall with detailed step-by-step output.

    Args:
        edges: List of (u, v, w) tuples representing directed edges
        n: Number of vertices (1 to n)
        iterations: Number of iterations to compute (None = all)

    Returns:
        dist: Final distance matrix after specified iterations
    """
    INF = float('inf')

    # Initialize distance matrix
    dist = [[INF] * (n + 1) for _ in range(n + 1)]

    # Distance from vertex to itself is 0
    for i in range(1, n + 1):
        dist[i][i] = 0

    # Fill in direct edges
    for u, v, w in edges:
        dist[u][v] = w

    print("=" * 70)
    print("INITIAL MATRIX (Direct edges only)")
    print("=" * 70)
    print_matrix(dist, n)
    print()

    # Floyd-Warshall iterations
    max_k = iterations if iterations else n

    for k in range(1, max_k + 1):
        print(f"{'=' * 70}")
        print(f"ITERATION k={k} (Considering paths through vertex {k})")
        print(f"{'=' * 70}")

        updates = []

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == k or j == k:
                    continue  # Skip row k and column k

                # Check if path through k is shorter
                if dist[i][k] != INF and dist[k][j] != INF:
                    new_dist = dist[i][k] + dist[k][j]
                    if new_dist < dist[i][j]:
                        updates.append((i, j, dist[i][j], new_dist))
                        dist[i][j] = new_dist

        if updates:
            print(f"\nUpdates made (path through vertex {k}):")
            for i, j, old, new in updates:
                if old == INF:
                    print(f"  dist[{i}][{j}]: ∞ → {new} (via dist[{i}][{k}] + dist[{k}][{j}] = {dist[i][k]} + {dist[k][j]})")
                else:
                    print(f"  dist[{i}][{j}]: {old} → {new} (via dist[{i}][{k}] + dist[{k}][{j}] = {dist[i][k]} + {dist[k][j]})")
        else:
            print(f"\nNo updates (no improvements found through vertex {k})")

        print()
        print_matrix(dist, n)
        print()

    return dist


def print_matrix(dist, n):
    """Print distance matrix in readable format."""
    INF = float('inf')

    # Header
    print("     ", end="")
    for j in range(1, n + 1):
        print(f"{j:>6}", end="")
    print()
    print("     " + "-" * (6 * n))

    # Rows
    for i in range(1, n + 1):
        print(f"{i:>3} |", end="")
        for j in range(1, n + 1):
            if dist[i][j] == INF:
                print(f"{'∞':>6}", end="")
            else:
                print(f"{dist[i][j]:>6}", end="")
        print()


def sum_non_infinite(dist, n):
    """Calculate sum of all non-infinite values in distance matrix."""
    INF = float('inf')
    total = 0
    count = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dist[i][j] != INF:
                total += dist[i][j]
                count += 1

    return total, count


def get_specific_sum(dist, cells):
    """
    Get sum of specific cells.

    Args:
        dist: Distance matrix
        cells: List of (i, j) tuples

    Returns:
        Sum of specified cells
    """
    total = 0
    INF = float('inf')

    print("\nCalculating sum of specific cells:")
    for i, j in cells:
        val = dist[i][j]
        if val == INF:
            print(f"  dist[{i}][{j}] = ∞ (CANNOT SUM INFINITE VALUES!)")
            return None
        else:
            print(f"  dist[{i}][{j}] = {val}")
            total += val

    return total


# ============================================================================
# EXAM PRACTICE EXAMPLES
# ============================================================================

def exam_example_1():
    """
    Past Exam 1, Q20 (2 marks)

    Graph: 1→2(-2), 2→4(-3), 2→3(1), 3→5(2), 4→5(20), 1→3(1), 2→5(3)

    Question: After the outer loop finished two iterations,
    what is the sum of all values in dist that are not equal to infinity?

    Answer: 11
    """
    print("\n" + "=" * 70)
    print("EXAM EXAMPLE 1: Past Exam Q20")
    print("=" * 70)
    print("\nGraph edges:")
    print("  1 → 2 (weight -2)")
    print("  1 → 3 (weight 1)")
    print("  2 → 3 (weight 1)")
    print("  2 → 4 (weight -3)")
    print("  2 → 5 (weight 3)")
    print("  3 → 5 (weight 2)")
    print("  4 → 5 (weight 20)")
    print("\nQuestion: After 2 iterations, sum of all non-infinite values?")
    print()

    edges = [
        (1, 2, -2),
        (1, 3, 1),
        (2, 3, 1),
        (2, 4, -3),
        (2, 5, 3),
        (3, 5, 2),
        (4, 5, 20)
    ]

    n = 5
    dist = floyd_warshall_step_by_step(edges, n, iterations=2)

    total, count = sum_non_infinite(dist, n)
    print(f"\n{'=' * 70}")
    print(f"FINAL ANSWER")
    print(f"{'=' * 70}")
    print(f"Sum of {count} non-infinite values: {total}")
    print(f"Expected answer: 11")
    print()


def exam_example_2():
    """
    Past Exam 2, Q11 (3 marks)

    Question: After second iteration, what is dist[4][3]+dist[5][4]+dist[5][6]?

    Answer: 46

    Note: This needs the actual graph from the exam to verify.
    """
    print("\n" + "=" * 70)
    print("EXAM EXAMPLE 2: Past Exam Q11")
    print("=" * 70)
    print("\nThis example requires the actual graph from the exam paper.")
    print("Use the template below to fill in your own graph.")
    print()


def custom_graph():
    """
    Template for practicing with your own graphs.

    Modify the edges and questions to match your exam practice problems.
    """
    print("\n" + "=" * 70)
    print("CUSTOM GRAPH PRACTICE")
    print("=" * 70)
    print("\nModify this function with your own graph!")
    print()

    # EXAMPLE: Modify these edges for your practice problem
    edges = [
        (1, 2, 5),
        (2, 3, 3),
        (1, 3, 10),
    ]

    n = 3  # Number of vertices
    iterations = 2  # How many iterations to compute

    dist = floyd_warshall_step_by_step(edges, n, iterations=iterations)

    # Calculate total sum
    total, count = sum_non_infinite(dist, n)
    print(f"\n{'=' * 70}")
    print(f"RESULTS")
    print(f"{'=' * 70}")
    print(f"Sum of all non-infinite values: {total} ({count} values)")

    # Calculate specific cells (modify as needed)
    cells = [(1, 3), (2, 3)]
    specific_sum = get_specific_sum(dist, cells)
    if specific_sum is not None:
        print(f"\nSum of dist[1][3] + dist[2][3] = {specific_sum}")
    print()


# ============================================================================
# QUICK CALCULATOR (For fast exam verification)
# ============================================================================

def quick_calculate(edges, n, iterations, cells=None):
    """
    Quick calculation without detailed output.

    Args:
        edges: List of (u, v, w) tuples
        n: Number of vertices
        iterations: Number of iterations
        cells: Optional list of (i,j) cells to sum

    Returns:
        dist: Final distance matrix
    """
    INF = float('inf')
    dist = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dist[i][i] = 0

    for u, v, w in edges:
        dist[u][v] = w

    for k in range(1, iterations + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][k] != INF and dist[k][j] != INF:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # Print result
    print_matrix(dist, n)

    if cells:
        total = sum(dist[i][j] for i, j in cells)
        print(f"\nSum of specified cells: {total}")
    else:
        total = sum(dist[i][j] for i in range(1, n+1) for j in range(1, n+1) if dist[i][j] != INF)
        print(f"\nSum of all non-infinite values: {total}")

    return dist


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    import sys

    print("Floyd-Warshall Exam Calculator")
    print("=" * 70)
    print()
    print("Available examples:")
    print("  1. Exam Example 1 (Past Exam Q20)")
    print("  2. Exam Example 2 (Past Exam Q11)")
    print("  3. Custom Graph (modify code)")
    print()

    if len(sys.argv) > 1:
        choice = sys.argv[1]
    else:
        choice = input("Select example (1/2/3) or press Enter for Example 1: ").strip()
        if not choice:
            choice = "1"

    if choice == "1":
        exam_example_1()
    elif choice == "2":
        exam_example_2()
    elif choice == "3":
        custom_graph()
    else:
        print("Invalid choice. Running Example 1.")
        exam_example_1()

    print("\n" + "=" * 70)
    print("QUICK TIPS FOR EXAM:")
    print("=" * 70)
    print("1. Draw matrix template first (15 sec)")
    print("2. Fill initial edges carefully (30 sec)")
    print("3. For each k, look at ROW k and COLUMN k")
    print("4. Only update if dist[i][k] + dist[k][j] < dist[i][j]")
    print("5. Double-check arithmetic with negative numbers!")
    print("=" * 70)
    print()