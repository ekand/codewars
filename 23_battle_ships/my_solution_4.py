# attempt 3 at kata found here
# https://www.codewars.com/kata/battle-ships-sunk-damaged-or-not-touched/train/python

# this time only use Piece class / object

# board = [[0,0,0,2,2,0],
#          [0,3,0,0,0,0],
#          [0,3,0,1,0,0],
#          [0,3,0,1,0,0]]
# attacks = [[2, 1], [1, 3], [4, 2]]\

board = [ [3, 0, 1],
          [3, 0, 1],
          [0, 2, 1],
          [0, 2, 0] ]

attacks = [[2, 1], [2, 2], [ 3, 2], [3, 3]]

# board = [ [0, 0, 1, 0],
#           [0, 0, 1, 0],
#           [0, 0, 1, 0] ]
#
# attacks = [[3, 1], [3, 2], [3, 3]];

class Piece:
    """ represents a piece of a boat

    Attributes:
    x: x position
    y: y position
    id: integet, boat id
    status: "damaged", "intact"
    """

    def __init__(self, x = 0, y = 0, id = -1, status = "intact"):
        self.x = x
        self.y = y
        self.id = id
        self.status = status

    def __str__(self):
        s = "Piece at: (" + str(self.x) + ", " + str(self.y) + ") with id " + str(self.id) + " and status: " + self.status + ". "
        return s

class Boat:
    """ represents a boat

    attributes:
    id: integer, boat id
    total_pieces: integer, number of total pieces
    damaged_pieces: integer, number of damaged pieces
    status: string. "sunk", "damaged", "not_touched"
    """

    def __init__(self, id = 0, total_pieces = 0, damaged_pieces = 0, status = "not_touched"):
        self.id = id
        self.total_pieces = total_pieces
        self.damaged_pieces = damaged_pieces
        self.status = status

    def __str__(self):
        s = "Boat id: " + str(self.id) + " with " + str(self.total_pieces) + " total pieces and " + str(self.damaged_pieces) + " damaged pieces, with status: " + self.status
        return s

def print_pieces(pieces):
    for piece in pieces:
        print(piece)

def get_pieces(board):
    pieces = []
    for y, row in enumerate(board[::-1]):
        for x, column in enumerate(row):
            if column != 0:
                pieces.append(Piece(x +1, y+1, column, "intact"))
    return(pieces)

# # test get pieces
# pieces = get_pieces(board)
# print_pieces(pieces)
# print("")

def apply_attack(pieces, attacks):
    for attack in attacks:
        for piece in pieces:
            if attack[0] == piece.x and attack[1]== piece.y:
                piece.status = "damaged"

    return pieces

# # test apply_attack
# pieces = apply_attack(pieces, attacks)
# print_pieces(pieces)

# # test print boat
boat1 = Boat()
print(boat1)


# plan boats dict
# key will be

def get_ship_status(pieces):
    boats = {}
    for piece in pieces:
        if piece.id not in boats:
            boats[piece.id] = Boat(piece.id)
    for boat in boats.values():
        for piece in pieces:

            if piece.id == boat.id:
                boat.total_pieces += 1
                if piece.status == 'damaged':
                    boat.damaged_pieces += 1
    result = {}
    result['sunk'] = 0
    result['damaged'] = 0
    result['not_touched'] = 0
    result['points'] = 0
    for boat in boats.values():
        print(boat)
        if boat.total_pieces == boat.damaged_pieces:
            boat.status = 'sunk'
            result['sunk'] += 1
        elif boat.damaged_pieces > 0:
            result['damaged'] += 1
        else:
            result['not_touched'] += 1
    result['points'] = 1 * result['sunk'] + 0.5 * result['damaged'] - 1 * result['not_touched']


    return result


def damaged_or_sunk (board, attacks):
    # Code here
    pass
    # read board and store pieces data
    pieces = get_pieces(board)
    print_pieces(pieces)
    print("")

    # apply attackes to pieces data
    pieces = apply_attack(pieces, attacks)
    print_pieces(pieces)
    print("")

    # read status of ships, report sunk, damaged, not_touched, point
    result = get_ship_status(pieces)
    return result


print(damaged_or_sunk(board, attacks))
