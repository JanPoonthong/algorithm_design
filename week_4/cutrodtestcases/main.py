import sys

sys.setrecursionlimit(1000000)

price = list(map(int, input().split()))
length = []
for i in range(1, len(price)+1):
    length.append(i)


def maxRev(l):
    if l == 0:
        return 0
    else:
        revenue = float('-inf')
        for i in length:
            if i <= l:
                revenue = max(price[i - 1] + maxRev(l - i), revenue)
    return revenue

print(maxRev(len(length)))