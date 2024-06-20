n = int(input())

x = [0] * n


def combination(i):
    if i == n:
        print(x)
    else:
        x[i] = 0
        combination(i+1)
        x[i] = 1
        combination(i+1)


combination(0)
