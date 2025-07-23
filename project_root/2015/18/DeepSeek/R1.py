import sys

def part1(data):
    steps, w, h = (100, 100, 100) if len(data) == 100 else (4, 6, 6)
    _map = [list(line) for line in data]
    
    directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,1), (1,-1), (-1,-1)]
    neighbors_map = {}
    for y in range(h):
        for x in range(w):
            neighbors = []
            for a, b in directions:
                ny, nx = y + a, x + b
                if 0 <= ny < h and 0 <= nx < w:
                    neighbors.append((ny, nx))
            neighbors_map[(y, x)] = neighbors

    for _ in range(steps):
        new_map = [['.'] * w for _ in range(h)]
        for y in range(h):
            for x in range(w):
                count = sum(1 for ny, nx in neighbors_map[(y, x)] if _map[ny][nx] == '#')
                if _map[y][x] == '#':
                    new_map[y][x] = '#' if count in (2, 3) else '.'
                else:
                    new_map[y][x] = '#' if count == 3 else '.'
        _map = new_map

    return sum(row.count('#') for row in _map)

def part2(data):
    steps, w, h = (100, 100, 100) if len(data) == 100 else (5, 6, 6)
    _map = [list(line) for line in data]
    corners = {(0, 0), (0, w-1), (h-1, 0), (h-1, w-1)}
    
    for y, x in corners:
        _map[y][x] = '#'

    directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,1), (1,-1), (-1,-1)]
    neighbors_map = {}
    for y in range(h):
        for x in range(w):
            neighbors = []
            for a, b in directions:
                ny, nx = y + a, x + b
                if 0 <= ny < h and 0 <= nx < w:
                    neighbors.append((ny, nx))
            neighbors_map[(y, x)] = neighbors

    for _ in range(steps):
        new_map = [['.'] * w for _ in range(h)]
        for y in range(h):
            for x in range(w):
                if (y, x) in corners:
                    new_map[y][x] = '#'
                else:
                    count = sum(1 for ny, nx in neighbors_map[(y, x)] if _map[ny][nx] == '#')
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