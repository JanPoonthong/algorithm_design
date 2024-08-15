def getNoOfWays(n):
    # Base case
    if n <= 2:
        return n

    return getNoOfWays(n - 1) + getNoOfWays(n - 2)


# Driver Code
print(getNoOfWays(3))
print(getNoOfWays(4))
