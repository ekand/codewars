def custom_fib(signature, indexes, n):
    values, l = list(signature), len(signature)
    print(values)
    print(signature)
    while len(values) <= n:
        values.append(sum(values[-l:][i] for i in indexes))
    return values[n]


signature, indexes, n = [3,5,2],[0,1,2],4

print(custom_fib(signature, indexes, n))
