def min_coins(amount, coins):
    dp = [float('inf')] * (amount + 1)
    parent = [-1] * (amount + 1)   # parent[i] = last coin used to reach amount i
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                parent[i] = coin   # ← remember which coin got us here

    if dp[amount] == float('inf'):
        return -1, []

    # Backtrack to reconstruct the combination:
    combination = []
    i = amount
    while i > 0:
        combination.append(parent[i])
        i -= parent[i]

    return dp[amount], combination

coins = [1, 3, 4]
amount = 126
count, combo = min_coins(amount, coins)
print(f"Minimum coins: {count}")
print(f"Combination: {combo}")   