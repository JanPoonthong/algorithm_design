
x = input().split()
M = int(x[0])    # number of rows
N = int(x[1])    # number of columns
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

        
