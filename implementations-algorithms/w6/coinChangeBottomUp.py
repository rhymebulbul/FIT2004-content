"""
Ignore. out of syllabus for mid semester test
"""
# # Tabulation
# def coin_change_bottom_up(V, coins):
#     # Initialize DP arrays
#     min_coins = [float('inf')] * (V + 1)  # min coins to make value v
#     coin_count = [[0] * len(coins) for _ in range(V + 1)]  # coins used for value v
#
#     # Base case
#     min_coins[0] = 0
#
#     for v in range(1, V + 1):
#         for i, c in enumerate(coins):
#             if c <= v:
#                 if min_coins[v - c] + 1 < min_coins[v]:
#                     min_coins[v] = min_coins[v - c] + 1
#                     # Copy previous coin counts
#                     coin_count[v] = coin_count[v - c].copy()
#                     coin_count[v][i] += 1  # add current coin
#
#     return min_coins[V], coin_count[V]
#
# # Example usage:
# V = 7
# coins = [1, 3, 8]
# total_coins, coins_used = coin_change_bottom_up(V, coins)
# print("Bottom-Up:")
# print("Total coins:", total_coins)
# print("Coins used:", coins_used)
