def queue_time(customers, n):
    res = 0
    customers = list(customers)
    tills = []
    for i in range(n):
        tills.append(0)
    while customers or any([t != 0 for t in tills]):
        for i, t in enumerate(tills):
            if t == 0 and customers:
                #print(customers)
                tills[i] = customers.pop(0)
        for i, t in enumerate(tills):
            if t:
                #print(type(tills[i]))
                tills[i] = tills[i] - 1
        res += 1


    return res

asdf = 1, 2
# print(queue_time(([], 1), 0))

print(queue_time([5], 1))
#
print(queue_time([2], 5))
#
print(queue_time(asdf))



# took 952ms on codewars
