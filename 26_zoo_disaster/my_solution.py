# attempted solution to kata found here
# https://www.codewars.com/kata/5902bc7aba39542b4a00003d/train/python

def make_eating_dict(zoo):
    d = {}
    d['grass'] = []
    d['little-fish'] = []
    d['leaves'] = []

    d['antelope'] = ['grass']
    d['big-fish'] = ['little-fish']
    d['bug'] = ['leaves']
    d['bear'] = ['big-fish']
    d['bear'].append('bug')
    d['bear'].append('chicken')
    d['bear'].append('cow')
    d['bear'].append('leaves')
    d['bear'].append('sheep')
    d['chicken'] = ['bug']
    d['cow'] = ['grass']
    d['fox'] = ['chicken']
    d['fox'].append('sheep')
    d['giraffe'] = ['leaves']
    d['lion'] = ['antelope']
    d['lion'].append('cow')
    d['panda'] = ['leaves']
    d['sheep'] = ['grass']

    t = zoo.split(',')
    for animal in t:
        if animal not in d:
            d[animal] = []

    return d

def who_eats_who(zoo):
    t = zoo.split(',')
    #print(t)
    eats = make_eating_dict(zoo)
    eaten = True
    output = [zoo]
    while eaten:
        print(t)
        eaten = False
        #print('animal:', t[0], 'eats[animal]:', eats[t[0]])
        if  len(t) > 1 and t[1] in eats[t[0]]:
            s = t[0] + ' eats ' + t[1]
            print(s)
            output.append(s)
            t.pop(1)
            eaten = True
            continue
        for i, animal in enumerate(t[1:-1]):
            #print('animal:', animal, 'eats[animal]:', eats[animal])
            j = i + 1
            if t[j-1] in eats[animal]:

                s = animal + ' eats ' + t[j-1]
                print(s)
                output.append(s)
                t.pop(j-1)
                eaten = True
                break
            elif t[j+1] in eats[animal]:
                s = animal + ' eats ' + t[j+1]
                print(s)
                output.append(s)
                t.pop(j+1)
                eaten = True
                break
        if eaten:
            continue
        #print('animal:', t[-1], 'eats[animal]:', eats[t[-1]])
        if len(t) > 1 and t[-2] in eats[t[-1]]:

            s = t[-1] + ' eats ' + t[-2]
            print(s)
            output.append(s)
            t.pop(-2)
            eaten = True

    s = ",".join(t)
    output.append(s)
    return output




input = "fox,bug,chicken,grass,sheep"


input = "fox,chicken,grass,sheep"
input = "chicken,fox,grass,sheep"

input = "fox,bug,chicken,grass,sheep"
input = 'fox,chicken,tree,chicken,bug,banana,bug,bear'

print(who_eats_who(input))
