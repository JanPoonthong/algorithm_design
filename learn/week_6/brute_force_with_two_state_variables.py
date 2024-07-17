import sys

sys.setrecursionlimit(10000)


def brute_force_with_two_state_variables():
    count = [0]
    length, max_weight_capacity = map(int, input().split())
    weights = list(map(int, input().split()))
    values = list(map(int, input().split()))

    def calculate(i, capacity):
        count[0] += 1

        if i == length:
            return 0
        else:
            skip = calculate(i + 1, capacity)
            if weights[i] <= capacity:  # cause different in recursive call
                take = values[i] + calculate(i + 1, capacity - weights[i])
            else:
                take = -1
            return max(skip, take)

    result = calculate(0, max_weight_capacity)
    print(f"Number of recursive calls: {count}")
    return result


print(brute_force_with_two_state_variables())
