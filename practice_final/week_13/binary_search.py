
# arr = [-5, 0, 3, 7, 9, 12, 16, 19]
# target = 9

arr = [-5, 0, 3, 7, 9, 12, 16, 19]
target = 6


def binary_search(arr, low, high, target):
    if low > high:
        return -1
    
    mid_point = (low + high) // 2
    
    if arr[mid_point] == target:
        return mid_point
    elif arr[mid_point] > target:
        return binary_search(arr, low, mid_point - 1, target)
    else:
        return binary_search(arr, mid_point + 1, high, target)
    

def main():
    if len(arr) == 0:
        return None
    else:
        print(binary_search(arr, 0, len(arr) - 1, target))

main()