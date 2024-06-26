import sys

sys.setrecursionlimit(10000)

n_list = list(map(int, input().split()))


def b_split(nums, i, sum1, sum2):
    if i == len(nums):
        return abs(sum1 - sum2)
    include = b_split(nums, i + 1, sum1 + nums[i], sum2)
    exclude = b_split(nums, i + 1, sum1, sum2 + nums[i])
    return min(include, exclude)


print(b_split(n_list, 0, 0, 0))
