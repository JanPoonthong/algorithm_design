import sys
sys.setrecursionlimit(20001)

n = 9
d = 3
p = []
for i in range(d):
    p += list(map(int, input().split()))

import copy

def valid(i,j):
    global d
    
    if i >= 0 and i < d and j >= 0 and j < d:
        return True
    else:
        return False

class state:
    def __init__(self, p):
        self.p = copy.deepcopy(p)
        self.g = 0

adj = [(0,-1),(0,1),(1,0),(-1,0)]

def goal(s):
    for i in range(n):
        if s.p[i] != i:
            return False
    return True

def successor(s):
    global d

    succ = []
    for i in range(len(s.p)):
            if s.p[i] == 0:
                hole = i
                break
    r = hole//d
    c = hole%d
    for a in adj:
        i = r + a[0]
        j = c + a[1]
        if valid(i,j):
            target = i*d + j
            m = s.p[:]
            m[target],m[hole] = m[hole],m[target]
            u = state(m)
            u.g = s.g+1
            succ.append(u)
    return succ

def DFS(s, maxDepth):
    global count

    if s.g > maxDepth:
        return -1
    elif goal(s):
        return s.g
    else:
        count += 1
        for u in successor(s):
            minstep = DFS(u, maxDepth)
            if minstep != -1:
                return minstep
        return -1
        

def IDS(s):  # Iterative Deepening Search
    # Complete this function (which utilizes DFS)

    
          
count = 0
s = state(p)
print(IDS(s))
print("state count = ", count)
