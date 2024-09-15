import math

count = 0
def find_divisors(n):
    global count
    divisors = set()  # Use a set to avoid duplicate divisors
    for i in range(1, int(math.sqrt(n)) + 1):
        count += 1
        if n % i == 0:
            divisors.add(i)  # i is a divisor
            divisors.add(n // i)  # n // i is also a divisor
    return sorted(divisors)  # Return sorted list of divisors

# Example usage
number = 84
print("Positive divisors of", number, "are:", find_divisors(number))
print(count)
