import sys

sys.setrecursionlimit(10000)

N, M = map(int, input().split())
weights = list(map(int, input().split()))
values = list(map(int, input().split()))

memo = [[-1] * (M+1) for _ in range(N+1)]

def knapsack(i, remaining_capacity):
    # Base case: if no items left or capacity is 0
    if i == N and remaining_capacity == 0:
        return 0
    
    # If already calculated, return the stored value
    if memo[i][remaining_capacity] != -1:
        return memo[i][remaining_capacity]
    
    # Option 1: Skip the current item
    max_value_without_item = knapsack(i+1, remaining_capacity)

    # Option 2: Include the current item (if it fits)
    max_value_with_item = 0
    if weights[i] <= remaining_capacity:
        max_value_with_item = values[i] + knapsack(i+1, remaining_capacity-weights[i])

    # Store the maximum value obtained in the memoization table
    memo[i][remaining_capacity] = max(max_value_without_item, max_value_with_item)

    return memo[i][remaining_capacity]

max_value = knapsack(0, M)
print(f"The maximum value that can be obtained is: {max_value}")