class obj:
    def __init__(self, w, v):
        self.w = w
        self.v = v
        self.r = v / w


x = input().split()
N = int(x[0])
M = int(x[1])
w = input().split()
v = input().split()
item = []
for i in range(N):
    item.append(obj(int(w[i]), int(v[i])))


def getKey(x):
    return x.r


item.sort(key=getKey, reverse=True)


def Bound(i, C):  # object i -> n-1, capacity = C (maximum value you can get)
    global item, N

    sw = 0
    sv = 0
    j = i
    f = 1.0
    while j < N and f == 1.0:
        wj = min(C - sw, item[j].w)
        f = float(wj) / item[j].w
        sw += f * item[j].w
        sv += f * item[j].v
        j += 1
    return sv


maxV = 0
count = 0


def dfs(i, sumW, sumV):
    global maxV, item, N, M, count
    if i == N:
        # if sumW <= M:
        maxV = max(maxV, sumV)
    else:
        count += 1

        boundTake = -1
        if sumW + item[i].w <= M:
            boundTake = sumV + item[i].v + Bound(i + 1, M - sumW - item[i].w)

        boundSkip = sumV + Bound(i + 1, M - sumW)

        if boundSkip > boundTake:
            if boundSkip > maxV:
                dfs(i + 1, sumW, sumV)
            if boundTake > maxV:
                dfs(i + 1, sumW + item[i].w, sumV + item[i].v)
        else:
            if boundTake > maxV:
                dfs(i + 1, sumW + item[i].w, sumV + item[i].v)
            if boundSkip > maxV:
                dfs(i + 1, sumW, sumV)


dfs(0, 0, 0)
print(maxV)
print(count)


# def dfs(i, sumW, sumV):
#     global maxV, item, N, M, count
#     count += 1
#     if i == N:
#         #if sumW <= M:
#             maxV = max(maxV, sumV)
#     else:
#         if sumW + item[i].w <= M:
#             if sumV + item[i].v + Bound(i+1, M-sumW-item[i].w) > maxV:
#                 dfs(i+1, sumW+item[i].w, sumV+item[i].v)
#         if sumV + Bound(i+1, M-sumW) > sumV:
#             dfs(i+1, sumW, sumV)

# def dfs(i, sumW, sumV):
#     global maxV, item, N, M, count
#     count += 1
#     if sumW <= M:
#         bound = Bound(i, M)
#         if sumV <= bound:
#             if i == N:
#                 if sumW <= M:
#                     maxV = max(maxV, sumV)
#             else:
#                 dfs(i+1, sumW, sumV)
#                 dfs(i+1, sumW+item[i].w, sumV+item[i].v)
