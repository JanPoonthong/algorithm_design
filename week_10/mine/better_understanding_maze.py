import copy

# Input the number of rows (M) and columns (N) for the maze
rows, cols = map(int, input().split())  # rows = M, cols = N

# Create a maze of size M x N filled with 0s
maze = [[0 for _ in range(cols)] for _ in range(rows)]

# Input starting position (sr, sc) and destination position (dr, dc)
start_row, start_col = map(int, input().split())
dest_row, dest_col = map(int, input().split())

# Input the maze layout where -1 represents a wall and 0 represents a free path
for r in range(rows):
    row_input = list(map(int, input().split()))  # Input row by row
    for c in range(cols):
        maze[r][c] = -row_input[c]  # Negative value for walls (easier to distinguish)


# Function to check if the next position is valid to move into (inside bounds and not a wall)
def is_valid_move(r, c):
    return 0 <= r < rows and 0 <= c < cols and maze[r][c] == 0


# Define the state class which stores the current position (row, column) and the step count
class State:
    def __init__(self, row, column, steps):
        self.row = row  # Current row
        self.col = column  # Current column
        self.steps = steps  # Steps taken to reach this point


# Directions for moving up, right, down, and left (in that order)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


# Function to generate valid successor states (next possible moves)
def get_successors(current_state):
    successors = []
    for direction in directions:
        new_row = current_state.row + direction[0]
        new_col = current_state.col + direction[1]

        if is_valid_move(new_row, new_col):  # Check if the move is valid
            # Create a new state for the valid move
            new_state = copy.deepcopy(current_state)
            new_state.row = new_row
            new_state.col = new_col
            new_state.steps += 1  # Increment the step count

            # Mark the new position with the step count to avoid visiting it again
            maze[new_row][new_col] = new_state.steps

            # Add the new state to the list of successors
            successors.append(new_state)

    return successors


# Check if the current state has reached the destination
def is_goal(current_state):
    return current_state.row == dest_row and current_state.col == dest_col


# Initialize BFS
queue = []
start_state = State(start_row, start_col, 0)  # Starting state with 0 steps
queue.append(start_state)

# BFS loop to explore all possible paths
while queue:
    current_state = queue.pop(0)  # Dequeue the first state

    if is_goal(current_state):  # If the goal is reached, print the number of steps and exit
        print(current_state.steps)
        break

    # Get all valid successors (next possible states) and add them to the queue
    for successor in get_successors(current_state):
        queue.append(successor)
