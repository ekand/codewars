# first, try to translate it too a loop
def find_x(n):
    if n == 0: return 0
    x = 0
    find_x_dict = {}
    find_x_dict[0] = 0
    #find_x_dict[1] = 3
    #find_x_dict[2] = 12
    for i in range(1, n+1):
        if (i-1) in find_x_dict:
            x += find_x_dict[i-1] + 3*i
        else:
            find_x_dict[i-1] = find_x(i-1)
            x += find_x_dict[i-1] + 3*i
    return x

n = 1
print(find_x(n))

# this is an improvement, but it still calls the
# for loop with adding 3*i too many times
