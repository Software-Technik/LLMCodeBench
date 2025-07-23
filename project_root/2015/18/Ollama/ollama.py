import sys

def part1(data):
    steps, w, h = (100, 100, 100) if len(data) == 100 else (4, 6, 6)
    _map = [list(i) for i in data]
    for _ in range(steps):
        new_map = ['.' * w for _ in range(h)]
        for y in range(h):
            for x in range(w):
                live_neighbors = sum(_map[ny][nx] == '#' for ny, nx in [(y + a, x + b) for a, b in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]] if 0 <= ny < h and 0 <= nx < w)
                current = _map[y][x]
                new_map[y] += ['.', '#'][current == '#' and live_neighbors in (2, 3) or current == '.' and live_neighbors == 3]

        _map = [list(row) for row in new_map]

    return sum(char == '#' for row in _map for char in row)

def part2(data):
    steps, w, h = (100, 100, 100) if len(data) == 100 else (5, 6, 6)
    _map = [list(i) for i in data]
    corners = [(0, 0), (0, w - 1), (h - 1, 0), (h - 1, w - 1)]
    for y, x in corners:
        _map[y][x] = '#'

    for _ in range(steps):
        new_map = ['.' * w for _ in range(h)]
        for y in range(h):
            for x in range(w):
                if (y, x) in corners:
                    new_map[y] += '#'
                else:
                    live_neighbors = sum(_map[ny][nx] == '#' for ny, nx in [(y + a, x + b) for a, b in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]] if 0 <= ny < h and 0 <= nx < w)
                    current = _map[y][x]
                    new_map[y] += ['.', '#'][current == '#' and live_neighbors in (2, 3) or current == '.' and live_neighbors == 3]

        _map = [list(row) for row in new_map]

    return sum(char == '#' for row in _map for char in row)

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")