import sys

def read_input():
    lines = []
    for line in sys.stdin:
        file_input = line.split()
        for j in file_input:
            lines.append(int(j))
    return lines

def root(user_input):
    pow_list = []
    for i in user_input:
        pow_list.append("%.4f" % (i**(1 / 2)))
    return pow_list

def main():
    list_of_root = root(read_input())

    for i in range(len(list_of_root) - 1, -1, -1):
        print(list_of_root[i])

main()
