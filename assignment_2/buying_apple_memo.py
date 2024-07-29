import sys

sys.setrecursionlimit(10000)

test_cases = int(input())
memo = {}


def hepler():
    n, k = input().split()
    n = int(n)
    k = int(k)
    packets = list(map(int, input().split(" ")))

    def brute_force(index, current_weight, current_cost):
        if (n, k) in memo:
            return memo[(n, k)]

        if current_weight == k:
            return current_cost
        if current_weight > k or index == n:
            return 100000000

        # Option 1: Skip the current packet
        option1 = brute_force(index + 1, current_weight, current_cost)

        # Option 2: Include the current packet if it is not -1
        option2 = 100000000
        if packets[index] != -1 and current_weight + index + 1 <= k:
            option2 = brute_force(
                index, current_weight + index + 1, current_cost + packets[index]
            )

        memo[(n, k)] = min(option1, option2)
        return memo[(n, k)]

    return brute_force(0, 0, 0)


a = []
for _ in range(test_cases):
    val = hepler()
    a.append(val)
    # if val == 100000000:
    #     print(-1)
    # else:
    #     print(val)

for i in a:
    if i == 100000000:
        print(-1)
    else:
        print(i)
