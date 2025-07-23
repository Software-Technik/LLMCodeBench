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

    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    dist = [[-1] * len(_map[0]) for _ in range(len(_map))]
    queue = deque()
    queue.append(start)
    dist[start[0]][start[1]] = 0

    while queue:
        r, c = queue.popleft()
        if (r, c) == target:
            return dist[r][c]

        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= len(_map) or nc < 0 or nc >= len(_map[0]):
                continue
            if dist[nr][nc] != -1:
                continue
            if _map[nr][nc] - _map[r][c] > 1:
                continue
            dist[nr][nc] = dist[r][c] + 1
            queue.append((nr, nc))

    return -1

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
        for j, c in enumerate(line):
            if c == 'a':
                starts.append((i, j))
        _map.append([ord(c) for c in line])

    starts_set = set(starts)
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    dist = [[-1] * len(_map[0]) for _ in range(len(_map))]
    queue = deque()
    queue.append(target)
    dist[target[0]][target[1]] = 0

    while queue:
        r, c = queue.popleft()
        if (r, c) in starts_set:
            return dist[r][c]

        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= len(_map) or nc < 0 or nc >= len(_map[0]):
                continue
            if dist[nr][nc] != -1:
                continue
            if _map[nr][nc] - _map[r][c] < -1:
                continue
            dist[nr][nc] = dist[r][c] + 1
            queue.append((nr, nc))

    return 99999

with open(sys.argv[1]) as f:
    data = [line.strip() for line in f]

print(f"{part1(data)}\n{part2(data)}")