n = int(input())
k = int(input())

x = [0] * n


def combination(i, count_ones):
    if i == n:
        if sum(x) == k:
            return 1
        else:
            return 0
    else:
        x[i] = 0
        s = combination(i + 1)
        x[i] = 1
        s += combination(i + 1)
        return s


print(combination(0))
