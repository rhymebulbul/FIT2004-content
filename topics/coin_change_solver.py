"""
Coin Change Problem Solver
Given: c = [2, 4, 8, 5], v = 8
Find: MinCoins[0], MinCoins[3], MinCoins[4], MinCoins[6], MinCoins[7]

Recurrence relation:
MinCoins[v] = min(MinCoins[v - c] + 1) for all coins c where c <= v
MinCoins[0] = 0 (base case)
"""

def coin_change_bottom_up(V, coins):
    """
    Bottom-up DP solution for coin change problem.
    Returns the MinCoins array.

    Time: O(V * len(coins))
    Space: O(V)
    """
    # Initialize DP array
    min_coins = [float('inf')] * (V + 1)

    # Base case: 0 coins needed to make value 0
    min_coins[0] = 0

    # Fill the table for each value from 1 to V
    for v in range(1, V + 1):
        # Try each coin
        for c in coins:
            if c <= v:
                # Can we improve the solution using this coin?
                if min_coins[v - c] != float('inf'):
                    min_coins[v] = min(min_coins[v], min_coins[v - c] + 1)

    return min_coins


def solve_with_trace(V, coins):
    """Solve and show step-by-step trace"""
    min_coins = [float('inf')] * (V + 1)
    min_coins[0] = 0

    print(f"Coins available: {coins}")
    print(f"Target value: {V}")
    print("\nStep-by-step computation:\n")

    for v in range(1, V + 1):
        print(f"Computing MinCoins[{v}]:")
        candidates = []

        for c in coins:
            if c <= v:
                prev_value = min_coins[v - c]
                if prev_value != float('inf'):
                    new_value = prev_value + 1
                    candidates.append(f"  Using coin {c}: MinCoins[{v}-{c}] + 1 = MinCoins[{v-c}] + 1 = {prev_value} + 1 = {new_value}")
                else:
                    candidates.append(f"  Using coin {c}: MinCoins[{v-c}] = inf (not possible)")

        if candidates:
            for cand in candidates:
                print(cand)

            # Compute minimum only from valid options
            valid_options = [min_coins[v - c] + 1 for c in coins if c <= v and min_coins[v - c] != float('inf')]
            if valid_options:
                min_coins[v] = min(valid_options)
                print(f"  → MinCoins[{v}] = {min_coins[v]}")
            else:
                print(f"  → MinCoins[{v}] = inf (all options impossible)")
        else:
            print(f"  No coins can be used (all too large)")
            print(f"  → MinCoins[{v}] = inf (impossible)")

        print()

    return min_coins


# Given values
c = [2, 4, 8, 5]
v = 8

print("="*60)
print("COIN CHANGE PROBLEM - DETAILED TRACE")
print("="*60)
print()

# Solve with detailed trace
min_coins = solve_with_trace(v, c)

print("="*60)
print("FINAL MinCoins ARRAY")
print("="*60)
for i in range(len(min_coins)):
    value = min_coins[i] if min_coins[i] != float('inf') else "∞"
    print(f"MinCoins[{i}] = {value}")

print("\n" + "="*60)
print("ANSWERS TO THE QUESTIONS")
print("="*60)
print(f"MinCoins[0] = {min_coins[0]}")
print(f"MinCoins[3] = {min_coins[3] if min_coins[3] != float('inf') else '∞ (impossible)'}")
print(f"MinCoins[4] = {min_coins[4]}")
print(f"MinCoins[6] = {min_coins[6]}")
print(f"MinCoins[7] = {min_coins[7] if min_coins[7] != float('inf') else '∞ (impossible)'}")
