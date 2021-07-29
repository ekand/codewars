import numpy

verbose = False


def ride_of_fortune(artifact, explorers):
    artifact_object = Artifact(artifact)
    if verbose:
        print(artifact_object.artifact)
    results = []
    for explorer_start_row in explorers:
        if verbose:
            print("====")
        explorer_object = Explorer(y=explorer_start_row, x=-1, dy=0, dx=1)
        while not explorer_object.exited:
            explorer_object.step()
            explorer_object.evaluate_and_rotate(artifact_object)
        results.append(explorer_object.result)
    return results


class Explorer():
    def __init__(self, y, x, dy, dx):
        self.y = y
        self.x = x
        self.dy = dy
        self.dx = dx
        self.result = None
        self.exited = False
        if verbose:
            print("new explorer at  y", self.y, "x", self.x, "moving dy", self.dy, "dx", self.dx)

    def step(self):
        if verbose:
            print("about to step at y", self.y, "x", self.x, "moving dy", self.dy, "dx", self.dx)
        self.y += self.dy
        self.x += self.dx
        if verbose:
            print("just stepped at  y", self.y, "x", self.x, "moving dy", self.dy, "dx", self.dx)

    def evaluate_and_rotate(self, artifact_object):
        if verbose:
            print("evaluating")
        if self.x < 0:
            self.exited = True
            self.result = None  # exits back to land
        elif self.x == artifact_object.width:
            self.exited = True
            self.result = [self.y, self.x - 1]  # exits at this location's portal
        elif self.y == artifact_object.height:
            self.exited = True
            self.result = [self.y - 1, self.x]
        elif self.y < 0:
            self.exited = True
            self.result = [0, self.x]
        if self.exited:
            if verbose:
                print("exited at        y", self.y, "x", self.x, "moving dy", self.dy, "dx", self.dx)
                print('result', self.result)

            return
        # decide whether to rotate
        if artifact_object.artifact[self.y][self.x] != 0:
            if verbose:
                print("about to rotate  y", self.y, "x", self.x, "moving dy", self.dy, "dx", self.dx)
                print(artifact_object.artifact)
            self.rotate(artifact_object)
            if verbose:
                print("did  rotate      y", self.y, "x", self.x, "moving dy", self.dy, "dx", self.dx)
                print(artifact_object.artifact)

    def rotate(self, artifact_object):
        switch_state = artifact_object.artifact[self.y][self.x]
        # rotate explorer
        if switch_state == 1:
            self.apply_state_one_rules()
        elif switch_state == -1:
            self.apply_state_minus_one_rules()
        artifact_object.artifact[self.y][self.x] *= -1

    def apply_state_one_rules(self):
        if verbose:
            print("State one rules")
        dy = self.dy
        dx = self.dx
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
        if verbose:
            print("State minus one rules")
        dy = self.dy
        dx = self.dx
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


class Artifact:

    def __init__(self, artifact):
        self.height = len(artifact)
        self.width = len(artifact[0])
        n = numpy.zeros((self.height, self.width))
        for i, row in enumerate(artifact):
            for j, char in enumerate(artifact[i]):
                if char == "A":
                    n[i][j] = 1
                elif char == "B":
                    n[i][j] = -1
        self.artifact = n