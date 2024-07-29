def min_cost_apples(test_cases):
    results = []
    for case in test_cases:
        N, K = case["N"], case["K"]
        prices = case["prices"]

        dp = [float("inf")] * (K + 1)
        dp[0] = 0

        for kg in range(1, K + 1):  # the kg
            if prices[kg - 1] != -1:
                for j in range(kg, K + 1):  # amount that we are considering
                    remaining = dp[j - kg]
                    if remaining != float("inf"):
                        dp[j] = min(dp[j], remaining + prices[kg - 1])

        result = dp[K] if dp[K] != float("inf") else -1
        results.append(result)

    return results


C = int(input())
test_cases = []

for _ in range(C):
    N, K = map(int, input().split())
    prices = list(map(int, input().split()))
    test_cases.append({"N": N, "K": K, "prices": prices})

results = min_cost_apples(test_cases)

for result in results:
    print(result)
