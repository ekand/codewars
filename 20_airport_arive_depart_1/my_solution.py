def flap_display(lines, rotors):
    output = lines
    print("lines", lines)
    print("rotors", rotors)
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ?!@#&()|<>.:=-+*/0123456789"
    chars_length = len(chars)
    display_list = list(lines[0])
    print("starting display list: ", display_list)

    def next_character(char):
        i = chars.find(char)
        i = (i+1) % chars_length
        return chars[i]

    for k, turns in enumerate(rotors[0]):
        # print(k, turns)
        for turn in range(turns):
            # print("turn", turn)
            for j, char in enumerate(display_list):
                #print(j, char)
                if j >= k:
                    #for _ in range(1):

                        #print(_)
                    char = next_character(char)
                    display_list[j] = char
                    # print(range(turn+1))
                    # print(display_list)


            output = "".join(display_list)


    return [output]

        
