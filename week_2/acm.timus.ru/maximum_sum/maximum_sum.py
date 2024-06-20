row = int(input())
user_input = []
for i in range(row):
    user_input.append(list(map(int, input().split())))


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


max_global = float("-inf")
running_row_sum = [0] * len(user_input)
for run in range(len(user_input[0])):
    running_row_sum = [0] * len(user_input)
    for l in range(run, len(user_input[0])):
        for r in range(len(user_input)):
            current_number = user_input[r][l]
            running_row_sum[r] += current_number
        best_max_sub_list = kadane(running_row_sum)
        if best_max_sub_list > max_global:
            max_global = best_max_sub_list

print(max_global)