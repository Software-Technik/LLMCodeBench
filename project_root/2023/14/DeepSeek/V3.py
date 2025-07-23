import sys

def part1(text):
    platform = [list(line.strip()) for line in text.strip().splitlines()]
    weight = 0
    for x in range(len(platform[0])):
        for y in range(len(platform)):
            if platform[y][x] == 'O':
                platform[y][x] = '.'
                new_y = y
                while new_y > 0 and platform[new_y - 1][x] == '.':
                    new_y -= 1
                platform[new_y][x] = 'O'
                weight += len(platform) - new_y
    return weight

def part2(text):
    platform = [list(line.strip()) for line in text.strip().splitlines()]
    direction, cycles = 0, 0
    states = {}

    while True:
        if direction == 0:  # North
            if states is not None:
                state = tuple(
                    (x, y)
                    for y, row in enumerate(platform)
                    for x, char in enumerate(row)
                    if char == 'O'
                )
                if state in states:
                    prev_cycle = states[state]
                    remaining = (1_000_000_000 - cycles) % (cycles - prev_cycle)
                    cycles = 1_000_000_000 - remaining
                    states = None
                else:
                    states[state] = cycles
            for x in range(len(platform[0])):
                for y in range(len(platform)):
                    if platform[y][x] == 'O':
                        platform[y][x] = '.'
                        new_y = y
                        while new_y > 0 and platform[new_y - 1][x] == '.':
                            new_y -= 1
                        platform[new_y][x] = 'O'
        elif direction == 1:  # West
            for y in range(len(platform)):
                for x in range(len(platform[0])):
                    if platform[y][x] == 'O':
                        platform[y][x] = '.'
                        new_x = x
                        while new_x > 0 and platform[y][new_x - 1] == '.':
                            new_x -= 1
                        platform[y][new_x] = 'O'
        elif direction == 2:  # South
            for x in range(len(platform[0])):
                for y in range(len(platform) - 1, -1, -1):
                    if platform[y][x] == 'O':
                        platform[y][x] = '.'
                        new_y = y
                        while new_y < len(platform) - 1 and platform[new_y + 1][x] == '.':
                            new_y += 1
                        platform[new_y][x] = 'O'
        else:  # East
            for y in range(len(platform)):
                for x in range(len(platform[0]) - 1, -1, -1):
                    if platform[y][x] == 'O':
                        platform[y][x] = '.'
                        new_x = x
                        while new_x < len(platform[0]) - 1 and platform[y][new_x + 1] == '.':
                            new_x += 1
                        platform[y][new_x] = 'O'
            cycles += 1
            if cycles == 1_000_000_000:
                return sum(len(platform) - y for y, row in enumerate(platform) for c in row if c == 'O')
        direction = (direction + 1) % 4

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")