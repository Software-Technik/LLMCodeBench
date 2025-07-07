import sys
from collections import deque

GOAL = (31, 39)
START = (1, 1)
DELTAS = ((1, 0), (-1, 0), (0, 1), (0, -1))

def calculate_open(x, y, data):
    result = x*x + 3*x + 2*x*y + y + y*y + data
    return bin(result).count('1') % 2 == 0

def part1(data):
    que = deque([(START, 0)])
    seen = set([START])

    while que:
        (x, y), steps = que.popleft()

        if (x, y) == GOAL:
            return steps

        for dx, dy in DELTAS:
            nx, ny = (x+dx, y+dy)
            if (nx, ny) not in seen and nx >= 0 and ny >= 0 and calculate_open(nx, ny, data):
                seen.add((nx, ny))
                que.append(((nx, ny), steps+1))

def part2(data):
    que = deque([(START, 0)])
    seen = set([START])

    while que:
        (x, y), steps = que.popleft()

        if steps >= 50:
            continue

        for dx, dy in DELTAS:
            nx, ny = (x+dx, y+dy)
            if (nx, ny) not in seen and nx >= 0 and ny >= 0 and calculate_open(nx, ny, data):
                seen.add((nx, ny))
                que.append(((nx, ny), steps+1))

    return len(seen)

inout_strings = sys.argv[1]
with open(inout_strings, 'r') as file:
    data = int(file.read().strip())

sys.stdout.write(f"{part1(data)} {part2(data)}")