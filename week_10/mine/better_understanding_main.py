# Rewrote in a more understanding way of arjan way of doing

N = int(input())  # Size of the chessboard (N x N)

# Function to check if two queens are in conflict
def is_conflict(queens, col1, col2):
    # Check if the queens in column col1 and col2 are in the same row or diagonal
    if queens[col1] == queens[col2] or abs(queens[col1] - queens[col2]) == abs(col1 - col2):
        return True
    return False

# Class representing the state of the board
class BoardState:
    def __init__(self, size):
        self.queens = [-1] * size  # Initialize all columns with no queen placed (-1)
        self.current_col = 0  # Start placing queens in column 0

# Function to check if placing a queen at (row, col) is valid
def is_valid(queens, col, row):
    # Make a copy of the current queen placement
    temp_queens = queens[:]
    temp_queens[col] = row  # Try placing the queen in the current column

    # Check for conflicts with previously placed queens
    for prev_col in range(col):
        if is_conflict(temp_queens, prev_col, col):
            return False  # Conflict found, invalid position
    return True  # No conflicts, valid position

import copy

# Function to generate successor states by placing a queen in the next column
def generate_successors(state):
    successors = []
    for row in range(N):  # Try placing a queen in each row of the current column
        if is_valid(state.queens, state.current_col, row):  # Check if it's a valid move
            new_state = copy.deepcopy(state)  # Create a new state
            new_state.queens[new_state.current_col] = row  # Place the queen
            new_state.current_col += 1  # Move to the next column
            successors.append(new_state)  # Add the new state to successors
    return successors

# Initialize queue for BFS
queue = []
initial_state = BoardState(N)
queue.append(initial_state)

# BFS to find the solution
while queue:
    current_state = queue.pop(0)  # Dequeue the next state
    if current_state.current_col == N:  # All queens placed (solution found)
        solution_state = current_state
        break
    # Enqueue successors (next possible queen placements)
    for successor_state in generate_successors(current_state):
        queue.append(successor_state)

# Function to print the board with queens placed
def print_queens(queens):
    board_size = len(queens)
    board = [["."] * board_size for _ in range(board_size)]  # Initialize an empty board

    # Place queens on the board
    for col in range(board_size):
        if queens[col] != -1:
            board[queens[col]][col] = "Q"

    # Print the board
    for row in board:
        print(" ".join(row))
    print()

# Print the solution
print_queens(solution_state.queens)
