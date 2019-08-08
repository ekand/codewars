# solution to the kata "Isograms"
# https://www.codewars.com/kata/54ba84be607a92aa900000f1/solutions/python
# 2019-08-07

def is_isogram(string):
    result = False
    string = string.lower()
    my_list = []
    for character in string:
        if character in my_list:
            return False
        my_list.append(character)
    return True
