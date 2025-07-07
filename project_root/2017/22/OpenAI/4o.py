import sys

# Lecture et parsing
input_strings = sys.argv[1]
with open(input_strings) as f:
    instructions = [line.strip() for line in f]

starting_position = (len(instructions) // 2, len(instructions[0]) // 2)
starting_direction = (-1, 0)

grid1 = {}
grid2 = {}

for i, line in enumerate(instructions):
    for j, mark in enumerate(line):
        if mark == '#':
            grid1[(i, j)] = 1
            grid2[(i, j)] = 2

def turn(direction, rotation):
    if rotation == "left":
        return (-direction[1], direction[0])
    elif rotation == "right":
        return (direction[1], -direction[0])
    elif rotation == "back":
        return (-direction[0], -direction[1])
    return direction

def add_pos(a, b):
    return (a[0] + b[0], a[1] + b[1])

def part1():
    direction = starting_direction
    position = starting_position
    infections = 0
    grid = grid1.copy()

    for _ in range(10000):
        status = grid.get(position, 0)
        if status == 0:
            direction = turn(direction, "left")
            grid[position] = 1
            infections += 1
        else:
            direction = turn(direction, "right")
            grid[position] = 0
        position = add_pos(position, direction)

    return infections

def part2():
    direction = starting_direction
    position = starting_position
    infections = 0
    grid = grid2.copy()

    for _ in range(10000000):
        status = grid.get(position, 0)
        if status == 0:
            direction = turn(direction, "left")
        elif status == 1:
            infections += 1
        elif status == 2:
            direction = turn(direction, "right")
        elif status == 3:
            direction = turn(direction, "back")
        grid[position] = (status + 1) % 4
        position = add_pos(position, direction)

    return infections

print(part1())
print(part2())