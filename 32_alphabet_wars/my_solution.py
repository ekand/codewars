# start fresh

# just a test change


"""
tasks:
identify letters outside of shelters
identify whether any bombs have landed
if no bombs landed, outside letters survive

identify letters in shelters
identify which shelters remain intact
letters in intact shelters survive
"""


def alphabet_war(battlefield):
    b = list(battlefield)
    in_shelter = False;
    any_bombs = False;
    survivors = []
    letters_outside = []
    for character in b: # find outside letters
        if not in_shelter and character.isalpha():
            letters_outside.append(character)
        if character == "[":
            in_shelter = True
        if character == "]":
            in_shelter = False
        if character =="#":
            any_bombs = True
    if not any_bombs:
        survivors.extend(letters_outside)

    shelter_counter = 0
    shelters = []
    for character in b:
        if character == "[":

            in_shelter = True
            shelters.append([])
        elif character == "]":
            in_shelter = False
            shelter_counter+=1
        elif in_shelter:
            shelters[shelter_counter].append(character);
    #print(shelters)


    for current_shelter_i, shelter in enumerate(shelters):
        #print(current_shelter_i, "Current shelter number")
        letters_in_this_shelter = []
        shelter_counter = 0;
        in_shelter = False
        bombs_next_to_shelter = 0
        #print("for character in b:")
        for character in b:
            #print("character", character)
            if character == "#" and (shelter_counter == current_shelter_i or shelter_counter == current_shelter_i + 1):
                bombs_next_to_shelter += 1
                #print('bombs_next_to_shelter', bombs_next_to_shelter)
            elif character == "[":
                in_shelter = True

            elif in_shelter and shelter_counter == current_shelter_i and character.isalpha():
                letters_in_this_shelter.append(character)
            elif character == "]":
                shelter_counter += 1
                in_shelter = False
            #print(letters_in_this_shelter)
        #print(bombs_next_to_shelter, "bombs")
        if bombs_next_to_shelter < 2:
            survivors.extend(letters_in_this_shelter)
    #print("survivors", survivors)
    survive.sort()
    return "".join(survivors)






#battlefield = "abde[fgh]ijk"
battlefield = "##abde[fgh]ijk[mn]op"
print(alphabet_war(battlefield))
