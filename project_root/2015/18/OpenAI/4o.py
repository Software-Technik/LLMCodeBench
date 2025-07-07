import sys

def part1(data):
    steps, w, h = (100, 100, 100) if len(data) == 100 else (4, 6, 6)
    _map = [list(i) for i in data]

    neighbors_offsets = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    for _ in range(steps):
        new_map = [['.'] * w for _ in range(h)]
        for y in range(h):
            for x in range(w):
                neighbor_count = sum(1 for a, b in neighbors_offsets if 0 <= y + a < h and 0 <= x + b < w and _map[y + a][x + b] == "#")
                if _map[y][x] == "#" and neighbor_count in [2, 3]:
                    new_map[y][x] = "#"
                elif _map[y][x] == "." and neighbor_count == 3:
                    new_map[y][x] = "#"
        _map = new_map

    return sum(row.count("#") for row in _map)

def part2(data):
    steps, w, h = (100, 100, 100) if len(data) == 100 else (5, 6, 6)
    _map = [list(i) for i in data]

    corners = [(0, 0), (0, w - 1), (h - 1, 0), (h - 1, w - 1)]
    for y, x in corners:
        _map[y][x] = "#"

    neighbors_offsets = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    for _ in range(steps):
        new_map = [['.'] * w for _ in range(h)]
        for y in range(h):
            for x in range(w):
                if (y, x) in corners:
                    new_map[y][x] = "#"
                else:
                    neighbor_count = sum(1 for a, b in neighbors_offsets if 0 <= y + a < h and 0 <= x + b < w and _map[y + a][x + b] == "#")
                    if _map[y][x] == "#" and neighbor_count in [2, 3]:
                        new_map[y][x] = "#"
                    elif _map[y][x] == "." and neighbor_count == 3:
                        new_map[y][x] = "#"
        _map = new_map

    return sum(row.count("#") for row in _map)

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")