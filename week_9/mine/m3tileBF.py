import sys

sys.setrecursionlimit(10001)

L = int(input())

def nWays(L):
    if L % 2 != 0:
        return 0

    if L == 0:
        return 1
    
    if L == 2:
        return 3
    
    return 4 * nWays(L - 2) - nWays(L - 4)


print(nWays(L))
