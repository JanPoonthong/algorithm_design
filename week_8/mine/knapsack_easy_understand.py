import time
# Input values
N, M = map(int, input("Enter the number of items and the knapsack capacity: ").split())
weights = list(map(int, input("Enter the weights of the items: ").split()))
values = list(map(int, input("Enter the values of the items: ").split()))

# Initialize the dp table with zeros
dp = [[0] * (M + 1) for _ in range(N + 1)]

start = time.process_time()
# Fill the dp table iteratively
for i in range(1, N + 1):  # Loop over all items
    for capacity in range(1, M + 1):  # Loop over all possible capacities
        if weights[i - 1] <= capacity:  # If the item fits into the knapsack
            # Option 1: Take the item and add its value to the optimal solution without this item's weight
            dp[i][capacity] = max(dp[i - 1][capacity], values[i - 1] + dp[i - 1][capacity - weights[i - 1]])
        else:
            # Option 2: Skip the item
            dp[i][capacity] = dp[i - 1][capacity]
end = time.process_time()
print(f"Time {end - start}")

# The final result is the maximum value for all items with full capacity
print(f"The maximum value that can be obtained is: {dp[N][M]}")

# check this to understand the code: https://www.youtube.com/watch?v=nLmhmB6NzcM