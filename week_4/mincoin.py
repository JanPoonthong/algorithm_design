import sys

sys.setrecursionlimit(100000)

n = list(map(int, input().split()))
total = int(input())
n = sorted(n, reverse=True)


def mincoin(v):
    if v in n:
        return 1
    else:
        s = 0
        min_coin = v
        for i in n:
            if i <= v:
                s += 1
                min_coin = min(min_coin, mincoin(v - i) + 1)
    return min_coin


print(mincoin(total))
