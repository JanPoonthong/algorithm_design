from sys import stdin

# Define a large number to represent "infinity"
INF = 10000000000

# Number of vertices (cities)
V = int(input())

# Adjacency list to store the graph, where each vertex has a list of (neighbor, weight)
adj = [[] for i in range(V)]

# Reading input from stdin to construct the graph
for line in stdin:
    x = line.split()
    u = int(x[0])  # Current city
    v = int(x[1])  # Neighboring city
    w = int(x[2])  # Distance/weight between cities
    adj[u].append((v, w))  # Add edge (v, w) to city u's adjacency list
    adj[v].append(
        (u, w)
    )  # Add edge (u, w) to city v's adjacency list (because the graph is undirected)

from simplePriorityQueue import Simple_Priority_Queue


# State class representing the city and its associated distance
class State:
    def __init__(self, city, d):
        self.city = city  # Current city
        self.d = d  # Distance from the starting city


# Function to find successor states (neighboring cities)
def successor(s):
    global shortest  # Reference to the shortest distances array

    succ = []  # List to store successors (neighboring states)

    # Iterate through neighbors of the current city
    for a in adj[s.city]:
        v = a[0]  # Neighboring city
        w = a[1]  # Weight of the edge to the neighbor

        # If a shorter path to v is found, update the shortest path and add to successors
        if s.d + w < shortest[v]:
            shortest[v] = s.d + w
            succ.append(
                State(v, s.d + w)
            )  # Add the new state to the successor list

    return succ  # Return all valid successors


# Initialize the shortest path array to infinity for all cities
shortest = [INF] * V


# Function to compare two states based on their distance for priority queue purposes
def cityCompare(x, y):
    return x.d < y.d


# Uniform Cost Search (UCS) starts here
pq = Simple_Priority_Queue(
    cityCompare
)  # Priority queue to store states (city, distance)
start_state = State(0, 0)  # Start from city 0 with a distance of 0

# While the goal city (V-1) is not reached
while start_state.city != V - 1:
    # Add all successors (neighboring cities) of the current state to the priority queue
    for next_state in successor(start_state):
        pq.enqueue(next_state)

    # Move to the state with the smallest distance (dequeue the priority queue)
    start_state = pq.dequeue()

# Once the goal city (V-1) is reached, print the distance to it
print(start_state.d)
