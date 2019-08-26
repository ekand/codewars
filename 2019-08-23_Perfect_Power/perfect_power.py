def isPP(n):
    l = []
    for k in range(2, int(n/4 + 5)):
        #print('k', k)
        m = n ** (1/k)
        #print('m', m)
        if abs(m - round(m)) < 0.000000000001:

            l.append(int(m))
            l.append(k)
            return l
    return None



print(isPP(7645373))


# doesn't work for random cases with large numbers
# probably I need a more efficient algorithm
