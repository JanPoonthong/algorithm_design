import KnapsackBound

class obj:
    def __init__(self, w, v):
        self.w = w
        self.v = v
        self.r = v / w

# Read input
x = input().split()
N = int(x[0])
M = int(x[1])
w = input().split()
v = input().split()

# Create list of items
item = []
for i in range(N):
    item.append(obj(int(w[i]), int(v[i])))

# Sort items by value-to-weight ratio
item.sort(key=lambda x: x.r, reverse=True)

# Initialize global variables
maxV = 0  # Maximum value found
num_calls = 0  # Number of recursive calls

def dfs(i, sumW, sumV):
    global maxV, item, N, M, num_calls

    # Count the number of recursive calls
    num_calls += 1

    # If weight exceeds capacity, prune this branch
    if sumW > M:
        return

    # Use the bound to prune the search space, passing 'item' and 'N'
    bound = sumV + KnapsackBound.Bound(i, M - sumW, item, N)
    if bound <= maxV:
        return  # Prune if bound is worse than current best

    # If all items have been considered, update maxV
    if i == N:
        if sumW <= M:
            maxV = max(maxV, sumV)
    else:
        # Explore both options: skip the item or take the item
        dfs(i + 1, sumW, sumV)  # Skip the item
        dfs(i + 1, sumW + item[i].w, sumV + item[i].v)  # Take the item

# Run DFS starting from the first item
dfs(0, 0, 0)

# Output the result
print("Maximum value:", maxV)
print("Total recursive calls:", num_calls)
