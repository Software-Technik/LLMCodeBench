import sys
from collections import deque



GOAL = (31, 39)
START = (1, 1)
DELTAS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def part1(data):
    formula = lambda x, y: x*x + 3*x + 2*x*y + y + y*y + data
    que = deque([(START, 0)])
    seen = set()

    while que:
        (x, y), steps = que.popleft()

        if (x, y) == GOAL:
            return steps

        seen.add((x, y))

        for dx, dy in DELTAS:
            nx, ny = (x+dx, y+dy)
            if not ((nx, ny) in seen
                    or any(n < 0 for n in (nx, ny))
                    or bin(formula(nx, ny)).count('1') % 2):
                que.append(((nx, ny), steps+1))


def part2(data):
    formula = lambda x, y: x*x + 3*x + 2*x*y + y + y*y + data
    que = deque([(START, 0)])
    seen = set()

    while que:
        (x, y), steps = que.popleft()

        if steps > 50:
            return len(seen)

        seen.add((x, y))

        for dx, dy in DELTAS:
            nx, ny = (x+dx, y+dy)
            if not ((nx, ny) in seen
                    or any(n < 0 for n in (nx, ny))
                    or bin(formula(nx, ny)).count('1') % 2):
                que.append(((nx, ny), steps+1))


inout_strings = sys.argv[1]
with open(inout_strings, 'r')  as file:
    data = int(file.read().strip())


sys.stdout.write(f"{part1(data)} {part2(data)}")  
