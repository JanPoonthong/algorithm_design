n = int(input())

x = [0] * n


def comb(i):
    if i == n:
        print(x)
        return 1
    else:
        x[i] = 0
        s = comb(i + 1)
        x[i] = 1
        s += comb(i + 1)
        return s


print(comb(0))
