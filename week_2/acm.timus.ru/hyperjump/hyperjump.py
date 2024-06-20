import sys

user_input = list(map(int, sys.stdin))


def kadane(user_input):
    max_global = float("-inf")
    max_current = 0
    for i in range(1, len(user_input)):
        max_current = max_current + user_input[i]
        if max_current > max_global:
            max_global = max_current
        if max_current < 0:
            max_current = 0

    if max_global < 0:
        return 0
    return max_global

print(kadane(user_input))