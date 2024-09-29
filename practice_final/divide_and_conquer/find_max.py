numbers = [9, 6, 4, 7, 10, 14, 8, 11]

def find_max(numbers, low, high):
    if low > high:
        return float("-inf")
    
    if low == high:
        return numbers[low]
    
    mid = (low + high) // 2

    left = numbers[:mid]
    right = numbers[mid:]

    left = find_max(numbers, low, mid)
    right = find_max(numbers, mid + 1, high)

    return max(left, right)


print(find_max(numbers, 0, len(numbers) - 1))