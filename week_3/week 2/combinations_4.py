n = int(input())
k = int(input())

x = [0] * n


def combination(i):
    if i == n:
        print(x)
    else:
        for a in [0, 1, 2]:
            x[i] = a
            combination(i+1)


print(combination(0))
