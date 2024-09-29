import KnapsackBound

# Define a class to represent an item with weight (w), value (v), and value-to-weight ratio (r)
class Item:
    def __init__(self, weight, value):
        self.weight = weight  # Item's weight
        self.value = value    # Item's value
        self.ratio = value / weight  # Value-to-weight ratio

# Read the first line of input: N (number of items) and M (maximum weight capacity)
N, M = map(int, input().split())

# Read the weights and values of the items from input
weights = list(map(int, input().split()))  # List of item weights
values = list(map(int, input().split()))   # List of item values

# Create a list of Item objects based on input weights and values
items = []
for i in range(N):
    items.append(Item(weights[i], values[i]))

# Sort items in descending order based on value-to-weight ratio (greedy approach for fractional knapsack)
items.sort(key=lambda item: item.ratio, reverse=True)

# Initialize global variables:
max_value = 0  # To track the maximum value found during DFS
num_calls = 0  # To track the number of recursive DFS calls made

# Define the Depth-First Search (DFS) function
def dfs(index, current_weight, current_value):
    """
    Perform DFS to explore different combinations of items to maximize value within weight capacity.

    Parameters:
    index: The current item index being considered
    current_weight: The total weight of the selected items so far
    current_value: The total value of the selected items so far
    """
    global max_value, items, N, M, num_calls

    # Increment the number of DFS calls (for analysis purposes)
    num_calls += 1

    # If the current weight exceeds the capacity, prune (stop exploring this path)
    if current_weight > M:
        return

    # Calculate an upper bound on the maximum value achievable from this point onwards
    # Using fractional items with the remaining capacity
    upper_bound = current_value + KnapsackBound.Bound(index, M - current_weight, items, N)

    # If the upper bound is worse than the current maximum value, prune this branch
    if upper_bound <= max_value:
        return

    # If all items have been considered, update the maximum value if current weight is valid
    if index == N:
        if current_weight <= M:
            max_value = max(max_value, current_value)
    else:
        # Option 1: Skip the current item and move to the next
        dfs(index + 1, current_weight, current_value)

        # Option 2: Take the current item (add its weight and value) and move to the next
        dfs(index + 1, current_weight + items[index].weight, current_value + items[index].value)

# Start the DFS from the first item, with no initial weight or value
dfs(0, 0, 0)

# Output the results:
print("Maximum value:", max_value)  # Maximum value that can be achieved without exceeding weight limit
print("Total recursive calls:", num_calls)  # Number of DFS calls made
