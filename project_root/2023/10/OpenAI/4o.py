import sys

START = "S"
VERTICAL_PIPE = "|"
HORIZONTAL_PIPE = "-"
NORTH_TO_EAST = "L"
NORTH_TO_WEST = "J"
SOUTH_TO_EAST = "F"
SOUTH_TO_WEST = "7"

UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"

def get_start(maze):
    for i, row in enumerate(maze):
        for j, ch in enumerate(row):
            if ch == START:
                return i, j
    return 0, 0

def part1(text):
    maze = text.splitlines()
    i, j = get_start(maze)

    direction = None

    if i > 0 and maze[i - 1][j] in {VERTICAL_PIPE, SOUTH_TO_EAST, SOUTH_TO_WEST}:
        i -= 1
        direction = UP
    elif i < len(maze) - 1 and maze[i + 1][j] in {VERTICAL_PIPE, NORTH_TO_EAST, NORTH_TO_WEST}:
        i += 1
        direction = DOWN
    elif j > 0 and maze[i][j - 1] in {HORIZONTAL_PIPE, SOUTH_TO_EAST, NORTH_TO_EAST}:
        j -= 1
        direction = LEFT
    elif j < len(maze[i]) - 1 and maze[i][j + 1] in {HORIZONTAL_PIPE, SOUTH_TO_WEST, NORTH_TO_WEST}:
        j += 1
        direction = RIGHT

    steps = 1
    while maze[i][j] != START:
        pipe = maze[i][j]
        if pipe == VERTICAL_PIPE:
            i += -1 if direction == UP else 1
        elif pipe == SOUTH_TO_EAST:
            if direction == UP:
                j += 1
                direction = RIGHT
            else:
                i += 1
                direction = DOWN
        elif pipe == HORIZONTAL_PIPE:
            j += -1 if direction == LEFT else 1
        elif pipe == SOUTH_TO_WEST:
            if direction == UP:
                j -= 1
                direction = LEFT
            else:
                i += 1
                direction = DOWN
        elif pipe == NORTH_TO_WEST:
            if direction == DOWN:
                j -= 1
                direction = LEFT
            else:
                i -= 1
                direction = UP
        elif pipe == NORTH_TO_EAST:
            if direction == DOWN:
                j += 1
                direction = RIGHT
            else:
                i -= 1
                direction = UP

        steps += 1

    return steps // 2

def get_edges(intersections):
    valid_edges = []
    for a, b in zip(intersections, intersections[1:] + [intersections[0]]):
        if a[0] == b[0]:
            continue
        valid_edges.append((a, b) if a[0] < b[0] else (b, a))
    return valid_edges

def part2(text):
    maze = [list(line) for line in text.splitlines()]
    start = get_start(maze)
    i, j = start

    intersections = [start]
    direction = None

    if i > 0 and maze[i - 1][j] in {VERTICAL_PIPE, SOUTH_TO_EAST, SOUTH_TO_WEST}:
        i -= 1
        direction = UP
    elif i < len(maze) - 1 and maze[i + 1][j] in {VERTICAL_PIPE, NORTH_TO_EAST, NORTH_TO_WEST}:
        i += 1
        direction = DOWN
    elif j > 0 and maze[i][j - 1] in {HORIZONTAL_PIPE, SOUTH_TO_EAST, NORTH_TO_EAST}:
        j -= 1
        direction = LEFT
    elif j < len(maze[i]) - 1 and maze[i][j + 1] in {HORIZONTAL_PIPE, SOUTH_TO_WEST, NORTH_TO_WEST}:
        j += 1
        direction = RIGHT

    while maze[i][j] != START:
        pipe = maze[i][j]
        if pipe == VERTICAL_PIPE:
            maze[i][j] = "X"
            i += -1 if direction == UP else 1
        elif pipe in {SOUTH_TO_EAST, SOUTH_TO_WEST, NORTH_TO_WEST, NORTH_TO_EAST}:
            maze[i][j] = "X"
            intersections.append((i, j))
            if pipe == SOUTH_TO_EAST:
                if direction == UP:
                    j += 1
                    direction = RIGHT
                else:
                    i += 1
                    direction = DOWN
            elif pipe == SOUTH_TO_WEST:
                if direction == UP:
                    j -= 1
                    direction = LEFT
                else:
                    i += 1
                    direction = DOWN
            elif pipe == NORTH_TO_WEST:
                if direction == DOWN:
                    j -= 1
                    direction = LEFT
                else:
                    i -= 1
                    direction = UP
            elif pipe == NORTH_TO_EAST:
                if direction == DOWN:
                    j += 1
                    direction = RIGHT
                else:
                    i -= 1
                    direction = UP
        elif pipe == HORIZONTAL_PIPE:
            maze[i][j] = "X"
            j += -1 if direction == LEFT else 1

    maze[start[0]][start[1]] = "X"

    edges = get_edges(intersections)
    intersections.sort()
    min_y, max_y = intersections[0][0], intersections[-1][0]

    total = 0
    for i in range(min_y + 1, max_y):
        active_edges = [edge for edge in edges if edge[0][0] <= i < edge[1][0]]
        active_edges.sort(key=lambda x: x[0][1])
        subtotal = 0
        for j in range(0, len(active_edges), 2):
            a, b = active_edges[j][0][1], active_edges[j + 1][0][1]
            subtotal += sum(maze[i][k] != "X" for k in range(a + 1, b))
        total += subtotal

    return total

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")