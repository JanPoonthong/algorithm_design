import sys

sys.setrecursionlimit(10000)

INPUT_IN = 3
my_list = [0] * INPUT_IN
# How many ones are there, count them
# 2 mean is there ones two times?
# 3 mean is there ones three times? -> all [1, 1, 1]
k = 3

def com(i, count_ones):
    if i == INPUT_IN:
        print(my_list)
        if count_ones == k:
            return 1
        else:
            return 0
    my_list[i] = 0
    count = com(i+1, count_ones)
    my_list[i] = 1
    count += com(i+1, count_ones+1)
    return count


print(com(0, 0))
