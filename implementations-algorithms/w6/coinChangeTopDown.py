"""
Ignore. out of syllabus for mid semester test
"""

# # Memoization
# def coin_change_top_down(V, coins):
#     memo = [None] * (V + 1)  # stores min coins for value v
#     coin_count_memo = [None] * (V + 1)  # stores coins used for value v
#
#     def helper(v):
#         if v == 0:
#             return 0, [0] * len(coins)
#         if memo[v] is not None:
#             return memo[v], coin_count_memo[v]
#
#         best = float('inf')
#         best_count = None
#         for i, c in enumerate(coins):
#             if c <= v:
#                 sub_coins, sub_count = helper(v - c)
#                 if sub_coins + 1 < best:
#                     best = sub_coins + 1
#                     best_count = sub_count.copy()
#                     best_count[i] += 1
#
#         memo[v] = best
#         coin_count_memo[v] = best_count
#         return best, best_count
#
#     return helper(V)
#
# # Example usage:
# V = 7
# coins = [1, 3, 8]
# total_coins, coins_used = coin_change_top_down(V, coins)
# print("Top-Down:")
# print("Total coins:", total_coins)
# print("Coins used:", coins_used)
