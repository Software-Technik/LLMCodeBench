import sys
import re

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


def get_start(maze: list[str]) -> tuple[int, int]:
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == START:
                return (i, j)
    return (0, 0)

def part1(text: str)->int:
    maze = text.splitlines()
    i, j = get_start(maze)

    direction = None

    # Up
    if i > 0 and maze[i - 1][j] in [VERTICAL_PIPE, SOUTH_TO_EAST, SOUTH_TO_WEST]:
        i -= 1
        direction = UP
    # Down
    elif i < len(maze) - 1 and maze[i + 1][j] in [
        VERTICAL_PIPE,
        NORTH_TO_EAST,
        NORTH_TO_WEST,
    ]:
        i += 1
        direction = DOWN
    # Left
    elif j > 0 and maze[i][j - 1] in [HORIZONTAL_PIPE, SOUTH_TO_EAST, NORTH_TO_EAST]:
        j -= 1
        direction = LEFT
    # Right
    elif j < len(maze[i]) - 1 and maze[i][j + 1] in [
        HORIZONTAL_PIPE,
        SOUTH_TO_WEST,
        NORTH_TO_WEST,
    ]:
        j += 1
        direction = RIGHT

    steps = 1
    while maze[i][j] != START:
        pipe = maze[i][j]
        if pipe == VERTICAL_PIPE:
            if direction == UP:
                i -= 1
            else:
                i += 1
        elif pipe == SOUTH_TO_EAST:
            if direction == UP:
                j += 1
                direction = RIGHT
            else:
                i += 1
                direction = DOWN
        elif pipe == HORIZONTAL_PIPE:
            if direction == LEFT:
                j -= 1
            else:
                j += 1
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


def get_edges(
    intersections: list[tuple[int, int]]
) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    """
    Given a list of intersections, return a list of edges used in the scanline algorithm.

    Horizontal edges are ignored, and the edges are sorted by their y coordinate.
    """
    edges = zip(intersections, intersections[1:] + [intersections[0]])
    valid_edges = []
    for a, b in edges:
        # Don't include horizontal edges
        if a[0] == b[0]:
            continue

        if a[0] < b[0]:
            valid_edges.append((a, b))
        else:
            valid_edges.append((b, a))
    return valid_edges


def get_start(maze: list[list[str]]) -> tuple[int, int]:
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == START:
                return (i, j)
    return (0, 0)

def part2(text: str) -> int:
    """
    Solve by getting the edges of the maze and using the scanline algorithm.

    First, we get the edges of the maze by following the pipes,
    then we use that to get all edges used in the scanline algorithm.

    References:
    - https://www.cs.drexel.edu/~deb39/Classes/CS430/Lectures/L-05_Polygons.pdf
    - https://www.geeksforgeeks.org/scan-line-polygon-filling-using-opengl-c/
    """
    maze = [[c for c in line] for line in text.splitlines()]
    start = get_start(maze)
    i, j = start

    intersections = [start]
    direction = None

    # Up
    if i > 0 and maze[i - 1][j] in [VERTICAL_PIPE, SOUTH_TO_EAST, SOUTH_TO_WEST]:
        i -= 1
        direction = UP
    # Down
    elif i < len(maze) - 1 and maze[i + 1][j] in [
        VERTICAL_PIPE,
        NORTH_TO_EAST,
        NORTH_TO_WEST,
    ]:
        i += 1
        direction = DOWN
    # Left
    elif j > 0 and maze[i][j - 1] in [HORIZONTAL_PIPE, SOUTH_TO_EAST, NORTH_TO_EAST]:
        j -= 1
        direction = LEFT
    # Right
    elif j < len(maze[i]) - 1 and maze[i][j + 1] in [
        HORIZONTAL_PIPE,
        SOUTH_TO_WEST,
        NORTH_TO_WEST,
    ]:
        j += 1
        direction = RIGHT

    pipe = maze[i][j]
    while maze[i][j] != START:
        pipe = maze[i][j]
        if pipe == VERTICAL_PIPE:
            maze[i][j] = "X"
            if direction == UP:
                i -= 1
            else:
                i += 1
        elif pipe == SOUTH_TO_EAST:
            maze[i][j] = "X"
            intersections.append((i, j))
            if direction == UP:
                j += 1
                direction = RIGHT
            else:
                i += 1
                direction = DOWN
        elif pipe == HORIZONTAL_PIPE:
            maze[i][j] = "X"
            if direction == LEFT:
                j -= 1
            else:
                j += 1
        elif pipe == SOUTH_TO_WEST:
            maze[i][j] = "X"
            intersections.append((i, j))
            if direction == UP:
                j -= 1
                direction = LEFT
            else:
                i += 1
                direction = DOWN
        elif pipe == NORTH_TO_WEST:
            maze[i][j] = "X"
            intersections.append((i, j))
            if direction == DOWN:
                j -= 1
                direction = LEFT
            else:
                i -= 1
                direction = UP
        elif pipe == NORTH_TO_EAST:
            maze[i][j] = "X"
            intersections.append((i, j))
            if direction == DOWN:
                j += 1
                direction = RIGHT
            else:
                i -= 1
                direction = UP

    # We always asume that S is an intersection!
    maze[start[0]][start[1]] = "X"

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
                if maze[i][k] != "X":
                    subtotal += 1
        total += subtotal

    return total
    


inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")