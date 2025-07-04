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

    while True:
        if direction in {0, 2}:
            if direction == 2:
                platform.reverse()
            else:
                if states is not None:
                    new_state = tuple(
                        (x, y)
                        for y, row in enumerate(platform)
                        for x, char in enumerate(row)
                        if char == 'O'
                    )
                    if new_state in states:
                        prev = states[new_state]
                        remaining = (1_000_000_000 - cycles) % (cycles - prev)
                        cycles = 1_000_000_000 - remaining
                        states = None
                    else:
                        states[new_state] = cycles

            for y, row in enumerate(platform):
                for x, char in enumerate(row):
                    if char == 'O':
                        platform[y][x] = '.'
                        i = y - 1
                        while i >= 0 and platform[i][x] == '.':
                            i -= 1
                        platform[i + 1][x] = 'O'

            if direction == 2:
                platform.reverse()

        elif direction == 1:  # West
            for x in range(len(platform[0])):
                for y in range(len(platform)):
                    if platform[y][x] == 'O':
                        platform[y][x] = '.'
                        i = x - 1
                        while i >= 0 and platform[y][i] == '.':
                            i -= 1
                        platform[y][i + 1] = 'O'

        else:  # East
            for x in range(len(platform[0]) - 1, -1, -1):
                for y in range(len(platform)):
                    if platform[y][x] == 'O':
                        platform[y][x] = '.'
                        i = x + 1
                        while i < len(platform[0]) and platform[y][i] == '.':
                            i += 1
                        platform[y][i - 1] = 'O'

            cycles += 1
            if cycles == 1_000_000_000:
                return sum(
                    len(platform) - y
                    for y, row in enumerate(platform)
                    for x, c in enumerate(row)
                    if c == 'O'
                )

        direction = (direction + 1) % 4


inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")