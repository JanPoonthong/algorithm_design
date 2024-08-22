x = input().split()
M = int(x[0])  # number of rows
N = int(x[1])  # number of columns
maze = [[0 for i in range(N)] for j in range(M)]
x = input().split()
sr = int(x[0])
sc = int(x[1])
x = input().split()
dr = int(x[0])
dc = int(x[1])
for i in range(M):
    x = input().split()
    for j in range(N):
        maze[i][j] = -int(x[j])  # set wall to -1 (so it won't mix with BFS


def valid(r, c):
    if r >= 0 and r < M and c >= 0 and c < N:
        if maze[r][c] == 0:
            return True
    return False


class state:
    def __init__(self, row, column, step):
        self.r = row
        self.c = column
        self.step = step


Adj = [(-1, 0), (0, 1), (1, 0), (0, -1)]

import copy


def successor(s):
    succ = []
    for d in Adj:
        r = s.r + d[0]
        c = s.c + d[1]
        if valid(r, c):
            u = copy.deepcopy(s)
            u.r = r
            u.c = c
            u.step += 1
            maze[u.r][u.c] = u.step
            succ.append(u)
    return succ


def goal(s):
    if s.r == dr and s.c == dc:
        return True
    return False


Queue = []
s = state(sr, sc, 0)
while not goal(s):
    for u in successor(s):
        Queue.append(u)
    s = Queue[0]
    del Queue[0]
print(s.step)
