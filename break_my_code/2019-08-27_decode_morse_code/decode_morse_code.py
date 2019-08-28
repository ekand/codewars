# my solution to kata found here:
# https://www.codewars.com/kata/54b724efac3d5402db00065e/solutions/python

def decodeMorse(morse_code):
    morse_code = morse_code.strip()
    morse_code = morse_code.replace('   ', ' * ')

    plain_text = []
    character_codes = morse_code.split()
    for character_code in character_codes:
        if character_code == '*':
            character = ' '
        else:
            for key in MORSE_CODE.keys():
                if character_code == key:
                    character = MORSE_CODE[key]
        plain_text.append(character)
    s_out = "".join(plain_text)

    return s_out
