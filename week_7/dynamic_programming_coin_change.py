import sys

sys.setrecursionlimit(10000)


def min_coin():
    coin_denominator = list(map(int, input().split()))
    amount_of_change = int(input())
    dp = [[float("inf")] * (amount_of_change + 1) for _ in range(len(coin_denominator))]

    def calculate():
        for i in range(len(coin_denominator)):
            dp[i][0] = 0  # 0 coins are needed to make 0 amount
            for j in range(1, amount_of_change + 1):
                if coin_denominator[i] <= j:
                    dp[i][j] = min(dp[i][j], 1 + dp[i][j - coin_denominator[i]])
                if i > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j])

        return dp[len(coin_denominator) - 1][amount_of_change]

    return calculate()


print(min_coin())
