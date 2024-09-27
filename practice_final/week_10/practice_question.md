Here's a question similar to the N-Queens problem that focuses on backtracking and constraint satisfaction:

**Problem: M-Coloring Problem**

You are given a graph with \( V \) vertices and \( E \) edges. The goal is to color the graph using at most \( M \) colors such that no two adjacent vertices share the same color. Write a function to determine if the graph can be colored with \( M \) colors.

### Input:
- An integer \( V \) representing the number of vertices.
- A list of tuples (or a 2D list) representing the edges of the graph.
- An integer \( M \) representing the number of colors.

### Output:
- Return `True` if the graph can be colored with \( M \) colors, otherwise return `False`.

### Example:
```plaintext
Input:
V = 4
edges = [(0, 1), (0, 2), (1, 2), (1, 3)]
M = 3

Output:
True
```

### Explanation:
You can color the graph with three colors as follows:
- Vertex 0: Color 1
- Vertex 1: Color 2
- Vertex 2: Color 3
- Vertex 3: Color 1

This problem can be solved using backtracking, similar to how you would approach the N-Queens problem.