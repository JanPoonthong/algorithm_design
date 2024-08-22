def tower(n, a, b, c):
    if n > 0:
        tower(n-1, a, c, b)
        print(f"Moving {a} to {c}")
        tower(n-1, b, a, c)


tower(10, 1, 2, 3)
