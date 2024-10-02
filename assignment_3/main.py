import sys
import copy

# Increase recursion limit to handle deep recursive calls
sys.setrecursionlimit(20001)

# Directions for moving the empty space (row, col): left, right, down, up
adj = [(0, -1), (0, 1), (1, 0), (-1, 0)]

n = 9  # 8-puzzle has 9 positions (3x3)
d = 3  # The dimension of the puzzle (3x3)

# Input the initial puzzle configuration as a 1D list
p = []
for i in range(d):
    p += list(map(int, input().split()))


# Helper function to check if a move is within bounds
def valid(i, j):
    return 0 <= i < d and 0 <= j < d


# State class to store puzzle configuration, number of moves (g), and heuristic (h)
class state:
    def __init__(self, p):
        self.p = copy.deepcopy(p)  # Puzzle configuration
        self.g = 0  # Number of moves made so far
        self.h = 1000000000  # Heuristic value (Manhattan distance)


# Manhattan distance heuristic function
def manhattan(p):
    h = 0
    for i in range(len(p)):
        if p[i] != 0:  # Don't count the empty space (0)
            target_row = (p[i] - 1) // d
            target_col = (p[i] - 1) % d
            current_row = i // d
            current_col = i % d
            h += abs(target_row - current_row) + abs(target_col - current_col)
    return h


# Generate successor states by moving the empty space (0)
def successor(s):
    succ = []
    # Find the index of the empty space (0)
    for i in range(len(s.p)):
        if s.p[i] == 0:
            hole = i
            break
    r = hole // d
    c = hole % d
    for a in adj:
        new_r = r + a[0]
        new_c = c + a[1]
        if valid(new_r, new_c):
            # Swap the empty space with the target tile
            target = new_r * d + new_c
            new_puzzle = s.p[:]
            new_puzzle[hole], new_puzzle[target] = new_puzzle[target], new_puzzle[hole]
            u = state(new_puzzle)
            u.g = s.g + 1  # Increment move count
            u.h = manhattan(new_puzzle)  # Update heuristic
            succ.append(u)
    return succ


# Depth-First Search with pruning (limited by atMost)
def DFS(s, atMost):
    global count, found

    if s.g + s.h > atMost:
        return s.g + s.h
    elif s.h == 0:
        found = True
        return s.g
    else:
        count += 1
        atLeast = 10000000000
        for u in successor(s):
            atLeast = min(atLeast, DFS(u, atMost))
            if found:
                break
        return atLeast


# Iterative Deepening A* algorithm
def IDAstar(s):
    global found

    # Start the search with the initial heuristic
    atMost = DFS(s, s.h)
    while not found:
        atMost = DFS(s, atMost)
    return atMost


# Initialize the search state
count = 0
s = state(p)
s.h = manhattan(s.p)  # Calculate the Manhattan distance for the initial state
found = False

# Solve the puzzle and print the result
print(IDAstar(s))
# print("state count =", count)
