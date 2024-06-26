import sys

sys.setrecursionlimit(100000)

n = list(map(int, input().split()))
total = int(input())
n.sort()


def mincoin(coins, change):
    min_coin = change
    if change <= 0:
        return 0
    elif change in n:
        return 1
    else:
        for i in [c for c in n if c <= change]:
            if i <= change:
                num_coin = mincoin(coins, change-i)
                min_coin = min(min_coin, num_coin + 1)
    return min_coin


print(mincoin(n.sort(), total))