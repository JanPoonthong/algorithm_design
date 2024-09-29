# Function to calculate an upper bound on the maximum value we can achieve.
# i: current item index, capacity: available capacity in the knapsack.
def calculate_bound(i, capacity):
    global items, N

    total_weight = 0  # Tracks the accumulated weight in the knapsack.
    total_value = 0  # Tracks the accumulated value in the knapsack.
    current_index = i  # Current item being considered.
    fraction = 1.0  # Determines if the next item can be taken fully or fractionally.

    # Loop through the remaining items.
    while current_index < N and fraction == 1.0:
        # Take as much of the current item as possible (fully or fractionally).
        available_weight = min(capacity - total_weight, items[current_index].weight)

        # Calculate the fraction of the current item that can be taken.
        fraction = float(available_weight) / items[current_index].weight

        # Accumulate weight and value based on the fraction of the item taken.
        total_weight += fraction * items[current_index].weight
        total_value += fraction * items[current_index].value

        current_index += 1  # Move to the next item.

    return total_value  # Return the estimated value (upper bound).
