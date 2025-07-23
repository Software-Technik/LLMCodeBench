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
        if START in row:
            return (i, row.index(START))
    return (0, 0)

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
            i += 1 if direction == DOWN else -1
        elif pipe == SOUTH_TO_EAST:
            if direction == UP:
                j += 1
                direction = RIGHT
            else:
                i += 1
                direction = DOWN
        elif pipe == HORIZONTAL_PIPE:
            j += 1 if direction == RIGHT else -1
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
    edges = []
    n = len(intersections)
    for k in range(n):
        a = intersections[k]
        b = intersections[(k + 1) % n]
        if a[0] != b[0]:
            edges.append((a, b) if a[0] < b[0] else (b, a))
    return edges

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
        maze[i][j] = 'X'
        if pipe == VERTICAL_PIPE:
            i += 1 if direction == DOWN else -1
        elif pipe == SOUTH_TO_EAST:
            intersections.append((i, j))
            if direction == UP:
                j += 1
                direction = RIGHT
            else:
                i += 1
                direction = DOWN
        elif pipe == HORIZONTAL_PIPE:
            j += 1 if direction == RIGHT else -1
        elif pipe == SOUTH_TO_WEST:
            intersections.append((i, j))
            if direction == UP:
                j -= 1
                direction = LEFT
            else:
                i += 1
                direction = DOWN
        elif pipe == NORTH_TO_WEST:
            intersections.append((i, j))
            if direction == DOWN:
                j -= 1
                direction = LEFT
            else:
                i -= 1
                direction = UP
        elif pipe == NORTH_TO_EAST:
            intersections.append((i, j))
            if direction == DOWN:
                j += 1
                direction = RIGHT
            else:
                i -= 1
                direction = UP

    maze[start[0]][start[1]] = 'X'
    edges = get_edges(intersections)
    intersections.sort()
    min_y = intersections[0][0]
    max_y = intersections[-1][0]

    total = 0
    for i in range(min_y + 1, max_y):
        active_edges = [(a, b) for a, b in edges if a[0] <= i < b[0]]
        active_edges.sort(key=lambda x: x[0][1])
        subtotal = 0
        for j in range(0, len(active_edges), 2):
            a = active_edges[j][0][1]
            b = active_edges[j + 1][0][1]
            for k in range(a + 1, b):
                if maze[i][k] != 'X':
                    subtotal += 1
        total += subtotal

    return total

with open(sys.argv[1]) as f:
    text = f.read()
print(f"{part1(text)} {part2(text)}")