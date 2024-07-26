def buying_apple():
    test_cases = int(input())

    def calculate(i, weight):
        dp = [[0] * (k+1) for _ in range(k+1)]

        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i == 0 or j == 0:
                    continue
                else:
                    if packets[j-1] == -1:
                        dp[i][j] = -1
                    elif packets[j-1] != -1:
                        dp[i][j] = packets[i-1]
        
        return dp[len(dp)-1][len(dp[0])-1]

    for _ in range(test_cases):
        n, k = list(map(int, input().split()))
        packets = list(map(int, input().split()))
        x = [0] * len(packets)
        print(calculate(0, k))

    # return calculate(0, k)

buying_apple()
