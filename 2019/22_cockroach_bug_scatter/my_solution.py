# solution in progress to kata found here:
# https://www.codewars.com/kata/cockroach-bug-scatter/train/python


"""
This is gonna take some planning...
create a 2x2 list representing the square of the room
"""


def cockroaches(room):
    class Cockroach:
        """ stores the location and direction of a cockroach

        attributes:
        position.x (left is x = 0, x increases to the right)
        position.y (top is y = 0, y increases downwards)
        direction
        in_hole
        """
        def __init__ (self, x=0, y=0, direction = "U", in_hole = False):
            self.x = x
            self.y = y
            self.direction = direction
            self.in_hole = in_hole

        def __str__ (self):
            s = "Roach at position: (" +str(self.x) + ", " + str(self.y) + ") facing in direction: " + self.direction + "."
            #"Roach at position: (" +  self.posision.x + ", " +  self.position.y, ") Facing: " + self.direction "."
            return s

        # end Cockroach class definitions

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

    # roach_1 = Cockroach()
    # print(roach_1)
    # hole_1 = Hole()
    # print(hole_1)


    def find_roaches(room_list):
        """ Returns a list of Cockroach objects
        """
        cockroaches = []
        for i, row in enumerate(room_list):
            for j, column in enumerate(row):
                if column in "UDLR":
                    roach = Cockroach(j, i, column) # x is in the inner list
                    cockroaches.append(roach)
        return cockroaches

    def find_holes(room_list):
        """ Returns a list of hole objects
        """
        holes = []
        for i, row in enumerate(room_list):
            for j, column in enumerate(row):
                if column in "0123456789":
                    hole = Hole(i, j, column)
                    holes.append(hole)
        return holes


    def move_roaches(room_list, cockroaches):
        room_height_y = len(room_list)
        # print("room_height_y", room_height_y)
        room_width_x = len(room_list[0])

        # print("room_width_x", room_width_x)
        for roach in cockroaches:
            if roach.x not in [0, room_width_x - 1] and roach.y not in [0, room_height_y - 1]:
                if roach.direction == "U":
                    roach.y -= 1
                if roach.direction == "D":
                    roach.y += 1
                if roach.direction == "L":
                    roach.x -= 1
                if roach.direction == "R":
                    roach.x += 1
        return cockroaches

    def test_roach_at_wall(room_list, roach):
        if roach.x in [0, room_width_x - 1] or roach.y in [0, room_height_y - 1]:
            return True
        return False

    def test_all_roaches_at_wall(room_list, roaches):
        at_wall_bool_list = []
        for roach in roaches:
            if test_roach_at_wall(room_list, roach):
                at_wall_bool_list.append(True)
            else:
                at_wall_bool_list.append(False)
        print(at_wall_bool_list)
        return all(at_wall_bool_list)

    def move_roach(room_list, roach):
        if roach.direction == "U":
            roach.y -= 1
        if roach.direction == "D":
            roach.y += 1
        if roach.direction == "L":
            roach.x -= 1
        if roach.direction == "R":
            roach.x += 1

    def turn_roaches_on_sides(room_list, roaches):
        for roach in roaches:
            if rocah_in_corner(room_list, roach):
                if roach.direction == 'U':
                    roach.direction = 'L'
                if roach.direction == 'L':
                    roach.direction = 'D'
                if roach.direction == 'D':
                    roach.direction = 'R'
                if roach.direction == 'R':
                    roach.direction = 'U'
            else:
                move_roach(room_list, roach)
        return roaches

    def roach_in_corner(room_list, roach):
        room_height_y = len(room_list)
        room_width_x = len(room_list[0])
        if roach.x == 0 and roach.y == 0:
            return True
        elif roach.x == 0 and roach.y == room_height_y:
            return True
        elif roach.x == room_width_x and roach.y == 0:
            return True
        elif roach.x == room_width_x and roach.y == room_height_y:
            return True
        else:
            return False



    def move_roaches_on_wall(room_list, roaches, holes):
        for roach in roaches:
            if not roach.in_hole:
                if roach_in_corner(room_list, roach):
                    pass # turn_roaches_in_corners(room_list, )
        return roaches


    def test_all_roaches_in_holes(room_list, cockroaches, holes):
        return False # TODO write test if all cockroaches are in holes

    def test_single_roach_in_hole(room_list, cockroach, holes):
        x = cockroach.x
        y = cockroach.y
        for hole in holes:
            if x == hole.x and y == hole.y:
                return True
        return False


    room_list = room
    # print(len(room_list))
    room_height_y = len(room_list)
    # print(len(room_list[0]))
    room_width_x = len(room_list[0])
    for i, row in enumerate(room_list):
        room_list[i] = list(row)

    print("find roaches")
    cockroaches = find_roaches(room_list)
    for roach in cockroaches:
        print(roach)

    print("find holes")
    holes = find_holes(room_list)
    for hole in holes:
        print(hole)

    while test_all_roaches_at_wall(room_list, cockroaches) == False: # and i < 30:
        print("move cockroaches")
        cockroaches = move_roaches(room_list, cockroaches)
        for roach in cockroaches:
            print(roach)
        i += 1

    #cockroaches = turn_roaches_in_corners(room_list, cockroaches)

    while i < 40: #test_all_roaches_in_holes == False and i < 40:
        cockroaches = move_roaches_on_wall(room_list, cockroaches, holes)
        print('i', i)
        for roach in cockroaches:
            print(roach)
        i += 1



    result = (0, 0, 0)
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
