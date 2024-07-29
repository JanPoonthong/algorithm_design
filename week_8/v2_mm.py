import sys
sys.setrecursionlimit(10000)

N,M = map(int, input().split())
w = list(map(int, input().split()))
v = list(map(int, input().split()))

mm = [[-1]*(M+1) for i in range(N+1)]

def maxVal(i,C):
    if mm[i][C] == -1:
        if i == N or C == 0:
            mm[i][C] = 0
        else:
            skip = maxVal(i+1, C)   # skip item i
            take = 0
            if w[i] <= C:
                take = v[i] + maxVal(i+1, C-w[i])  # take item i
            mm[i][C] = max(skip,take)
    return mm[i][C]

print(maxVal(0,M))
