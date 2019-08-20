# from kata here: https://www.codewars.com/kata/54e6533c92449cc251001667/solutions/python

def unique_in_order(iterable):
    unique_list = []
    for i, character in enumerate(iterable):
        if i == 0:
            unique_list.append(character)
        else:
            if character != prev:
                unique_list.append(character)
        prev = character
    return unique_list


# solution voted best practices initialized prev before the for
# loop, so it was able to dispense with the enumerate and
# the if else
