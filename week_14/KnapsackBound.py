def Bound(i, C, item, N):  # Object i -> N-1, Capacity = C, with item and N passed
    sw = 0  # Sum of weights
    sv = 0  # Sum of values
    j = i  # Start from the current item index
    f = 1.0  # Fraction to handle fractional items

    # Continue adding items until no capacity remains
    while j < N and f == 1.0:
        # Add as much of item j as possible (or fractional part)
        wj = min(C - sw, item[j].w)  # Remaining capacity or full item weight
        f = float(wj) / item[j].w  # Fraction of the item taken
        sw += f * item[j].w  # Update sum of weights
        sv += f * item[j].v  # Update sum of values
        j += 1  # Move to the next item

    return sv  # Return the upper bound of value
