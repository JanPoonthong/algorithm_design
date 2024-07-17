import sys

sys.setrecursionlimit(10000)

length, max_weight_capacity = map(int, input().split())
weights = list(map(int, input().split()))
values = list(map(int, input().split()))


def knap_sack():
    x = [0] * length
    count = [0]

    def calculate(i):
        count[0] += 1

        if i == length:
            state_weight = state_value = 0
            for j in range(length):
                if x[j] == 1:
                    state_weight += weights[j]
                    state_value += values[j]
            if state_weight > max_weight_capacity:
                return -1
            else:
                return state_value
        else:
            x[i] = 0
            a = calculate(i + 1)
            x[i] = 1
            b = calculate(i + 1)
            return max(a, b)

    result = calculate(0)
    print(f"Number of recursive calls: {count}")
    return result


print(knap_sack())
