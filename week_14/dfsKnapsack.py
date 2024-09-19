import KnapsackBound

class obj:
    def __init__(self,w,v):
        self.w = w
        self.v = v
        self.r = v/w

x = input().split()
N = int(x[0])
M = int(x[1])
w = input().split()
v = input().split()
item = []
for i in range(N):
    item.append(obj(int(w[i]),int(v[i])))

maxV = 0

def dfs(i, sumW, sumV):
    global maxV, item, N, M

    if sumW <= M and maxV < sumV + KnapsackBound.Bound(i, M-sumW):
        if i == N:
            if sumW <= M:
                maxV = max(maxV, sumV)
        else:
            dfs(i+1, sumW, sumV)
            dfs(i+1, sumW+item[i].w, sumV+item[i].v)

dfs(0,0,0)
print(maxV)




    
