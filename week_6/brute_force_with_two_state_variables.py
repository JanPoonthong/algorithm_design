import sys
sys.setrecursionlimit(10000)

length, max_weight_capacity = map(int, input().split())
weights = list(map(int, input().split()))
values = list(map(int, input().split()))

def brute_force_with_two_state_variables():

    def calculate(i, capacity):
        if i == length:
            return 0
        else:
            skip = calculate(i+1, capacity)
            if weights[i] <= capacity:
                take = values[i] + calculate(i+1, capacity-weights[i])
            else:
                take = -1
            return max(skip, take)
    
    return calculate(0, max_weight_capacity)

print(brute_force_with_two_state_variables())