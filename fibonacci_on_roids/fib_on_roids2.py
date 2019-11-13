def custom_fib(signature, indexes, n):
    values = list(signature)
    l = len(signature)
    while len(values) <= n: # why not < n ? ### because it could alternately be len(values) + 1 < n. so n would end up equal to lenth of values + 1. it's a stupid index from 1 or 0 thing
        #print('len(values)', len(values))
        values.append(get_next_value(values, indexes, l))
        print(values)
    #print('len(values)', len(values), 'n', n, 'values', values, 'values[n]', values[n])
    return values[n]

def get_next_value(values, indexes, l):
    num = 0
    for index in indexes:
        num += values[-l:][index]
    return num


print(custom_fib([1,1],[0,1],3)) # 3
print(custom_fib([3,5,2],[0,1,2],4)) # 17
print(custom_fib([7,3,4,1],[1,1],6)) # 2
print(custom_fib([3, 0, 9, 7, 7], [4, 1, 2], 1)) #0
