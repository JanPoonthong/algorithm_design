import sys

sys.setrecursionlimit(100000)

p = list(map(int, input().split()))
l = len(p)
p = [0] + p


def max_rev(l):
    if l == 0:
        return 0
    else:
        mxp = 0
        for c in range(1, l + 1):
            mxp = max(mxp, p[c] + max_rev(l - c))
    return mxp


print(max_rev(l))
