import sys

sys.setrecursionlimit(10000)


def minimal_difference_memoized(values):
    n = len(values)
    total_sum = sum(values)
    memo = {}
    call_count = [0]

    def com(i, sum_one, sum_two):
        call_count[0] += 1
        if i == n:
            return abs(sum_one - sum_two)

        a = com(i + 1, sum_one + values[i], sum_two)
        b = com(i + 1, sum_one, sum_two + values[i])
        return min(a, b)

    min_diff = com(0, 0, 0)
    print(f"Number of recursive calls: {call_count[0]}")
    return min_diff


values = [5, 8, 13, 27, 14]
print(minimal_difference_memoized(values))
