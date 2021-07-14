# kata found here
# https://www.codewars.com/kata/the-road-kill-detective/train/python
# print('\n'.join(ANIMALS))

def road_kill(photo):




    def test_animal(animal, photo):
        #print(animal, photo)
        animal_index = 0
        recognized_animal = ''
        for char in photo:
            #print(char, animal[animal_index])

            if animal_index < len(animal) and animal[animal_index] == char:
                recognized_animal += char
                animal_index += 1
        if recognized_animal == animal:
            return True
        return False

    for animal in ANIMALS:
        if test_animal(animal, photo):
            return animal
        if test_animal(animal[::-1], photo):
            return animal
    return "??"



ANIMALS = ['aardvark', 'alligator', 'armadillo', 'antelope', 'baboon', 'bear', 'bobcat', 'butterfly', 'cat', 'camel', 'cow', 'chameleon', 'dog', 'dolphin', 'duck', 'dragonfly', 'eagle', 'elephant', 'emu', 'echidna', 'fish', 'frog', 'flamingo', 'fox', 'goat', 'giraffe', 'gibbon', 'gecko', 'hyena', 'hippopotamus', 'horse', 'hamster', 'insect', 'impala', 'iguana', 'ibis', 'jackal', 'jaguar', 'jellyfish', 'kangaroo', 'kiwi', 'koala', 'killerwhale', 'lemur', 'leopard', 'llama', 'lion', 'monkey', 'mouse', 'moose', 'meercat', 'numbat', 'newt', 'ostrich', 'otter', 'octopus', 'orangutan', 'penguin', 'panther', 'parrot', 'pig', 'quail', 'quokka', 'quoll', 'rat', 'rhinoceros', 'racoon', 'reindeer', 'rabbit', 'snake', 'squirrel', 'sheep', 'seal', 'turtle', 'tiger', 'turkey', 'tapir', 'unicorn', 'vampirebat', 'vulture', 'wombat', 'walrus', 'wildebeast', 'wallaby', 'yak', 'zebra']

# photo = "==========h===yyyyyy===eeee=n==a========"
# animal = "hyena"
# print(test_animal(animal, photo))

photo = "==========h===yyyyyy===eeee=n==a========"
print(road_kill(photo))


"""
result: passes most tests,
eg hyena ==========h===yyyyyy===eeee=n==a========
but fails on ones like this:
Shouldn't find unicorn in skid: ==unnn==Lii===cccccooor==nn: 'unicorn' should equal '??'
"""
