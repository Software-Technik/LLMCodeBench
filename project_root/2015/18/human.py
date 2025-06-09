import sys

def part1(data):
    steps, w, h = (100, 100, 100) if len(data) == 100 else (4, 6, 6)
    _map = [[*i] for i in data]

    for _ in range(steps):
        new_map = [list("." * w) for _ in range(h)]
        for y in range(h):
            for x in range(w):
                neighbors = [_map[y + a][x + b] for a, b in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)] if 0 <= y + a < h and 0 <= x + b < w]
                if _map[y][x] == "#":
                    new_map[y][x] = [".", "#"][neighbors.count("#") in [2, 3]]
                else:
                    new_map[y][x] = [".", "#"][neighbors.count("#") == 3]
        _map = new_map

    return sum([i.count("#") for i in _map])

def part2(data):
    steps, w, h = (100, 100, 100) if len(data) == 100 else (5, 6, 6)
    _map = [[*i] for i in data]

    for (y, x) in [(0, 0), (0, w - 1), (h - 1, 0), (h - 1, w - 1)]:
        _map[y][x] = "#"

    for _ in range(steps):
        new_map = [list("." * w) for _ in range(h)]
        for y in range(h):
            for x in range(w):
                if (y, x) in [(0, 0), (0, w - 1), (h - 1, 0), (h - 1, w - 1)]:
                    new_map[y][x] = "#"
                else:
                    neighbors = [_map[y + a][x + b] for a, b in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)] if 0 <= y + a < h and 0 <= x + b < w]
                    if _map[y][x] == "#":
                        new_map[y][x] = [".", "#"][neighbors.count("#") in [2, 3]]
                    else:
                        new_map[y][x] = [".", "#"][neighbors.count("#") == 3]
        _map = new_map

    return sum([i.count("#") for i in _map])

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")