import sys

sys.setrecursionlimit(10000)


def dynamic_edit_distance():
    first_word = "FOOD"
    second_word = "MONEY"

    dp = [
        [float("inf")] * (len(second_word) + 1)
        for _ in range(len(first_word) + 1)
    ]

    def calculate():
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if first_word[i - 1] == second_word[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]
                    )

        return dp[len(dp) - 1][len(dp[0]) - 1]

    result = calculate()
    return result


print(dynamic_edit_distance())
