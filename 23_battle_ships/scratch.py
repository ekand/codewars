class Piece_o_boat:
    """ represents a 1-point piece of a boat

    Attributes:
    x: horizonat position (left is zero, right is +)
    y: vertical position (up is zero, down is +)
    hit: True or False, tells whether this piece has bee hit
    """

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        s = "piece position: (" + str(self.x) + ", " + str(self.y) + ")"
        return s

def damaged_or_sunk (board, attacks):
    # Code here

boat_piece = Piece_o_boat()
print(boat_piece)
