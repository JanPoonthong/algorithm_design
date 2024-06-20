import time

user_input = list(map(int, input().split()))


def my_sum(x, i, j):
    s = x[j]
    if i > 0:
        s -= x[i - 1]
    return s


for i in range(1, len(user_input)):
    user_input[i] += user_input[i - 1]

start = time.process_time()
current_max = 0
for i in range(1, len(user_input)):
    for j in range(i, len(user_input)):
        result = my_sum(user_input, i, j)
        if result > current_max:
            current_max = result
end = time.process_time()

print(current_max)
print("Running time: ", end - start)
