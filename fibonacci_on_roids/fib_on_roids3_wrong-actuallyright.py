def custom_fib(signature, indexes, n):
    t = list(signature)
    for _ in range(n-(len(signature)-1)):
        t.append(get_next_element(t, indexes))
        t.pop(0)
        print(t)
    print(t)
    return t[-1]

def get_next_element(t, indexes):
    num = 0
    for index in indexes:
        num += t[index]
    return num


print(custom_fib([1,1],[0,1],3)) # 3
print(custom_fib([3,5,2],[0,1,2],4)) # 17
print(custom_fib([7,3,4,1],[1,1],6)) # 2
print(custom_fib([3, 0, 9, 7, 7], [4, 1, 2], 1)) #0
