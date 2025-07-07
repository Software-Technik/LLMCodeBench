import sys
from collections import Counter

def part1(text):
    platform = [list(line) for line in text.strip().splitlines()]
    H, W = len(platform), len(platform[0])
    weight = 0
    for y in range(H):
        for x in range(W):
            if platform[y][x] == 'O':
                platform[y][x] = '.'
                i = y - 1
                while i >= 0 and platform[i][x] == '.':
                    i -= 1
                platform[i + 1][x] = 'O'
                weight += H - i - 1
    return weight

def part2(text):
    grid = text.strip().splitlines()
    H, W = len(grid), len(grid[0])
    positions = {(x, y) for y, row in enumerate(grid) for x, c in enumerate(row) if c == 'O'}
    direction = 0
    cycles = 0
    states = {}
    GOAL = 10**9
    while True:
        if direction == 0:
            if states is not None:
                state = frozenset(positions)
                if state in states:
                    prev = states[state]
                    period = cycles - prev
                    rem = (GOAL - cycles) % period
                    cycles = GOAL - rem
                    states = None
                else:
                    states[state] = cycles
            cnt = Counter(x for x, y in positions)
            positions = {(x, i) for x, n in cnt.items() for i in range(n)}
        elif direction == 2:
            cnt = Counter(x for x, y in positions)
            positions = {(x, H-1-i) for x, n in cnt.items() for i in range(n)}
        elif direction == 1:
            cnt = Counter(y for x, y in positions)
            positions = {(i, y) for y, n in cnt.items() for i in range(n)}
        else:
            cnt = Counter(y for x, y in positions)
            positions = {(W-1-i, y) for y, n in cnt.items() for i in range(n)}
            cycles += 1
            if cycles == GOAL:
                return sum(H - y for x, y in positions)
        direction = (direction + 1) % 4

if __name__ == "__main__":
    text = open(sys.argv[1]).read()
    sys.stdout.write(f"{part1(text)} {part2(text)}")