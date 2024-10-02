import sys

sys.setrecursionlimit(10001)

FLAT = 0
UPPER2 = 1
LOWER2 = 2

L = int(input())
dp = [[-1] * 3 for d in range(L + 1)]


# This is dynamic programming version
def nWays(d, s):
    if dp[d][s] == -1:
        if d == L:
            if s == FLAT:
                dp[d][s] = 1
            else:
                dp[d][s] = 0
        else:
            counter = 0
            if s == FLAT:
                counter += nWays(d + 1, UPPER2)
                counter += nWays(d + 1, LOWER2)  # Actually, this is symmetric to UPPER2
                if d < L - 1:
                    counter += nWays(d + 2, FLAT)
            else:  # s is either UPPER2 or LOWER2
                counter += nWays(d + 1, FLAT)
                if d < L - 1:
                    counter += nWays(d + 2, s)
            dp[d][s] = counter
    return dp[d][s]


for d in range(L, -1, -1):
    for s in [FLAT, UPPER2, LOWER2]:
        dp[d][s] = nWays(d, s)

# print(nWays(0, FLAT))
print(dp[0][FLAT])
