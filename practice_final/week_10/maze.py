rows, cols = map(int, input().split())
start_row, start_col = map(int, input().split())
exit_row, exit_col = map(int, input().split())

maze = [[0 for _ in range(cols)] for _ in range(rows)]

for r in range(rows):
    row_input = list(map(int, input().split()))
    for c in range(cols):
        maze[r][c] = row_input[c]

import copy

class MazeState:
    def __init__(self):
        self.row = start_row
        self.col = start_col
        self.step = 0


def is_valid(r, c):
    if r >= 0 and r < rows and c >= 0 and c < cols and maze[r][c] == 0:
        return True
    return False

adj = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def generate_successors(current_state):
    successors = []

    for row, col in adj:
        new_row = current_state.row + row
        new_col = current_state.col + col

        if is_valid(new_row, new_col):
            new_state = copy.deepcopy(current_state)
            new_state.row = new_row
            new_state.col = new_col
            new_state.step += 1

            maze[new_row][new_col] = new_state.step

            successors.append(new_state)
    
    return successors

queue = []
initial_state = MazeState()
queue.append(initial_state)

solution_state = None
while queue:
    current_state = queue.pop(0)
    if current_state.row == exit_row and current_state.col == exit_col:
        solution_state = current_state
        break
    for successor_state in generate_successors(current_state):
        queue.append(successor_state)

def print_solution(solution_state):
    print(solution_state.step)

# Print the solution
if solution_state:
    print("Solution found:")
    print_solution(solution_state)
else:
    print("No solution exists.")