To solve this problem, we need to find the solution to both parts of the Advent of Code challenge. The first part involves finding the number of steps to reach the farthest point in a loop from the starting position, and the second part involves counting the number of tiles enclosed by the loop.

### Approach
1. **Part 1: Finding the Farthest Point**
   - **Problem Analysis**: The maze consists of pipes forming a loop. The starting point 'S' connects to two adjacent pipes. The goal is to traverse the loop in both directions simultaneously and find the point where they meet, which is the farthest point from the start.
   - **Algorithm**: Start from 'S' and traverse the loop in one direction, counting steps until returning to 'S'. The farthest point is half the total steps of the loop.
   - **Optimization**: Directly traverse the loop without additional data structures, leveraging the pipe directions to navigate efficiently.

2. **Part 2: Counting Enclosed Tiles**
   - **Problem Analysis**: The loop forms a polygon. Tiles enclosed by the loop are those not part of the loop and inside the polygon.
   - **Algorithm**: 
     - **Mark the Loop**: Traverse the loop again, marking each pipe segment as part of the loop ('X').
     - **Scanline Algorithm**: For each row between the topmost and bottommost loop segments:
       - Identify active vertical edges (non-horizontal pipe segments).
       - Sort these edges by their x-coordinate.
       - Process edges in pairs to determine segments between them that are inside the polygon.
       - Count non-pipe tiles within these segments.
   - **Optimization**: Efficiently track active edges per row and count enclosed tiles by processing edge pairs.

### Solution Code

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
        for j, char in enumerate(row):
            if char == START:
                return (i, j)
    return (0, 0)

def part1(text: str) -> int:
    maze = text.splitlines()
    i, j = get_start(maze)

    direction = None

    if i > 0 and maze[i - 1][j] in [VERTICAL_PIPE, SOUTH_TO_EAST, SOUTH_TO_WEST]:
        i -= 1
        direction = UP
    elif i < len(maze) - 1 and maze[i + 1][j] in [
        VERTICAL_PIPE,
        NORTH_TO_EAST,
        NORTH_TO_WEST,
    ]:
        i += 1
        direction = DOWN
    elif j > 0 and maze[i][j - 1] in [HORIZONTAL_PIPE, SOUTH_TO_EAST, NORTH_TO_EAST]:
        j -= 1
        direction = LEFT
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

def get_edges(intersections):
    edges = list(zip(intersections, intersections[1:] + [intersections[0]]))
    valid_edges = []
    for a, b in edges:
        if a[0] == b[0]:
            continue
        if a[0] < b[0]:
            valid_edges.append((a, b))
        else:
            valid_edges.append((b, a))
    return valid_edges

def part2(text: str) -> int:
    maze = [list(line) for line in text.splitlines()]
    start = get_start(maze)
    i, j = start

    intersections = [start]
    direction = None

    if i > 0 and maze[i - 1][j] in [VERTICAL_PIPE, SOUTH_TO_EAST, SOUTH_TO_WEST]:
        i -= 1
        direction = UP
    elif i < len(maze) - 1 and maze[i + 1][j] in [
        VERTICAL_PIPE,
        NORTH_TO_EAST,
        NORTH_TO_WEST,
    ]:
        i += 1
        direction = DOWN
    elif j > 0 and maze[i][j - 1] in [HORIZONTAL_PIPE, SOUTH_TO_EAST, NORTH_TO_EAST]:
        j -= 1
        direction = LEFT
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
            maze[i][j] = 'X'
            if direction == UP:
                i -= 1
            else:
                i += 1
        elif pipe == SOUTH_TO_EAST:
            maze[i][j] = 'X'
            intersections.append((i, j))
            if direction == UP:
                j += 1
                direction = RIGHT
            else:
                i += 1
                direction = DOWN
        elif pipe == HORIZONTAL_PIPE:
            maze[i][j] = 'X'
            if direction == LEFT:
                j -= 1
            else:
                j += 1
        elif pipe == SOUTH_TO_WEST:
            maze[i][j] = 'X'
            intersections.append((i, j))
            if direction == UP:
                j -= 1
                direction = LEFT
            else:
                i += 1
                direction = DOWN
        elif pipe == NORTH_TO_WEST:
            maze[i][j] = 'X'
            intersections.append((i, j))
            if direction == DOWN:
                j -= 1
                direction = LEFT
            else:
                i -= 1
                direction = UP
        elif pipe == NORTH_TO_EAST:
            maze[i][j] = 'X'
            intersections.append((i, j))
            if direction == DOWN:
                j += 1
                direction = RIGHT
            else:
                i -= 1
                direction = UP

    maze[start[0]][start[1]] = 'X'

    edges = get_edges(intersections)
    if not intersections:
        return 0
    intersections.sort()
    min_y = intersections[0][0]
    max_y = intersections[-1][0]

    total = 0
    for i in range(min_y + 1, max_y):
        active_edges = []
        for a, b in edges:
            if a[0] <= i < b[0]:
                active_edges.append((a, b))
        active_edges.sort(key=lambda x: x[0][1])
        subtotal = 0
        for idx in range(0, len(active_edges), 2):
            if idx + 1 >= len(active_edges):
                break
            a = active_edges[idx][0][1]
            b = active_edges[idx + 1][0][1]
            for k in range(a + 1, b):
                if maze[i][k] != 'X':
                    subtotal += 1
        total += subtotal

    return total

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read().strip()
sys.stdout.write(f"{part1(text)} {part2(text)}")


### Explanation
1. **Part 1**:
   - **Finding Start**: Locate 'S' in the maze.
   - **Traversal**: From 'S', move in a valid direction (up, down, left, or right) based on adjacent pipes. Continue moving through the loop, counting steps until returning to 'S'.
   - **Result**: The farthest point is half the total steps (since traversal is bidirectional).

2. **Part 2**:
   - **Marking Loop**: Traverse the loop again, marking each pipe segment as 'X'.
   - **Edge Identification**: Collect vertices (corners and start) to form polygon edges, excluding horizontal edges.
   - **Scanline Algorithm**:
     - For each row between the topmost and bottommost loop segments:
       - Identify active vertical edges (edges crossing the current row).
       - Sort edges by their x-coordinate.
       - Process edges in pairs; the area between each pair is inside the polygon.
       - Count non-pipe tiles ('X') within these segments.
   - **Result**: Sum of enclosed tiles across all rows.