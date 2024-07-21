def harvester(n):
    if n in memo:
        return memo[n]
    if n == 1 :
        return 1
    if n == 2: 
        return 2
    else:
        # 1 is male and 2 is female
        memo[n] = harvester(n-1) + harvester(n-2)
        return memo[n]

generation = 28
memo = {}
print(harvester(generation))