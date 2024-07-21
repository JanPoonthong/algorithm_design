import sys

sys.setrecursionlimit(10000)


def above_pel():
    memo = {}
    generation_above_pel = int(input())
    count = [0]

    def calculate(i, track):
        if (i, track) in memo:
            return memo[(i, track)]

        if i == generation_above_pel:
            if track == "male":
                return 1
            elif track == "female":
                return 2

        if track == "male":
            count[0] = calculate(i + 1, "female")
        elif track == "female":
            count[0] = calculate(i + 1, "male") + calculate(i + 1, "female")

        memo[(i, track)] = count[0]
        return count[0]

    result = calculate(1, "male")
    return result


print(above_pel())
