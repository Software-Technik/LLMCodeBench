import sys

# Lecture et parsing
input_strings = sys.argv[1]
with open(input_strings) as f:
    instructions = [line.strip() for line in f.readlines()]

starting_position = (len(instructions) // 2, len(instructions[0]) // 2)
direction_offsets = ((-1, 0), (0, 1), (1, 0), (0, -1))

turn_map = {'left': 3, 'right': 1, 'back': 2}

def turn(direction_index, rotation):
    return (direction_index + turn_map[rotation]) % 4

def add_pos(a, b):
    return (a[0] + b[0], a[1] + b[1])

grid1 = {(i, j): (1 if mark == '#' else 0) for i, line in enumerate(instructions) for j, mark in enumerate(line)}
grid2 = grid1.copy()

def part1(direction_index=0):
    direction = direction_offsets[direction_index]
    position = starting_position
    infections = 0

    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    for _ in range(10000):
        status = grid1.get(position, 0)
        if status == 0:
            direction_index = turn(direction_index, "left")
            grid1[position] = 1
            infections += 1
        else:
            direction_index = turn(direction_index, "right")
            grid1[position] = 0

        position = add_pos(position, directions[direction_index])

    return infections

def part2():
    direction_index = 0  # north to start
    position = starting_position
    infections = 0

    for _ in range(100000):
        status = grid2.get(position, 2)
        if status == 0:
            direction_index = turn(direction_index, "left")
        elif status == 1:
            infections += 1
        elif status == 2:
            direction_index = turn(direction_index, "right")
        else:
            direction_index = turn(direction_index, "back")

        grid2[position] = (status + 1) % 4
        position = add_pos(position, direction_offsets[direction_index])

    return infections

print(part1())
print(part2())