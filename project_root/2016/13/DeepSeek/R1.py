import sys
from collections import deque

GOAL = (31, 39)
START = (1, 1)
DELTAS = ((1, 0), (-1, 0), (0, 1), (0, -1))

def part1(data):
    cache = {}
    def is_open(x, y):
        if (x, y) in cache:
            return cache[(x, y)]
        num = x*x + 3*x + 2*x*y + y + y*y + data
        bits = bin(num).count('1')
        res = (bits % 2 == 0)
        cache[(x, y)] = res
        return res

    que = deque([(START, 0)])
    seen = set()

    while que:
        (x, y), steps = que.popleft()

        if (x, y) == GOAL:
            return steps

        seen.add((x, y))

        for dx, dy in DELTAS:
            nx, ny = x + dx, y + dy
            if nx >= 0 and ny >= 0 and (nx, ny) not in seen and is_open(nx, ny):
                que.append(((nx, ny), steps + 1))

def part2(data):
    cache = {}
    def is_open(x, y):
        if (x, y) in cache:
            return cache[(x, y)]
        num = x*x + 3*x + 2*x*y + y + y*y + data
        bits = bin(num).count('1')
        res = (bits % 2 == 0)
        cache[(x, y)] = res
        return res

    que = deque([(START, 0)])
    seen = set()

    while que:
        (x, y), steps = que.popleft()

        if steps > 50:
            return len(seen)

        seen.add((x, y))

        for dx, dy in DELTAS:
            nx, ny = x + dx, y + dy
            if nx >= 0 and ny >= 0 and (nx, ny) not in seen and is_open(nx, ny):
                que.append(((nx, ny), steps + 1))

inout_strings = sys.argv[1]
with open(inout_strings, 'r') as file:
    data = int(file.read().strip())

sys.stdout.write(f"{part1(data)} {part2(data)}")