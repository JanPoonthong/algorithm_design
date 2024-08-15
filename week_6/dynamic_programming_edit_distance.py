import sys

sys.setrecursionlimit(10000)


def dynamic_edit_distance():
    first_word = input().rstrip()
    second_word = input().rstrip()
    dynamic = [
        [None] * (len(second_word) + 1) for _ in range(len(first_word) + 1)
    ]

    def calculate():
        for i in range(len(dynamic)):
            for j in range(len(dynamic[0])):
                if i == 0:
                    dynamic[i][j] = j
                elif j == 0:
                    dynamic[i][j] = i
                else:
                    if first_word[i - 1] == second_word[j - 1]:
                        dynamic[i][j] = dynamic[i - 1][j - 1]
                    else:
                        replace = 1 + dynamic[i - 1][j - 1]
                        delete = 1 + dynamic[i - 1][j]
                        insert = 1 + dynamic[i][j - 1]
                        dynamic[i][j] = min(replace, delete, insert)
        return dynamic[len(dynamic) - 1][len(dynamic[0]) - 1]

    result = calculate()
    return result


print(dynamic_edit_distance())
