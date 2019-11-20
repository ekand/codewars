class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties


def most_money(students):
    # NOTE: the Student class is preloaded
    pass
    max = -1
    richest_names = []
    for student in students:
        money = 5 *student.fives + 10 * student.tens + 20 * student.twenties
        print("name", student.name, "money", money)
        if money == max:
            richest_names.append(student.name)
        elif money > max:
            max = money
            richest_names.clear()
            richest_names.append(student.name)

    print(richest_names)
    print(students)

    if len(richest_names) == 1:
        return richest_names[0]
    elif len(richest_names) == len(students):
        return "all"

    else:
        return "foo"



phil = Student("Phil", 2, 2, 1)
cam = Student("Cameron", 2, 2, 0)
geoff = Student("Geoff", 0, 3, 0)
print(most_money([cam, geoff, phil]))
print()

print(most_money([cam, geoff]))
print()
print(most_money([geoff]))
print()
