MOD = 2147483647

def mutiply2D(A, B):
    result = [[0, 0], [0, 0]]

    result[0][0] = (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD
    result[0][1] = (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD
    result[1][0] = (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD
    result[1][1] = (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD

    return result

A = [[1, 1], [1, 0]]
B = [[1, 1], [1, 0]]

print(mutiply2D(A, B))