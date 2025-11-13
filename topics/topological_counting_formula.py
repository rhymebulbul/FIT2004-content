"""
Formula-based counting of topological orderings for series-parallel decomposition
"""

import math

def binomial_coefficient(n, k):
    """Calculate C(n, k) = n! / (k! * (n-k)!)"""
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

def count_interleavings(len_a, len_b):
    """
    Count ways to interleave two sequences of lengths len_a and len_b.
    This is the binomial coefficient C(len_a + len_b, len_a).
    """
    return binomial_coefficient(len_a + len_b, len_a)

if __name__ == "__main__":
    print("=" * 70)
    print("FORMULA-BASED TOPOLOGICAL ORDERING COUNT")
    print("=" * 70)
    print()

    print("Graph decomposition:")
    print("  Chain 1: A → B (2 nodes)")
    print("  Chain 2: C → D (2 nodes)")
    print("  Convergence: E")
    print("  Chain 3: F → G (2 nodes, from E)")
    print("  Single node: H (from E)")
    print("  Convergence: I")
    print()

    # Step 1: Count ways to interleave A→B and C→D before E
    print("Step 1: Interleaving chains before E")
    print("-" * 70)
    chain1_length = 2  # A → B
    chain2_length = 2  # C → D

    ways_to_E = count_interleavings(chain1_length, chain2_length)
    print(f"  Chain 1 (A→B): {chain1_length} nodes")
    print(f"  Chain 2 (C→D): {chain2_length} nodes")
    print(f"  Formula: C({chain1_length + chain2_length}, {chain1_length}) = {chain1_length + chain2_length}! / ({chain1_length}! × {chain2_length}!)")
    print(f"  Calculation: {math.factorial(4)} / ({math.factorial(2)} × {math.factorial(2)})")
    print(f"  Result: {ways_to_E} ways to reach E")
    print()

    # Step 2: Count ways to interleave F→G and H after E
    print("Step 2: Interleaving chains after E")
    print("-" * 70)
    chain3_length = 2  # F → G
    chain4_length = 1  # H

    ways_from_E = count_interleavings(chain3_length, chain4_length)
    print(f"  Chain 3 (F→G): {chain3_length} nodes")
    print(f"  Chain 4 (H): {chain4_length} node")
    print(f"  Formula: C({chain3_length + chain4_length}, {chain3_length}) = {chain3_length + chain4_length}! / ({chain3_length}! × {chain4_length}!)")
    print(f"  Calculation: {math.factorial(3)} / ({math.factorial(2)} × {math.factorial(1)})")
    print(f"  Result: {ways_from_E} ways from E to I")
    print()

    # Step 3: Multiply (series composition)
    print("Step 3: Total count (series composition)")
    print("-" * 70)
    total = ways_to_E * ways_from_E
    print(f"  Formula: count(before E) × count(after E)")
    print(f"  Calculation: {ways_to_E} × {ways_from_E}")
    print(f"  TOTAL: {total} distinct topological orderings")
    print()

    print("=" * 70)
    print("SUMMARY: Quick Formula")
    print("=" * 70)
    print()
    print(f"  Answer = C(4, 2) × C(3, 2)")
    print(f"         = 6 × 3")
    print(f"         = {total}")
    print()

    # Show the general formula pattern
    print("=" * 70)
    print("GENERAL PATTERN FOR SIMILAR GRAPHS")
    print("=" * 70)
    print()
    print("For a graph with structure:")
    print("  Parallel chains → Convergence → Parallel chains → Convergence")
    print()
    print("Formula:")
    print("  1. Identify independent parallel components")
    print("  2. For each parallel section with chains of lengths n₁, n₂, ..., nₖ:")
    print("     Count = (n₁ + n₂ + ... + nₖ)! / (n₁! × n₂! × ... × nₖ!)")
    print("     This is the multinomial coefficient")
    print("  3. Multiply counts from all series sections")
    print()
    print("For this specific graph:")
    print("  Section 1 (parallel A→B and C→D): C(2+2, 2) = 6")
    print("  Section 2 (parallel F→G and H): C(2+1, 2) = 3")
    print("  Total: 6 × 3 = 18")
    print()