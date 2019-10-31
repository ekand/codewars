# attempt 3 at kata found here:
# https://www.codewars.com/kata/cockroach-bug-scatter/train/python

# it passed!

class Roach_crowd:
    """ represents all of the cockroaches

    attrubutes:
    roaches: a list of roach objects
    """
    def __init__(self):
        self.roaches = []

    def print_roach_crowd(self):
        print("roaches:")
        for i, roach in enumerate(self.roaches):
            print(i, roach)

class Roach:
    """ represents a single cockroach

    attrbutes:
    position.x (left is x = 0, x increases to the right)
    position.y (top is y = 0, y increases downwards)
    direction   U, D, L, R. the direction it is facing
    at_wall     True while at wall
    in_corner   True while in a corner
    in_hole     True if in hole

    """
    def __init__(self, x=0, y=0, direction="U",at_wall=False, in_corner=False, in_hole=False):
        self.x = x
        self.y = y
        self.direction = direction
        self.at_wall = False
        self.in_hole = False

    def __str__(self):
        s = "Roach at position: (" +str(self.x) + ", " + str(self.y) + ") facing in direction: " + self.direction + "."
        return s

class Hole:
    """ Represents a hole object
    Attributes:
    x: position in x direction
    y: position in y direction
    ID: number label, 0 to 9
    """
    def __init__(self, x=0, y=0, ID="0"):
        self.x = x
        self.y = y
        self.ID = ID

    def __str__(self):
        s = "Hole at position: (" + str(self.x) + ", " + str(self.y) + ") with ID: " + str(self.ID) + "."
        return s

def find_roaches(room_list): # uses variable room_list from cockroaches() scope
    roach_crowd = Roach_crowd()
    for i, row in enumerate(room_list):
        for j, column in enumerate(row):
            if column in "UDLR":
                roach = Roach(j, i, column) # x is in the inner list
                roach_crowd.roaches.append(roach)
    return roach_crowd

def find_holes(room_list):
    holes = []
    for i, row in enumerate(room_list):
        for j, column in enumerate(row):
            if column in "0123456789":
                hole = Hole(j, i, column) # x is inner, I think? #todo check this later
                holes.append(hole)
    return holes


def move_roach_to_hole(roach, room_list, holes):
    # move to wall:
    while not test_at_wall(roach, room_list):
        roach = step_roach(roach)
    roach = turn_roach(roach)
    while (not test_in_hole(roach, holes)):
        if test_in_corner(roach, room_list):
            roach = turn_roach(roach)
            roach = step_roach(roach)
        else:
            roach = step_roach(roach)
    return roach


def test_at_wall(roach, room_list):
    room_height, room_width = get_room_width_height(room_list)
    if roach.x in [0, room_width - 1] or roach.y in [0, room_height - 1]:
        return True
    else:
        return False

def test_in_hole(roach, holes):
    for hole in holes:
        if roach.x == hole.x and roach.y == hole.y:
            return True
    return False

def test_in_corner(roach, room_list):
    room_height, room_width = get_room_width_height(room_list)
    if roach.x == 0 and roach.y == 0:
        return True
    elif roach.x == 0 and roach.y == room_height-1:
        return True
    elif roach.x == room_width-1 and roach.y == 0:
        return True
    elif roach.x == room_width-1 and roach.y == room_height-1:
        return True
    else:
        return False

def step_roach(roach):
    if roach.direction == "U":
        roach.y -= 1
    if roach.direction == "D":
        roach.y += 1
    if roach.direction == "L":
        roach.x -= 1
    if roach.direction == "R":
        roach.x += 1

    return roach
def turn_roach(roach):
    if roach.direction == 'U':
        roach.direction = 'L'
    elif roach.direction == 'L':
        roach.direction = 'D'
    elif roach.direction == 'D':
        roach.direction = 'R'
    elif roach.direction == 'R':
        roach.direction = 'U'
    return roach

def get_room_width_height(room_list):
    room_height = len(room_list)
    room_width = len(room_list[0])
    return room_height, room_width

def count_roaches(roach_crowd_in_holes, holes):
    result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for roach in roach_crowd_in_holes.roaches:
        for hole in holes:
            if roach.x == hole.x and roach.y == hole.y:
                result[int(hole.ID)] += 1
    return result



def cockroaches(room): # main function for code wars
    room_list = room
    #print(type(room))
    #print(room)
    for i, row in enumerate(room_list):
        room_list[i] = list(row)
    #print(room_list)
    roach_crowd = find_roaches(room_list) #uses room_list
    # roach_crowd.print_roach_crowd()

    holes = find_holes(room_list)
    #for hole in holes:
        #print(hole)
    roach_crowd_in_holes = Roach_crowd()
    for x, roach in enumerate(roach_crowd.roaches):
        roach_crowd_in_holes.roaches.append(move_roach_to_hole(roach, room_list, holes))
    #roach_crowd_in_holes.print_roach_crowd()
    result = count_roaches(roach_crowd_in_holes, holes)

    return result




room = ["+----------------0---------------+",
      "|                                |",
      "|                                |",
      "|          U        D            |",
      "|     L                          |",
      "|              R                 |",
      "|           L                    |",
      "|  U                             1",
      "3        U    D                  |",
      "|         L              R       |",
      "|                                |",
      "+----------------2---------------+"]
print(cockroaches(room))
