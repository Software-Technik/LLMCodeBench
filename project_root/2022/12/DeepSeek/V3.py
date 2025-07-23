import sys
from collections import deque

def part1(data):
    _map = []
    start = target = None
    for i, line in enumerate(data):
        row = list(line)
        if 'S' in row:
            start = (i, row.index('S'))
            row[start[1]] = 'a'
        if 'E' in row:
            target = (i, row.index('E'))
            row[target[1]] = 'z'
        _map.append([ord(c) for c in row])

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque([(start, 0)])
    seen = {start: 0}

    while queue:
        pos, step = queue.popleft()
        if pos == target:
            return step
        for dy, dx in directions:
            ny, nx = pos[0] + dy, pos[1] + dx
            if 0 <= ny < len(_map) and 0 <= nx < len(_map[0]):
                if (ny, nx) in seen and seen[(ny, nx)] <= step + 1:
                    continue
                if _map[ny][nx] - _map[pos[0]][pos[1]] > 1:
                    continue
                seen[(ny, nx)] = step + 1
                queue.append(((ny, nx), step + 1))

def part2(data):
    _map = []
    starts = []
    target = None
    for i, line in enumerate(data):
        row = list(line)
        if 'S' in row:
            row[row.index('S')] = 'a'
        if 'E' in row:
            target = (i, row.index('E'))
            row[target[1]] = 'z'
        for j, c in enumerate(row):
            if c == 'a':
                starts.append((i, j))
        _map.append([ord(c) for c in row])

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque([(target, 0)])
    seen = {target: 0}
    res = float('inf')

    while queue:
        pos, step = queue.popleft()
        if step >= res:
            continue
        if pos in starts:
            res = step
            continue
        for dy, dx in directions:
            ny, nx = pos[0] + dy, pos[1] + dx
            if 0 <= ny < len(_map) and 0 <= nx < len(_map[0]):
                if (ny, nx) in seen and seen[(ny, nx)] <= step + 1:
                    continue
                if _map[pos[0]][pos[1]] - _map[ny][nx] > 1:
                    continue
                seen[(ny, nx)] = step + 1
                queue.append(((ny, nx), step + 1))
    return res

with open(sys.argv[1]) as f:
    data = [line.strip() for line in f]

print(f"{part1(data)}\n{part2(data)}")