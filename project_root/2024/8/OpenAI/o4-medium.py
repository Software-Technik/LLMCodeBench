import sys
grid = open(sys.argv[1]).read().splitlines()
n = len(grid)
locs = {}
for i, row in enumerate(grid):
    for j, c in enumerate(row):
        if c != '.':
            locs.setdefault(c, []).append((i, j))
a1 = set()
a2 = set()
for pts in locs.values():
    L = len(pts)
    for i in range(L):
        ax, ay = pts[i]
        for j in range(i + 1, L):
            bx, by = pts[j]
            dx = bx - ax; dy = by - ay
            cx = ax - dx; cy = ay - dy
            if 0 <= cx < n and 0 <= cy < n: a1.add((cx, cy))
            cx2 = bx + dx; cy2 = by + dy
            if 0 <= cx2 < n and 0 <= cy2 < n: a1.add((cx2, cy2))
            if dx > 0:
                ibx = ax // dx; fbx = (n - 1 - bx) // dx
            elif dx < 0:
                ibx = (n - 1 - ax) // -dx; fbx = bx // -dx
            else:
                ibx = n; fbx = n
            if dy > 0:
                iby = ay // dy; fby = (n - 1 - by) // dy
            elif dy < 0:
                iby = (n - 1 - ay) // -dy; fby = by // -dy
            else:
                iby = n; fby = n
            ib = ibx if ibx < iby else iby
            fb = fbx if fbx < fby else fby
            for k in range(ib + 1):
                a2.add((ax - dx * k, ay - dy * k))
            for k in range(fb + 1):
                a2.add((bx + dx * k, by + dy * k))
print(len(a1), len(a2))