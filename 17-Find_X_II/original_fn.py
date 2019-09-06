# optimize
def find_x(n):
    if n == 0: return 0
    x = 0
    for i in range(1, n+1):
        x += find_x(i-1) + 3*i
        print(x)
    return x

# consider the stack

n = 100
print(find_x(n))

"""
try n = 0
find_x(0)
    returns 0 at first line
so find_x(0) = 0



try n = 1
find_x(1)
    the for loop will happen only for i = 1
    for loop, iteration i = 1:
        calls find_x(0) which returns 0
        adds this to 3 * i (i=1), stores it to x (x=3)
    returns x (x = 3)
so find_x(1) = 3

try n = 2
find_x(2)
    the for loop will happen for i = i and i = 2
    for loop, iteration i = 1
        stores x = 3 (see above)
    for loop, iteration i = 2
        calls find_x(1), which returns 3
        adds this to 3*2, resulting in 9
        increments x by 9, resulting in x = 12
so find_x(2) = 12


"""
# I'm having a thought. We could store results of f(n)
# in a dict to reduce duplicate calculations
