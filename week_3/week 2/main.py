import sys

sys.setrecursionlimit(10000)


def f(x):
    if x <= 0:
        print("done")
        return 1
    else:
        y = f(x-1)+1
        print(y)
        return y

# x = int(input())
print(f(5))
