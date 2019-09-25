# kata found here
# https://www.codewars.com/kata/airport-arrivals-slash-departures-number-1/train/python




def flap_display(lines, rotors):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ?!@#&()|<>.:=-+*/0123456789"
    output = []
    if lines == [None]:
        return [None]

    def next_character(char):
        i = chars.find(char)
        i = (i+1) % len(chars)
        return chars[i]

    def turn_rotors(line, rotor_codes):
        line_list = list(line)
        for k, turns in enumerate(rotor_codes):
            for turn in range(turns):
                for j, char in enumerate(line_list):
                    if j >= k:
                        char = next_character(char)
                        line_list[j] = char
        output = "".join(line_list)
        return output

    for m in range(len(lines)):
        print(lines[m], rotors[m])
        output.append(turn_rotors(lines[m], rotors[m]))
        
    return output

lines = ['CAT']
rotors = [[1, 13, 27]]
print(flap_display(lines, rotors))
