n = int(input())
x = [0] * n


def combination(i):
    if i == n:
        print(x)
        return 1
    else:
        s = 0
        for a in [0, 1, 2]:
            x[i] = a
            s += combination(i + 1)
        return s


print(combination(0))
