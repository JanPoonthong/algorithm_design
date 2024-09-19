MOD = 2147483647


def multiply2D(A, B):
    result = [[0, 0], [0, 0]]

    result[0][0] = ((A[0][0] * B[0][0]) % MOD + (A[0][1] * B[1][0]) % MOD) % MOD
    result[0][1] = ((A[0][0] * B[0][1]) % MOD + (A[0][1] * B[1][1]) % MOD) % MOD
    result[1][0] = ((A[1][0] * B[0][0]) % MOD + (A[1][1] * B[1][0]) % MOD) % MOD
    result[1][1] = ((A[1][0] * B[0][1]) % MOD + (A[1][1] * B[1][1]) % MOD) % MOD

    return result


def matrix_power(M, n):
    if n == 0:
        return [[1, 0], [0, 1]]
    else:
        Mhalf = matrix_power(M, n // 2)
        if n % 2 == 0:
            return multiply2D(Mhalf, Mhalf)
        else:
            return multiply2D(M, multiply2D(Mhalf, Mhalf))


n = int(input())
M = [[1, 1], [1, 0]]

if n <= 1:
    print(1)
else:
    A = matrix_power(M, n - 1)
    print((A[0][0] + A[0][1]) % MOD)
