def smallest(n):
    # rough plan: find smallest digit in number (d at index i)
    # take it out, add it to the beginning of the number
    # I realize this won't work in all cases, but I still want to try it to get a feel for
    # the challenge
    # to find smallest digit in number, need to have number as a list of integers

    # create a list of the digits in the integer n
    n_list = []
    n_string = str(n)
    for character in n_string:
        n_list.append(int(character))

    # find index of smallest digit, then insert it at position 0
    i = n_list.index(min(n_list))
    d = n_list.pop(i)
    n_list.insert(0, d)
    print(n_list)

    # convert n_list into an integer, n
    n_string = ''
    for digit in n_list:
        n_string = n_string + str(digit)
    n = int(n_string)

    # return a list of n, i , (j = 0)
    return [n, i, 0]
