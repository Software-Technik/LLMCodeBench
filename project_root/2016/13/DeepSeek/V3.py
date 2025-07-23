import sys
from collections import deque

GOAL = (31, 39)
START = (1, 1)
DELTAS = ((1, 0), (-1, 0), (0, 1), (0, -1))

def is_wall(x, y, data):
    num = x*x + 3*x + 2*x*y + y + y*y + data
    return bin(num).count('1') % 2 != 0

def part1(data):
    que = deque([(START[0], START[1], 0)])
    seen = set()
    seen.add(START)

    while que:
        x, y, steps = que.popleft()

        if (x, y) == GOAL:
            return steps

        for dx, dy in DELTAS:
            nx, ny = x + dx, y + dy
            if nx >= 0 and ny >= 0 and (nx, ny) not in seen and not is_wall(nx, ny, data):
                seen.add((nx, ny))
                que.append((nx, ny, steps + 1))

def part2(data):
    que = deque([(START[0], START[1], 0)])
    seen = set()
    seen.add(START)

    while que:
        x, y, steps = que.popleft()

        if steps > 50:
            continue

        for dx, dy in DELTAS:
            nx, ny = x + dx, y + dy
            if nx >= 0 and ny >= 0 and (nx, ny) not in seen and not is_wall(nx, ny, data):
                seen.add((nx, ny))
                que.append((nx, ny, steps + 1))

    return len(seen)

inout_strings = sys.argv[1]
with open(inout_strings, 'r') as file:
    data = int(file.read().strip())

sys.stdout.write(f"{part1(data)} {part2(data)}")