import sys

input_strings = sys.argv[1]
with open(input_strings) as f:
    instructions = [line.strip() for line in f.readlines()]

starting_position = (len(instructions) // 2, len(instructions[0]) // 2)
grid1 = {}
grid2 = {}

for i, line in enumerate(instructions):
    for j, mark in enumerate(line):
        if mark == '#':
            grid1[(i, j)] = 1
            grid2[(i, j)] = 2

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def part1():
    grid = grid1.copy()
    direction_index = 0
    row, col = starting_position
    infections = 0

    for _ in range(10000):
        key = (row, col)
        current = grid.get(key, 0)
        if current == 0:
            direction_index = (direction_index + 3) % 4
            grid[key] = 1
            infections += 1
        else:
            direction_index = (direction_index + 1) % 4
            grid[key] = 0
        dx, dy = dirs[direction_index]
        row += dx
        col += dy

    return infections

def part2():
    grid = grid2.copy()
    direction_index = 0
    row, col = starting_position
    infections = 0

    for _ in range(10000000):
        key = (row, col)
        current = grid.get(key, 0)
        if current == 0:
            direction_index = (direction_index + 3) % 4
        elif current == 1:
            infections += 1
        elif current == 2:
            direction_index = (direction_index + 1) % 4
        elif current == 3:
            direction_index = (direction_index + 2) % 4
        grid[key] = (current + 1) % 4
        dx, dy = dirs[direction_index]
        row += dx
        col += dy

    return infections

print(part1())
print(part2())