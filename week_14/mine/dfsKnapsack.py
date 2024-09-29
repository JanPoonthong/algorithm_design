# Class to represent an item with weight, value, and value-to-weight ratio (r)
class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight  # Value-to-weight ratio for sorting


# Input for number of items (N) and knapsack capacity (M)
inputs = input().split()
N = int(inputs[0])  # Number of items
M = int(inputs[1])  # Capacity of knapsack

# Input weights and values of the items
weights = input().split()
values = input().split()

# Creating a list of Item objects
items = []
for i in range(N):
    items.append(Item(int(weights[i]), int(values[i])))


# Function to get the sorting key, which is the value-to-weight ratio
def get_ratio(item):
    return item.ratio


# Sort items based on value-to-weight ratio in descending order
items.sort(key=get_ratio, reverse=True)


# Function to calculate the bound (upper bound on the max value we can achieve)
# i: current item index, remaining_capacity: available capacity in the knapsack
def calculate_bound(i, remaining_capacity):
    total_weight = 0  # Accumulated weight
    total_value = 0  # Accumulated value
    current_index = i
    fractional_part = 1.0  # Tracks whether the next item can be taken fully or fractionally

    # Loop through the remaining items
    while current_index < N and fractional_part == 1.0:
        # Take as much of the current item as possible (fractional if needed)
        available_weight = min(remaining_capacity - total_weight, items[current_index].weight)
        fractional_part = float(available_weight) / items[current_index].weight
        total_weight += fractional_part * items[current_index].weight
        total_value += fractional_part * items[current_index].value
        current_index += 1

    return total_value  # Return the estimated value (upper bound)


# Global variables to track the maximum value found and the number of DFS calls
max_value = 0
call_count = 0


# DFS (Depth-First Search) function to explore all item combinations
# i: current item index, current_weight: current weight in knapsack, current_value: current value in knapsack
def dfs(i, current_weight, current_value):
    global max_value, items, N, M, call_count
    if i == N:
        # Base case: All items are considered, update max_value
        max_value = max(max_value, current_value)
    else:
        call_count += 1  # Track the number of recursive calls

        # Calculate the bounds for taking and skipping the current item
        bound_if_take = -1
        if current_weight + items[i].weight <= M:
            bound_if_take = (
                current_value + items[i].value + calculate_bound(i + 1, M - current_weight - items[i].weight)
            )

        bound_if_skip = current_value + calculate_bound(i + 1, M - current_weight)

        # Decide whether to take or skip the current item based on bounds
        if bound_if_skip > bound_if_take:
            if bound_if_skip > max_value:
                dfs(i + 1, current_weight, current_value)  # Skip the item
            if bound_if_take > max_value:
                dfs(
                    i + 1,
                    current_weight + items[i].weight,
                    current_value + items[i].value,
                )  # Take the item
        else:
            if bound_if_take > max_value:
                dfs(
                    i + 1,
                    current_weight + items[i].weight,
                    current_value + items[i].value,
                )  # Take the item
            if bound_if_skip > max_value:
                dfs(i + 1, current_weight, current_value)  # Skip the item


# Start the DFS search
dfs(0, 0, 0)

# Output the maximum value found and the number of DFS calls made
print(max_value)
print(call_count)
