# good start

class Shelter:
    """ represents a nuclear shelter

    Attributes:
    hits: string. how many times a bomb has landed near the shelter
    letters: list of strings: the letters in the shelter
    """
    def __init__(self, letters = None, hits = 0):
        if letters == None:
            self.letters = []
        else:
            self.letters = letters
        self.hits = hits

    def __str__(self):
        s = "shelter containing " + str(self.letters) + " with " + str(self.hits) + " hits."
        return s

def alphabet_war(battlefield):
    safe_letters = []
    letters_outside = []
    in_shelter = False
    any_bombs = False
    t = list(battlefield)
    shelters = []
    # print(t)
    for character in t:
        if in_shelter == True:
            if character.isalpha():
                shelters[-1].letters.extend(character)
            elif character == ']':
                in_shelter == False;
        elif character == '[':
            shelter = Shelter()
            shelters.append(shelter)
            in_shelter = True
        elif character.isalpha():
            letters_outside.append(character)
        elif character == '#':
            any_bombs = True;
    bomb_counter = 0
    # for character in t:
    #     if character == '#':
    #         bomb_counter += 1
    #     if character == '[':
    #         shelter.hits += bomb_counter
    #         bomb_counter = 0


    # construct answer
    res = ""
    # for shelter in shelters:
    #     if shelter.hits < 2:
            # res += str(shelter.letters)
    if any_bombs == False:
        res += str(letters_outside)

    res = sorted(res)

    return res



battlefield = '[a]#[b]#[c]'
print(alphabet_war(battlefield))
