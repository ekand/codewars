"""
working on kata found here
https://www.codewars.com/kata/55983863da40caa2c900004e/train/python

so far have succsesfully completed the simple cases
where swapping two digits is enough
however, there are cases where it is required to
"""
def next_bigger(n):
    #print(n)
    s = str(n)
    n_list = []
    for digit in s:
        n_list.append(int(digit))

    for i in range(len(n_list)):


        try:
            #print(n_list[-i-2],n_list[-i-1])
            if n_list[-i-2] < n_list[-i-1]:
                n_list[-i-2], n_list[-i-1] = n_list[-i-1], n_list[-i-2]
                break
        except:
            return -1
    s = ""
    for digit in n_list:
        s = s + str(digit)
    n = int(s)
    return(n)

n = 12
print('n =', n, 'result:', next_bigger(n))
n = 513
print('n =', n, 'result:', next_bigger(n))
n = 2017
print('n =', n, 'result:', next_bigger(n))
n = 9
print('n =', n, 'result:', next_bigger(n))
n = 123456789
print('n =', n, 'result:', next_bigger(n))
n = 1234567890
print('n =', n, 'result:', next_bigger(n))
print('but it should = 1234567908')
n = 59884848459853
print('n =', n, 'result:', next_bigger(n))
print('but it should = 59884848483559')
