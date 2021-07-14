# solution in progress to kata found here
# https://www.codewars.com/kata/591eab1d192fe0435e000014/train/python

class Position:
    """ represents my position in the carpark.

    Attributes:
    x: integer indexed from zero on left side
    y: integer indexed from zero on top
    path: list of strings representing
    """
    def __init__(self, x=0, y=0, path = None):
        self.x = x
        self.y = y
        if path == None:
            self.path = []
        else:
            self.path = path

    def __str__(self):
        s = "Standing at (" + str(self.x) + ", " + str(self.y) + ") with path " + str(self.path)
        return s


def escape(carpark):
    # if stairway is to the right, step right an appropriate number of times
    # if stairway is to the left, step left an appropriate number of times
    # if on a stairway, go down one level
    # if on bottom level walk to the right
    # if on the right side of bottom level, exit

    # load starting position y = ?, x = ?
    position = load_starting_position(carpark)
    print(position)


    # determine direction of travel (if not on lowest level)
    stair_y = position.y
    if stair_y != len(carpark):
        row = carpark[stair_y]
        stair_x = row.index(1)
    if stair_x > position.x:
        direction = "R"
    else:
        direction = "L"
    print("direction", direction)
    print("hi")

    return 'foo'



def load_starting_position(carpark): # load starting position y = ?, x = ?
    for y, row in enumerate(carpark):
        x = None
        try:
            x = row.index(2)
        except:
            pass
        if x:
            break
    position = Position(x, y)
    return position















carpark = [[0, 2, 0, 0, 1],
           [0, 0, 0, 0, 1],
           [0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]]
print(carpark)
print(escape(carpark))


result = ["R3", "D3"]
