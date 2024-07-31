import time

user_input = list(map(int, input().split()))

# The find maximum profit in a list
def kadane(user_input):
    max_global = float("-inf")
    max_current = 0
    for i in range(len(user_input)):
        max_current += user_input[i]
        if max_current > max_global:
            max_global = max_current
        if max_current < 0:
            max_current = 0
    return max_global


start = time.process_time()
print(kadane(user_input))
end = time.process_time()
print("Running time: ", end - start)
