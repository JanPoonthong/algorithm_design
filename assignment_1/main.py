import sys
sys.setrecursionlimit(10000)

def above_pel():
    memo = {"male": 1, "female": 2}
    # generation_above_pel = input()
    generation_above_pel = 29
    count_harvesters = [0]

    def calculate(i, track):
        if i == generation_above_pel:
            count_harvesters[0] += 1
            return

        if track == "female":
            count_harvesters[0] += 2
            track = "male"
        elif track == "male":
            # count_harvesters[0] += 1
            track = "female"

        return calculate(i+1, track)

    result = calculate(0, "male")
    return count_harvesters[0]


print(above_pel())
