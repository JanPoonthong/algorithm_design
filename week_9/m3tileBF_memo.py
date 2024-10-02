import sys

sys.setrecursionlimit(10001)

FLAT = 0
UPPER2 = 1
LOWER2 = 2

L = int(input())
# dp = [[-1]*3 for d in range(L+1)]
memo = {}


# This is memorized version
def nWays(d, s):
    if (d, s) in memo:
        return memo[(d, s)]

    if d == L:
        if s == FLAT:
            memo[(d, s)] = 1
        else:
            memo[(d, s)] = 0
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
        memo[(d, s)] = counter
    return memo[(d, s)]


print(nWays(0, FLAT))
