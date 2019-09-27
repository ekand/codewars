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
        position.x
        position.y
        direction
        """
        def __init__ (self, x=0, y=0, direction = "U"):
            self.x = x
            self.y = y
            self.direction = direction

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

    roach_1 = Cockroach()
    print(roach_1)
    hole_1 = Hole()
    print(hole_1)


    def find_roaches(room_list):
        """ Returns a list of Cockroach objects
        """
        cockroaches = []
        for i, row in enumerate(room_list):
            for j, column in enumerate(row):
                if column in "UDLR":
                    roach = Cockroach(i, j, column)
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
        room_width_x = len(room_list[0])
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
                at_wass_bool_list.append(False)
        # if all True, return True. else return False
        return None #TODO return true or false




    room_list = room
    print(len(room_list))
    room_height_y = len(room_list)
    print(len(room_list[0]))
    room_width_x = len(room_list[0])
    for i, row in enumerate(room_list):
        room_list[i] = list(row)

    cockroaches = find_roaches(room_list)
    for roach in cockroaches:
        print(roach)

    holes = find_holes(room_list)
    for hole in holes:
        print(hole)

    cockroaches = move_roaches(room_list, cockroaches)
    for roach in cockroaches:
        print(roach)

#     room_width = len(room[0])
#     print(room_width)
#     room_height = len(room)
#     print(room_height)
#     for i, string in enumerate(room):
#         room[i] = list(string)

#     def find_holes(room):
#         hole_dict = {}
#         for i, row in enumerate(room):
#             for j, entry in enumerate(row):
#                 if entry in "0123456789":
#                     hole_dict[(i,j)] = entry
#         return hole_dict

#     def find_roaches(room):
#         roach_dict = {}
#         for i, row in enumerate(room):
#             for j, entry in enumerate(row):
#                 if entry in "UDLR":
#                     roach_dict[(i, j)] = entry
#         return roach_dict

#     def move_roaches(roach_dict):
#         for position, direction in roach_dict.items():
#             if position[0] != 0 and position[0] != room_height and position[1] != 0 and position[1] != room_width
#                 del roachdict[position]
#                 if direction == U:
#                     position

       # pass
    # Your code here!
    pass
