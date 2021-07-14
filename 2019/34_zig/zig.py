import numpy as np


# class Switch:
#     def __init__(self, x=0, y=0, state="A"):
#         self.x = x
#         self.y = y
#         self.state = state
#
#     def __str__(self):
#         s = "switch at location {}, {} with state {}.".format(self.x, self.y, self.state)
#         return s
#
#     def change_state(self):
#         if self.state == "A":
#             self.state = "B"
#         elif self.state == "B":
#             self.state = "A"
#         else:
#             print("oops, this code should not have executed")


class Explorer:
    """
    class with attributes position (list) and direction (string)
    """

    def __init__(self, x, y, direction="E"):
        self.x = x
        self.y = y
        self.direction = direction

    def __str__(self):
        s = "explorer at position {}, {} facing in direction {}.".format(self.x, self.y, self.direction)
        return s

    def step_explorer(self, room):
        # self is an explorer

        self.turn_explorer(room)

        # move explorer forward
        if self.direction == "N":
            self.y -= 1
        if self.direction == "E":
            self.x += 1
        if self.direction == "S":
            self.y += 1
        if self.direction == "W":
            self.x -= 1

    def turn_explorer(self, room):
        if room[self.y][self.x] == 1:
            if self.direction == "W":
                self.direction = "N"
            elif self.direction == "E":
                self.direction = "S"
            elif self.direction == "S":
                self.direction = "E"
            elif self.direction == "N":
                self.direction = "W"
            room[self.y][self.x] = -1
        elif room[self.y][self.x] == -1:
            if self.direction == "W":
                self.direction = "S"
            elif self.direction == "E":
                self.direction = "N"
            elif self.direction == "S":
                self.direction = "W"
            elif self.direction == "N":
                self.direction = "E"
            room[self.y][self.x] = 1

    def test_explorer_in_room(self, height, width):
        if self.x < 0 or self.x > (width - 1) or self.y < 0 or self.y > (height - 1):
            return False
        else:
            return True


def convert_switch(char):
    if char == "A":
        return 1
    elif char == "B":
        return -1
    else:
        return 0


def parse_artifact(artifact):
    artifact = [[convert_switch(char) for char in row] for row in artifact]
    room = np.array(artifact, dtype="int8")
    return room


def move_explorer(explorer_row, room):
    explorer = Explorer(x=0, y=explorer_row, direction="E")
    in_room = True
    height, width = room.shape
    while in_room:
        in_room = explorer.test_explorer_in_room(height, width)
        if not in_room:
            break
        explorer.step_explorer(room)
    return explorer.x, explorer.y


def ride_of_fortune(artifact, explorers):

    room = parse_artifact(artifact)
    room_height, room_width = room.shape

    exit_locations = [None for _ in explorers]
    for i, explorer_row in enumerate(explorers):
        x, y = move_explorer(explorer_row, room)

        if x < 0:
            exit_location = None
        elif x > room_width - 1 or y > room_height - 1 or y < 0:
            if x > room_width-1:
                x -= 1
            elif y > room_height-1:
                y -= 1
            elif y < 0:
                y += 1
            exit_location = [y, x]
             # exit_location = [x, y]
        exit_locations[i] = exit_location
        pass # print([x, y])
    return exit_locations


# switch = Switch()
# print(switch)
# switch.change_state()
# print(switch)
#
# explorer = Explorer()
# print(explorer)



