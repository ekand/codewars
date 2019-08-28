def get_middle(s):
    while len(s) > 2:
        s = get_middle(s[1:-1])
    return s
