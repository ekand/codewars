# attempt 3 at kata found here
# https://www.codewars.com/kata/battle-ships-sunk-damaged-or-not-touched/train/python

# this time only use Piece class / object

board = [[0,0,0,2,2,0],
         [0,3,0,0,0,0],
         [0,3,0,1,0,0],
         [0,3,0,1,0,0]]
attacks = [[2, 1], [1, 3], [4, 2]]

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
    for y, row in enumerate(board):
        for x, column in enumerate(row):
            if column != 0:
                pieces.append(Piece(x, y, column, "intact"))
    return(pieces)

# # test get pieces
# pieces = get_pieces(board)
# print_pieces(pieces)
# print("")

def apply_attack(pieces, attacks):
    for attack in attacks:
        for piece in pieces:
            if attack[0] == piece.x and attack[1] == piece.y:
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
        if piece.id in []:
            pass
    result = {}
    result['sunk'] = 'foo'
    result['damaged'] = 'foo'
    result['not_touched'] = 'foo'
    result['points'] = 'foo'
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
