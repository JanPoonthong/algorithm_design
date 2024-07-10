n = int(input())

x = [0] * n


def comb(i):
    if i == n:
        return 1
    count = 0
    x[i] = 0
    count += comb(i + 1)
    x[i] = 1
    count += comb(i + 1)
    return count


print(comb(0))
