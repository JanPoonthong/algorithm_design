
from collections import Counter

count = 0
def prime_factors(n):
    global count
    i = 2
    factors = Counter()

    while i * i <= n:
        while (n % i) == 0:
            count += 1
            factors[i] += 1
            n //= i

        i += 1

    if n > 1:
        factors[n] += 1
    return factors


print(prime_factors(84))
print(count)