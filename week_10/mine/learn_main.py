N = int(input())

class State:
    def __init__(self, n):
        self.queen = [1] * n
        self.col = 0

def valid(Q, col, row):
    q = Q[:]
    q[col] = row

def successor(s):
    succ = []
    for r in range(N):
        if valid(s.queen, s.col, r)

Queue = []
s = State(N)
while s.col < N:
    for u in successor(s):
