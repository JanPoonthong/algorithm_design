import sys
import math
from functools import reduce
from collections import Counter


def count_divisors(num):
    divisors = set()
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            divisors.add(i)
            divisors.add(num // i)
    return len(divisors)


def get_last_digit_of_divisors_count(nums):
    # Calculate the product of all integers
    product = reduce(lambda x, y: x * y, nums)
    print(product)

    # Count the number of positive divisors of the product
    num_divisors = count_divisors(product)

    # Return the last digit of the number of divisors
    return num_divisors % 10


# Example usage
a = [int(sys.stdin.readline().strip()) for _ in range(10)]
# Replace with actual input
print(
    "The last digit of the number of divisors is:",
    get_last_digit_of_divisors_count(a),
)
