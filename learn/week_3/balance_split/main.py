import sys

sys.setrecursionlimit(10000)

INPUT_IN = [5, 8, 13, 27, 14]

def com(i, sum_one, sum_two):
    if i == len(INPUT_IN):
        return abs(sum_one - sum_two)
    else:
        a = com(i+1, sum_one+INPUT_IN[i], sum_two)
        b = com(i+1, sum_one, sum_two+INPUT_IN[i])
    
    return min(a, b)


print(com(0, 0, 0))
