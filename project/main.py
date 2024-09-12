import sys
from collections import Counter

numbers = [int(sys.stdin.readline().strip()) for _ in range(10)]

def prime_factors(n):
    i = 2
    factors = Counter()

    while i * i <= n:
        while (n % i) == 0:
            factors[i] += 1
            n //= i

        i += 1

    if n > 1:
        factors[n] += 1
    return factors


total_exponents = Counter()

for number in numbers:
    factors = prime_factors(number)
    total_exponents.update(factors)

total = 1
for base, expo in total_exponents.items():
    total *= expo + 1

print(total % 10)
