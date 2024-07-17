"setrecursionlimit"
import sys

sys.setrecursionlimit(10000)

INPUT_IN = 2
my_list = [0] * INPUT_IN


def com(i):
    "combination with more option"

    if i == INPUT_IN:
        print(my_list)
        return 1

    count = 0
    for j in [0, 1, 2]:
        my_list[i] = j
        count += com(i + 1)
    return count


print(com(0))
