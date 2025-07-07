import sys

input_path = sys.argv[1]
with open(input_path) as f:
    lines = [list(line.rstrip('\n')) for line in f if line.strip()]

h, w = len(lines), len(lines[0])
dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def simulate(seats, tolerance, neighbor_fn):
    prev = seats
    while True:
        new = [row.copy() for row in prev]
        changed = False
        for y in range(h):
            for x in range(w):
                c = prev[y][x]
                if c == '.': continue
                occ = neighbor_fn(prev, x, y)
                if c == 'L' and occ == 0:
                    new[y][x] = '#'; changed = True
                elif c == '#' and occ >= tolerance:
                    new[y][x] = 'L'; changed = True
        if not changed:
            return sum(row.count('#') for row in new)
        prev = new

def adj_count(seats, x, y):
    cnt = 0
    for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if 0 <= nx < w and 0 <= ny < h and seats[ny][nx] == '#':
            cnt += 1
    return cnt

# Precompute visible neighbors for part 2
visible = {}
for y in range(h):
    for x in range(w):
        if lines[y][x] == '.': continue
        lst = []
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            while 0 <= nx < w and 0 <= ny < h:
                if lines[ny][nx] != '.':
                    lst.append((nx, ny))
                    break
                nx += dx; ny += dy
        visible[(x,y)] = lst

def vis_count(seats, x, y):
    return sum(1 for nx, ny in visible[(x,y)] if seats[ny][nx] == '#')

part1 = simulate(lines, 4, adj_count)
part2 = simulate(lines, 5, vis_count)
print(part1, part2)