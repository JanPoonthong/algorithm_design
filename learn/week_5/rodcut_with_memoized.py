import sys

sys.setrecursionlimit(100000)


def rodcut():
    prices = sorted([1, 5, 8, 12, 14, 16, 17, 20, 24, 27])
    lengths = [i for i in range(1, len(prices) + 1)]
    count = [0]
    memo = {}

    def calculate(current_length):
        count[0] += 1

        if current_length == 0:
            return 0

        if current_length in memo:
            return memo[current_length]

        else:
            maximum_price = 0
            for j in range(current_length):
                if lengths[j] <= current_length:
                    maximum_price = max(
                        maximum_price,
                        prices[j] + calculate(current_length - lengths[j]),
                    )

        memo[current_length] = maximum_price
        return maximum_price

    result = calculate(len(lengths))
    print(f"Number of recursive calls: {count}")
    return result


print(rodcut())
