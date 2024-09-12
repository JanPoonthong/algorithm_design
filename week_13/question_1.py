a = int(input())
x = int(input())
mod = 2147483647

def compute_power(a, x):
    result = 1
    for _ in range(x):
        result = (result * a) % mod
    return result


print(compute_power(a, x))
