import sys

sys.setrecursionlimit(100000)

def minimum_coin_change():
    coin_denominator = sorted([1, 3, 4, 5], reverse=True)
    amount_of_change = 7
    count = [0]

    def calculate(amount_of_change):
        count[0] += 1
        
        if amount_of_change in coin_denominator:
            return 1
        
        minimum_coin_need = amount_of_change

        for c in coin_denominator:
            if c <= amount_of_change:
                minimum_coin_need = min(minimum_coin_need, calculate(amount_of_change-c) + 1)

        return minimum_coin_need
    
    result = calculate(amount_of_change)
    print(f"Number of recursive calls: {count}")
    return result



print(minimum_coin_change())