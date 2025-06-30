import sys

def get_char(grid, pos):
    y, x = int(pos[0]), int(pos[1])
    if 0 <= y < len(grid) and 0 <= x < len(grid[y]):
        return grid[y][x]
    return ' '

def part1(grid):
    y = 0
    x = grid[0].index('|')
    dir_y, dir_x = 1, 0  # direction: down
    letters = []

    while True:
        c = get_char(grid, (y, x))
        if c == ' ':
            break
        if c.isalpha():
            letters.append(c)
        if c == '+':
            # Try left and right directions
            if dir_x == 0:
                if get_char(grid, (y, x - 1)) != ' ':
                    dir_y, dir_x = 0, -1
                else:
                    dir_y, dir_x = 0, 1
            else:
                if get_char(grid, (y - 1, x)) != ' ':
                    dir_y, dir_x = -1, 0
                else:
                    dir_y, dir_x = 1, 0
        y += dir_y
        x += dir_x

    return ''.join(letters)

def part2(grid):
    y = 0
    x = grid[0].index('|')
    dir_y, dir_x = 1, 0
    steps = 0

    while True:
        c = get_char(grid, (y, x))
        if c == ' ':
            break
        steps += 1
        if c == '+':
            if dir_x == 0:
                if get_char(grid, (y, x - 1)) != ' ':
                    dir_y, dir_x = 0, -1
                else:
                    dir_y, dir_x = 0, 1
            else:
                if get_char(grid, (y - 1, x)) != ' ':
                    dir_y, dir_x = -1, 0
                else:
                    dir_y, dir_x = 1, 0
        y += dir_y
        x += dir_x

    return steps

# Partie constante pour tous les tests
input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.rstrip('\n') for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")

