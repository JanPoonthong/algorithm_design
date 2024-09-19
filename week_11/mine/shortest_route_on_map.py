import heapq


def dijkstra(graph, start):
    # Initialize distances with infinity
    distances = {node: float("inf") for node in graph}
    distances[start] = 0  # Distance to the start node is 0

    # Priority queue to hold nodes to explore, initialized with the start node
    priority_queue = [(0, start)]  # (distance, node)

    while priority_queue:
        # Get the node with the smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip processing if we have already found a shorter path
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Example graph represented as an adjacency list
# The graph is a dictionary where keys are nodes and values are dictionaries
# of neighbors and their associated edge weights
graph = {
    "A": {"B": 1, "C": 4},
    "B": {"A": 1, "C": 2, "D": 5},
    "C": {"A": 4, "B": 2, "D": 1},
    "D": {"B": 5, "C": 1},
}

# Finding shortest paths from node 'A'
distances = dijkstra(graph, "A")
print(distances)
