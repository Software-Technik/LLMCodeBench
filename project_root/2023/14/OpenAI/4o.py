import sys

def part1(text):
    platform = [list(line.strip()) for line in text.strip().splitlines()]
    weight = 0
    for y in range(len(platform)):
        row = platform[y]
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
    cycles = 0
    states = {}
    direction = 0

    while True:
        if direction in {0, 2}:
            if direction == 2:
                platform.reverse()
            else:
                current_state = tuple(
                    (x, y) for y in range(len(platform))
                    for x in range(len(platform[0]))
                    if platform[y][x] == 'O'
                )
                if current_state in states:
                    prev = states[current_state]
                    remaining_cycles = (1_000_000_000 - cycles) % (cycles - prev)
                    cycles = 1_000_000_000 - remaining_cycles
                else:
                    states[current_state] = cycles

            for y in range(len(platform)):
                for x, char in enumerate(platform[y]):
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
                    for y in range(len(platform))
                    for x in range(len(platform[0]))
                    if platform[y][x] == 'O'
                )

        direction = (direction + 1) % 4
        if states is None:
            break

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")