# this is kind of a mess.
# probably a good idea to start over, make a plan, then implement

class Boat:
    """ represents a boat on the board

    Attributes:
    id: a string, id number
    Pieces: a list of Boat pieces
    status: "intact", "damaged", or "sunk"
    """

    def __init__(self, id = "0", pieces = [], status = "intact"):
        self.id = id
        self.pieces = pieces
        self.status = status


    def __str__(self):
        s = "Boat id: " + self.id + ", Pieces: " + str(self.pieces) + ", status: " + self.status
        return s



# boat1 = Boat()
# print(boat1)
#
# boat2 = Boat(pieces = [[3,1,"hit",],[3,2,"not_hit"]])
# print(boat2)
# board = [ [3, 0, 1],
#           [3, 0, 1],
#           [0, 2, 1],
#           [0, 2, 0] ]
# attacks = [[2, 1], [2, 2], [ 3, 2], [3, 3]]
board = [[0,0,0,2,2,0],
         [0,3,0,0,0,0],
         [0,3,0,1,0,0],
         [0,3,0,1,0,0]]
attacks = [[2, 1], [1, 3], [4, 2]]

boats = {}
for i, row in enumerate(board):
    for j, column in enumerate(row):
        if True:
            if column != 0:
                print(column)
                if column in boats.keys():
                    boats[column].pieces.append([j, i, "not_hit1", column])
                else:
                    boats[column] = Boat(id = str(column), status = "intact")
                    boats[column].pieces.append([j, i, "not-hit2", column])
                for id, boat in boats.items():
                    print(id, ":", boat)

print("final")
for id, boat in boats.items():
    print(id, ":", boat)










def damaged_or_sunk (board, attacks):
    # Code here
    pass
