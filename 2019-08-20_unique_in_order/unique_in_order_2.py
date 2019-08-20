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
