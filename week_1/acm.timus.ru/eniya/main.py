def multiply_list(input_list):
    result = 1
    for i in input_list:
        result *= i
    return result

user_input = list(map(int, input().split()))
print(multiply_list(user_input) * 2)
