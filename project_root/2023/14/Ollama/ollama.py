import sys

def part1(text):
    platform = [list(line.strip()) for line in text.strip().splitlines()]
    weight = 0
    for y, row in enumerate(platform):
        for x, char in enumerate(row):
            if char == 'O':
                platform[y][x] = '.'
                i = y - 1
                while i >= 0 and platform[i][x] == '.':
                    i -= 1
                platform[i + 1][x] = 'O'
                weight += len(platform) - i - 1
    return weight

def part2(text):
    platform = [list(line.strip()) for line in text.strip().splitlines()]
    direction, cycles = 0, 0
    states = {}

    def move_rocks():
        nonlocal states
        if direction == 0:
            state = tuple(row[:] for row in platform)
            if state in states:
                return True
            else:
                states[state] = cycles
        elif direction == 2:
            platform.reverse()

        if direction % 2 == 0:
            y_range, x = range(len(platform)), enumerate
            dir_step = -1 if direction == 0 else 1
        else:
            y_range = len(platform)
            x = lambda _: range(dir_step * (len(platform[0]) - 1), dir_step * -1, dir_step)

        for y in y_range:
            for x_idx in x(y):
                if platform[y][x_idx] == 'O':
                    platform[y][x_idx] = '.'
                    i = x_idx + dir_step
                    while 0 <= abs(i) < len(platform[0]) and platform[y][i - dir_step * (dir_step == -1)] == '.':
                        i += dir_step
                    platform[y][i - dir_step] = 'O'

        if direction == 2:
            platform.reverse()

    while cycles < 1_000_000_000:
        move_rocks()
        direction = (direction + 1) % 4
        if direction == 0 and states:
            return sum((len(platform) - y) for y, row in enumerate(platform) for x, c in enumerate(row) if c == 'O')
        cycles += 1

with open(sys.argv[1]) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")