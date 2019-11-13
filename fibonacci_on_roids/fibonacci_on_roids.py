def custom_fib(signature,indexes,n):
    t = list(signature)
    res = list(t)
    for _ in range(n-(len(signature)-1)):
        #t.append(add_stuff(t[-len(signature):], indexes))
        t.append(add_stuff(t, indexes))
        res.append(t[-1])
        t.pop(0)
        print(t)
    print(res)
    return res[-1]



def add_stuff(arr,inds):
    next_num = 0
    for ind in inds:

        next_num += arr[ind]
    return next_num
#a = add_stuff([1,1],[0,1])
# a = add_stuff([1,1],[0,1])
# print(a)

# a = add_stuff([1,1],[0,1])
# print(a)

print(custom_fib([1,1],[0,1],3)) # 3
print(custom_fib([3,5,2],[0,1,2],4)) # 17
print(custom_fib([7,3,4,1],[1,1],6)) # 2
print(custom_fib([3, 0, 9, 7, 7], [4, 1, 2], 1)) #0


# print(custom_fib([1, 4, 8, 4], [1, 3, 1, 1], 15))


# https://www.codewars.com/kata/5d96030e4a3366001d24b3b7


# def custom_fib(signature, indexes, n):
#     values, l = list(signature), len(signature)
#     while len(values) <= n:
#         values.append(sum(values[-l:][i] for i in indexes))
#     return values[n]
