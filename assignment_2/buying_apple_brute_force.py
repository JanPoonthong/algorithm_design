def buying_apple():
    test_cases = int(input())

    def calculate(n, k, packets):
        def brute_force(index, current_weight, current_cost):
            if current_weight == k:
                return current_cost
            if current_weight > k or index == n:
                return float("inf")

            # Option 1: Skip the current packet
            option1 = brute_force(index + 1, current_weight, current_cost)

            # Option 2: Include the current packet if it is not -1
            option2 = float("inf")
            if packets[index] != -1 and current_weight + index + 1 <= k:
                option2 = brute_force(
                    index, current_weight + index + 1, current_cost + packets[index]
                )

            return min(option1, option2)

        min_cost = brute_force(0, 0, 0)
        return min_cost if min_cost != float("inf") else -1

    a = []
    for _ in range(test_cases):
        n, k = map(int, input().split())
        packets = list(map(int, input().split()))
        a.append(calculate(n, k, packets))

    for i in a:
        print(i)


buying_apple()
