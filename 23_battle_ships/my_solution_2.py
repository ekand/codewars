# attempt 2 at kata found here
# https://www.codewars.com/kata/battle-ships-sunk-damaged-or-not-touched/train/python

board = [[0,0,0,2,2,0],
         [0,3,0,0,0,0],
         [0,3,0,1,0,0],
         [0,3,0,1,0,0]]
attacks = [[2, 1], [1, 3], [4, 2]]

class Boat:
    """ represents a boat on the board

    Attributes:
    id: an integer, id number
    Pieces: a list of Boat pieces
    status: "intact", "damaged", or "sunk"
    """

    def __init__(self, id = 0, pieces = [], status = "intact"):
        self.id = id
        self.pieces = pieces
        self.status = status

    def __str__(self):
        s = "Boat id: " + str(self.id) + ", Pieces: " # + str(self.pieces) + ", status: " + self.status
        for piece in self.pieces:
            s += "hi" + str(piece)
        s += "Boat status: " + self.status
        return s


class Piece:
    """ represents a piece of a boat

    Attributes:
    x: x position
    y: y position
    status: "damaged", "intact"
    """

    def __init__(self, x = 0, y = 0, status = "intact"):
        self.x = x
        self.y = y
        self.status = status

    def __str__(self):
        s = "Piece at: (" + str(self.x) + ", " + str(self.y) + ") with status: " + self.status + ". "
        return s

boat1 = Boat()
for _ in range(5):
    boat1.pieces.append(Piece())
#print(boat1)

def get_boats(board):
    boats = {}
    for y, row in enumerate(board):
        for x, column in enumerate(row):
            if column != '0':
                boats[column] = Boat(1)# int(row))
                boats[column].pieces.append(Piece)
    #print(boats)
    return(boats)

# test get boats
boats = get_boats(board)
print(boats)
# for boat in boats.values():
#     print(boat)
# print(str(boats[3].pieces))





def damaged_or_sunk (board, attacks):
    # Code here
    pass
    # read board and store ships data
    #boats = get_boats(board)


    # apply attackes to ships data

    # read status of ships, report sunk, damaged, not_touched, points
