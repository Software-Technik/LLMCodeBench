import sys
from collections import deque

def part1(data):
    _map = []
    start = None
    target = None

    for i, line in enumerate(data):
        line = list(line)
        if "S" in line:
            sx = line.index("S")
            start = (i, sx)
            line[sx] = "a"
        if "E" in line:
            ex = line.index("E")
            target = (i, ex)
            line[ex] = "z"
        _map.append([ord(c) for c in line])

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque([(start, 0)])
    seen = set()
    seen.add(start)

    while queue:
        pos, step = queue.popleft()

        if pos == target:
            return step

        for dy, dx in directions:
            np = (pos[0] + dy, pos[1] + dx)
            if 0 <= np[0] < len(_map) and 0 <= np[1] < len(_map[0]):
                if np not in seen and _map[np[0]][np[1]] - _map[pos[0]][pos[1]] <= 1:
                    seen.add(np)
                    queue.append((np, step + 1))

def part2(data):
    _map = []
    starts = []
    target = None

    for i, line in enumerate(data):
        line = list(line)
        if "S" in line:
            sx = line.index("S")
            line[sx] = "a"
        if "E" in line:
            ex = line.index("E")
            target = (i, ex)
            line[ex] = "z"

        for idx, char in enumerate(line):
            if char == "a":
                starts.append((i, idx))

        _map.append([ord(c) for c in line])

    res = float('inf')
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque([(target, 0)])
    seen = set()
    seen.add(target)

    while queue:
        pos, step = queue.popleft()

        if pos in starts:
            res = min(res, step)
            continue

        if step > res:
            continue

        for dy, dx in directions:
            np = (pos[0] + dy, pos[1] + dx)
            if 0 <= np[0] < len(_map) and 0 <= np[1] < len(_map[0]):
                if np not in seen and _map[np[0]][np[1]] - _map[pos[0]][pos[1]] >= -1:
                    seen.add(np)
                    queue.append((np, step + 1))

    return res

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")