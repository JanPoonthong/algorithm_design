import sys

sys.setrecursionlimit(10000)

INPUT_IN = 2
my_list = [0] * INPUT_IN


def com(i):
    if i == INPUT_IN:
        print(my_list)
        return 1
    my_list[i] = 0
    count = com(i + 1)
    my_list[i] = 1
    count += com(i + 1)
    return count


print("Count:", com(0))
