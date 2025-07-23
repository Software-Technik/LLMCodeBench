import sys
from collections import deque

GOAL = (31, 39)
START = (1, 1)
DELTAS = ((1, 0), (-1, 0), (0, 1), (0, -1))

def part1(data):
    que = deque([(START, 0)])
    seen = {START}
    while que:
        (x, y), steps = que.popleft()
        if (x, y) == GOAL:
            return steps
        for dx, dy in DELTAS:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or (nx, ny) in seen or bin((nx * nx + 3 * nx + 2 * nx * ny + ny + ny * ny) % data).count('1') % 2:
                continue
            que.append(((nx, ny), steps+1))
            seen.add((nx, ny))

def part2(data):
    que = deque([(START, 0)])
    seen = {START}
    while que:
        (x, y), steps = que.popleft()
        if steps > 50:
            return len(seen)
        for dx, dy in DELTAS:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or (nx, ny) in seen or bin((nx * nx + 3 * nx + 2 * nx * ny + ny + ny * ny) % data).count('1') % 2:
                continue
            que.append(((nx, ny), steps+1))
            seen.add((nx, ny))

inout_strings = sys.argv[1]
with open(inout_strings, 'r') as file:
    data = int(file.read().strip())

sys.stdout.write(f"{part1(data)} {part2(data)}\n")