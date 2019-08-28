def name_in_str(str, name):
    str = str.lower()
    name = name.lower()
    i = 0
    for letter in name:
        found_index = str.find(letter,i)
        if  found_index != -1:
            i = found_index + 1
        else:
            return False
    return True
