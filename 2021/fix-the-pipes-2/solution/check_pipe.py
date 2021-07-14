def make_zeroes_map(pipe_map):
    zeroes_map = []
    height = len(pipe_map)
    width = len(pipe_map[0])
    for h in range(height):
        zeroes_map.append([])
        for w in range(width):
            zeroes_map[h].append(0)
    return zeroes_map


def check_pipe(pipe_map):
    height = len(pipe_map)
    width = len(pipe_map[0])
    #     print(make_zeroes_map(pipe_map))
    for h in range(height):
        for w in range(width):
            if check_from_location(pipe_map, w, h) == 'exposed':
                if is_pipe_connected_to_edge(pipe_map, w, h) == 'connected':
                    return False
                elif is_pipe_connected_to_edge(pipe_map, w, h) == 'spilled':
                    return True
    return True


def check_from_location(pipe_map, w, h):
    zeroes_map = make_zeroes_map(pipe_map)
    #     if wetness_map[h][w] != 0:
    #         return "already checked"
    current_location = (w, h)
    current_char_code = ord(pipe_map[h][w])
    motion_table = get_motion_table()
    if current_char_code == 46:
        return 'okay'
    else:
        for direction in ['up', 'down', 'left', 'right']:
            if direction in motion_table[current_char_code]:
                if direction == 'up':
                    test_location = (w, h - 1)
                elif direction == 'down':
                    test_location = (w, h + 1)
                elif direction == 'left':
                    test_location = (w - 1, h)
                elif direction == 'right':
                    test_location = (w + 1, h)
                if evaluate_test_location(test_location, pipe_map) == 'exposed':
                    return 'exposed'
    return False


def evaluate_test_location(test_location, pipe_map):
    height = len(pipe_map)
    width = len(pipe_map[0])
    w = test_location[0]
    h = test_location[1]
    if (w < 0 or w >= width or h < 0 or h >= height):
        return "outside"
    elif ord(pipe_map[h][w]) == 46:  # the dot
        return "exposed"
    else:
        return "pipe"


def get_motion_table():
    d = dict()
    """dictionary of ord to [(w1,h1),(w2,y2)] of where water can spread"""
    d[46] = []  # .  -   46 - the dot
    d[9495] = ['up', 'right']  # ┗ - 9495 - BOX DRAWINGS HEAVY UP AND RIGHT
    d[9491] = ['down', 'left']  # ┓ - 9491 - BOX DRAWINGS HEAVY DOWN AND LEFT
    d[9487] = ['down', 'right']  # ┏ - 9487 - BOX DRAWINGS HEAVY DOWN AND RIGHT
    d[9499] = ['up', 'left']  # ┛ - 9499 - BOX DRAWINGS HEAVY UP AND LEFT
    d[9473] = ['left', 'right']  # ━ - 9473 - BOX DRAWINGS HEAVY HORIZONTAL
    d[9475] = ['up', 'down']  # ┃ - 9475 - BOX DRAWINGS HEAVY VERTICAL
    d[9507] = ['up', 'right', 'down']  # ┣ - 9507 - BOX DRAWINGS HEAVY VERTICAL AND RIGHT
    d[9515] = ['up', 'down', 'left']  # ┫ - 9515 - BOX DRAWINGS HEAVY VERTICAL AND LEFT
    d[9523] = ['down', 'left', 'right']  # '''┳ - 9523 - BOX DRAWINGS HEAVY DOWN AND HORIZONTAL'''
    d[9531] = ['up', 'left', 'right']  # ┻ - 9531 - BOX DRAWINGS HEAVY UP AND HORIZONTAL
    d[9547] = ['up', 'down', 'left', 'right']  # ╋ - 9547 - BOX DRAWINGS HEAVY VERTICAL AND HORIZONTAL
    return d


def get_step_in_h_w():
    return ['up', 'down', 'left', 'right']


"""   
┗ - 9495 - BOX DRAWINGS HEAVY UP AND RIGHT
┓ - 9491 - BOX DRAWINGS HEAVY DOWN AND LEFT
┏ - 9487 - BOX DRAWINGS HEAVY DOWN AND RIGHT
┛ - 9499 - BOX DRAWINGS HEAVY UP AND LEFT
━ - 9473 - BOX DRAWINGS HEAVY HORIZONTAL
┃ - 9475 - BOX DRAWINGS HEAVY VERTICAL
┣ - 9507 - BOX DRAWINGS HEAVY VERTICAL AND RIGHT
┫ - 9515 - BOX DRAWINGS HEAVY VERTICAL AND LEFT
┳ - 9523 - BOX DRAWINGS HEAVY DOWN AND HORIZONTAL
┻ - 9531 - BOX DRAWINGS HEAVY UP AND HORIZONTAL
╋ - 9547 - BOX DRAWINGS HEAVY VERTICAL AND HORIZONTAL
.  -   46 - the dot"""


class Explorer:
    def __init__(self, pipe_map, w=0, h=0):
        self.pipe_map = pipe_map
        self.w = w
        self.h = h
        self.already_visited = make_zeroes_map(pipe_map)

    def mark_current_position_visited(self):
        self.already_visited[self.h][self.w] = 1

    def get_char_code_at_current_position(self):
        char = self.pipe_map[self.h][self.w]
        return ord(char)

    def move_right(self):
        self.w += 1

    def move_left(self):
        self.w -= 1

    def move_up(self):
        self.h -= 1

    def move_down(self):
        self.h += 1

    def get_position(self):
        return self.w, self.h

    def set_position(self, w, h):
        self.w = w
        self.h = h

    def is_off_grid(self):
        height = len(self.pipe_map)
        width = len(self.pipe_map[0])
        if self.w < 0 or self.h < 0 or self.w >= width or self.h >= height:
            return True

    def move_in_direction(self, direction):
        if direction == "up":
            self.h -= 1
        if direction == "down":
            self.h += 1
        if direction == "right":
            self.w += 1
        if direction == "left":
            self.w -= 1


def is_pipe_connected_to_edge(pipe_map, w, h):
    already_visited = make_zeroes_map(pipe_map)
    start_position = (w, h)
    motion_table = get_motion_table()
    explorer = Explorer(pipe_map, w, h)
    for direction in motion_table[explorer.get_char_code_at_current_position()]:
        explorer2 = Explorer(pipe_map, w, h)
        explorer2.move_in_direction(direction)
        if explorer2.get_char_code_at_current_position() == ".":
            return "spilled"
        elif explorer2.is_off_grid():
            return "connected"







        #
        #
        #
        # current_position = start_position
        # current_char_code = ord(pipe_map[h][w])
        # off_edge = False
        # # move in directions that the pipe allow
        # motion_table = get_motion_table()
        # for direction in motion_table[current_char_code]:
        #     current_position
