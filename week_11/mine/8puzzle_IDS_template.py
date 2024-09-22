import sys
import copy

# Increase recursion depth to allow deeper recursive calls for DFS
sys.setrecursionlimit(20001)

# Initialize the puzzle
n = 9  # Total number of pieces (3x3 puzzle, so 9 pieces)
d = 3  # Dimension of the puzzle (3x3 puzzle, so d = 3)

# Input the puzzle state from the user
p = []
for _ in range(d):
    p += list(map(int, input().split()))


# Check if a position (i, j) is within the puzzle grid
def is_valid_position(i, j):
    return 0 <= i < d and 0 <= j < d


# Class representing the state of the puzzle
class PuzzleState:
    def __init__(self, p):
        # Create a deep copy of the puzzle list to avoid modifying the original list
        self.p = copy.deepcopy(p)
        self.g = 0  # 'g' represents the depth (number of moves made)


# List of possible moves: left, right, down, and up
moves = [(0, -1), (0, 1), (1, 0), (-1, 0)]


# Check if the current puzzle state is the goal state (solved)
def is_goal_state(state):
    for i in range(n):
        if state.p[i] != i:
            return False
    return True


# Generate all possible next states by moving the blank space (0)
def get_successors(state):
    successors = []

    # Find the position of the blank space (0)
    hole = state.p.index(0)
    row, col = divmod(hole, d)  # Get the row and column from the index

    # Try moving the blank space in all possible directions
    for move in moves:
        new_row = row + move[0]
        new_col = col + move[1]

        if is_valid_position(new_row, new_col):
            # Calculate the new index for the blank space after moving
            target = new_row * d + new_col

            # Swap the blank space with the target piece
            new_puzzle = state.p[:]
            new_puzzle[hole], new_puzzle[target] = (
                new_puzzle[target],
                new_puzzle[hole],
            )

            # Create a new state for the resulting puzzle configuration
            new_state = PuzzleState(new_puzzle)
            new_state.g = state.g + 1  # Increment the depth (number of moves)
            successors.append(new_state)

    return successors


# Depth-First Search with a depth limit
def depth_first_search(state, max_depth):
    global count

    # If the current depth exceeds the max depth, stop this branch
    if state.g > max_depth:
        return -1

    # If the current state is the goal, return the number of moves taken
    if is_goal_state(state):
        return state.g

    # Increment the count of visited states
    count += 1

    # Recursively explore successor states
    for successor_state in get_successors(state):
        result = depth_first_search(successor_state, max_depth)
        if result != -1:  # If a solution is found, return it
            return result

    return -1  # No solution found at this depth


# Iterative Deepening Search (IDS)
def iterative_deepening_search(initial_state):
    depth_limit = 0

    # Try solving the puzzle by gradually increasing the depth limit
    result = depth_first_search(initial_state, depth_limit)

    # Keep increasing the depth limit until a solution is found
    while result == -1:
        depth_limit += 1
        result = depth_first_search(initial_state, depth_limit)

    return result


# Main code execution
count = 0  # Variable to count the number of states explored
initial_state = PuzzleState(p)

# Perform the search and print the result
solution_depth = iterative_deepening_search(initial_state)
print(solution_depth)  # Print the number of moves to solve the puzzle
print("State count = ", count)  # Print the number of states explored
