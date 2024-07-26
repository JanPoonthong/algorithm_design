def min_cost_apples(test_cases):
    results = []
    for case in test_cases:
        N, K = case['N'], case['K']
        prices = case['prices']
        
        # Initialize dp array
        dp = [float('inf')] * (K + 1)
        dp[0] = 0  # Cost to buy 0 kg is 0

        # Fill dp array
        for i in range(1, K + 1):
            if prices[i - 1] != -1:  # Prices are 1-based, hence prices[i-1]
                for j in range(i, K + 1):
                    if dp[j - i] != float('inf'):
                        dp[j] = min(dp[j], dp[j - i] + prices[i - 1])

        # Result for this test case
        result = dp[K] if dp[K] != float('inf') else -1
        results.append(result)
    
    return results

# Read input
C = int(input())
test_cases = []

for _ in range(C):
    N, K = map(int, input().split())
    prices = list(map(int, input().split()))
    test_cases.append({'N': N, 'K': K, 'prices': prices})

# Get results
results = min_cost_apples(test_cases)

# Print results
for result in results:
    print(result)
