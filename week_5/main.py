import sys

sys.setrecursionlimit(1000000)

price = list(map(int, input().split()))
length = []
for i in range(1, len(price)+1):
    length.append(i)
calls = [0] * (len(length) + 1)

def maxRev(l):
    global calls
    calls[l] += 1
    if l == 0:
        return 0
    else:
        revenue = float('-inf')
        for i in length:
            if i <= l:
                revenue = max(price[i - 1] + maxRev(l - i), revenue)
                print(i, revenue)
    return revenue

print(maxRev(len(length)))
print(calls)


# Exam: 100 stair how possible way to to go up the stair, can go 1 step or 2 step