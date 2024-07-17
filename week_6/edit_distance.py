import sys

sys.setrecursionlimit(10000)


def edit_distance():
    first_word = input().rstrip()
    second_word = input().rstrip()
    count = [0]

    def calculate(str_one, str_two, m, n):
        count[0] += 1

        if m == 0:
            return n

        if n == 0:
            return m

        if str_one[m - 1] == str_two[n - 1]:
            return calculate(str_one, str_two, m - 1, n - 1)

        return 1 + min(
            calculate(str_one, str_two, m, n - 1),  # Insert
            calculate(str_one, str_two, m - 1, n),  # Remove
            calculate(str_one, str_two, m - 1, n - 1),  # Replace
        )

    result = calculate(first_word, second_word, len(first_word), len(second_word))
    print(f"Number of recursive calls: {count}")
    return result


print(edit_distance())
