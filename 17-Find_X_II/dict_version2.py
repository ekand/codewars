# first, try to translate it too a loop
def find_x(n):
    find_x_dict = {}
    find_x_dict[0] = 0
    x = 0
    for_loop_dict = {}
    for i in range(1, n+1):
    # okay, what do I want here? I want a dictionary such
    # that, when I enter n, the dict returns the amount
    # by which x would be incremented if the for loop happens
    for_loop_increment(n)





    # def for_loop_result(n):
    #     if n in for_loop_dict:
    #         return for_loop_dict[n]
    #     else:
    #         for i in range(1, n+1):
    #             if (i-1) in find_x_dict:
    #                 x += find_x_dict[i-1] + 3*i
    #             else:
    #                 find_x_dict[i-1] = find_x(i-1)
    #                 x += find_x_dict[i-1] + 3*i
    # for i in range(1, n+1):

    return x

n = 2
print(find_x(n))
