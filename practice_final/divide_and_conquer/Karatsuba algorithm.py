# Importing required module
import math


def addBinary(a, b):
    a_bigint = int(a, 2)
    b_bigint = int(b, 2)
    result = bin(a_bigint + b_bigint)[2:]
    return result


def shiftLeft(string, n):
    return string + "0" * n


def classicalMultiply(str1, str2):
    result = "0"
    n = len(str2)
    for i in range(n):
        if str2[n - 1 - i] == "1":
            result = addBinary(result, shiftLeft(str1, i))
    return result


def karatsubaMultiply(X, Y):
    n = max(len(X), len(Y))

    # Make the lengths equal
    X = X.rjust(n, "0")
    Y = Y.rjust(n, "0")

    if n == 1:
        return bin(int(X, 2) * int(Y, 2))[2:]

    m = n // 2

    Xl = X[:m]
    Xr = X[m:]
    Yl = Y[:m]
    Yr = Y[m:]

    P1 = karatsubaMultiply(Xl, Yl)
    P2 = karatsubaMultiply(Xr, Yr)
    P3 = karatsubaMultiply(addBinary(Xl, Xr), addBinary(Yl, Yr))

    C1 = shiftLeft(P1, 2 * (n - m))
    C2 = shiftLeft(addBinary(subtractBinary(P3, addBinary(P1, P2)), P2), n - m)

    return addBinary(addBinary(C1, C2), P2)


def subtractBinary(a, b):
    a_bigint = int(a, 2)
    b_bigint = int(b, 2)
    result = bin(a_bigint - b_bigint & (2 ** (max(len(a), len(b))) - 1))[2:]
    return result


if __name__ == "__main__":
    # Given binary numbers
    first_number = "011011010100"
    second_number = "10111010111"

    # Classical Algorithm
    print("Classical Algorithm:")
    classic_result = classicalMultiply(first_number, second_number)
    print("Binary Result:", classic_result)
    print("Decimal Result:", int(classic_result, 2))

    # Karatsuba Algorithm
    print("\nKaratsuba Algorithm:")
    karatsuba_result = karatsubaMultiply(first_number, second_number)
    print("Binary Result:", karatsuba_result)
    print("Decimal Result:", int(karatsuba_result, 2))
