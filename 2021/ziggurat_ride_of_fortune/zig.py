import numpy

verbose = False
def ride_of_fortune(artifact, explorers):
    artifact_object = Artifact(artifact)
    results = []
    for explorer in explorers:
        exp = Explorer(x=0, y=explorer)
        while not exp.exited:
            exp.move()
            exp.evaluate(artifact_object)
        #         print("***result***", exp.result)
        results.append(exp.result)
    return results

    # explorer class. has position and direction
    # moves by stepping in its direction, then
    # checking if there is a switch on its location and
    # turning if necessary


class Explorer:
    def __init__(self, x=0, y=0):
        self.result = None
        self.exited = False
        self.x = x
        self.y = y
        self.dy = 0
        self.dx = 1
        if verbose:
            print("new  explorer   at y", self.y, "x", self.x, "moving dy", self.dy, "dx", self.dx)

    def move(self):
        if verbose:
            print("about to step   at y", self.y, "x", self.x, "moving dy", self.dy, "dx", self.dx)
        self.step()
        if verbose:
            print("just  stepped   at y", self.y, "x", self.x, "moving dy", self.dy, "dx", self.dx)

    def evaluate(self, artifact_object):
        if verbose:
            print("evaluating")
        height = artifact_object.height
        width = artifact_object.width
        if verbose:
            print("height", height, "self.x", self.x)
        #         print(self.y, self.x)
        if self.x < 0:
            self.exited = True
            self.result = None  # exits back to the land by the temple
        elif self.x == width:
            self.exited = True
            self.result = [self.y, self.x - 1]  # exits at this location's portal
        elif self.y == height:
            self.exited = True
            self.result = [self.y - 1, self.x]
        elif self.y < 0:
            self.exited = True
            self.result = [0, self.x]
        if self.exited:
            if verbose:
                print("exited         at y", self.y, "x", self.x, "moving dy", self.dy, "dx", self.dx)
            if verbose:
                print(self.result, "self.result")
            if verbose:
                print("===")
            return
        #         print("hello")
        if artifact_object.artifact[self.y][self.x] != 0:
            if verbose:
                print("about to rotate at y", self.y, "x", self.x, "moving dy", self.dy, "dx", self.dx)
                print(artifact_object.artifact)
            self.rotate(artifact_object)
            if verbose:
                print(artifact_object.artifact)
                print("did      rotate at y", self.y, "x", self.x, "moving dy", self.dy, "dx", self.dx)

    def rotate(self, artifact_object):
        switch_state = artifact_object.artifact[self.y][self.x]
        # rotate explorer
        if switch_state == 1:
            self.apply_state_one_rules()
        elif switch_state == -1:
            self.apply_state_minus_one_rules()
        artifact_object.artifact[self.y][self.x] = - artifact_object.artifact[self.y][self.x]  # chagne switch state

    def step(self):
        self.x += self.dx
        self.y += self.dy

    def apply_state_one_rules(self):
        dy = self.dy
        dx = self.dx
        if verbose:
            print("state one rules")
        if dy == 1 and dx == 0:  # south
            dy, dx = 0, 1  # east
        elif dy == 0 and dx == 1:  # east
            dy, dx = 1, 0  # south
        elif dy == -1 and dx == 0:  # north
            dy, dx = 0, -1  # west
        elif dy == 0 and dx == -1:  # west
            dy, dx = -1, 0  # north
        self.dy = dy
        self.dx = dx

    def apply_state_minus_one_rules(self):
        dy = self.dy
        dx = self.dx
        if verbose:
            print("state two rules")
        if dy == 1 and dx == 0:  # south
            dy, dx = 0, -1  # west
        elif dy == 0 and dx == -1:  # west
            dy, dx = 1, 0  # south
        elif dy == -1 and dx == 0:  # north
            dy, dx = 0, 1  # east
        elif dy == 0 and dx == 1:  # east
            dy, dx = -1, 0  # north
        self.dy = dy
        self.dx = dx


# numpy array of integers. 0 for nothing there, 1 for A, -1 for B
class Artifact():

    def parse_artifact(self, artifact):
        height = len(artifact)
        width = len(artifact[0])
        n = numpy.zeros((height, width))
        for i, row in enumerate(artifact):
            for j, char in (enumerate(artifact[i])):
                if char == "A":
                    n[i][j] = 1
                elif char == "B":
                    n[i][j] = -1
        return n, width, height

    def __init__(self, artifact):
        self.artifact, self.width, self.height = self.parse_artifact(artifact)

