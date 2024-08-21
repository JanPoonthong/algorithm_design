N = int(input())

def conflict(Q, i, j):
    if Q[i] == Q[j] or abs(Q[i]-Q[j]) == abs(i-j):
        return True
    
    return False

class state:
    def __init__(self, n):
        self.queen = [1] * n
        self.col = 0

def valid(Q, col, row):
    q = Q[:]
    q[col] = row
    valid = True
    for i in range(col):
        if conflict(q, i, col):
            valid = False
            break
    return valid

import copy

def successor(s):
    succ = []
    for r in range(N):
        if valid(s.queen, s.col, r):
            u = copy.deepcopy(s)
            u.queen[u.col] = r
            u.col += 1
            succ.append(u)
    return succ

Queue = []
s = state(N)
while s.col < N:
    for u in successor(s):
        Queue.append(u)
    s = Queue[0]
    del Queue[0]


def printqueens(Q):
    n = len(Q)
    board = [['.']*n for i in range(n)]
    for j in range(n):
        board[Q[j]][j] = 'Q'
    for i in range(n):
        for j in range(n):
            print(board[i][j], end='')
        print()


printqueens(u.queen)