import sys
sys.setrecursionlimit(10000)

def above_pel():
    memo = {}
    # generation_above_pel = input()
    generation_above_pel = 3
    count = [0]
    # {3: 3, 4: 5, 5: 8, 6: 13, 7: 21, 8: 34, 9: 55, 10: 89, 11: 144}


    def calculate(i, track):

        if i in memo:
            return memo[i]

        if i == generation_above_pel:
            if track == "male":
                return 1
            elif track == "female":
                return 2
        
        if track == "male":
            count[0] = calculate(i+1, "female")
        elif track == "female":
            count[0] = calculate(i+1, "male") + calculate(i+1, "female")

        memo[i] = count[0]
        return count[0]

    result = calculate(1, "male")
    return result


print(above_pel())
