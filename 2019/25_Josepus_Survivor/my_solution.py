def josephus_survivor(n,k):
    my_array = list(range(1, n+1))
    # print(my_array)
    i = 0
    while len(my_array) > 1:
        length = len(my_array)
        # print(my_array)
        # print(length)
        # print('i', i)
        while not i < length:
            i -= length
        i += k - 1
        while not i < length:
            i -= length
        # print(my_array)
        # print('length', length)
        # print('i', i)
        _ = my_array.pop(i)
        # print('pop out', _)
        # print(my_array)

        # print()


        # if i < length:
        #     i += k
        #     if i >= length:
        #         i -= length
        #     result = my_array.pop(i)
        #     print(result)
        #     print(my_array)
        # if i > length -1:
        #     i -= length
        # # print('result', result)
    return my_array[0]


# n, k = (7,3) # 4 expected
# print (josephus_survivor(n, k))

n, k = (11,19) # 10 expected
print (josephus_survivor(n, k))
