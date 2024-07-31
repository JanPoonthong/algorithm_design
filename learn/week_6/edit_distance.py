def edit_distance():
    first_string = input().rstrip()
    second_string = input().rstrip()
    count = [0]

    def calculate(i, j):
        count[0] += 1

        if i == len(first_string) and j <= len(second_string):
            return len(second_string) - j

        if j == len(second_string) and i <= len(first_string):
            return len(first_string) - i

        if first_string[i] == second_string[j]:
            return calculate(i + 1, j + 1)

        return 1 + min(
            calculate(i, j + 1),  # Insert
            calculate(i + 1, j),  # Delete
            calculate(i + 1, j + 1),  # Replace
        )

    result = calculate(0, 0)
    print(f"Number of recursive calls: {count}")
    return result


print(edit_distance())
