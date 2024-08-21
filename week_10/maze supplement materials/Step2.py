
def valid(r,c):
    if r >= 0 and r < M and c >= 0 and c < N:
        if maze[r][c] == 0:
            return True
    return False

