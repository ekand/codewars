"""
attempt two at kata found here
https://www.codewars.com/kata/the-road-kill-detective/train/python
"""

def road_kill(photo):
    ANIMALS = ['aardvark', 'alligator', 'armadillo', 'antelope', 'baboon', 'bear', 'bobcat', 'butterfly', 'cat', 'camel', 'cow', 'chameleon', 'dog', 'dolphin', 'duck', 'dragonfly', 'eagle', 'elephant', 'emu', 'echidna', 'fish', 'frog', 'flamingo', 'fox', 'goat', 'giraffe', 'gibbon', 'gecko', 'hyena', 'hippopotamus', 'horse', 'hamster', 'insect', 'impala', 'iguana', 'ibis', 'jackal', 'jaguar', 'jellyfish', 'kangaroo', 'kiwi', 'koala', 'killerwhale', 'lemur', 'leopard', 'llama', 'lion', 'monkey', 'mouse', 'moose', 'meercat', 'numbat', 'newt', 'ostrich', 'otter', 'octopus', 'orangutan', 'penguin', 'panther', 'parrot', 'pig', 'quail', 'quokka', 'quoll', 'rat', 'rhinoceros', 'racoon', 'reindeer', 'rabbit', 'snake', 'squirrel', 'sheep', 'seal', 'turtle', 'tiger', 'turkey', 'tapir', 'unicorn', 'vampirebat', 'vulture', 'wombat', 'walrus', 'wildebeast', 'wallaby', 'yak', 'zebra']
    ANIMALS_REVERSED = []
    for animal in ANIMALS:
        ANIMALS_REVERSED.append(animal[::-1])

    def test_photo(photo, animal):
        test = False
        animal_index = 0
        for character in photo:
            if character == "=":
                pass
            elif animal_index < len(animal) and character == animal[animal_index]:
                test = True
                animal_index += 1
            elif character == animal[animal_index - 1]:
                pass
            else:
                test = False
                break
        if test:
            return True
        return False

    for animal in ANIMALS:
        test = test_photo(photo, animal)
        if test:
            return animal

    for animal in ANIMALS_REVERSED:
        test = test_photo(photo, animal)
        if test:
            return animal[::-1]

    return "??"

photo = "==========h===yyyyyy===eeee=n==a========"
#photo = "==unnn==Lii===cccccooor==nn"
#photo = "==========h===yyyyyy===eeee=n==a===b====="
#photo = "=====r=rrr=rra=====eee======bb====b======="
print(road_kill(photo))
