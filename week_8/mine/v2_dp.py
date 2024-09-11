import time

N, M = map(int, input().split())
weights = list(map(int, input().split()))
values = list(map(int, input().split()))

dp = [[0] * (M+1) for _ in range(N+1)]

start = time.process_time()

for i in range(N-1, -1, -1):
    for capacity in range(M+1):
        # Option 1: Skip the item
        max_value_without_item = dp[i+1][capacity]

        # Option 2: Take the item (if it fits)
        max_value_with_item = 0
        if weights[i] <= capacity:
            max_value_with_item = values[i] + dp[i+1][capacity - weights[i]]

        # Store the maximum value in the dp table
        dp[i][capacity] = max(max_value_without_item, max_value_with_item)

end = time.process_time()
print(f"Time {end - start}")

# The final result is the maximum value for all items with full capacity
print(f"The maximum value that can be obtained is: {dp[0][M]}")