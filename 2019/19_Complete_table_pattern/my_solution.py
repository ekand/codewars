# my solution to kata found here
# https://www.codewars.com/kata/complete-the-table-pattern/train/python

def add_bar(result, columns):
    result += "+"
    for i in range(columns):
        result += "---+"
    return result

def add_row(result, columns, t):
    result += "|"
    for i in range(columns):
        try:
            a = t.pop(0)
        except:
            a = " "
        result = result + " " + a + " "
        result += "|"
    return result, t

def pattern(row, columns, s):
    result = ""
    t = list(s)
    for i in range(row):
        result = add_bar(result, columns)
        result += ("\n")
        result, t = add_row(result, columns, t)
        result += ("\n")
    result = add_bar(result, columns)

    return result


print(pattern(4, 4, "Hello World!"))
print("")
print(pattern(3, 3, "codewars"))
print("")
print(pattern(3, 4, "Nice pattern"))
