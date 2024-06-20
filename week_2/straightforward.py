import time

user_input = list(map(int, input().split()))


def my_sum(x, i, j):
    s = 0
    for k in range(i, j + 1):
        s += x[k]
    return s


start = time.process_time()
current_max = 0
max_con_list = []
for i in range(len(user_input)):
    for j in range(len(user_input)):
        result = my_sum(user_input, i, j)
        if result > current_max:
            current_max = result
            max_con_list = user_input[i : j + 1]
end = time.process_time()

print(max_con_list)
print(current_max)
print("Running time: ", end - start)
