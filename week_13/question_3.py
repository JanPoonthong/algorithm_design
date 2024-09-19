def fast_power(base, exponent):
    mod = 2147483647
    result = 1

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % mod

        base = (base * base) % mod
        exponent //= 2

    return result


# Example usage
a = int(input("Enter the base: "))
x = int(input("Enter the exponent: "))
print(fast_power(a, x))
