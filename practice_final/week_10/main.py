V = 4
edges = [(0, 1), (0, 2), (1, 2), (1, 3)]
M = 3

import copy

class ColoringState:
    def __init__(self, size):
        self.colors = [-1] * size
        self.current_vertex = 0


def is_valid(colors, vertex, color, graph):
    for neighbor in range(len(graph)):
        if graph[vertex][neighbor] == 1 and colors[neighbor] == color:
            return False
    return True


def create_adjacency_matrix(V, edges):
    matrix = [[0 for _ in range(V)] for _ in range(V)]
    for edge in edges:
        u, v = edge
        matrix[u][v] = 1
        matrix[v][u] = 1

    return matrix

def generate_successors(state, graph, M):
    successors = []
    for color in range(1, M+1):
        if is_valid(state.colors, state.current_vertex, color, graph):
            new_state = copy.deepcopy(state)
            new_state.colors[new_state.current_vertex] = color
            new_state.current_vertex += 1
            successors.append(new_state)
    return successors

graph = create_adjacency_matrix(V, edges)

queue = []
initial_state = ColoringState(V)
queue.append(initial_state)

solution_state = None
while queue:
    current_state = queue.pop(0)
    if current_state.current_vertex == V:
        solution_state = current_state
        break
    for successor_state in generate_successors(current_state, graph, M):
        queue.append(successor_state)


def print_solution(colors):
    if colors:
        for vertex in range(V):
            print(f"Vertex {vertex}: Color {colors[vertex]}")
    else:
        print("No solution exists.")

# Print the solution
if solution_state:
    print("Solution found:")
    print_solution(solution_state.colors)
else:
    print("No solution exists.")