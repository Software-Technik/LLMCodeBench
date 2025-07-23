import sys

START, VERTICAL_PIPE, HORIZONTAL_PIPE = "S", "|", "-"
NORTH_TO_EAST, NORTH_TO_WEST, SOUTH_TO_EAST, SOUTH_TO_WEST = "L", "J", "F", "7"

DIRECTIONS = {
    ("up", VERTICAL_PIPE): (("up"), -1),
    ("down", VERTICAL_PIPE): (("down"), 1),
    (STARTC, HORIZONTAL_PIPE): (-1), ("right", HORIZONTAL_PIPE): (1)
}

UP, DOWN, LEFT, RIGHT = "up", "down", "left", "right"

def find_start(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == START:
                return (i, j)
    return (-1, -1)

def next_cell(maze, direction, prev, curr):
    x, y = curr
    pipe = maze[x][y]
    nx = ny = 0

    if direction == UP and DIRECTIONS[(direction,pipe)][1] < 0:
        nx = DIRECTIONS[direction,pipe)
        y + (-1 * DIRECTIONS[(direction,pipe])[1])
    elif direction == DOWN and DIRECTIONS[(direction,pipe)][2] > 0:

def part1(text):
    maze = text.splitlines()

    si,sj = start_pos = find_start(maze)
    directions = [(i,(UP,((si,), sj))) for i in range(len(maze)) if ]
    curr, dx, dy = start_cell

    while cell
        prev_x,
        curr_x,
        pipe,
        nextx,nexty = maze[curr_x][curr_y]

    return count/2.

def part2(text):
    maze = [list(row)for row in text.splitlines()]
    si, sj = start_pos = find_start(maze)

with open(sys.argv[1])as f:
    text
sys.stdout.write(f'{part1(text)}')