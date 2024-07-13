def minimum_coin_change():
    coin_denominator = sorted([1, 3, 4, 5], reverse=True)
    amount_of_change = 14
    count = [0]

    # Dictionary to store the results of subproblems
    memo = {}

    def calculate(amount_of_change):
        count[0] += 1
        # Check if result is already computed
        if amount_of_change in memo:
            return memo[amount_of_change]

        # Base cases
        if amount_of_change == 0:
            return 0  # No coins needed
        if amount_of_change < 0:
            return float('inf')  # Invalid path, return a large number
        
        # If amount_of_change is exactly one of the coin denominations
        if amount_of_change in coin_denominator:
            return 1

        # Initialize minimum coins to a large number
        min_coins = float('inf')

        # Recursively calculate the minimum coins needed
        for coin in coin_denominator:
            if coin <= amount_of_change:
                num_coins = calculate(amount_of_change - coin)
                if num_coins != float('inf'):  # Check if the path was valid
                    min_coins = min(min_coins, num_coins + 1)

        # Store the computed result in the memo dictionary
        memo[amount_of_change] = min_coins
        return min_coins

    result = calculate(amount_of_change)
    print(f"Number of recursive calls: {count}")
    return result if result != float('inf') else -1  # Return -1 if change cannot be made

print(minimum_coin_change())
