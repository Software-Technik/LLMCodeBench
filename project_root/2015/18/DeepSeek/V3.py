import sys

def part1(data):
    steps, w, h = (100, 100, 100) if len(data) == 100 else (4, 6, 6)
    _map = [list(line) for line in data]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

    for _ in range(steps):
        new_map = [['.' for _ in range(w)] for _ in range(h)]
        for y in range(h):
            for x in range(w):
                count = 0
                for a, b in directions:
                    ny, nx = y + a, x + b
                    if 0 <= ny < h and 0 <= nx < w and _map[ny][nx] == '#':
                        count += 1
                if _map[y][x] == '#':
                    new_map[y][x] = '#' if count in (2, 3) else '.'
                else:
                    new_map[y][x] = '#' if count == 3 else '.'
        _map = new_map

    return sum(row.count('#') for row in _map)

def part2(data):
    steps, w, h = (100, 100, 100) if len(data) == 100 else (5, 6, 6)
    _map = [list(line) for line in data]
    corners = {(0, 0), (0, w - 1), (h - 1, 0), (h - 1, w - 1)}
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

    for y, x in corners:
        _map[y][x] = '#'

    for _ in range(steps):
        new_map = [['.' for _ in range(w)] for _ in range(h)]
        for y in range(h):
            for x in range(w):
                if (y, x) in corners:
                    new_map[y][x] = '#'
                else:
                    count = 0
                    for a, b in directions:
                        ny, nx = y + a, x + b
                        if 0 <= ny < h and 0 <= nx < w and _map[ny][nx] == '#':
                            count += 1
                    if _map[y][x] == '#':
                        new_map[y][x] = '#' if count in (2, 3) else '.'
                    else:
                        new_map[y][x] = '#' if count == 3 else '.'
        _map = new_map

    return sum(row.count('#') for row in _map)

input_file = sys.argv[1]
with open(input_file) as f:
    data = [line.strip() for line in f]
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")