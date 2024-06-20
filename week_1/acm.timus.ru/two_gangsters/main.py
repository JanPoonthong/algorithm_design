user_input = list(map(int, input().split()))

all_cans = user_input[0] + user_input[1] - 1
print(all_cans - user_input[0], all_cans - user_input[1])
