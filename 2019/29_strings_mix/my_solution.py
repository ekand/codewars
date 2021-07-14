# solution to kata found here:
# https://www.codewars.com/kata/5629db57620258aa9d000014/train/python


from collections import Counter


def sort_frequency_list(frequency_list):
    frequency_list.sort(reverse = True)
    max = frequency_list[0][0]
    new_list_2 = []
    for i in range(max, 1, -1):
        new_list = []
        #print('i', i)
        for frequency_entry in frequency_list:
            #print('frequency_entry', frequency_entry)
            if frequency_entry[0] == i:
                new_list.append(frequency_entry[2])
                print(new_list)
            #print(new_list)
        print(new_list)
        new_list.sort()
        new_list_2.extend(new_list)
        print(new_list_2)
    return new_list_2

# def sort_my_list(my_list):
#     print(my_list)
#
#
#     return my_list

def mix(s1, s2):
    # print(Counter(s1))
    # print(Counter(s2))
    d = {}
    for character_1, frequency_1 in Counter(s1).items():
        for character_2, frequency_2 in Counter(s2).items():
            if character_1 == character_2 and character_1.isalpha() and character_1.islower():
                if frequency_1 == frequency_2 and frequency_1 > 1:
                    d[character_1] = (frequency_1, character_1, '=:' + character_1 * frequency_1)
                elif frequency_1 > frequency_2 and frequency_1 > 1:
                    d[character_1] = (frequency_1, character_1, '1:' + character_1 * frequency_1)
                elif frequency_1 < frequency_2 and frequency_2 > 1:
                    d[character_2] = (frequency_2, character_2, '2:' + character_2 * frequency_2)
    print(d)
    frequency_list = list(d.values())
    frequency_list.sort(reverse = True)
    my_list = sort_frequency_list(frequency_list)

    #print(frequency_list)
    #print(frequency_list)
    #return frequency_list
    #my_list = [entry[2] for entry in frequency_list]
    # my_list = sort_my_list(my_list)
    #print(my_list)
    result = "/".join(my_list)
    return result

string = ("Are they here", "yes, they are here")
string = ("looping is fun but dangerous", "less dangerous than coding")
string = ("Lords of the Fallen", "gamekult")
print('Final: ' + mix(*string))

#print(mix("looping is fun but dangerous", "less dangerous than coding"))

### on 2019-10-24
### almost solved, but didn't account for the case where a letter only appears
### in one of the two strings. Not sure how to incorporate that...
