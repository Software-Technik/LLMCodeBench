import sys
from collections import defaultdict, deque

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
        _map.append([ord(i) for i in line])

    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque([(start, 0)])
    seen = {start: 0}

    while queue:
        pos, step = queue.popleft()

        if pos == target:
            return step

        next_pos = [(pos[0] + dy, pos[1] + dx) for dy, dx in d]
        for np in next_pos:
            y, x = np
            if 0 <= y < len(_map) and 0 <= x < len(_map[0]):
                if _map[y][x] - _map[pos[0]][pos[1]] > 1 or np in seen and seen[np] <= step + 1:
                    continue
                seen[np] = step + 1
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

        for idx in range(len(line)):
            if line[idx] == "a":
                starts.append((i, idx))

        _map.append([ord(i) for i in line])

    res = 99999
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque([(target, 0)])
    seen = {target: 0}

    while queue:
        pos, step = queue.popleft()

        if any(start == pos for start in starts):
            res = min(res, step)
            continue

        if step > res:
            continue

        next_pos = [(pos[0] + dy, pos[1] + dx) for dy, dx in d]
        for np in next_pos:
            y, x = np
            if 0 <= y < len(_map) and 0 <= x < len(_map[0]):
                if _map[y][x] - _map[pos[0]][pos[1]] >= -1 or np not in seen or seen[np] > step + 1:
                    seen[np] = step + 1
                    queue.append((np, step + 1))

    return res

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")