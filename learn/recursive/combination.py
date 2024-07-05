def com(i):
    if i == input_in:
        print(my_list)
        return
    my_list[i] = 0
    com(i+1)
    my_list[i] = 1
    com(i+1)


input_in = 2
my_list = [0] * input_in
com(0)