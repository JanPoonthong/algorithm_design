def min_coin():
    coins = [1, 3, 4, 5]
    amount_of_change = 7

    dp = [[float("inf")] * (amount_of_change + 1) for _ in range(len(coins))]

    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if i == 0 or j == 0:
                dp[i][j] = 0

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            remain = j - coins[i - 1]
            if coins[i - 1] <= j:
                dp[i][j] = min(dp[i][j], 1 + dp[i][remain])
            if coins[i - 1] > j:
                dp[i][j] = dp[i - 1][j]

    return dp[len(dp) - 1][len(dp[0]) - 1]


print(min_coin())
