import sys

sys.setrecursionlimit(20001)

# Problem configuration
n = 9  # Total number of states to explore
d = 3  # Dimension of the puzzle (3x3 puzzle)
p = []  # Puzzle initial state (list of numbers)

# Read the input for the initial puzzle configuration
for i in range(d):
    p += list(map(int, input().split()))

import copy


# Check if a position (i, j) is within the bounds of the puzzle grid
def is_valid(i, j):
    if 0 <= i < d and 0 <= j < d:
        return True
    return False


# Define a class to represent a state in the puzzle
class State:
    def __init__(self, puzzle):
        self.puzzle = copy.deepcopy(puzzle)  # Puzzle configuration (deep copy)
        self.g = 0  # Cost from the start state to the current state
        self.h = float(
            "inf"
        )  # Heuristic value, initially set to a large number


# Calculate the Manhattan distance as the heuristic (lower bound on moves required)
def calculate_manhattan(puzzle):
    h = 0  # Heuristic value
    for i in range(len(puzzle)):
        if puzzle[i] != 0:  # Ignore the empty space (represented by 0)
            current_row, current_col = divmod(i, d)
            target_row, target_col = divmod(puzzle[i], d)
            h += abs(current_row - target_row) + abs(current_col - target_col)
    return h


# Possible movements in the puzzle: left, right, down, up
adjacent_moves = [(0, -1), (0, 1), (1, 0), (-1, 0)]


# Get all the valid successor states of the current state by moving the empty space (0)
def get_successors(current_state):
    successors = []

    # Find the index of the empty space (0)
    hole_index = current_state.puzzle.index(0)

    # Get the row and column of the empty space
    hole_row, hole_col = divmod(hole_index, d)

    # Try moving the empty space in all four directions
    for move in adjacent_moves:
        new_row = hole_row + move[0]
        new_col = hole_col + move[1]

        if is_valid(new_row, new_col):
            new_index = new_row * d + new_col  # Convert the 2D index back to 1D
            new_puzzle = current_state.puzzle[:]  # Copy the current puzzle
            new_puzzle[hole_index], new_puzzle[new_index] = (
                new_puzzle[new_index],
                new_puzzle[hole_index],
            )  # Swap tiles

            # Create a new state and update its cost and heuristic
            new_state = State(new_puzzle)
            new_state.g = current_state.g + 1  # Increase the cost
            new_state.h = calculate_manhattan(
                new_puzzle
            )  # Calculate the heuristic
            successors.append(new_state)

    return successors


# Perform Depth-First Search (DFS) with a limit on the cost
def DFS(current_state, max_cost):
    global count, goal_found

    # If the estimated cost exceeds the current limit, return
    if current_state.g + current_state.h > max_cost:
        return current_state.g + current_state.h

    # If the heuristic is 0, we've reached the goal state
    if current_state.h == 0:
        goal_found = True
        return current_state.g

    # Otherwise, keep searching for a solution
    count += 1
    min_cost_exceeded = float(
        "inf"
    )  # Minimum cost that exceeded the current limit

    # Explore all successor states
    for successor in get_successors(current_state):
        min_cost_exceeded = min(min_cost_exceeded, DFS(successor, max_cost))
        if goal_found:
            break

    return min_cost_exceeded


# Perform IDA* search starting from the initial state
def IDA_star(start_state):
    global goal_found

    # Initial search limit is the heuristic value of the start state
    max_cost = DFS(start_state, start_state.h)

    # Continue searching with increasing limits until the goal is found
    while not goal_found:
        max_cost = DFS(start_state, max_cost)

    return max_cost


# Initialize variables
count = 0
goal_found = False

# Create the initial state and calculate its heuristic
start_state = State(p)
start_state.h = calculate_manhattan(start_state.puzzle)

# If the puzzle is already solved, mark the goal as found
if start_state.h == 0:
    goal_found = True

# Perform IDA* search and print the results
solution_cost = IDA_star(start_state)
print("Solution found with cost:", solution_cost)
print("Number of states explored:", count)
