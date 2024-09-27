def count_tiling_ways(L):
    if L % 2 != 0:
        return 0  # Odd width cannot be fully tiled with 2x1 tiles

    # Initialize the dp array
    dp = [0] * (L + 1)
    dp[0] = 1  # Base case: One way to tile a 3x0 grid
    if L >= 2:
        dp[2] = 3  # Base case: Three ways to tile a 3x2 grid

    for i in range(4, L + 1, 2):
        dp[i] = 4 * dp[i - 2] - dp[i - 4]

    return dp[L]


# Example usage:
L = int(input())
print(count_tiling_ways(L))
