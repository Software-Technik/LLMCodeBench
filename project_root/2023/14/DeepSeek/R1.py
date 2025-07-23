import sys

def part1(text):
    platform = [list(line.strip()) for line in text.strip().splitlines()]
    n = len(platform)
    m = len(platform[0])
    total = 0
    for j in range(m):
        next_row = 0
        for i in range(n):
            if platform[i][j] == 'O':
                if i != next_row:
                    platform[next_row][j] = 'O'
                    platform[i][j] = '.'
                total += n - next_row
                next_row += 1
            elif platform[i][j] == '#':
                next_row = i + 1
    return total

def part2(text):
    platform = [list(line.strip()) for line in text.strip().splitlines()]
    n = len(platform)
    m = len(platform[0])
    direction = 0
    cycles = 0
    states = {}

    while True:
        if direction == 0:
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
            for j in range(m):
                next_row = 0
                for i in range(n):
                    if platform[i][j] == 'O':
                        if i != next_row:
                            platform[next_row][j] = 'O'
                            platform[i][j] = '.'
                        next_row += 1
                    elif platform[i][j] == '#':
                        next_row = i + 1
        elif direction == 1:
            for i in range(n):
                next_col = 0
                for j in range(m):
                    if platform[i][j] == 'O':
                        if j != next_col:
                            platform[i][next_col] = 'O'
                            platform[i][j] = '.'
                        next_col += 1
                    elif platform[i][j] == '#':
                        next_col = j + 1
        elif direction == 2:
            for j in range(m):
                next_row = n - 1
                for i in range(n-1, -1, -1):
                    if platform[i][j] == 'O':
                        if i != next_row:
                            platform[next_row][j] = 'O'
                            platform[i][j] = '.'
                        next_row -= 1
                    elif platform[i][j] == '#':
                        next_row = i - 1
        else:
            for i in range(n):
                next_col = m - 1
                for j in range(m-1, -1, -1):
                    if platform[i][j] == 'O':
                        if j != next_col:
                            platform[i][next_col] = 'O'
                            platform[i][j] = '.'
                        next_col -= 1
                    elif platform[i][j] == '#':
                        next_col = j - 1
            cycles += 1
            if cycles == 1000000000:
                total = 0
                for i, row in enumerate(platform):
                    for c in row:
                        if c == 'O':
                            total += n - i
                return total
        direction = (direction + 1) % 4

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")