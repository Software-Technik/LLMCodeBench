import sys
import math

def load_points(data):
    pts = []
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c == '#':
                pts.append((x, y))
    return pts

def visible_count(from_pt, pts):
    seen = set()
    fx, fy = from_pt
    for x, y in pts:
        if (x, y) == from_pt: continue
        dx, dy = x - fx, y - fy
        g = math.gcd(dx, dy)
        seen.add((dx // g, dy // g))
    return len(seen)

def part1(pts):
    return max(visible_count(p, pts) for p in pts)

def part2(pts):
    station = max(pts, key=lambda p: visible_count(p, pts))
    dirs = {}
    sx, sy = station
    for x, y in pts:
        if (x, y) == station: continue
        dx, dy = x - sx, y - sy
        g = math.gcd(dx, dy)
        d = (dx // g, dy // g)
        dirs.setdefault(d, []).append((dx*dx+dy*dy, x, y))
    for arr in dirs.values():
        arr.sort()
    angles = []
    for d in dirs:
        a = math.atan2(d[0], -d[1])
        if a < 0: a += 2*math.pi
        angles.append((a, d))
    angles.sort()
    count = 0
    while True:
        for _, d in angles:
            lst = dirs[d]
            if lst:
                _, x, y = lst.pop(0)
                count += 1
                if count == 200:
                    return x * 100 + y

data = open(sys.argv[1]).read().splitlines()
pts = load_points(data)
print(part1(pts), part2(pts))