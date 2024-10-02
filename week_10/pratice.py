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
        maze[i][j] = -int(x[j])  # set wall to -1 (so it won't mix with BFS)


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


import copy
Adj = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def successor(s):
    succ = []
    for row, col in Adj:
        new_row = s.r + row
        new_col = s.c + col

        if valid(new_row, new_col):
            u = copy.deepcopy(s)
            u.r = new_row
            u.c = new_col
            u.step += 1
            maze[u.r][u.c] = u.step
            succ.append(u)

    return succ

Queue = []
s = state(sr, sc, 0)
while not (s.r == dr and s.c == dc):
    for u in successor(s):
        Queue.append(u)
    s = Queue[0]
    del Queue[0]
    
print(s.step)