def Bound(current_index, remaining_capacity, items, total_items):
    """
    Calculate an upper bound on the maximum achievable value from the current item onwards,
    assuming fractional items can be taken.

    Parameters:
    current_index: The index of the current item being considered.
    remaining_capacity: The remaining capacity of the knapsack.
    items: A list of Item objects, each with a weight and value.
    total_items: The total number of items.

    Returns:
    The maximum possible value that can be achieved starting from the current item,
    including potential fractional items.
    """
    total_weight = 0  # Accumulates the total weight used so far
    total_value = 0   # Accumulates the total value obtained so far
    index = current_index  # Start with the current item
    fraction = 1.0  # Fraction of the current item we are allowed to take (1.0 means full item)

    # Loop through the items starting from the current one
    while index < total_items and fraction == 1.0:
        # Calculate how much of the current item we can take (either full or fractional)
        available_capacity = remaining_capacity - total_weight  # How much space is left
        item_weight = items[index].weight  # Weight of the current item
        item_value = items[index].value  # Value of the current item

        # Take as much of the current item as possible (either the full item or what's left of the capacity)
        weight_taken = min(available_capacity, item_weight)
        fraction = weight_taken / item_weight  # Fraction of the item taken (1.0 if full, less if partial)

        # Update the total weight and value based on the fraction of the item taken
        total_weight += fraction * item_weight
        total_value += fraction * item_value

        # Move to the next item
        index += 1

    # Return the total value, which represents the upper bound of the value that can be obtained
    return total_value
