def getNoOfWays(n):
    # Base case
    if n < 4:
        return 1

    return getNoOfWays(n - 1) + getNoOfWays(n - 4)


# Driver Code
print(getNoOfWays(7))
print(getNoOfWays(4))

# https://youtu.be/EhjU_X7Src0
