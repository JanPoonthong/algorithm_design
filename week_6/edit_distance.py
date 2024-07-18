import sys
sys.setrecursionlimit(10000)

def edit_distance():
    first_word = input().rstrip()
    second_word = input().rstrip()
    count = [0]

    def calculate(str_one, str_two, i, j):
        count[0] += 1

        # Base cases
        if i == len(str_one):
            return len(str_two) - j
        if j == len(str_two):
            return len(str_one) - i

        # If characters are the same, move to the next characters
        if str_one[i] == str_two[j]:
            return calculate(str_one, str_two, i + 1, j + 1)

        # If characters are different, consider all three operations
        return 1 + min(calculate(str_one, str_two, i, j + 1),    # Insert
                       calculate(str_one, str_two, i + 1, j),    # Remove
                       calculate(str_one, str_two, i + 1, j + 1) # Replace
                       )

    result = calculate(first_word, second_word, 0, 0)
    print(f"Number of recursive calls: {count}")
    return result

print(edit_distance())
